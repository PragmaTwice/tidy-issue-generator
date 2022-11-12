#!/usr/bin/env python

import re

file = open('tidy.log')
lines = file.readlines()
file.close()

current_tag = ''
current_warn = ''

warn_map = dict()

for line in lines:
    if line.strip():
        if start := re.search('warning:.*\[(.*)\]', line):
            if current_tag:
                if current_tag not in warn_map:
                    warn_map[current_tag] = [current_warn]
                else:
                    warn_map[current_tag].append(current_warn)

            current_tag = start.group(1)
            current_warn = line
        elif end := re.search('--use-color -p=build', line):
            if current_tag:
                if current_tag not in warn_map:
                    warn_map[current_tag] = [current_warn]
                else:
                    warn_map[current_tag].append(current_warn)
            
            current_tag = ''
            current_warn = ''
        else:
            current_warn += line

for tag, list in warn_map.items():
    f = open(f'./tidy-issue/{tag}.md', 'w')
    f.write(f'# Fix `{tag}` warning reported by clang-tidy\n\n')
    f.write('*This issue is tracked by #1029.*\n\n')
    f.write('***We welcome new contributors to take these issues as a beginning of a deep dive to kvrocks***\n\n')
    f.write('Currently we have enabled lots of clang-tidy checks, '
        'but there are so many reports already exist in the kvrocks code, '
        'so we cannot treat these report as errors to block future PR with some clang-tidy reported warnings in CI.\n\n')
    f.write(f'Hence the goal of this issue is to solve all `{tag}` tagged clang-tidy reports, '
        'and then enable `warnings-as-errors` for this specific check in `.clang-tidy`.\n\n')
    f.write('To get clang-tidy reports for latest kvrocks code, there are several ways: '
        'you can run `./x.py check tidy` locally, '
        'or check the log of the latest run of GitHub Actions on the unstable branch '
        '(e.g. https://github.com/apache/incubator-kvrocks/actions/runs/3449328741/jobs/5757148924#step:8:916). '
        f'To be friendly for new contributors, we list all `{tag}` tagged reports below, '
        'so in normal cases you can just follow the log below and fix them one by one.\n\n'
    )
    f.write('```log\n')
    for warn in list:
        f.write(warn)
    f.write('```\n\n')
    f.write('Some of these reports will give modification suggestions in the log, you can refer to them directly; '
        'otherwise, you need to understand the content of the warning and combine your C++ knowledge to fix it. '
        '(Fortunately, most reports (except those by clang static analyzer) are intuitive and easy to fix.)\n\n')
    f.write(f'When you fixed these all reports listed above, you can now add the check `{tag}` '
        'to `warnings-as-errors` in `.clang-tidy` (in the root dir of the repo): '
        'We show a sample diff below to illustrate how to modify `.clang-tidy`:\n\n')
    f.write('```diff\n'
        '--- a/.clang-tidy\n'
        '+++ b/.clang-tidy\n'
        '@@ -1,7 +1,7 @@\n'
        ' # refer to https://clang.llvm.org/extra/clang-tidy/checks/list.html\n'
        ' Checks: ...\n'
        '\n'
        '-WarningsAsErrors: ...\n'
        f'+WarningsAsErrors: ..., {tag}\n'
        '```\n\n'
    )
    f.write('Then, if all of the above are completed, congratulations, you can submit a PR for your changes now!\n\n')
    f.close()
