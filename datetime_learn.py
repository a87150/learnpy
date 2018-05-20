from datetime import datetime, timedelta, timezone
import re

tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now() # 获取当前datetime
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
#很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
dt2 = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00

print(now)
print(now + timedelta(days=2, hours=12))
print(now.strftime('%a, %b %d %H:%M'))
print(dt)
print(dt2)
print(dt.timestamp())
print(datetime.fromtimestamp(dt.timestamp()))
print(cday)

# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

def to_timestamp(dt_str, tz_str):
    m = re.match(r'UTC([\+\-]{1}[\d]{1,2})', tz_str)       #获得时区
    n = int(m.group(1))
    dt_str = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt_str = dt_str - timedelta(hours=n-8)              #转为本地时间
    dt_str = dt_str.timestamp()
    return dt_str

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2