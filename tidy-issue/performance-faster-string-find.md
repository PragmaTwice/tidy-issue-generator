# Fix `performance-faster-string-find` warning reported by clang-tidy

*This issue is tracked by #1029.*

***We welcome new contributors to take these issues as a beginning of a deep dive to kvrocks***

Currently we have enabled lots of clang-tidy checks, but there are so many reports already exist in the kvrocks code, so we cannot treat these report as errors to block future PR with some clang-tidy reported warnings in CI.

Hence the goal of this issue is to solve all `performance-faster-string-find` tagged clang-tidy reports, and then enable `warnings-as-errors` for this specific check in `.clang-tidy`.

To get clang-tidy reports for latest kvrocks code, there are several ways: you can run `./x.py check tidy` locally, or check the log of the latest run of GitHub Actions on the unstable branch (e.g. https://github.com/apache/incubator-kvrocks/actions/runs/3449328741/jobs/5757148924#step:8:916). To be friendly for new contributors, we list all `performance-faster-string-find` tagged reports below, so in normal cases you can just follow the log below and fix them one by one.

```log
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_stream_base.cc:64:25: warning: 'find' called with a string literal consisting of a single character; consider using the more effective overload accepting a character [performance-faster-string-find]
  auto pos = input.find("-");
                        ^~~
                        '-'
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_stream_base.cc:87:25: warning: 'find' called with a string literal consisting of a single character; consider using the more effective overload accepting a character [performance-faster-string-find]
  auto pos = input.find("-");
                        ^~~
                        '-'
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_stream_base.cc:121:25: warning: 'find' called with a string literal consisting of a single character; consider using the more effective overload accepting a character [performance-faster-string-find]
  auto pos = input.find("-");
                        ^~~
                        '-'
```

Some of these reports will give modification suggestions in the log, you can refer to them directly; otherwise, you need to understand the content of the warning and combine your C++ knowledge to fix it. (Fortunately, most reports (except those by clang static analyzer) are intuitive and easy to fix.)

When you fixed these all reports listed above, you can now add the check `performance-faster-string-find` to `warnings-as-errors` in `.clang-tidy` (in the root dir of the repo): We show a sample diff below to illustrate how to modify `.clang-tidy`:

```diff
--- a/.clang-tidy
+++ b/.clang-tidy
@@ -1,7 +1,7 @@
 # refer to https://clang.llvm.org/extra/clang-tidy/checks/list.html
 Checks: ...

-WarningsAsErrors: ...
+WarningsAsErrors: ..., performance-faster-string-find
```

Then, if all of the above are completed, congratulations, you can submit a PR for your changes now!

