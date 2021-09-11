import random

top = [11]
while(1):
  answer = random.randrange(1,101) #1~100까지의 랜덤 수를 정답으로 지정

  print(answer)
  print("UP & DOWN 게임에 오신걸 환영합니다~")
  print("1. 게임시작 2. 기록확인 3. 게임종료")
  num = int(input(">>")) #기능 선택
  max = 100
  min = 1
  if num==1:
    for i in range(1,11):
      n=int(input("%d번째 숫자 입력(%d~%d):" %(i,min,max))) #숫자 입력
      if answer>n:
        print("UP")
        min = n #입력 값이 정답 값보다 작으면 범위를 (입력값,최대값)으로 수정
      elif answer<n:
        print("DOWN")
        max = n #입력 값이 정답 값보다 크면  범위를 (최소값,입력값)으로 수정
      else:
        print("정답입니다!!\n%d번째만에 맞추셨습니다." %i)
        top.append(i)
        if top[0] > i:
          print("최고기록 갱신~!")
        break
        
  elif num==2:
    top.sort()
    for i in range(len(top)-1):
      print("%d %d" %(i+1,top[i]))
  else:
    break
