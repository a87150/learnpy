import re
import time

pattern = '/devices/([^/]+)/([^/]+)'
test_rounds = 1000000
 
begin_time = time.time()
for i in range(test_rounds):
    re.match(pattern, '/devices/sn_201312201560/uplink_frequency')
    re.match(pattern, '/alarm/system')

print(time.time() - begin_time)
 
begin_time = time.time()
compiled_pattern = re.compile(pattern)
for i in range(test_rounds):
    compiled_pattern.match('/devices/sn_201312201560/uplink_frequency')
    compiled_pattern.match('/alarm/system')

print(time.time() - begin_time)