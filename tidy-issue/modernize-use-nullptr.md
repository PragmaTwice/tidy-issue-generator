# Fix `modernize-use-nullptr` warning reported by clang-tidy

*This issue is tracked by #1029.*

***We welcome new contributors to take these issues as a beginning of a deep dive to kvrocks***

Currently we have enabled lots of clang-tidy checks, but there are so many reports already exist in the kvrocks code, so we cannot treat these report as errors to block future PR with some clang-tidy reported warnings in CI.

Hence the goal of this issue is to solve all `modernize-use-nullptr` tagged clang-tidy reports, and then enable `warnings-as-errors` for this specific check in `.clang-tidy`.

To get clang-tidy reports for latest kvrocks code, there are several ways: you can run `./x.py check tidy` locally, or check the log of the latest run of GitHub Actions on the unstable branch (e.g. https://github.com/apache/incubator-kvrocks/actions/runs/3449328741/jobs/5757148924#step:8:916). To be friendly for new contributors, we list all `modernize-use-nullptr` tagged reports below, so in normal cases you can just follow the log below and fix them one by one.

```log
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/redis_db.cc:338:30: warning: use nullptr [modernize-use-nullptr]
    unsigned int seed = time(NULL);
                             ^~~~
                             nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/storage.cc:340:37: warning: use nullptr [modernize-use-nullptr]
  rocksdb::Checkpoint *checkpoint = NULL;
                                    ^~~~
                                    nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/storage.cc:733:39: warning: use nullptr [modernize-use-nullptr]
    rocksdb::Checkpoint *checkpoint = NULL;
                                      ^~~~
                                      nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:169:15: warning: use nullptr [modernize-use-nullptr]
  if (hash == NULL || step > 32 || step == 0 || RANGEPISZERO(lat_range) || RANGEPISZERO(long_range)) return 0;
              ^~~~
              nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:206:27: warning: use nullptr [modernize-use-nullptr]
  if (HASHISZERO(hash) || NULL == area || RANGEISZERO(lat_range) || RANGEISZERO(long_range)) {
                          ^~~~
                          nullptr
```

Some of these reports will give modification suggestions in the log, you can refer to them directly; otherwise, you need to understand the content of the warning and combine your C++ knowledge to fix it. (Fortunately, most reports (except those by clang static analyzer) are intuitive and easy to fix.)

When you fixed these all reports listed above, you can now add the check `modernize-use-nullptr` to `warnings-as-errors` in `.clang-tidy` (in the root dir of the repo): We show a sample diff below to illustrate how to modify `.clang-tidy`:

```diff
--- a/.clang-tidy
+++ b/.clang-tidy
@@ -1,7 +1,7 @@
 # refer to https://clang.llvm.org/extra/clang-tidy/checks/list.html
 Checks: ...

-WarningsAsErrors: ...
+WarningsAsErrors: ..., modernize-use-nullptr
```

Then, if all of the above are completed, congratulations, you can submit a PR for your changes now!

