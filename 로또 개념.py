import random

print(random(random())) # 0 이상 1 미만의 임의의 실수 반환

# 주사위처럼 임의의 1~6
print(random.randrange(1,7)) # 1 이상 7 미만의 난수
print(random.randint(1,45))

abc = [1,2,3,4,5] # 데이터를 썩어 넣음
#abc = random.shuffle(abc)
#print(abc)

random.choice(abc)