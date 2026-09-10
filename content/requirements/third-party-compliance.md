# Third-party adoption and commercial release requirements

Status: **required product practice; implementation and release clearance outstanding**.
Updated: 7 September 2026. The user requires third-party rights and obligations to be checked
before the product depends on a tool, and again before commercialization.

This requirement applies to the core editor and any future theme ecosystem. The future marketplace
remains a planning project with no tasks. This document defines the review process; it does not
certify compliance with every applicable law or approve any product dependency for release.

## Scope

Cover direct and transitive software dependencies, browser bundles, server libraries, Magento and
Hyvä packages, copied code, theme templates, fonts, icons, images, demo content, build/documentation
tools, SDKs, and hosted services. Review what is actually used or shipped, including assets obtained
outside package managers. Development-only tools still have their own usage terms; determine whether
their output contains licensed material rather than assuming every build tool is redistributed.

Treat an open-source core, paid extension, cloud service, and enterprise SDK as separate products
with potentially different terms. A free trial, public repository, or marketing claim is not a
substitute for permission covering the intended commercial use.

## Before adoption

Before selecting a dependency for product implementation, create a review record with:

| Record field | Required evidence |
| --- | --- |
| Identity and provenance | Name, publisher, source/package URL, exact version or commit, edition, and artifact identity where available |
| License or contract | License texts, notices and relevant file-level exceptions; SPDX expression where applicable; service terms with review date or contract version |
| Intended use | Hosted service, delivered browser code, Magento distribution, theme distribution, development-only use, or licensed content; modifications and embedded output |
| Permissions and obligations | Commercial use, modification, redistribution, embedding/white-label use, sublicensing or resale where needed, attribution, notices, source obligations, and trademark restrictions |
| Commercial limits | Applicable domains, stores, users/seats, traffic, usage or revenue thresholds, fees, renewal, termination, and continued-use rights |
| Service data | What data leaves the product, recipient, purpose, applicable retention/training terms, processing arrangements and operating regions |
| Dependency coverage | Transitive packages, bundled/copied code, plugins and assets; known gaps and the method used to check them |
| Review outcome | Accepted for the specified use, unresolved, or rejected; rationale, required implementation actions, reviewer and date, evidence links, and change triggers |

Acceptance is tied to a version/edition and use case. It is not a perpetual approval of a brand
or an assertion that the entire product is legally cleared.

An engineer can complete routine reviews where the published terms clearly cover the intended use
and the obligations are understood. Ambiguous redistribution rights, disputed provenance, unclear
copyleft interactions, or custom contracts need qualified legal review before adoption. Record the
specific uncertainty; do not invent a universal requirement to obtain legal approval for every
permissively licensed package.

Research may continue while a candidate is unresolved, subject to its research/trial terms.
Do not merge that candidate into the production dependency set or make the architecture depend
on rights that have not been established. Prefer an already-reviewed alternative when practical.

## During implementation and upgrades

Keep exact dependency locks and a human-reviewed third-party register. Identify new or changed
dependencies and license/edition changes during code review, including transitive changes. Reassess
terms when usage changes, such as moving from internal tooling to a customer-facing service,
redistributing a Magento package, or adding paid plugins.

Produce a software bill of materials for the release from the actual dependency graph and
artifacts, using a suitable standard such as SPDX. Track hosted-service contracts and separately
sourced assets alongside it. A scanner is evidence, not a legal decision: SPDX explicitly excludes
legal interpretation and determination of compliance actions from its scope.
[SPDX overview](https://spdx.dev/learn/overview/)

Preserve required upstream notices in source and delivered packages. Define where applicable
licenses and notices appear in the actual browser bundles, downloadable modules, theme packages,
containers, and other distribution materials. Generate or maintain a third-party notices artifact
and verify it survives production bundling. Do not replace upstream notices with our copyright.

Automated dependency/license checks should eventually flag missing or unrecognized terms and
changes for review. No product SBOM, scanner, CI enforcement, or third-party notices artifact
has been implemented by this planning change.

## Before commercial release

| ID | Required result |
| --- | --- |
| TP-01 | Every adopted direct dependency, transitive dependency, service, and included asset has a review outcome for its actual use |
| TP-02 | The reviewed inventory matches the exact release, including browser assets, Magento packages, theme packages and packaged dependencies |
| TP-03 | Applicable licenses, attribution, notices and any source-related obligations are fulfilled in the distribution or service as required |
| TP-04 | Paid SDK/service entitlements cover the intended deployment, customer scope and commercial model; unresolved rights are excluded from release |
| TP-05 | Applicable service-data obligations and asset redistribution rights have been assessed and implemented |
| TP-06 | Unresolved legal interpretations are resolved by qualified counsel or the affected component is replaced or removed |
| TP-07 | A dated review records the release commit/artifact identities, evidence, reviewer, remaining limits, and completed obligations |

Do not label a release compliant because an upstream license permits commercial use or because
a dependency scanner passed. The release review must cover the actual combination and distribution.
General privacy, consumer, tax, payment, trademark, patent, and other legal questions depend on the
product and jurisdictions and require appropriate separate assessment where relevant.

## License distinctions that affect architecture

MIT and BSD-3-Clause permit commercial use subject to their conditions. MIT requires the copyright
and permission notice in copies or substantial portions; BSD-3-Clause includes source/binary notice
conditions and a non-endorsement condition. These are useful starting points, not exemptions from
dependency review.
[MIT license](https://opensource.org/license/mit),
[BSD-3-Clause license](https://opensource.org/license/bsd-3-clause)

Commercial use and keeping every component proprietary are separate questions. Copyleft does not
automatically prohibit charging money; source and distribution obligations depend on the license
and how the software is used. For example, AGPL contains obligations concerning modified versions
used through a network. Do not assume hosted deployment removes all source-related obligations.
[AGPL-3.0 license text](https://spdx.org/licenses/AGPL-3.0-only.html)

GrapesJS core's license does not grant the separate Studio SDK entitlement; deploying Studio on a
public web domain requires its own configured license. Likewise, a JavaScript library review does not
establish the rights for a Magento/Hyvä derivative theme, a purchased template, a font, or a vendor's
hosted service.
[GrapesJS Studio SDK licensing](https://app.grapesjs.com/docs-sdk/overview/licenses)

## Current evidence limits

The earlier discussion checked the published upstream licenses of several proposed JavaScript
libraries. No product versions, complete transitive dependency graph, final bundle, deployment
contract set, or complete asset inventory has been reviewed for release. Those upstream checks
remain candidate evidence only. This process should be applied before implementation choices become
costly to replace, then repeated for the exact release and relevant subsequent changes.

## Planning references

The core Linear project contains the
[third-party requirements artifact](https://linear.app/solventech/document/magethemeeditor-third-party-adoption-and-commercial-release-7d5f78809e85).
Existing planning issues now cover the two stages:

- [SOL-491: scope and adoption prerequisites](https://linear.app/solventech/issue/SOL-491/define-mvp-scope-and-the-storefront-support-matrix).
- [SOL-517: licensing and commercial release evidence](https://linear.app/solventech/issue/SOL-517/define-pricing-licensing-data-ownership-and-subscription-behavior).

These additions define outstanding acceptance criteria. They do not complete either issue or
introduce tasks in the separate future marketplace project. The original research and dated Linear
baseline remain historical records.
