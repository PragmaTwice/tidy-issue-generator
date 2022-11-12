# Fix `cppcoreguidelines-narrowing-conversions` warning reported by clang-tidy

*This issue is tracked by #1029.*

***We welcome new contributors to take these issues as a beginning of a deep dive to kvrocks***

Currently we have enabled lots of clang-tidy checks, but there are so many reports already exist in the kvrocks code, so we cannot treat these report as errors to block future PR with some clang-tidy reported warnings in CI.

Hence the goal of this issue is to solve all `cppcoreguidelines-narrowing-conversions` tagged clang-tidy reports, and then enable `warnings-as-errors` for this specific check in `.clang-tidy`.

To get clang-tidy reports for latest kvrocks code, there are several ways: you can run `./x.py check tidy` locally, or check the log of the latest run of GitHub Actions on the unstable branch (e.g. https://github.com/apache/incubator-kvrocks/actions/runs/3449328741/jobs/5757148924#step:8:916). To be friendly for new contributors, we list all `cppcoreguidelines-narrowing-conversions` tagged reports below, so in normal cases you can just follow the log below and fix them one by one.

```log
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:207:17: warning: narrowing conversion from 'unsigned long' to signed type '__time_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    tv.tv_sec = timeout / 1000;
                ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:208:18: warning: narrowing conversion from 'unsigned long' to signed type '__suseconds_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    tv.tv_usec = (timeout % 1000) * 1000;
                 ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:422:42: warning: narrowing conversion from 'std::basic_string<char>::size_type' (aka 'unsigned long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  return StringMatchLen(pattern.c_str(), pattern.length(), in.c_str(), in.length(), nocase);
                                         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:422:72: warning: narrowing conversion from 'std::basic_string<char>::size_type' (aka 'unsigned long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  return StringMatchLen(pattern.c_str(), pattern.length(), in.c_str(), in.length(), nocase);
                                                                       ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/common/util.cc:655:31: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  if ((retval = poll(&pfd, 1, timeout)) == 1) {
                              ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/config/config.cc:269:43: warning: narrowing conversion from 'int64_t' (aka 'long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
         compaction_checker_range.Start = start;
                                          ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/config/config.cc:270:42: warning: narrowing conversion from 'int64_t' (aka 'long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
         compaction_checker_range.Stop = stop;
                                         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/config/config.cc:817:50: warning: narrowing conversion from 'std::basic_string<char>::size_type' (aka 'unsigned long') to signed type 'std::streamsize' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  output_file.write(string_stream.str().c_str(), string_stream.str().size());
                                                 ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/redis_connection.cc:200:37: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    if (reply != nullptr) reply("", subcribe_patterns_.size());
                                    ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/redis_connection.cc:237:37: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    if (reply != nullptr) reply("", subscribe_channels_.size());
                                    ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/redis_request.cc:114:70: warning: narrowing conversion from 'unsigned long' to signed type 'ssize_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
        char *data = reinterpret_cast<char *>(evbuffer_pullup(input, bulk_len_ + 2));
                                                                     ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:183:31: warning: narrowing conversion from 'long' to signed type 'int32_t' (aka 'int') is implementation-defined [cppcoreguidelines-narrowing-conversions]
          last_compact_date = now / 86400;
                              ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:242:30: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    config_->SetMaster(host, port);
                             ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:1036:81: warning: narrowing conversion from 'unsigned long' to 'double' [cppcoreguidelines-narrowing-conversions]
    double used_percent = config_->max_db_size ? storage_->GetTotalSize() * 100 / (config_->max_db_size * GiB) : 0;
                                                                                ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:1044:34: warning: narrowing conversion from 'unsigned long' to 'double' [cppcoreguidelines-narrowing-conversions]
      double used_disk_percent = used_disk_size * 100 / disk_capacity;
                                 ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/server.cc:1413:39: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  std::string value = Redis::MultiLen(tokens.size());
                                      ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/server/worker.cc:167:23: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    conn->SetAddr(ip, port);
                      ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/stats/log_collector.cc:30:32: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  output.append(Redis::Integer(id));
                               ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/stats/log_collector.cc:32:32: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  output.append(Redis::Integer(duration));
                               ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/stats/log_collector.cc:40:32: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  output.append(Redis::Integer(id));
                               ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/stats/log_collector.cc:43:32: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  output.append(Redis::Integer(duration));
                               ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/stats/log_collector.cc:59:10: warning: narrowing conversion from 'size_t' (aka 'unsigned long') to signed type 'ssize_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  return n;
         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/stats/log_collector.cc:104:33: warning: narrowing conversion from 'size_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  output.append(Redis::MultiLen(n));
                                ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/lock_manager.cc:28:16: warning: narrowing conversion from 'unsigned int' to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  hash_mask_ = (1U << hash_power) - 1;
               ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:206:11: warning: narrowing conversion from 'lua_Number' (aka 'double') to 'int' [cppcoreguidelines-narrowing-conversions]
  level = lua_tonumber(lua, -argc);
          ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:272:67: warning: narrowing conversion from 'int' to signed type 'char' is implementation-defined [cppcoreguidelines-narrowing-conversions]
      funcname[j + 2] = (sha[j] >= 'A' && sha[j] <= 'Z') ? sha[j] + ('a' - 'A') : sha[j];
                                                                  ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:272:83: warning: narrowing conversion from 'int' to signed type 'char' is implementation-defined [cppcoreguidelines-narrowing-conversions]
      funcname[j + 2] = (sha[j] >= 'A' && sha[j] <= 'Z') ? sha[j] + ('a' - 'A') : sha[j];
                                                                                  ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/scripting.cc:843:26: warning: narrowing conversion from 'unsigned long' to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    lua_rawseti(lua, -2, i + 1);
                         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/storage.cc:173:88: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  rate_limiter_ = std::shared_ptr<rocksdb::RateLimiter>(rocksdb::NewGenericRateLimiter(max_io_mb * MiB));
                                                                                       ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/storage.cc:629:36: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  rate_limiter_->SetBytesPerSecond(max_io_mb * MiB);
                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/storage/storage.cc:648:27: warning: narrowing conversion from 'size_t' (aka 'unsigned long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  const int charset_len = strlen(charset);
                          ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:188:17: warning: narrowing conversion from 'unsigned long long' to 'double' [cppcoreguidelines-narrowing-conversions]
  lat_offset *= (1ULL << step);
                ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:189:18: warning: narrowing conversion from 'unsigned long long' to 'double' [cppcoreguidelines-narrowing-conversions]
  long_offset *= (1ULL << step);
                 ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:190:29: warning: narrowing conversion from 'double' to 'uint32_t' (aka 'unsigned int') [cppcoreguidelines-narrowing-conversions]
  hash->bits = interleave64(lat_offset, long_offset);
                            ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:190:41: warning: narrowing conversion from 'double' to 'uint32_t' (aka 'unsigned int') [cppcoreguidelines-narrowing-conversions]
  hash->bits = interleave64(lat_offset, long_offset);
                                        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:223:55: warning: narrowing conversion from 'unsigned long long' to 'double' [cppcoreguidelines-narrowing-conversions]
  area->latitude.min = lat_range.min + (ilato * 1.0 / (1ull << step)) * lat_scale;
                                                      ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:224:61: warning: narrowing conversion from 'unsigned long long' to 'double' [cppcoreguidelines-narrowing-conversions]
  area->latitude.max = lat_range.min + ((ilato + 1) * 1.0 / (1ull << step)) * lat_scale;
                                                            ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:225:57: warning: narrowing conversion from 'unsigned long long' to 'double' [cppcoreguidelines-narrowing-conversions]
  area->longitude.min = long_range.min + (ilono * 1.0 / (1ull << step)) * long_scale;
                                                        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/geohash.cc:226:63: warning: narrowing conversion from 'unsigned long long' to 'double' [cppcoreguidelines-narrowing-conversions]
  area->longitude.max = long_range.min + ((ilono + 1) * 1.0 / (1ull << step)) * long_scale;
                                                              ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:168:21: warning: narrowing conversion from 'uint8_t' (aka 'unsigned char') to signed type '__gnu_cxx::__alloc_traits<std::allocator<char>, char>::value_type' (aka 'char') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      fragment[i] = swap_table[static_cast<uint8_t>(fragment[i])];
                    ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:214:26: warning: narrowing conversion from 'int' to signed type '__gnu_cxx::__alloc_traits<std::allocator<char>, char>::value_type' (aka 'char') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    value[byte_index] |= 1 << bit_offset;
                         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:216:26: warning: narrowing conversion from 'int' to signed type '__gnu_cxx::__alloc_traits<std::allocator<char>, char>::value_type' (aka 'char') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    value[byte_index] &= ~(1 << bit_offset);
                         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap.cc:539:10: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  *len = max_size;
         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:54:14: warning: narrowing conversion from 'int' to signed type 'char' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  byteval &= ~(1 << bit_offset);
             ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:55:14: warning: narrowing conversion from 'int' to signed type 'char' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  byteval |= ((new_bit & 0x1) << bit_offset);
             ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:75:26: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  if (start < 0) start = strlen + start;
                         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:76:24: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  if (stop < 0) stop = strlen + stop;
                       ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:79:52: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  if (stop >= static_cast<int64_t>(strlen)) stop = strlen - 1;
                                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:95:26: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  if (start < 0) start = strlen + start;
                         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:96:24: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  if (stop < 0) stop = strlen + stop;
                       ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_bitmap_string.cc:99:52: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  if (stop >= static_cast<int64_t>(strlen)) stop = strlen - 1;
                                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:109:29: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    int64_t result_length = geo_points->size();
                            ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:200:13: warning: narrowing conversion from 'unsigned long' to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
      idx = (hash.bits >> (52 - ((i + 1) * 5))) & 0x1f;
            ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:246:10: warning: narrowing conversion from 'unsigned int' to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  return count;
         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:257:37: warning: narrowing conversion from 'GeoHashFix52Bits' (aka 'unsigned long') to 'double' [cppcoreguidelines-narrowing-conversions]
  return getPointsInRange(user_key, min, max, lon, lat, radius, geo_points);
                                    ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_geo.cc:257:42: warning: narrowing conversion from 'GeoHashFix52Bits' (aka 'unsigned long') to 'double' [cppcoreguidelines-narrowing-conversions]
  return getPointsInRange(user_key, min, max, lon, lat, radius, geo_points);
                                         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_hash.cc:135:21: warning: narrowing conversion from 'double' to 'float' [cppcoreguidelines-narrowing-conversions]
        old_value = std::stod(value_bytes, &idx);
                    ^
4668 warnings generated.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:87:10: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
6728 warnings generated.
  *ret = metadata.size;
Suppressed 6733 warnings (6728 in non-user code, 5 NOLINT).
         ^
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:337:10: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
Suppressed 6391 warnings (6386 in non-user code, 5 NOLINT).
  *ret = metadata.size;
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
         ^
4135 warnings generated.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:350:27: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
Suppressed 4138 warnings (4135 in non-user code, 3 NOLINT).
  if (index < 0) index += metadata.size;
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
                          ^
2699 warnings generated.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:417:26: warning: narrowing conversion from 'unsigned int' to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
  if (index < 0) index = metadata.size + index;
767 warnings generated.
Suppressed 754 warnings (749 in non-user code, 5 NOLINT).
                         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:600:26: warning: narrowing conversion from 'unsigned int' to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
Suppressed 6839 warnings (6836 in non-user code, 3 NOLINT).
  if (start < 0) start = metadata.size + start;
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
                         ^
4672 warnings generated.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:601:85: warning: narrowing conversion from 'unsigned int' to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
Suppressed 4674 warnings (4671 in non-user code, 3 NOLINT).
  if (stop < 0) stop = static_cast<int>(metadata.size) >= -1 * stop ? metadata.size + stop : -1;
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
                                                                                    ^
6367 warnings generated.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_list.cc:601:94: warning: narrowing conversion from constant value 4294967295 (0xFFFFFFFF) of type 'unsigned int' to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
Suppressed 6363 warnings (6360 in non-user code, 3 NOLINT).
  if (stop < 0) stop = static_cast<int>(metadata.size) >= -1 * stop ? metadata.size + stop : -1;
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
                                                                                             ^
3314 warnings generated.
Suppressed 3314 warnings (3314 in non-user code).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
6363 warnings generated.
Suppressed 6367 warnings (6362 in non-user code, 5 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
6748 warnings generated.
Suppressed 6725 warnings (6722 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
6504 warnings generated.
Suppressed 6499 warnings (6495 in non-user code, 4 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
5847 warnings generated.
Suppressed 5850 warnings (5847 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
3867 warnings generated.
Suppressed 3857 warnings (3857 in non-user code).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
5013 warnings generated.
Suppressed 5014 warnings (5011 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
6366 warnings generated.
Suppressed 6365 warnings (6362 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
5853 warnings generated.
Suppressed 5856 warnings (5853 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
5835 warnings generated.
Suppressed 5838 warnings (5835 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
5842 warnings generated.
Suppressed 5845 warnings (5842 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
3773 warnings generated.
Suppressed 3772 warnings (3772 in non-user code).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
6370 warnings generated.
Suppressed 6369 warnings (6366 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
4914 warnings generated.
Suppressed 4912 warnings (4909 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
5838 warnings generated.
Suppressed 5841 warnings (5838 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
6685 warnings generated.
Suppressed 6667 warnings (6664 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
7315 warnings generated.
Suppressed 7304 warnings (7298 in non-user code, 6 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
6369 warnings generated.
Suppressed 6368 warnings (6365 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
1582 warnings generated.
Suppressed 1556 warnings (1555 in non-user code, 1 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
5868 warnings generated.
Suppressed 5856 warnings (5853 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
5859 warnings generated.
Suppressed 5841 warnings (5838 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
5894 warnings generated.
Suppressed 5885 warnings (5882 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
6161 warnings generated.
Suppressed 6163 warnings (6160 in non-user code, 3 NOLINT).
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_set.cc:132:10: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  *ret = metadata.size;
         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_sortedint.cc:110:10: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  *ret = metadata.size;
         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_string.cc:167:21: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  metadata.expire = expire;
                    ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_string.cc:243:21: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  metadata.expire = expire;
                    ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_string.cc:375:23: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    metadata.expire = expire;
                      ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_string.cc:417:23: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    metadata.expire = expire;
                      ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_string.cc:463:23: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    metadata.expire = expire;
                      ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:146:10: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  *ret = metadata.size;
         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:176:56: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  if (count > static_cast<int>(metadata.size)) count = metadata.size;
                                                       ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:241:27: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  if (start < 0) start += metadata.size;
                          ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:242:25: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
  if (stop < 0) stop += metadata.size;
                        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:708:23: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    if (size) *size = mscores.size();
                      ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/types/redis_zset.cc:757:23: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    if (size) *size = mscores.size();
                      ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/main.cc:83:44: warning: narrowing conversion from 'size_t' (aka 'unsigned long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
      LOG(ERROR) << std::left << std::setw(max_msg_len) << messages[i] << "  " << func_info;
                                           ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:414:32: warning: narrowing conversion from 'std::basic_string<char>::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
Suppressed 5848 warnings (5845 in non-user code, 3 NOLINT).
      *output = Redis::Integer(value.size());
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
                               ^
5876 warnings generated.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:641:14: warning: narrowing conversion from 'long' to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
4696 warnings generated.
      ttl_ = *ttl_ms / 1000;
Suppressed 4695 warnings (4692 in non-user code, 3 NOLINT).
             ^
Use -header-filter=.* to display errors from all non-system headers. Use -system-headers to display errors from system headers as well.
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1075:38: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      output->append(Redis::MultiLen(infos.size()));
                                     ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:1195:18: warning: narrowing conversion from 'StatusOr<long>::value_type' (aka 'long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    timestamp_ = *parse_result;
                 ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2131:36: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output->append(Redis::MultiLen(exists.size()));
                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2529:36: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output->append(Redis::MultiLen(memeber_scores.size() * 2));
                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2579:38: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      output->append(Redis::MultiLen(member_scores.size()));
                                     ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2581:38: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      output->append(Redis::MultiLen(member_scores.size() * 2));
                                     ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2687:38: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      output->append(Redis::MultiLen(member_scores.size()));
                                     ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:2689:38: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      output->append(Redis::MultiLen(member_scores.size() * 2));
                                     ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3222:32: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      *output = Redis::Integer(geo_points.size());
                               ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3230:25: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
    int result_length = geo_points.size();
                        ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3402:36: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output->append(Redis::MultiLen(exists.size()));
                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3442:36: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output->append(Redis::MultiLen(ids.size()));
                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3498:36: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output->append(Redis::MultiLen(ids.size()));
                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3546:30: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    *output = Redis::Integer(result);
                             ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3603:33: warning: narrowing conversion from 'std::deque::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    conn->Reply(Redis::MultiLen(conn->GetMultiExecCommands()->size()));
                                ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3675:32: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      *output = Redis::Integer(stats.n_key);
                               ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3802:38: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      output->append(Redis::MultiLen(channel_subscribe_nums.size() * 2));
                                     ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:3805:39: warning: narrowing conversion from 'size_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
        output->append(Redis::Integer(chan_subscribe_num.subscribe_num));
                                      ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4161:32: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      *output = Redis::Integer(conn->GetID());
                               ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4271:47: warning: narrowing conversion from 'unsigned long' to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
        auto s = GetKeysFromCommand(args_[2], args_.size() - 2, &keys_indexes);
                                              ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4618:30: warning: narrowing conversion from 'uint32_t' (aka 'unsigned int') to signed type 'int' is implementation-defined [cppcoreguidelines-narrowing-conversions]
      conn->SetListeningPort(port_);
                             ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4715:68: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to 'double' [cppcoreguidelines-narrowing-conversions]
            static_cast<uint64_t>(static_cast<double>(file_size) / max_replication_bytes * (1000 * 1000));
                                                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4786:40: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
        output->append(Redis::MultiLen(infos.size()));
                                       ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4788:42: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
          output->append(Redis::MultiLen(info.nodes.size() + 2));
                                         ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4904:61: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      Status s = svr->cluster_->SetClusterNodes(nodes_str_, set_version_, force_);
                                                            ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4918:61: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      Status s = svr->cluster_->SetSlot(slot_id_, args_[4], set_version_);
                                                            ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:4925:19: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      int64_t v = svr->cluster_->GetVersion();
                  ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5013:33: warning: narrowing conversion from 'unsigned long' to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      *output = Redis::MultiLen(args_.size() - 2);
                                ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5211:30: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    *output = Redis::Integer(deleted);
                             ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5230:30: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    *output = Redis::Integer(len);
                             ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5286:35: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output->append(Redis::Integer(info.size));
                                  ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5292:35: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output->append(Redis::Integer(info.entries_added));
                                  ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5314:38: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      output->append(Redis::MultiLen(info.entries.size()));
                                     ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5396:36: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output->append(Redis::MultiLen(result.size()));
                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5486:36: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output->append(Redis::MultiLen(result.size()));
                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5631:36: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output->append(Redis::MultiLen(results.size()));
                                   ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5636:38: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      output->append(Redis::MultiLen(result.entries.size()));
                                     ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5742:35: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    output.append(Redis::MultiLen(results.size()));
                                  ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5747:37: warning: narrowing conversion from 'std::vector::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
      output.append(Redis::MultiLen(result.entries.size()));
                                    ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:5883:30: warning: narrowing conversion from 'uint64_t' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
    *output = Redis::Integer(removed);
                             ^
/home/runner/work/incubator-kvrocks/incubator-kvrocks/src/commands/redis_cmd.cc:6160:32: warning: narrowing conversion from 'std::map<std::basic_string<char>, const Redis::CommandAttributes *>::size_type' (aka 'unsigned long') to signed type 'int64_t' (aka 'long') is implementation-defined [cppcoreguidelines-narrowing-conversions]
  info->append(Redis::MultiLen(original_commands.size()));
                               ^
```

Some of these reports will give modification suggestions in the log, you can refer to them directly; otherwise, you need to understand the content of the warning and combine your C++ knowledge to fix it. (Fortunately, most reports (except those by clang static analyzer) are intuitive and easy to fix.)

When you fixed these all reports listed above, you can now add the check `cppcoreguidelines-narrowing-conversions` to `warnings-as-errors` in `.clang-tidy` (in the root dir of the repo): We show a sample diff below to illustrate how to modify `.clang-tidy`:

```diff
--- a/.clang-tidy
+++ b/.clang-tidy
@@ -1,7 +1,7 @@
 # refer to https://clang.llvm.org/extra/clang-tidy/checks/list.html
 Checks: ...

-WarningsAsErrors: ...
+WarningsAsErrors: ..., cppcoreguidelines-narrowing-conversions
```

Then, if all of the above are completed, congratulations, you can submit a PR for your changes now!

