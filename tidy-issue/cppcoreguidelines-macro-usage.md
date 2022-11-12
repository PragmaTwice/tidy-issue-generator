# Fix `cppcoreguidelines-macro-usage` warning reported by clang-tidy

*This issue is tracked by #1029.*

***We welcome new contributors to take these issues as a beginning of a deep dive to kvrocks***

Currently we have enabled lots of clang-tidy checks, but there are so many reports already exist in the kvrocks code, so we cannot treat these report as errors to block future PR with some clang-tidy reported warnings in CI.

Hence the goal of this issue is to solve all `cppcoreguidelines-macro-usage` tagged clang-tidy reports, and then enable `warnings-as-errors` for this specific check in `.clang-tidy`.

To get clang-tidy reports for latest kvrocks code, there are several ways: you can run `./x.py check tidy` locally, or check the log of the latest run of GitHub Actions on the unstable branch (e.g. https://github.com/apache/incubator-kvrocks/actions/runs/3449328741/jobs/5757148924#step:8:916). To be friendly for new contributors, we list all `cppcoreguidelines-macro-usage` tagged reports below, so in normal cases you can just follow the log below and fix them one by one.

```log
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:46:9: warning: function-like macro 'rol' used; consider a 'constexpr' template function [cppcoreguidelines-macro-usage]
#define rol(value, bits) (((value) << (bits)) | ((value) >> (32 - (bits))))
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:51:9: warning: function-like macro 'blk0' used; consider a 'constexpr' template function [cppcoreguidelines-macro-usage]
#define blk0(i) (block->l[i] = (rol(block->l[i], 24) & 0xFF00FF00) | (rol(block->l[i], 8) & 0x00FF00FF))
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:57:9: warning: function-like macro 'blk' used; consider a 'constexpr' template function [cppcoreguidelines-macro-usage]
#define blk(i)        \
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:62:9: warning: function-like macro 'R0' used; consider a 'constexpr' template function [cppcoreguidelines-macro-usage]
#define R0(v, w, x, y, z, i)                                   \
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:65:9: warning: function-like macro 'R1' used; consider a 'constexpr' template function [cppcoreguidelines-macro-usage]
#define R1(v, w, x, y, z, i)                                  \
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:68:9: warning: function-like macro 'R2' used; consider a 'constexpr' template function [cppcoreguidelines-macro-usage]
#define R2(v, w, x, y, z, i)                          \
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:71:9: warning: function-like macro 'R3' used; consider a 'constexpr' template function [cppcoreguidelines-macro-usage]
#define R3(v, w, x, y, z, i)                                            \
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:74:9: warning: function-like macro 'R4' used; consider a 'constexpr' template function [cppcoreguidelines-macro-usage]
#define R4(v, w, x, y, z, i)                          \
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:63:9: warning: macro 'AE_READABLE' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define AE_READABLE 1
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:64:9: warning: macro 'AE_WRITABLE' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define AE_WRITABLE 2
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:65:9: warning: macro 'AE_ERROR' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define AE_ERROR 4
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:66:9: warning: macro 'AE_HUP' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define AE_HUP 8
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:69:9: warning: macro 'MAX_LONG_DOUBLE_CHARS' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define MAX_LONG_DOUBLE_CHARS 5 * 1024
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:324:9: warning: macro 'LUA_GC_CYCLE_PERIOD' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define LUA_GC_CYCLE_PERIOD 50
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:62:9: warning: macro 'D_R' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define D_R (M_PI / 180.0)
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:63:9: warning: macro 'R_MAJOR' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define R_MAJOR 6378137.0
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:64:9: warning: macro 'R_MINOR' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define R_MINOR 6356752.3142
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:65:9: warning: macro 'RATIO' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define RATIO (R_MINOR / R_MAJOR)
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:66:9: warning: macro 'ECCENT' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define ECCENT (sqrt(1.0 - (RATIO * RATIO)))
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:67:9: warning: macro 'COM' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define COM (0.5 * ECCENT)
        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/main.cc:30:9: warning: macro '_XOPEN_SOURCE' used to declare a constant; consider using a 'constexpr' constant [cppcoreguidelines-macro-usage]
#define _XOPEN_SOURCE 700
        ^
```

Some of these reports will give modification suggestions in the log, you can refer to them directly; otherwise, you need to understand the content of the warning and combine your C++ knowledge to fix it. (Fortunately, most reports (except those by clang static analyzer) are intuitive and easy to fix.)

When you fixed these all reports listed above, you can now add the check `cppcoreguidelines-macro-usage` to `warnings-as-errors` in `.clang-tidy` (in the root dir of the repo): We show a sample diff below to illustrate how to modify `.clang-tidy`:

```diff
--- a/.clang-tidy
+++ b/.clang-tidy
@@ -1,7 +1,7 @@
 # refer to https://clang.llvm.org/extra/clang-tidy/checks/list.html
 Checks: ...

-WarningsAsErrors: ...
+WarningsAsErrors: ..., cppcoreguidelines-macro-usage
```

Then, if all of the above are completed, congratulations, you can submit a PR for your changes now!

