# Fix `modernize-use-auto` warning reported by clang-tidy

*This issue is tracked by #1029.*

***We welcome new contributors to take these issues as a beginning of a deep dive to kvrocks***

Currently we have enabled lots of clang-tidy checks, but there are so many reports already exist in the kvrocks code, so we cannot treat these report as errors to block future PR with some clang-tidy reported warnings in CI.

Hence the goal of this issue is to solve all `modernize-use-auto` tagged clang-tidy reports, and then enable `warnings-as-errors` for this specific check in `.clang-tidy`.

To get clang-tidy reports for latest kvrocks code, there are several ways: you can run `./x.py check tidy` locally, or check the log of the latest run of GitHub Actions on the unstable branch (e.g. https://github.com/apache/incubator-kvrocks/actions/runs/3449328741/jobs/5757148924#step:8:916). To be friendly for new contributors, we list all `modernize-use-auto` tagged reports below, so in normal cases you can just follow the log below and fix them one by one.

```log
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/batch_extractor.cc:73:9: warning: use auto when initializing with a cast to avoid duplicating the type name [modernize-use-auto]
        RedisCommand cmd = static_cast<RedisCommand>(*parse_result);
        ^~~~~~~~~~~~
        auto
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/batch_extractor.cc:106:9: warning: use auto when initializing with a cast to avoid duplicating the type name [modernize-use-auto]
        RedisCommand cmd = static_cast<RedisCommand>(*parse_result);
        ^~~~~~~~~~~~
        auto
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/batch_extractor.cc:152:9: warning: use auto when initializing with a cast to avoid duplicating the type name [modernize-use-auto]
        RedisCommand cmd = static_cast<RedisCommand>(*parse_result);
        ^~~~~~~~~~~~
        auto
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/batch_extractor.cc:243:9: warning: use auto when initializing with a cast to avoid duplicating the type name [modernize-use-auto]
        RedisCommand cmd = static_cast<RedisCommand>(*parse_result);
        ^~~~~~~~~~~~
        auto
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:250:3: warning: use auto when initializing with a cast to avoid duplicating the type name [modernize-use-auto]
  uint32_t u_start = static_cast<uint32_t>(start);
  ^~~~~~~~
  auto
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:251:3: warning: use auto when initializing with a cast to avoid duplicating the type name [modernize-use-auto]
  uint32_t u_stop = static_cast<uint32_t>(stop);
  ^~~~~~~~
  auto
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:300:3: warning: use auto when initializing with a cast to avoid duplicating the type name [modernize-use-auto]
  uint32_t u_start = static_cast<uint32_t>(start);
  ^~~~~~~~
  auto
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:301:3: warning: use auto when initializing with a cast to avoid duplicating the type name [modernize-use-auto]
  uint32_t u_stop = static_cast<uint32_t>(stop);
  ^~~~~~~~
  auto
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:433:11: warning: use auto when initializing with a cast to avoid duplicating the type name [modernize-use-auto]
          uint64_t *lres = reinterpret_cast<uint64_t *>(frag_res.get());
          ^~~~~~~~
          auto
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4714:9: warning: use auto when initializing with a cast to avoid duplicating the type name [modernize-use-auto]
        uint64_t shortest =
        ^~~~~~~~
        auto
```

Some of these reports will give modification suggestions in the log, you can refer to them directly; otherwise, you need to understand the content of the warning and combine your C++ knowledge to fix it. (Fortunately, most reports (except those by clang static analyzer) are intuitive and easy to fix.)

When you fixed these all reports listed above, you can now add the check `modernize-use-auto` to `warnings-as-errors` in `.clang-tidy` (in the root dir of the repo): We show a sample diff below to illustrate how to modify `.clang-tidy`:

```diff
--- a/.clang-tidy
+++ b/.clang-tidy
@@ -1,7 +1,7 @@
 # refer to https://clang.llvm.org/extra/clang-tidy/checks/list.html
 Checks: ...

-WarningsAsErrors: ...
+WarningsAsErrors: ..., modernize-use-auto
```

Then, if all of the above are completed, congratulations, you can submit a PR for your changes now!

