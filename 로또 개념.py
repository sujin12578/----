import random

print(random(random())) # 0 이상 1 미만의 임의의 실수 반환

# 주사위처럼 임의의 1~6
print(random.randrange(1,7)) # 1 이상 7 미만의 난수
print(random.randint(1,45))

abc = [1,2,3,4,5] # 데이터를 썩어 넣음
#abc = random.shuffle(abc)
#print(abc)

random.choice(abc)
menu = ('쫄면', '육개장', '비빔밥')
random.choice(menu)
random.choice([True, False])

# 1. 리스트로 뽑아낼 것
# 2. 중복을 제거할 것
# 3. 로직 작성 시 for문으로 리스트에서 제공하는 함수 등으로 구성할 것것
lotto = LottoNum()

print(lotto.get_lotto_nums()) # [1,2,3,4,5,6]
