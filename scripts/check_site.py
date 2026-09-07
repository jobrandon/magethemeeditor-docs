#!/usr/bin/env python3
"""Check built HTML links and content/output boundaries without network access."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SITE = ROOT / "site"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.navigation = []
        self.nav_depth = 0
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "nav":
            self.nav_depth += 1
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if self.nav_depth and tag == "a" and attrs.get("href"):
            self.navigation.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "nav":
            self.nav_depth -= 1


def main():
    errors = []
    pages = {path.resolve(): Page(path) for path in SITE.rglob("*.html")}
    if not pages:
        sys.exit("No HTML output. Run make build first.")
    if SITE.resolve().is_relative_to(CONTENT.resolve()):
        errors.append("Generated output is inside authored content.")

    def target_for(source, raw):
        link = urlsplit(raw)
        if link.scheme or link.netloc:
            return None, None
        target = ((SITE if link.path.startswith("/") else source.parent)
                  / unquote(link.path).lstrip("/")).resolve() if link.path else source
        if target.is_dir():
            target /= "index.html"
        return target, unquote(link.fragment)

    local_links = 0
    nav_targets = set()
    for source, page in pages.items():
        for raw in page.navigation:
            target, _ = target_for(source, raw)
            if target:
                nav_targets.add(target)
        for raw in page.links:
            target, fragment = target_for(source, raw)
            if target is None:
                continue
            local_links += 1
            if not target.is_relative_to(SITE.resolve()):
                errors.append(f"{source.relative_to(SITE)}: link escapes site: {raw}")
            elif not target.is_file():
                errors.append(f"{source.relative_to(SITE)}: missing target: {raw}")
            elif fragment and target in pages and fragment not in pages[target].ids:
                errors.append(f"{source.relative_to(SITE)}: missing anchor: {raw}")

    # MkDocs uses directory URLs; the build config intentionally leaves that default enabled.
    sources = list(CONTENT.rglob("*.md"))
    for source in sources:
        rel = source.relative_to(CONTENT)
        if "_private" in rel.parts or source.name == "AGENTS.md":
            continue
        output = SITE / (rel if source.name == "index.md" else rel.with_suffix("") / "index.md")
        output = output.with_suffix(".html").resolve()
        if output not in pages:
            errors.append(f"Authored page missing from output: {rel}")
        elif output not in nav_targets:
            errors.append(f"Authored page missing from rendered navigation: {rel}")

    forbidden = {".git", ".venv", ".venv-tools", ".local", ".secrets", "_private"}
    for path in SITE.rglob("*"):
        if forbidden.intersection(path.relative_to(SITE).parts) or path.name in {
            "AGENTS.md", "README.md", ".pages", "mkdocs.yml", "requirements.txt", "requirements.in"
        }:
            errors.append(f"Non-content support path leaked into site: {path.relative_to(SITE)}")

    if errors:
        sys.exit("\n".join(sorted(set(errors))))
    print(f"PASS: {len(sources)} source pages, {len(pages)} HTML pages, {local_links} local links; "
          "anchors, assets, navigation, and source/output boundaries checked.")
    print("External URLs, dynamically loaded assets, and Magento runtime behavior are not checked.")


if __name__ == "__main__":
    main()
