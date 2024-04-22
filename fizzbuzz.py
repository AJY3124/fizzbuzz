# issue룰 추가 후 수정했습니다
for i in range(100):
    if i % 3 == 0 or i % 5 ==0:
        print('Fizz'*(i%3==0) + 'Buzz'*(i%5==0))
    else:
        print(i)

