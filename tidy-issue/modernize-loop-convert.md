# Fix `modernize-loop-convert` warning reported by clang-tidy

*This issue is tracked by #1029.*

***We welcome new contributors to take these issues as a beginning of a deep dive to kvrocks***

Currently we have enabled lots of clang-tidy checks, but there are so many reports already exist in the kvrocks code, so we cannot treat these report as errors to block future PR with some clang-tidy reported warnings in CI.

Hence the goal of this issue is to solve all `modernize-loop-convert` tagged clang-tidy reports, and then enable `warnings-as-errors` for this specific check in `.clang-tidy`.

To get clang-tidy reports for latest kvrocks code, there are several ways: you can run `./x.py check tidy` locally, or check the log of the latest run of GitHub Actions on the unstable branch (e.g. https://github.com/apache/incubator-kvrocks/actions/runs/3449328741/jobs/5757148924#step:8:916). To be friendly for new contributors, we list all `modernize-loop-convert` tagged reports below, so in normal cases you can just follow the log below and fix them one by one.

```log
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/task_runner.cc:57:3: warning: use range-based for loop instead [modernize-loop-convert]
  for (size_t i = 0; i < threads_.size(); i++) {
  ^   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      (auto & thread : threads_)
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/stats/stats.cc:33:5: warning: use range-based for loop instead [modernize-loop-convert]
    for (int j = 0; j < STATS_METRIC_SAMPLES; j++) {
    ^   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        (unsigned long & sample : im.samples)
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/stats/stats.cc:108:3: warning: use range-based for loop instead [modernize-loop-convert]
  for (int j = 0; j < STATS_METRIC_SAMPLES; j++) sum += inst_metrics[metric].samples[j];
  ^   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      (unsigned long sample : inst_metrics[metric].samples) sample
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/redis_db.cc:614:3: warning: use range-based for loop instead [modernize-loop-convert]
  for (size_t i = 0; i < args_.size(); i++) {
  ^   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      (auto & arg : args_)
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_set.cc:311:3: warning: use range-based for loop instead [modernize-loop-convert]
  for (size_t i = 0; i < keys.size(); i++) {
  ^   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      (auto key : keys)
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_string.cc:140:3: warning: use range-based for loop instead [modernize-loop-convert]
  for (size_t i = 0; i < ns_keys.size(); i++) {
  ^   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      (auto & ns_key : ns_keys)
```

Some of these reports will give modification suggestions in the log, you can refer to them directly; otherwise, you need to understand the content of the warning and combine your C++ knowledge to fix it. (Fortunately, most reports (except those by clang static analyzer) are intuitive and easy to fix.)

When you fixed these all reports listed above, you can now add the check `modernize-loop-convert` to `warnings-as-errors` in `.clang-tidy` (in the root dir of the repo): We show a sample diff below to illustrate how to modify `.clang-tidy`:

```diff
--- a/.clang-tidy
+++ b/.clang-tidy
@@ -1,7 +1,7 @@
 # refer to https://clang.llvm.org/extra/clang-tidy/checks/list.html
 Checks: ...

-WarningsAsErrors: ...
+WarningsAsErrors: ..., modernize-loop-convert
```

Then, if all of the above are completed, congratulations, you can submit a PR for your changes now!

