# Fabrication Audit — Code Trail (`code-trail`)

**Run audited:** `out/code-trail/20260711-123935/`
**Audited:** 2026-07-11

## What Firecrawl actually returned

- **Query:** `github trending repository today 2026`
- **Title:** Trending repositories on GitHub today
- **URL:** https://github.com/trending
- **Description (verbatim, as captured in `topic.json`):**
  > Trending · wonderwhy-er / DesktopCommanderMCP · oven-sh / bun · abseil / abseil-cpp · addyosmani / agent-skills · jbeder / yaml-cpp · mattpocock / skills · obra / ...

This is a bare list of repo names with no algorithm explanation, no descriptions of what any project does, and no commentary — the entire "ground truth" is a name list.

## Claim-by-claim findings

### hook — "GitHub's trending repositories revealed"
- **Status:** SOURCE-GROUNDED — directly restates the page title/topic.

### concept_card — "Popular open-source projects on GitHub"
- **Traits:** trending, github, repositories
- **Status:** SOURCE-GROUNDED — generic restatement, no specific claim.

### bridge — "But what makes a project trend?"
- **Status:** N/A — rhetorical transition, no factual claim.

### code_demo — "Here's binary search in six lines" + Python `binary_search` snippet
- **Status:** ILLUSTRATIVE-BY-DESIGN — the pipeline's script prompt explicitly asks for a real, syntactically-correct textbook algorithm unrelated to the sourced topic (binary search is not one of the trending repos). Not a claim about the sourced topic at all. Spot-checked the snippet by hand: correct binary search implementation, no bugs.

### explanation — "GitHub's trending algorithm prioritizes activity"
- **Status:** FABRICATED — the Firecrawl snippet contains zero information about how GitHub's trending algorithm works (it's just a repo name list). GitHub does not publicly document its exact trending algorithm. This is NIM asserting a specific mechanism as fact with no source support and no way to verify it's even true.

### mechanism — "GitHub's trending algorithm: a breakdown"
- **Traits:** algorithm, github, trending
- **Status:** FABRICATED (heading for the same ungrounded claim as above) — sets up on-screen framing ("a breakdown") implying an authoritative explanation follows, but nothing in the source backs it.

### conclusion — "Check GitHub daily for new trending projects"
- **Status:** N/A — generic CTA, no factual claim.

## Summary

| Status | Count |
|---|---|
| Source-grounded | 2 |
| Illustrative-by-design | 1 |
| Fabricated | 2 |
| N/A (no claim) | 2 |

**Overall risk: MODERATE.** The two fabricated beats (`explanation`, `mechanism`) invent a specific, named mechanism ("GitHub's trending algorithm") and present it as an authoritative explanation, when the actual source never described any algorithm at all — this is the same shape as the Charlie Kirk date issue (a specific, checkable claim asserted with no grounding), just about a mechanism rather than a date. Not verifiably *false* (GitHub's real ranking does weight recent star velocity), but not sourced either — it's NIM's general training knowledge dressed up as "here's what the trending page told us."
