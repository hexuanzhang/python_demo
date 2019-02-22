from datetime import timedelta, datetime

time = timedelta(days=1, seconds=60, weeks=1)

# 属性
print(time.min) # 最小值，'-999999999 days, 0:00:00'
print(time.max) # 最大值，'999999999 days, 23:59:59.999999'
print(time.resolution) # 精度，0:00:00.000001

print('------')

# 方法
print(time)
print(str(time)) # 返回字符串，格式为 [D day[s], ][H]H:MM:SS[.UUUUUU]
print(repr(time)) # 返回字符串，格式为：datetime.timedelta(D[, S[, U]])
print(time.total_seconds()) # 返回总秒数，等同于 td / timedelta(seconds=1)

print('------')

today = datetime.now()
print(today)
print(today + timedelta(minutes=30, seconds=30)) # 增加三十分钟三十秒
print(today + timedelta(hours=3)) # 增加三小时
print(today + timedelta(days=1)) # 增加一天
print(today + timedelta(weeks=1)) # 增加一周



