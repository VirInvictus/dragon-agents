# GLM-5.4 (Z.ai) release-day assessment: loop-transformer flagship, Coding Plan only, no published benchmarks

**Date:** 2026-11-23. **As-of:** every source below was fetched live on 2026-11-23 (EST), the same day Z.ai announced the model; GitHub issue timestamps are UTC and quoted as filed. Publication dates are given where the page states them.

**Freshness note (required by dispatch):** GLM-5.4 was announced this morning, so this is genuinely sparse territory. Confirmed on day one: the release blog and docs page (primary, fetched raw), the plan-mechanics docs, a 1045-point Hacker News thread, the ZCode feedback tracker and GLM-5 issue tracker (both carrying day-one GLM-5.4 bug reports), the HuggingFace org listing, OpenRouter's model API, and the X announcement post. Thin or absent: any benchmark number for GLM-5.4 (none exists in text form anywhere I could reach), independent evals (none yet), API pricing (the model is not on general API sale yet), and Reddit thread bodies (blocked at the network layer; titles and search summaries only, flagged single-source throughout). Nothing below is padded from pre-5.4 memory.

**Question as dispatched:** verified facts about GLM-5.4 for a model-routing decision over a 38-agent fleet tiered GLM-5.3-Flash / GLM-5.3, where GLM-5.4 is a candidate audit-tier model: official facts, benchmarks versus GLM-5.3 specifically, pricing and plan availability, the reported over-investigation behavior, strengths, weaknesses, day-one independent evals, and the open-weights angle.

---

## Findings first

1. **GLM-5.4 is Z.ai's first Loop Transformer flagship, and it is an architecture change, not a routine post-training bump.** It "loops 28 layers of the GLM-5 base model for two iterations" at what the blog calls the 750B scale, with gated progressive updates, a hybrid KV cache (cross-loop global sharing plus a per-pass sliding window), and sparse-attention index reuse; Z.ai claims intelligence "comparable to 2T-3T parameter models" (vendor claim) [S1][S2].
2. **Availability today is GLM Coding Plan only.** "The Model API will be made available upon completion of the security assessment" [S1]. All plan tiers (Lite, Pro, Max) got it on release day [S4]. Model IDs: `glm-5.4`, with `glm-5.4[1m]` requesting 1M context in Claude Code [S4].
3. **No benchmark scores are published.** The blog and docs carry only images (a "GLM-5.4 Win Rate" chart and a 30B ablation table) and qualitative claims. Every GLM-5.3-versus-5.4 benchmark comparison the dispatch asks for is therefore unanswered by primary sources on release day; HN commenters flagged the same absence [S1][S2][S6].
4. **Plan economics favor 5.4 heavily.** Credit multipliers are 4.6/1.1/16 (input/cached/output) versus GLM-5.3's 6.9/1.7/24, exactly two-thirds per token on input and output, and weekly-quota plans get "1.5x that of GLM-5.3" in quota for 5.4 [S3][S1]. Derived arithmetic (mine, not vendor): the two together give roughly 2.25x GLM-5.3's effective weekly token budget, but S3's own Estimated Token Allowance table shows 5.4 at only 1.50-1.52x GLM-5.3's weekly tokens in every cell, so whether the quota increase and the multiplier discount stack is unresolved; treat 2.25x as an upper bound and the vendor table's ~1.5x as the planning number.
5. **The over-investigation criticism is partially corroborated, not fully verified.** Z.ai itself admits the model "tends to get caught in overly long 'marathon thinking' loops" [S1][S2]. Community reports of thinking loops and multi-minute responses on 5.4 exist at summary level (single-source). The specific "keeps digging / research without implementing" agent pattern was not found in any reachable source today; see Q4.
6. **Day-one weaknesses on record:** slow interactive turnaround with heavy token usage on small tasks (primary feedback report), writing quality complaints (single-source title-level), and two reproducible endpoint bugs specific to the 5.4 route [S10][S11][S12][S18].
7. **No open weights.** None on HuggingFace (newest zai-org upload remains the 2026-08-25 GLM-5.3 set); the blog promises release "responsibly after completing necessary safety hardening" with no date [S2][S8].
8. **No independent eval was found on any readable surface:** Artificial Analysis 404, OpenRouter unlisted, Aider leaderboard absent; LiveBench renders as a JS shell that established neither presence nor absence [S15][S16][S17].

## Q1. Official facts

**Announcement surfaces.** The release post is https://z.ai/blog/glm-5.4, titled "Toward Generalized Coding with Our First Loop Transformer" (fetched in full via the reader tool; the page's own og-image filename embeds the date 20261123) [S2]. The docs page is https://docs.z.ai/guides/llm/glm-5.4, fetched as raw markdown [S1]. On X, Zixuan Li (@ZixuanLi_) posted "GLM-5.4 is now available to all GLM Coding Plan users" with "50% more quota compared to GLM-5.3" for weekly-quota users; @Zai_org reposted it (1.1M views at fetch) [S7][S19]. The HN submission of the blog went up 2026-11-23T10:06Z and reached 1045 points and 339 comments the same day [S6].

**Architecture.** GLM-5.4 reuses 28 layers of the GLM-5 base model across two iterations, converted from a pre-trained base through continued training rather than trained looped from scratch [S1][S2]. Three modifications at 750B scale: per-token gates per iteration that write candidate updates proportionally into the residual stream (first pass conservative, second pass full-write, step size adapting to token difficulty); a hybrid KV cache where the second loop reuses the first loop's sparse KV plus its own sliding-window KV, so "an extra loop only costs one sliding window of KV cache rather than a full context cache"; and reuse of the first pass's sparse-attention indices, "adding zero indexing overhead" [S2]. Z.ai validated the loop architecture progressively on 1B, 4B, 30B, and 750B bases before committing the flagship [S2].

**Parameter counts: not published for 5.4.** No source gives total or active parameter counts or an MoE breakdown for GLM-5.4; the only figure is the blog's "at the 750B scale" phrasing about the base model [S2]. For reference, the GLM-5 repo's weights table lists the 5.3 family at 744B total / 40B active and 5.3-Flash at 320B / 18B, and that table has no 5.4 row (the repo was last pushed 2026-10-15, before release) [S20].

**Context and modalities.** Context length 1M (a maximum, requested explicitly in Claude Code via the `glm-5.4[1m]` suffix); maximum output 128K [S1][S4]. Input modalities: Video / Image / Text / File; output Text [S1]. The model-switching guide states "Both GLM-5.4 and GLM-5.3-Flash are multimodal models," which positions 5.4 with Flash on image input, unlike the text-only GLM-5.3 [S4].

**Thinking control.** Thinking mode is supported; the docs frame the loop as shifting "part of the reasoning... from explicit output tokens into the implicit depth of the loop" [S1]. Effort control is the same three-value vocabulary as 5.3: `low` / `high` / `max`, default `max`, set in Claude Code via `/effort`; harness values remap (`minimal`/`light`/`low` to low, `medium`/`high` to high, `xhigh`/`max`/`ultra` to max, unknown strings fall back to max with a logged hint); disabling thinking converts to `low` rather than turning it off [S4]. Z.ai recommends `max` "for deeper reasoning and more stable complex task performance" on coding [S4].

**Access channels today:** GLM Coding Plan (subscribe page), ZCode (zcode.z.ai), Z.ai Chat (chat.z.ai); Model API listed as "Coming Soon" [S2]. Open weights: planned, undated, license unstated [S2].

## Q2. Benchmarks versus GLM-5.3

**The core finding is an absence.** As of fetch time on release day, no GLM-5.4 benchmark score exists in text form in any source I could reach, vendor or independent. The blog's only quantitative material: the 30B iso-parameter ablation (identical parameter counts, roughly 10% more training compute, clear gains largest in "math, scientific reasoning, and long-context tasks," and average output length down 10–14% on GPQA-Diamond and MMLU-Pro, "mostly from shorter chains of thought"), and inference throughput of "up to 200 tokens/s" off-peak and 70–80 tokens/s at peak [S2]. The docs add a "GLM-5.4 Win Rate" figure whose contents are an image I cannot read, and the ablation table is likewise image-only [S1]. HN commenters called the gap out immediately ("Hard to say how good this is without benchmarks... or else they would have included the scores?"; "The benchmarks are from an unspecified 30B model based on the same architecture"), with speculation that scores are withheld pending cyber-capability hardening (commenter speculation, labeled as such) [S6].

For orientation, the incumbent's own vendor-reported numbers, which any future 5.4 comparison will be measured against (all vendor-reported, from the GLM-5.3 docs page fetched today) [S14]:

| Benchmark | GLM-5.3 (vendor-reported) | GLM-5.4 | Notes |
|---|---|---|---|
| Terminal-Bench 3.0 | 28.3 (up from 4.6 on GLM-5.2) | not published | [S14] |
| DeepSWE v1.1 | 66.9 (up from 46.2) | not published | [S14] |
| Agents' Last Exam | 28.5 (up from 23.8) | not published | [S14] |
| Z.ai Code Bench (in-house) | 34.5% at ~75K output tokens, Max effort | not published | private benchmark; 31.4% at ~50K at High beat Claude Opus 4.8's 29.5% at 120K [S14] |
| CyberGym | 84.5% (5.2: 77.2%) | not published | [S14] |
| ExploitBench | 54.4% (5.2: 24.4%) | not published | [S14] |
| ExploitGym | 105 tasks / 2h, 130 / 6h | not published | [S14] |
| SWE-bench Verified | not on the 5.3 docs page fetched today | not published | no number for either model in today's sources |
| LiveCodeBench, tau2-bench, BFCL v3, GPQA Diamond, AIME/HMMT | not on the 5.3 docs page fetched today | not published | GPQA-Diamond and MMLU-Pro appear for 5.4 only as output-length deltas in the 30B ablation [S2] |

One secondhand independent datapoint for the eventual comparison: an HN commenter cites Artificial Analysis scoring GLM-5.3 at Intelligence Index 32 at max effort versus 23 at low, as the reference for what effort changes on the incumbent [S6].

## Q3. Pricing and availability

**API (pay-as-you-go): GLM-5.4 is not on sale and has no published price.** The pricing page's Latest Models table lists GLM-5.3 at $1.4 input / $0.26 cached input / $4.4 output per million tokens, GLM-5.3-Flash at $0.15 / $0.03 / $0.50, and GLM-5.3-FlashX at $0.37 / $0.075 / $1.25; there is no GLM-5.4 row [S5]. The docs tip box states the Model API "will be made available upon completion of the security assessment" [S1].

**Coding Plan: available to every tier on day one.** "The GLM Coding Plan now supports the latest GLM-5.4 model for all users (Max, Pro, and Lite)" [S4]; the plan overview adds "All plans support GLM-5.4, GLM-5.3 and GLM-5.3-Flash" [S3]. Quota: "For users on weekly quota plans, the available quota for GLM-5.4 is increased to 1.5x that of GLM-5.3" [S1], phrased on X as "50% more quota compared to GLM-5.3" [S7].

**Credit multipliers (per 10,000 tokens in the credit formula):**

| Model | Input | Cached input | Output |
|---|---|---|---|
| GLM-5.4 | 4.6 | 1.1 | 16 |
| GLM-5.3 | 6.9 | 1.7 | 24 |
| GLM-5.3-Flash | 2.3 | 0.56 | 8 |

Source: plan overview, fetched today [S3]. GLM-5.4's per-token credit cost is exactly two-thirds of GLM-5.3's on input and output (4.6/6.9 and 16/24). Off-peak still bills at 50% of standard credits, peak being weekdays 14:00-18:00 Singapore time [S3]. Derived arithmetic (mine, not a vendor claim): combining the 1.5x weekly quota with the two-thirds per-token cost, a weekly-quota subscriber would get roughly 2.25x GLM-5.3's effective weekly output-token budget on 5.4. That stacking assumption is unresolved: the same page's Estimated Token Allowance table (the vendor's own planning numbers) shows 5.4 at 1.50-1.52x GLM-5.3's weekly tokens in all 18 cells, consistent with the quota sentence describing the multiplier discount itself rather than an additional grant. Treat 2.25x as an upper bound. How the 1.5x interacts with the 5-hour rolling credit window is also not stated in the pages fetched.

**Endpoints.** No general Model API yet [S1]. Day-one issue reproductions confirm 5.4 is served on the Coding Plan's Anthropic-compatible gateway (`https://api.z.ai/api/anthropic/v1/messages`) and the coding endpoint (`https://api.z.ai/api/coding/paas/v4/chat/completions`) [S10][S11], matching the 5.3-era endpoint set.

**Against the dispatch's harness context** (individual Coding Plan account sees GLM-5.4; idle and highspeed accounts do not): the public docs support the first half exactly, since every Coding Plan tier (Lite/Pro/Max) received 5.4 today [S3][S4]. No public doc mentions account classes named "idle" or "highspeed"; if those are non-Coding-Plan surfaces (different products or API-only accounts), the docs are consistent with the observation, but public pages cannot confirm or contradict it further.

**Day-one endpoint bugs, both specific to the 5.4 route:** GLM-5 issue #183 (open, filed 14:06 UTC after a failure window the reporter dates to 13:39 UTC): every `anthropic-beta` header value tested returns HTTP 529 `overloaded_error [1305]` on `glm-5.4` while the identical request returns 200 on `glm-5.3` and `glm-5.3-flash`; dropping the header, the same glm-5.4 request returns 200. The reporter notes it breaks Claude Code auto mode [S10]. ZCode feedback #1630 (open): 100% of requests fail with HTTP 429 code 1305 when and only when the system prompt contains the exact case-sensitive string "You run on Hermes Agent," on `glm-5.4` via the coding endpoint; `glm-5.3` unaffected, reworded first line passes [S11].

## Q4. The over-investigation criticism

**What is verified:**

- **The official admission, in the release post and docs verbatim:** "The model still has some limitations. Most notably, it tends to get caught in overly long 'marathon thinking' loops, though this prolonged reflection and self-correction does consistently improve accuracy beyond its parameter count" [S1][S2]. This is a thinking-side behavior (prolonged reflection), not specifically a tool-use pattern.
- **Community reports of thinking loops on 5.4, at summary level only:** search summaries of r/ZaiGLM day-one threads include "5.4 takes 10 minutes to answer per prompt" and "gets stuck in thinking loops" (single-source; thread bodies unreachable, see dead-end log) [S18].
- **A primary steerability report:** ZCode feedback #1629 (open, filed 12:54 UTC on release day): GLM-5.4 on the individual Coding Plan "feels very slow for interactive, time-boxed coding work" with "long generations and heavy token usage," while "its quality on bigger multi-file builds is excellent"; the filer asks for a per-task effort/speed control [S12]. This documents slowness and token burn, not a research-without-action loop.
- **Lineage context for why the criticism is plausible:** HN carries standing complaints about overthinking across the GLM line (a quoted measurement of output per task growing from 118k tokens on 5.1 to 274k on 5.2; "This is why the 5.3 quota exhausted so fast"), and about reasoning-heavy Chinese-model behavior generally [S6].

**What is not verified:** the dispatch's specific phrasing, agents that are "overly investigative / keep digging / continue exploring without implementing a fix," appears in no reachable source as of today. No report of endless tool-call loops, exploration-without-implementation, or per-task token-burn measurements on GLM-5.4 specifically. That is a finding about release-day evidence, not a refutation; the model has been public for hours.

**Mitigations on record:** the effort control exists (`low`/`high`/`max`, default `max`, `/effort` in Claude Code) [S4]; no official mitigation for marathon thinking is documented anywhere fetched; feedback #1629 explicitly requests better per-task speed control, implying the existing effort lever felt insufficient to that user for interactive work [S12]; on 5.3, dropping to low effort carried a large quality cost per the AA numbers cited on HN (index 32 to 23), and no equivalent trade-off measurement exists for 5.4 yet [S6]. No step-cap or prompt-constraint guidance for 5.4 is published.

## Q5. Reported strengths

- **Deeper reasoning at fixed parameters (vendor).** The loop adds effective depth without parameter growth; ablation gains concentrate in math, scientific reasoning, and long-context tasks; output length on GPQA-Diamond and MMLU-Pro dropped 10–14%, which the blog frames as reasoning moving from explicit tokens into loop depth [S2].
- **Generalized Coding demos (vendor, unprompted showcases):** a self-narrated music video, a complete game with physics and art assets, a 6-axis robotic arm modeled in FreeCAD, and an interactive 3D scene in GLSL [S2]. These are curated demos, not benchmark results.
- **Throughput and cost claims (vendor):** "up to 200 tokens/s" off-peak, 70–80 tokens/s at peak; deployment cost increase over GLM-5.3 "well under control" at 1M context thanks to the hybrid KV design [S2].
- **Coding quality, day-one community signal:** r/LocalLLaMA thread titled "GLM 5.4 is great at coding..." [S18]; feedback #1629's "quality on bigger multi-file builds is excellent" (primary) [S12]; one r/ZaiGLM summary has it "beats many other harnesses in overall performance" (single-source) [S18]; the X announcement claims "stronger all-round coding performance" (vendor) [S7].
- **Practical headroom:** the vendor's own Estimated Token Allowance table grants 5.4 about 1.5x GLM-5.3's weekly tokens (my ranking: the most quota-generous strong-tier model on the plan today); the two-thirds multipliers would imply up to 2.25x if they stack on top, which the vendor table does not show (see Q3) [S1][S3].

## Q6. Reported weaknesses and regressions

- **Writing quality:** r/LocalLLaMA thread "GLM 5.4 is great at coding. But absolutely garbage at writing and anything but that. Are future open weight models going to be just codemaxxed??" (title-level, single-source; body unreachable) [S18].
- **Interactive latency:** feedback #1629, slow for quick fixes and small refactors, discouraging everyday use despite build quality (primary) [S12]; r/ZaiGLM summaries of 10-minute responses (single-source) [S18].
- **Marathon thinking:** the official limitation above [S1][S2].
- **One unimpressed debugging comparison:** an r/ZaiGLM user ran a codebase debug on both DS 4.1 Flash 1017 and GLM-5.4 at Max effort and was "not impressed at all so far" (single-source, summary-level) [S18].
- **Endpoint bugs on day one:** the 529-on-beta-header failure [S10] and the deterministic 429-on-system-prompt-string failure [S11]; a third report logs mid-task "Reconnecting 5/10" stalls during a long 5.4 run in ZCode desktop [S13].
- **Transparency regression versus the 5.3 launch:** GLM-5.3 shipped with a public benchmark table and harness configs; 5.4 shipped with none [S14 versus S1][S6].
- **No API, no weights, no independent numbers yet** [S1][S5][S8][S15][S16].

## Q7. Day-one independent evals

None were found on any readable surface as of fetch time. Artificial Analysis has no GLM-5.4 page (HTTP 404) [S16]. OpenRouter's model API lists the full GLM family including 5.3, 5.3-prime, flashx variants, and no 5.4, so there is also no usage or ranking signal [S15]. The Aider polyglot leaderboard shows no GLM entry of any version, and its footer reads "last updated November 20, 2025," which predates even GLM-5.3, so its absence is weak evidence of anything except its own staleness [S17]. LiveBench rendered as a JS shell with no extractable model table (dead-end log).

## Q8. Open-weights angle

No weights exist publicly. The HuggingFace org's newest models remain GLM-5.3 / GLM-5.3-Flash / their BF16 twins, all created 2026-08-25 [S8]. The blog's Getting Started section: "Open Weights: We plan to open-source the model weights responsibly after completing necessary safety hardening" [S2]; the API is gated behind the same safety assessment [S1]. Consequently there are no vLLM, SGLang, llama.cpp, or quantization reports to report, and the GLM-5 repo's weights table has no 5.4 row [S20]. An HN commenter expects weights in "a few weeks" based on prior GLM cadence (speculation, labeled) [S6]. Adjacent context from the same thread: Thinking Machines released Inkling 2 Mini, an open-weights looped model, the week before, making GLM-5.4 by that thread's framing the second looped-model release but the first at flagship scale [S6].

---

## Sources

All fetched 2026-11-23 unless noted. Vendor-reported numbers and claims are labeled at point of use; Reddit items are search-summary evidence with bodies unreachable.

| # | URL | What it supported | As-of |
|---|---|---|---|
| S1 | https://docs.z.ai/guides/llm/glm-5.4 (fetched as raw .md) | Plan-availability tip verbatim, modalities, 1M/128K, capability list, marathon-thinking limitation, win-rate image existence | 2026-11-23 |
| S2 | https://z.ai/blog/glm-5.4 ("Toward Generalized Coding with Our First Loop Transformer") | Full release post: loop architecture, 28 layers x 2 iterations, 750B scale, KV and gating design, 30B ablation claims, throughput, Getting Started (API coming soon, open weights planned), Looking Ahead | 2026-11-23 |
| S3 | https://docs.z.ai/devpack/overview | "All plans support GLM-5.4...", credit multiplier table (4.6/1.1/16), off-peak 50%, peak window | 2026-11-23 |
| S4 | https://docs.z.ai/devpack/latest-model | All-tiers availability (Max/Pro/Lite), glm-5.4 and glm-5.4[1m] model IDs, effort table and fallbacks, max-for-coding recommendation, 5.4-and-Flash-multimodal statement | 2026-11-23 |
| S5 | https://docs.z.ai/guides/overview/pricing | No GLM-5.4 row; 5.3 / Flash / FlashX per-million prices | 2026-11-23 |
| S6 | https://news.ycombinator.com/item?id=50609685 (1045 pts, 339 comments; comments pulled via hn.algolia.com API) | Benchmark-absence reactions and speculation, lineage overthinking complaints (118k to 274k quote), AA 32/23 reference for 5.3, Inkling 2 Mini context, weights-cadence speculation | 2026-11-23 |
| S7 | https://x.com/ZixuanLi_/status/2124719275864670681 | "available to all GLM Coding Plan users", "50% more quota compared to GLM-5.3", glm-5.4[1m] usage note, no-benchmarks reply | 2026-11-23 |
| S8 | https://huggingface.co/api/models?author=zai-org (keyless API) | No GLM-5.4 weights; newest zai-org uploads dated 2026-08-25 | 2026-11-23 |
| S9 | https://api.github.com/orgs/zai-org/repos (keyless API) | No GLM-5.4 repo; GLM-5 last pushed 2026-10-15; ZCode and zcode-plugins pushed on release day | 2026-11-23 |
| S10 | https://github.com/zai-org/GLM-5/issues/183 (filed 2026-11-23T14:06Z) | 529 overloaded_error [1305] on any anthropic-beta header, glm-5.4 only; endpoint URLs | 2026-11-23 |
| S11 | https://github.com/zai-org/feedback/issues/1630 (filed 2026-11-23T13:55Z) | Deterministic 429 code 1305 on system-prompt string "You run on Hermes Agent", glm-5.4 only; coding endpoint URL | 2026-11-23 |
| S12 | https://github.com/zai-org/feedback/issues/1629 (filed 2026-11-23T12:54Z) | Slow interactive work, heavy token usage, excellent multi-file build quality, per-task effort request | 2026-11-23 |
| S13 | https://github.com/zai-org/feedback/issues/1628 (filed 2026-11-23T12:54Z) | Mid-task "Reconnecting 5/10" during long GLM-5.4 run, ZCode desktop 4.0.0 | 2026-11-23 |
| S14 | https://docs.z.ai/guides/llm/glm-5.3 (fetched as raw .md) | GLM-5.3 vendor benchmark baselines (Terminal-Bench 3.0, DeepSWE, ALE, Z.ai Code Bench, CyberGym, ExploitBench, ExploitGym) | 2026-11-23 |
| S15 | https://openrouter.ai/api/v1/models (keyless API) | Full GLM family listing with no GLM-5.4 entry | 2026-11-23 |
| S16 | https://artificialanalysis.ai/models/glm-5-4 | HTTP 404, no page exists | 2026-11-23 |
| S17 | https://aider.chat/docs/leaderboards/ | No GLM entries; footer "last updated November 20, 2025" | 2026-11-23 |
| S18 | Reddit, titles and search summaries only: r/LocalLLaMA comments/1y3lqu3 ("great at coding... garbage at writing"), comments/1y392m4 ("No benchmarks yet, hands-on feedback is much more precious"), comments/1y3enps, r/singularity comments/1y3flzd, r/ZaiGLM day-one threads ("10 minutes to answer", "stuck in thinking loops", DS 4.1 Flash debug comparison, "beats many other harnesses") | Day-one community sentiment; all single-source at summary level, bodies blocked | 2026-11-23 |
| S19 | https://x.com/Zai_org/status/2124719658074825004 | Official account's repost of S7 (not an original announcement); engagement figures | 2026-11-23 |
| S20 | https://github.com/zai-org/GLM-5 (README via raw.githubusercontent.com) | Weights table 744B-A40B / 320B-A18B with no 5.4 row; 5.3-equals-5.2-base statement | 2026-11-23 |

## Dead-end log

- **WebSearch rate-limiting:** the first three queries (announcement, benchmarks, pricing) all returned 429 / error 1302 with no results; the service recovered minutes later and delivered the Reddit and thinking-loop results, then 429'd again on two follow-up queries. Intermittent, not permanent; direct fetches carried the load meanwhile.
- **z.ai/blog/glm-5.4 via WebFetch:** empty body (JS-rendered page, same behavior as the 5.3-flash blog in the sibling report). Full text recovered on the first try through the web reader tool; no reader retries were needed this run.
- **Reddit thread bodies, every route:** the .json endpoint returns 403, old.reddit returns a 302 (block), WebFetch returns an empty shell, and the reader tool returns the JS skeleton ("Reddit - The heart of the internet" plus a tracking pixel). Titles and search-result summaries are the only usable layer; every Reddit-derived claim above is flagged single-source.
- **Artificial Analysis GLM-5.4 page:** 404. Expected on day one; recorded so the next researcher re-checks rather than assumes.
- **LiveBench (livebench.ai):** renders a title-only shell ("LiveBench 2.0") with the table behind JS; no model data extractable by fetch. Neither presence nor absence of GLM-5.4 could be established.
- **Aider polyglot leaderboard:** no GLM models at all, and the footer's "last updated November 20, 2025" predates GLM-5.3, so the page is stale rather than evidence of a fresh omission.
- **OpenRouter:** no glm-5.4 entry (also logged as a Q7 finding, since it forecloses usage-rank signals).
- **zai-org/GLM-5 repo:** no 5.4 mention anywhere; last push 2026-10-15, before the release. No 5.4-specific repo exists in the org (S9).
- **ZCode README:** no model-name mentions to extract; the repo was pushed on release day but the README does not name models.

## Unknowns

- **Total and active parameter counts, MoE structure, for GLM-5.4.** Only "at the 750B scale" is published [S2]; the family table stops at 5.3 [S20].
- **Every benchmark score.** The win-rate chart and the 30B ablation table are images; their numeric contents are unread in this pass (text-only research seat). No vendor or independent score exists in text form.
- **API pricing and general-availability date**, gated behind an unspecified "security assessment" [S1][S5].
- **Weights release date and license** [S2].
- **Whether the marathon-thinking behavior is better or worse than GLM-5.3's**: no controlled comparison exists on day one; the official text claims accuracy gains from the prolonged reflection without quantifying the latency cost [S2].
- **The dispatch's exact over-investigation pattern** (endless tool-call loops, research without implementation, per-task token burn on 5.4): unverified in reachable sources today.
- **Effort-versus-quality trade-off on 5.4**: the control exists, but no measurement of what low effort costs on 5.4 (the 32-to-23 AA drop is a 5.3 figure, secondhand) [S4][S6].
- **How the 1.5x weekly quota interacts with the 5-hour rolling window**, and any RPM/TPM differences on the 5.4 route (the rate-limits page remains login-walled per the sibling report).
- **Community sentiment depth**: Reddit bodies are blocked, so day-one reports rest on titles and summaries; the r/ZaiGLM threads could not be captured with URLs.
- **The "idle" and "highspeed" account classes** from the dispatch context: not documented in any public page fetched; unverifiable beyond the all-Coding-Plan-tiers statement.
- **Whether the 1.5x weekly quota and the two-thirds credit multipliers stack.** S3's Estimated Token Allowance table (1.50-1.52x in all 18 cells) suggests they may not; 2.25x is derived upper-bound arithmetic, not a vendor figure.
- **S1 and S2 are not independent sources.** The blog bundle sets its embedded document to the docs page URL, and the docs page mirrors the blog's architecture section; the marathon quote appears in both because they share text.

**Confidence:** high on official release facts, plan mechanics, pricing-table state, and the benchmark absence (multiple primary pages fetched raw, cross-checked against day-one issue reproductions that exercise the live endpoints); high on the day-one endpoint bugs (primary issue reports with curl reproductions); medium on the marathon-thinking community signal (official admission is primary, the r/ZaiGLM loop reports are single-source summaries); low on writing-quality and debugging-comparison reports (title-level only); the derived quota arithmetic is labeled as mine wherever it appears.
