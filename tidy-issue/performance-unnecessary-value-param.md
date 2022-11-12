# Fix `performance-unnecessary-value-param` warning reported by clang-tidy

*This issue is tracked by #1029.*

***We welcome new contributors to take these issues as a beginning of a deep dive to kvrocks***

Currently we have enabled lots of clang-tidy checks, but there are so many reports already exist in the kvrocks code, so we cannot treat these report as errors to block future PR with some clang-tidy reported warnings in CI.

Hence the goal of this issue is to solve all `performance-unnecessary-value-param` tagged clang-tidy reports, and then enable `warnings-as-errors` for this specific check in `.clang-tidy`.

To get clang-tidy reports for latest kvrocks code, there are several ways: you can run `./x.py check tidy` locally, or check the log of the latest run of GitHub Actions on the unstable branch (e.g. https://github.com/apache/incubator-kvrocks/actions/runs/3449328741/jobs/5757148924#step:8:916). To be friendly for new contributors, we list all `performance-unnecessary-value-param` tagged reports below, so in normal cases you can just follow the log below and fix them one by one.

```log
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/config/config.cc:724:30: warning: the parameter 'key' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
void Config::Get(std::string key, std::vector<std::string> *values) {
                             ^
                 const      &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/redis_connection.cc:198:54: warning: the parameter 'reply' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
void Connection::UnSubscribeAll(unsubscribe_callback reply) {
                                                     ^
                                const               &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/redis_connection.cc:235:55: warning: the parameter 'reply' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
void Connection::PUnSubscribeAll(unsubscribe_callback reply) {
                                                      ^
                                 const               &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:215:38: warning: the parameter 'host' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
Status Server::AddMaster(std::string host, uint32_t port, bool force_reconnect) {
                                     ^
                         const      &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:406:63: warning: the parameter 'channels' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
void Server::ListChannelSubscribeNum(std::vector<std::string> channels,
                                                              ^
                                     const                   &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:1324:54: warning: the parameter 'addr' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
void Server::KillClient(int64_t *killed, std::string addr, uint64_t id, uint64_t type, bool skipme,
                                                     ^
                                         const      &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/worker.cc:426:75: warning: the parameter 'addr' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
void Worker::KillClient(Redis::Connection *self, uint64_t id, std::string addr, uint64_t type, bool skipme,
                                                                          ^
                                                              const      &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/redis_db.cc:166:33: warning: the parameter 'prefix' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
void Database::Keys(std::string prefix, std::vector<std::string> *keys, KeyNumStats *stats) {
                                ^
                    const      &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:54:70: warning: the parameter 'elems' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
rocksdb::Status List::push(const Slice &user_key, std::vector<Slice> elems, bool create_if_missing, bool left,
6420 warnings generated.
                                                                     ^
Suppressed 6422 warnings (6419 in non-user code, 3 NOLINT).
                                                  const             &
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_sortedint.cc:36:77: warning: the parameter 'ids' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
rocksdb::Status Sortedint::Add(const Slice &user_key, std::vector<uint64_t> ids, int *ret) {
                                                                            ^
                                                      const                &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_sortedint.cc:70:80: warning: the parameter 'ids' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
rocksdb::Status Sortedint::Remove(const Slice &user_key, std::vector<uint64_t> ids, int *ret) {
                                                                               ^
                                                         const                &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_sortedint.cc:213:80: warning: the parameter 'ids' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
rocksdb::Status Sortedint::MExist(const Slice &user_key, std::vector<uint64_t> ids, std::vector<int> *exists) {
                                                                               ^
                                                         const                &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:418:71: warning: the parameter 'spec' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
rocksdb::Status ZSet::RangeByLex(const Slice &user_key, ZRangeLexSpec spec, std::vector<std::string> *members,
                                                                      ^
                                                        const        &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:877:45: warning: the parameter 'arg' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
Status getBitOffsetFromArgument(std::string arg, uint32_t *offset) {
                                            ^
                                const      &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3710:61: warning: the parameter 'name' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
void SubscribeCommandReply(std::string *output, std::string name, std::string sub_name, int num) {
                                                            ^
                                                const      &
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3710:79: warning: the parameter 'sub_name' is copied for each invocation but only used as a const reference; consider making it a const reference [performance-unnecessary-value-param]
void SubscribeCommandReply(std::string *output, std::string name, std::string sub_name, int num) {
                                                                              ^
                                                                  const      &
```

Some of these reports will give modification suggestions in the log, you can refer to them directly; otherwise, you need to understand the content of the warning and combine your C++ knowledge to fix it. (Fortunately, most reports (except those by clang static analyzer) are intuitive and easy to fix.)

When you fixed these all reports listed above, you can now add the check `performance-unnecessary-value-param` to `warnings-as-errors` in `.clang-tidy` (in the root dir of the repo): We show a sample diff below to illustrate how to modify `.clang-tidy`:

```diff
--- a/.clang-tidy
+++ b/.clang-tidy
@@ -1,7 +1,7 @@
 # refer to https://clang.llvm.org/extra/clang-tidy/checks/list.html
 Checks: ...

-WarningsAsErrors: ...
+WarningsAsErrors: ..., performance-unnecessary-value-param
```

Then, if all of the above are completed, congratulations, you can submit a PR for your changes now!

