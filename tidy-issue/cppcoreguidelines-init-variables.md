# Fix `cppcoreguidelines-init-variables` warning reported by clang-tidy

*This issue is tracked by #1029.*

***We welcome new contributors to take these issues as a beginning of a deep dive to kvrocks***

Currently we have enabled lots of clang-tidy checks, but there are so many reports already exist in the kvrocks code, so we cannot treat these report as errors to block future PR with some clang-tidy reported warnings in CI.

Hence the goal of this issue is to solve all `cppcoreguidelines-init-variables` tagged clang-tidy reports, and then enable `warnings-as-errors` for this specific check in `.clang-tidy`.

To get clang-tidy reports for latest kvrocks code, there are several ways: you can run `./x.py check tidy` locally, or check the log of the latest run of GitHub Actions on the unstable branch (e.g. https://github.com/apache/incubator-kvrocks/actions/runs/3449328741/jobs/5757148924#step:8:916). To be friendly for new contributors, we list all `cppcoreguidelines-init-variables` tagged reports below, so in normal cases you can just follow the log below and fix them one by one.

```log
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:81:12: warning: variable 'a' is not initialized [cppcoreguidelines-init-variables]
  uint32_t a, b, c, d, e;
           ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:81:15: warning: variable 'b' is not initialized [cppcoreguidelines-init-variables]
  uint32_t a, b, c, d, e;
              ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:81:18: warning: variable 'c' is not initialized [cppcoreguidelines-init-variables]
  uint32_t a, b, c, d, e;
                 ^
                   = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:81:21: warning: variable 'd' is not initialized [cppcoreguidelines-init-variables]
  uint32_t a, b, c, d, e;
                    ^
                      = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:81:24: warning: variable 'e' is not initialized [cppcoreguidelines-init-variables]
  uint32_t a, b, c, d, e;
                       ^
                         = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:212:12: warning: variable 'i' is not initialized [cppcoreguidelines-init-variables]
  uint32_t i, j;
           ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:212:15: warning: variable 'j' is not initialized [cppcoreguidelines-init-variables]
  uint32_t i, j;
              ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:233:12: warning: variable 'i' is not initialized [cppcoreguidelines-init-variables]
  unsigned i;
           ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/sha1.cc:235:17: warning: variable 'c' is not initialized [cppcoreguidelines-init-variables]
  unsigned char c;
                ^
                  = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:70:7: warning: variable 'rv' is not initialized [cppcoreguidelines-init-variables]
  int rv;
      ^
         = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:72:20: warning: variable 'servinfo' is not initialized [cppcoreguidelines-init-variables]
  addrinfo hints, *servinfo, *p;
                   ^
                            = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:72:31: warning: variable 'p' is not initialized [cppcoreguidelines-init-variables]
  addrinfo hints, *servinfo, *p;
                              ^
                                = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:192:9: warning: variable 'socket_arg' is not initialized [cppcoreguidelines-init-variables]
    int socket_arg;
        ^
                   = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:268:7: warning: variable 'flags' is not initialized [cppcoreguidelines-init-variables]
  int flags;
      ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:448:13: warning: variable 'not_symbol' is not initialized [cppcoreguidelines-init-variables]
        int not_symbol, match;
            ^
                       = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:448:25: warning: variable 'match' is not initialized [cppcoreguidelines-init-variables]
        int not_symbol, match;
                        ^
                              = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:544:10: warning: variable 'd' is not initialized [cppcoreguidelines-init-variables]
  double d;
         ^
           = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:578:67: warning: variable 'p' is not initialized [cppcoreguidelines-init-variables]
  const char *start = value.data(), *end = start + value.size(), *p;
                                                                  ^
                                                                    = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:648:20: warning: variable 'retval' is not initialized [cppcoreguidelines-init-variables]
  int retmask = 0, retval;
                   ^
                          = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/config/config.cc:263:18: warning: variable 'start' is not initialized [cppcoreguidelines-init-variables]
         int64_t start, stop;
                 ^
                       = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/config/config.cc:263:25: warning: variable 'stop' is not initialized [cppcoreguidelines-init-variables]
         int64_t start, stop;
                        ^
                             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/config/config.cc:518:14: warning: variable 'val' is not initialized [cppcoreguidelines-init-variables]
         int val;
             ^
                 = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/config/config_util.cc:37:8: warning: variable 'quote' is not initialized [cppcoreguidelines-init-variables]
  char quote;  // single or double quote
       ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/redis_connection.cc:37:10: warning: variable 'now' is not initialized [cppcoreguidelines-init-variables]
  time_t now;
         ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/redis_connection.cc:137:10: warning: variable 'now' is not initialized [cppcoreguidelines-init-variables]
  time_t now;
         ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/redis_connection.cc:145:10: warning: variable 'now' is not initialized [cppcoreguidelines-init-variables]
  time_t now;
         ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:702:12: warning: variable 'memtable_sizes' is not initialized [cppcoreguidelines-init-variables]
  uint64_t memtable_sizes, cur_memtable_sizes, num_snapshots, num_running_flushes;
           ^
                          = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:702:28: warning: variable 'cur_memtable_sizes' is not initialized [cppcoreguidelines-init-variables]
  uint64_t memtable_sizes, cur_memtable_sizes, num_snapshots, num_running_flushes;
                           ^
                                              = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:702:48: warning: variable 'num_snapshots' is not initialized [cppcoreguidelines-init-variables]
  uint64_t memtable_sizes, cur_memtable_sizes, num_snapshots, num_running_flushes;
                                               ^
                                                             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:702:63: warning: variable 'num_running_flushes' is not initialized [cppcoreguidelines-init-variables]
  uint64_t memtable_sizes, cur_memtable_sizes, num_snapshots, num_running_flushes;
                                                              ^
                                                                                  = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:703:12: warning: variable 'num_immutable_tables' is not initialized [cppcoreguidelines-init-variables]
  uint64_t num_immutable_tables, memtable_flush_pending, compaction_pending;
           ^
                                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:703:34: warning: variable 'memtable_flush_pending' is not initialized [cppcoreguidelines-init-variables]
  uint64_t num_immutable_tables, memtable_flush_pending, compaction_pending;
                                 ^
                                                        = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:703:58: warning: variable 'compaction_pending' is not initialized [cppcoreguidelines-init-variables]
  uint64_t num_immutable_tables, memtable_flush_pending, compaction_pending;
                                                         ^
                                                                            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:704:12: warning: variable 'num_running_compaction' is not initialized [cppcoreguidelines-init-variables]
  uint64_t num_running_compaction, num_live_versions, num_superversion, num_backgroud_errors;
           ^
                                  = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:704:36: warning: variable 'num_live_versions' is not initialized [cppcoreguidelines-init-variables]
  uint64_t num_running_compaction, num_live_versions, num_superversion, num_backgroud_errors;
                                   ^
                                                     = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:704:55: warning: variable 'num_superversion' is not initialized [cppcoreguidelines-init-variables]
  uint64_t num_running_compaction, num_live_versions, num_superversion, num_backgroud_errors;
                                                      ^
                                                                       = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:704:73: warning: variable 'num_backgroud_errors' is not initialized [cppcoreguidelines-init-variables]
  uint64_t num_running_compaction, num_live_versions, num_superversion, num_backgroud_errors;
                                                                        ^
                                                                                             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:720:14: warning: variable 'estimate_keys' is not initialized [cppcoreguidelines-init-variables]
    uint64_t estimate_keys, block_cache_usage, block_cache_pinned_usage, index_and_filter_cache_usage;
             ^
                           = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:720:29: warning: variable 'block_cache_usage' is not initialized [cppcoreguidelines-init-variables]
    uint64_t estimate_keys, block_cache_usage, block_cache_pinned_usage, index_and_filter_cache_usage;
                            ^
                                              = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:720:48: warning: variable 'block_cache_pinned_usage' is not initialized [cppcoreguidelines-init-variables]
    uint64_t estimate_keys, block_cache_usage, block_cache_pinned_usage, index_and_filter_cache_usage;
                                               ^
                                                                        = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:720:74: warning: variable 'index_and_filter_cache_usage' is not initialized [cppcoreguidelines-init-variables]
    uint64_t estimate_keys, block_cache_usage, block_cache_pinned_usage, index_and_filter_cache_usage;
                                                                         ^
                                                                                                      = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:772:10: warning: variable 'now' is not initialized [cppcoreguidelines-init-variables]
  time_t now;
         ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:826:10: warning: variable 'now' is not initialized [cppcoreguidelines-init-variables]
  time_t now;
         ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/worker.cc:121:16: warning: variable 'bev' is not initialized [cppcoreguidelines-init-variables]
  bufferevent *bev;
               ^
                   = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/worker.cc:165:12: warning: variable 'port' is not initialized [cppcoreguidelines-init-variables]
  uint32_t port;
           ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/worker.cc:200:7: warning: variable 'af' is not initialized [cppcoreguidelines-init-variables]
  int af, rv, fd, sock_opt = 1;
      ^
         = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/worker.cc:200:11: warning: variable 'rv' is not initialized [cppcoreguidelines-init-variables]
  int af, rv, fd, sock_opt = 1;
          ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/worker.cc:200:15: warning: variable 'fd' is not initialized [cppcoreguidelines-init-variables]
  int af, rv, fd, sock_opt = 1;
              ^
                 = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/worker.cc:208:27: warning: variable 'srv_info' is not initialized [cppcoreguidelines-init-variables]
  struct addrinfo hints, *srv_info, *p;
                          ^
                                   = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/worker.cc:208:38: warning: variable 'p' is not initialized [cppcoreguidelines-init-variables]
  struct addrinfo hints, *srv_info, *p;
                                     ^
                                       = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/stats/log_collector.cc:56:10: warning: variable 'n' is not initialized [cppcoreguidelines-init-variables]
  size_t n;
         ^
           = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/stats/log_collector.cc:95:10: warning: variable 'n' is not initialized [cppcoreguidelines-init-variables]
  size_t n;
         ^
           = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/redis_db.cc:520:28: warning: variable 'snapshot' is not initialized [cppcoreguidelines-init-variables]
  const rocksdb::Snapshot *snapshot;
                           ^
                                    = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/redis_metadata.cc:45:12: warning: variable 'key_size' is not initialized [cppcoreguidelines-init-variables]
  uint32_t key_size;
           ^
                    = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/redis_metadata.cc:46:11: warning: variable 'namespace_size' is not initialized [cppcoreguidelines-init-variables]
  uint8_t namespace_size;
          ^
                         = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/redis_metadata.cc:64:11: warning: variable 'namespace_size' is not initialized [cppcoreguidelines-init-variables]
  uint8_t namespace_size;
          ^
                         = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/redis_metadata.cc:128:11: warning: variable 'namespace_size' is not initialized [cppcoreguidelines-init-variables]
  uint8_t namespace_size;
          ^
                         = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/redis_metadata.cc:134:14: warning: variable 'slot_id' is not initialized [cppcoreguidelines-init-variables]
    uint16_t slot_id;
             ^
                     = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:196:7: warning: variable 'j' is not initialized [cppcoreguidelines-init-variables]
  int j, level, argc = lua_gettop(lua);
      ^
        = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:196:10: warning: variable 'level' is not initialized [cppcoreguidelines-init-variables]
  int j, level, argc = lua_gettop(lua);
         ^
               = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:217:12: warning: variable 'len' is not initialized [cppcoreguidelines-init-variables]
    size_t len;
           ^
               = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:218:17: warning: variable 's' is not initialized [cppcoreguidelines-init-variables]
    const char *s;
                ^
                  = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:341:7: warning: variable 'j' is not initialized [cppcoreguidelines-init-variables]
  int j, argc = lua_gettop(lua);
      ^
        = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:359:19: warning: variable 'obj_s' is not initialized [cppcoreguidelines-init-variables]
      const char *obj_s;
                  ^
                        = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:360:14: warning: variable 'obj_len' is not initialized [cppcoreguidelines-init-variables]
      size_t obj_len;
             ^
                     = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:522:10: warning: variable 'len' is not initialized [cppcoreguidelines-init-variables]
  size_t len;
         ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:523:15: warning: variable 's' is not initialized [cppcoreguidelines-init-variables]
  const char *s;
              ^
                = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:550:7: warning: variable 'j' is not initialized [cppcoreguidelines-init-variables]
  int j;
      ^
        = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:625:11: warning: variable 'value' is not initialized [cppcoreguidelines-init-variables]
  int64_t value;
          ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:634:11: warning: variable 'bulklen' is not initialized [cppcoreguidelines-init-variables]
  int64_t bulklen;
          ^
                  = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:668:11: warning: variable 'mbulklen' is not initialized [cppcoreguidelines-init-variables]
  int64_t mbulklen;
          ^
                   = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:702:10: warning: variable 'd' is not initialized [cppcoreguidelines-init-variables]
  double d;
         ^
           = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:734:10: warning: variable 'obj_len' is not initialized [cppcoreguidelines-init-variables]
  size_t obj_len;
         ^
                 = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/storage.cc:208:16: warning: variable 'tmp_db' is not initialized [cppcoreguidelines-init-variables]
  rocksdb::DB *tmp_db;
               ^
                      = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/storage.cc:588:12: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
  uint64_t size, total_size = 0;
           ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/storage.cc:606:8: warning: variable 'reach_db_size_limit' is not initialized [cppcoreguidelines-init-variables]
  bool reach_db_size_limit;
       ^
                           = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/storage.cc:946:12: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
  uint64_t size;
           ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/table_properties_collector.cc:33:7: warning: variable 'now' is not initialized [cppcoreguidelines-init-variables]
  int now;
      ^
          = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/table_properties_collector.cc:34:11: warning: variable 'type' is not initialized [cppcoreguidelines-init-variables]
  uint8_t type;
          ^
               = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/table_properties_collector.cc:35:12: warning: variable 'expired' is not initialized [cppcoreguidelines-init-variables]
  uint32_t expired, subkeys = 0;
           ^
                   = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/table_properties_collector.cc:36:12: warning: variable 'version' is not initialized [cppcoreguidelines-init-variables]
  uint64_t version;
           ^
                   = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:390:10: warning: variable 'min_lon' is not initialized [cppcoreguidelines-init-variables]
  double min_lon, max_lon, min_lat, max_lat;
         ^
                 = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:390:19: warning: variable 'max_lon' is not initialized [cppcoreguidelines-init-variables]
  double min_lon, max_lon, min_lat, max_lat;
                  ^
                          = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:390:28: warning: variable 'min_lat' is not initialized [cppcoreguidelines-init-variables]
  double min_lon, max_lon, min_lat, max_lat;
                           ^
                                   = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:390:37: warning: variable 'max_lat' is not initialized [cppcoreguidelines-init-variables]
  double min_lon, max_lon, min_lat, max_lat;
                                    ^
                                            = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:392:7: warning: variable 'steps' is not initialized [cppcoreguidelines-init-variables]
  int steps;
      ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:475:10: warning: variable 'lat1r' is not initialized [cppcoreguidelines-init-variables]
  double lat1r, lon1r, lat2r, lon2r, u, v;
         ^
               = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:475:17: warning: variable 'lon1r' is not initialized [cppcoreguidelines-init-variables]
  double lat1r, lon1r, lat2r, lon2r, u, v;
                ^
                      = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:475:24: warning: variable 'lat2r' is not initialized [cppcoreguidelines-init-variables]
  double lat1r, lon1r, lat2r, lon2r, u, v;
                       ^
                             = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:475:31: warning: variable 'lon2r' is not initialized [cppcoreguidelines-init-variables]
  double lat1r, lon1r, lat2r, lon2r, u, v;
                              ^
                                    = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:475:38: warning: variable 'u' is not initialized [cppcoreguidelines-init-variables]
  double lat1r, lon1r, lat2r, lon2r, u, v;
                                     ^
                                       = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:475:41: warning: variable 'v' is not initialized [cppcoreguidelines-init-variables]
  double lat1r, lon1r, lat2r, lon2r, u, v;
                                        ^
                                          = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:125:12: warning: variable 'frag_index' is not initialized [cppcoreguidelines-init-variables]
  uint32_t frag_index, valid_size;
           ^
                      = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:125:24: warning: variable 'valid_size' is not initialized [cppcoreguidelines-init-variables]
  uint32_t frag_index, valid_size;
                       ^
                                  = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:201:12: warning: variable 'expand_size' is not initialized [cppcoreguidelines-init-variables]
    size_t expand_size;
           ^
                       = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:391:14: warning: variable 'i' is not initialized [cppcoreguidelines-init-variables]
    uint64_t i, frag_numkeys = num_keys, stop_index = (max_size - 1) / kBitmapSegmentBytes;
             ^
               = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:395:19: warning: variable 'output' is not initialized [cppcoreguidelines-init-variables]
    unsigned char output, byte;
                  ^
                         = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:395:27: warning: variable 'byte' is not initialized [cppcoreguidelines-init-variables]
    unsigned char output, byte;
                          ^
                               = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:133:13: warning: variable 'p4' is not initialized [cppcoreguidelines-init-variables]
  uint32_t *p4;
            ^
               = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:144:14: warning: variable 'aux1' is not initialized [cppcoreguidelines-init-variables]
    uint32_t aux1, aux2, aux3, aux4, aux5, aux6, aux7;
             ^
                  = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:144:20: warning: variable 'aux2' is not initialized [cppcoreguidelines-init-variables]
    uint32_t aux1, aux2, aux3, aux4, aux5, aux6, aux7;
                   ^
                        = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:144:26: warning: variable 'aux3' is not initialized [cppcoreguidelines-init-variables]
    uint32_t aux1, aux2, aux3, aux4, aux5, aux6, aux7;
                         ^
                              = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:144:32: warning: variable 'aux4' is not initialized [cppcoreguidelines-init-variables]
    uint32_t aux1, aux2, aux3, aux4, aux5, aux6, aux7;
                               ^
                                    = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:144:38: warning: variable 'aux5' is not initialized [cppcoreguidelines-init-variables]
    uint32_t aux1, aux2, aux3, aux4, aux5, aux6, aux7;
                                     ^
                                          = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:144:44: warning: variable 'aux6' is not initialized [cppcoreguidelines-init-variables]
    uint32_t aux1, aux2, aux3, aux4, aux5, aux6, aux7;
                                           ^
                                                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:144:50: warning: variable 'aux7' is not initialized [cppcoreguidelines-init-variables]
    uint32_t aux1, aux2, aux3, aux4, aux5, aux6, aux7;
                                                 ^
                                                      = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:195:13: warning: variable 'l' is not initialized [cppcoreguidelines-init-variables]
  uint64_t *l;
            ^
              = nullptr
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:196:12: warning: variable 'skipval' is not initialized [cppcoreguidelines-init-variables]
  uint64_t skipval, word = 0, one;
           ^
                   = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:196:31: warning: variable 'one' is not initialized [cppcoreguidelines-init-variables]
  uint64_t skipval, word = 0, one;
                              ^
                                  = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:198:12: warning: variable 'j' is not initialized [cppcoreguidelines-init-variables]
  uint64_t j;
           ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:199:7: warning: variable 'found' is not initialized [cppcoreguidelines-init-variables]
  int found;
      ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:122:11: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
      int ret;
          ^
              = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:193:9: warning: variable 'idx' is not initialized [cppcoreguidelines-init-variables]
    int idx;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:216:16: warning: variable 'i' is not initialized [cppcoreguidelines-init-variables]
  unsigned int i, count = 0, last_processed = 0;
               ^
                 = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:254:20: warning: variable 'min' is not initialized [cppcoreguidelines-init-variables]
  GeoHashFix52Bits min, max;
                   ^
                       = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:254:25: warning: variable 'max' is not initialized [cppcoreguidelines-init-variables]
  GeoHashFix52Bits min, max;
                        ^
                            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:309:7: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
  int size;
      ^
           = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:328:10: warning: variable 'distance' is not initialized [cppcoreguidelines-init-variables]
  double distance, xy[2];
         ^
                  = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:274:45: warning: variable 'new_elem_index' is not initialized [cppcoreguidelines-init-variables]
6346 warnings generated.
  uint64_t pivot_index = metadata.head - 1, new_elem_index;
Suppressed 6349 warnings (6346 in non-user code, 3 NOLINT).
                                            ^
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
                                                           = 0
6386 warnings generated.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:400:14: warning: variable 'index' is not initialized [cppcoreguidelines-init-variables]
Suppressed 2699 warnings (2699 in non-user code).
    uint64_t index;
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
             ^
345 warnings generated.
                   = 0
Suppressed 345 warnings (345 in non-user code).
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:439:13: warning: variable 'type' is not initialized [cppcoreguidelines-init-variables]
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
  RedisType type;
4811 warnings generated.
Suppressed 4813 warnings (4810 in non-user code, 3 NOLINT).
            ^
                 = 0
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:449:7: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
5701 warnings generated.
  int ret;
Suppressed 5686 warnings (5681 in non-user code, 5 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
      ^
          = 0
6848 warnings generated.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_set.cc:247:13: warning: variable 'type' is not initialized [cppcoreguidelines-init-variables]
  RedisType type;
            ^
                 = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_sortedint.cc:144:12: warning: variable 'id' is not initialized [cppcoreguidelines-init-variables]
  uint64_t id, pos = 0;
           ^
              = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_sortedint.cc:193:12: warning: variable 'id' is not initialized [cppcoreguidelines-init-variables]
  uint64_t id;
           ^
              = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_stream_base.cc:158:14: warning: variable 'len' is not initialized [cppcoreguidelines-init-variables]
    uint32_t len;
             ^
                 = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_string.cc:250:7: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
  int size;
      ^
           = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_string.cc:339:15: warning: variable 'idx' is not initialized [cppcoreguidelines-init-variables]
  std::size_t idx;
              ^
                  = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_string.cc:399:7: warning: variable 'exists' is not initialized [cppcoreguidelines-init-variables]
  int exists;
      ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:156:7: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
  int ret;
      ^
          = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:386:12: warning: variable 'score' is not initialized [cppcoreguidelines-init-variables]
    double score;
           ^
                 = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:622:12: warning: variable 'score' is not initialized [cppcoreguidelines-init-variables]
    double score;
           ^
                 = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:664:7: warning: variable 'target_size' is not initialized [cppcoreguidelines-init-variables]
  int target_size;
      ^
                  = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:721:7: warning: variable 'target_size' is not initialized [cppcoreguidelines-init-variables]
  int target_size;
      ^
                  = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:508:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
Suppressed 5876 warnings (5873 in non-user code, 3 NOLINT).
    int ret;
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
        ^
5855 warnings generated.
            = 0
Suppressed 5852 warnings (5849 in non-user code, 3 NOLINT).
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:541:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
    int ret;
5846 warnings generated.
        ^
Suppressed 5849 warnings (5846 in non-user code, 3 NOLINT).
            = 0
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:683:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
6169 warnings generated.
    int ret;
Suppressed 6162 warnings (6159 in non-user code, 3 NOLINT).
        ^
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
            = 0
6219 warnings generated.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:704:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
Suppressed 6209 warnings (6206 in non-user code, 3 NOLINT).
    int ret;
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
        ^
7195 warnings generated.
            = 0
Suppressed 7196 warnings (7193 in non-user code, 3 NOLINT).
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:722:13: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
    int64_t ret;
7293 warnings generated.
            ^
                = 0
Suppressed 7178 warnings (7175 in non-user code, 3 NOLINT).
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:734:13: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int64_t ret;
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
            ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:755:13: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int64_t ret;
            ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:779:12: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    double ret;
           ^
               = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:803:13: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int64_t ret;
            ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:896:10: warning: variable 'bit' is not initialized [cppcoreguidelines-init-variables]
    bool bit;
         ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:925:10: warning: variable 'old_bit' is not initialized [cppcoreguidelines-init-variables]
    bool old_bit;
         ^
                 = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:960:14: warning: variable 'cnt' is not initialized [cppcoreguidelines-init-variables]
    uint32_t cnt;
             ^
                 = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1001:13: warning: variable 'pos' is not initialized [cppcoreguidelines-init-variables]
    int64_t pos;
            ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1055:15: warning: variable 'type' is not initialized [cppcoreguidelines-init-variables]
    RedisType type;
              ^
                   = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1090:9: warning: variable 'ttl' is not initialized [cppcoreguidelines-init-variables]
    int ttl;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1105:9: warning: variable 'ttl' is not initialized [cppcoreguidelines-init-variables]
    int ttl;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1245:9: warning: variable 'ttl' is not initialized [cppcoreguidelines-init-variables]
    int ttl;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1277:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1305:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1337:14: warning: variable 'count' is not initialized [cppcoreguidelines-init-variables]
    uint32_t count;
             ^
                   = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1359:13: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int64_t ret;
            ^
                = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1384:12: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    double ret;
           ^
               = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1432:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1552:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1823:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1851:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1897:14: warning: variable 'count' is not initialized [cppcoreguidelines-init-variables]
    uint32_t count;
             ^
                   = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2044:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2062:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2076:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2104:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2209:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2357:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2425:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2443:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2467:12: warning: variable 'score' is not initialized [cppcoreguidelines-init-variables]
    double score;
           ^
                 = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2493:9: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
    int size;
        ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2629:9: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
    int size;
        ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2679:9: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
    int size;
        ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2707:9: warning: variable 'rank' is not initialized [cppcoreguidelines-init-variables]
    int rank;
        ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2743:9: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
    int size;
        ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2772:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2799:9: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
    int size;
        ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2824:9: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
    int size;
        ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2841:12: warning: variable 'score' is not initialized [cppcoreguidelines-init-variables]
    double score;
           ^
                 = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2938:9: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
    int size;
        ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2959:9: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
    int size;
        ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3045:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3071:12: warning: variable 'distance' is not initialized [cppcoreguidelines-init-variables]
    double distance;
           ^
                    = NAN
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3326:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3354:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3371:9: warning: variable 'ret' is not initialized [cppcoreguidelines-init-variables]
    int ret;
        ^
            = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3493:9: warning: variable 'size' is not initialized [cppcoreguidelines-init-variables]
    int size;
        ^
             = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3537:15: warning: variable 'type' is not initialized [cppcoreguidelines-init-variables]
    RedisType type;
              ^
                   = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4304:15: warning: variable 'protocol' is not initialized [cppcoreguidelines-init-variables]
      int64_t protocol;
              ^
                       = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4758:15: warning: variable 'state' is not initialized [cppcoreguidelines-init-variables]
      int64_t state;
              ^
                    = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5058:16: warning: variable 'max_len_idx' is not initialized [cppcoreguidelines-init-variables]
        size_t max_len_idx;
               ^
                           = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5087:16: warning: variable 'min_id_idx' is not initialized [cppcoreguidelines-init-variables]
        size_t min_id_idx;
               ^
                          = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5205:14: warning: variable 'deleted' is not initialized [cppcoreguidelines-init-variables]
    uint64_t deleted;
             ^
                     = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5224:14: warning: variable 'len' is not initialized [cppcoreguidelines-init-variables]
    uint64_t len;
             ^
                 = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5812:14: warning: variable 'max_len_idx' is not initialized [cppcoreguidelines-init-variables]
      size_t max_len_idx;
             ^
                         = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5831:14: warning: variable 'min_id_idx' is not initialized [cppcoreguidelines-init-variables]
      size_t min_id_idx;
             ^
                        = 0
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5877:14: warning: variable 'removed' is not initialized [cppcoreguidelines-init-variables]
    uint64_t removed;
             ^
                     = 0
```

Some of these reports will give modification suggestions in the log, you can refer to them directly; otherwise, you need to understand the content of the warning and combine your C++ knowledge to fix it. (Fortunately, most reports (except those by clang static analyzer) are intuitive and easy to fix.)

When you fixed these all reports listed above, you can now add the check `cppcoreguidelines-init-variables` to `warnings-as-errors` in `.clang-tidy` (in the root dir of the repo): We show a sample diff below to illustrate how to modify `.clang-tidy`:

```diff
--- a/.clang-tidy
+++ b/.clang-tidy
@@ -1,7 +1,7 @@
 # refer to https://clang.llvm.org/extra/clang-tidy/checks/list.html
 Checks: ...

-WarningsAsErrors: ...
+WarningsAsErrors: ..., cppcoreguidelines-init-variables
```

Then, if all of the above are completed, congratulations, you can submit a PR for your changes now!

