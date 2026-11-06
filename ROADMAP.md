# Roadmap

Goal: decide, with numbers instead of intuition, whether SBPP's shared
backup capacity is actually worth it against Fast Reroute and global
recompute — and write that up for the exam.

## Milestones

- [x] **1. Proposal** — problem, hypotheses, experimental plan agreed and
      sent (`docs/proposta.pdf`).
- [x] **2. Scaffold** — package layout and the shared `RecoveryStrategy`
      interface, so the three strategies are comparable from day one.
- [ ] **3. One strategy, end to end** — prove the pipeline works before
      investing in MILP.
- [ ] **4. The other two strategies** — the actual comparison becomes
      possible once all three exist.
- [ ] **5. Metrics and plots** — turn raw runs into the four figures from
      the proposal.
- [ ] **6. Experimental campaign** — run it for real, across topologies,
      loads and failure types.
- [ ] **7. Analysis and report** — read the results, check the hypotheses,
      write the final document.

Each milestone only starts once the previous one is done — there's no
point tuning plots on fake data, or running a campaign on solvers that
aren't implemented yet.

---

## 3. One strategy, end to end

Pick Fast Reroute first: it's shortest-path routing, no MILP, so it
validates the plumbing (topology → failure → plan → react → metrics)
without also debugging an optimization model at the same time.

- `topology.random_network` / `random_demands` — connected random graphs
  with capacities, sampled demands.
- `failure.single_link_failures` — one scenario per edge.
- `solvers.fast_reroute.FastReroute` — shortest-path primaries, a
  precomputed detour per link.
- `metrics.restoration_rate` and `metrics.path_stretch` — the two metrics
  that don't need capacity-overhead bookkeeping.
- `benchmark.run` wired enough to produce one `BenchmarkResult` per
  (strategy, failure) pair for this single strategy.

Done when: `benchmark.run` on a small random network with only
`FastReroute` produces sane, inspectable results — by hand-checking a
few, not by trusting the numbers blindly.

## 4. The other two strategies

- `solvers.sbpp.SBPP` — MILP per the proposal's formulation (primary +
  disjoint backup per demand, shared reserve across non-simultaneous
  failures). Start with `pulp` + the default CBC solver.
- `solvers.global_recompute.GlobalRecompute` — monolithic variant first
  (re-solve everything), incremental variant after, since monolithic is
  the simpler MILP.
- `metrics.capacity_overhead` and `metrics.churn` now apply.

Done when: all three strategies run through the same `benchmark.run` call
on the same scenario and produce comparable metrics.

## 5. Metrics and plots

- Extend `BenchmarkResult` / `benchmark.run` with whatever columns the
  plots need that don't exist yet (load factor, network size).
- Implement `plotting.py`'s four figures against real (not fake)
  benchmark output, on the small network first.

Done when: the four figures render from one `benchmark.run` call without
manual data wrangling.

## 6. Experimental campaign

- Load real topologies (SNDlib, Topology Zoo) via NetworkX, per the
  proposal.
- Sweep load factor, failure type (single / double / shared-risk group),
  and strategy, with enough random instances per combination for
  confidence intervals.
- Use the campaign-size calculator logic from the proposal to size this
  before running it unattended overnight.

Done when: a full campaign run produces the CSV the final figures and
report are built from.

## 7. Analysis and report

- Re-render the four figures on the real campaign data.
- Check each of the four hypotheses from the proposal against what the
  data actually shows — including the ones that turn out false.
- Write the final report, explicit about the declared limitations
  (network size, solver time limits, link-only protection, synthetic
  traffic).
