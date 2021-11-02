import random

# 10부터 99까지의 난수와 입력값 비교
# 두자리 다 맞을 경우, 두자리 중 하나만 맞을 경우, 안맞을 경우

num1 = random.randint(10, 99)
print("생성된 난수 : ", num1)

num2 = int(input("입력값 : "))

if num1 == num2:
    print("두자리 다 맞음.")
elif num1 // 10 == num2 // 10 or num1 % 10 == num2 % 10:
    print("한자리만 맞음")
else:
    print("두자리 모두 안맞음.")

# 다른 방법
li_num1 = list(str(num1))
li_num2 = list(str(num2))
cnt = 0
for i in range(len(li_num1)):
    if li_num1[i] == li_num2[i]:
        cnt += 1

if cnt == 2:
    print("두자리 다 맞음.")
elif cnt == 1:
    print("한자리만 맞음")
else:
    print("두자리 모두 안맞음.")
