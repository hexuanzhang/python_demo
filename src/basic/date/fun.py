from datetime import datetime, timedelta

def timeInterval(date):

    if not isinstance(date, datetime):
        date = datetime.strptime(date, '%y-%m-%d %H:%M:%S')

    daySeconds = 24 * 60 * 60
    now = datetime.now()

    today_from_time = datetime(now.year, now.month, now.day) # 今天零点
    yesterday_from_time = today_from_time - timedelta(days=1) # 昨天零点
    seven_days_from_time = today_from_time - timedelta(days=7) # 七天前零点

    if (date >= today_from_time) and (date < today_from_time + timedelta(1)):
        print('今天')
    elif (date >= yesterday_from_time) and (date < yesterday_from_time + timedelta(1)):
        print('昨天')
    elif (date >= seven_days_from_time) and (date < seven_days_from_time + timedelta(1)):
        print('昨天')
    else:
        print(str(date))

timeInterval(datetime.now() - timedelta(days=20))