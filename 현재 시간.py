# datetime 모듈

from datetime import datetime

now = datetime.now() # 현재시간 리턴

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# 특정한 날짜 객체 생성
dt = datetime(2023,1,1)
print(dt)

dt = datetime(2019, 9, 2, 21, 25, 29)
#__str__ = dt.strftime("%Y %m %d %H %M %S")

print(dt) # dt.strftime("%Y %m")

print(dt.weekday()) #weekday(): 요일 반환 (0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일)
print(dt.strftime("%Y====%m=====%d")) # format 약속된것도 넣을수 있고, 내가 넣고 넣을수 있고.

# 시간 연산

dt1 = datetime(2016, 2, 19, 14)
dt2 = datetime(2016, 1, 2, 13)
td = dt1 - dt2

#timedelta 클래스

print(td)
print(td.days)
print(td.seconds)
print(td.microseconds)
print(td.total_seconds())

import datetime

now = datetime.datetime.now()

print(type(now))
print(now)

if (4 <= now.hour) and (now.hour < 12):
    print("굿모닝")
elif 12 <= now.hour < 18:
    print("굿애프터눈")
elif 18 <= now.hour < 22:
    print("굿이브닝")
else:
    print("굿나잇")






