import random  #answer값을 랜덤으로 받아와야 함
from datetime import datetime #날짜 호출하려고 import

top = [11]  # top리스트 초기화, 비교값 설정해주려고 임의로 값 넣어줌
nameSave = []
dateSave = []
while (1):  #게임종료를 누르지 않는 이상 게임은 계속 진행된다.
    answer = random.randrange(1, 101)  #1~100까지의 랜덤 수를 정답으로 지정
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    num = int(input(">>"))  #기능 선택
    max = 100
    min = 1
    f = open('record.txt', 'w')
    if num == 1:
     #try:
        for i in range(1, 11):
            
            n = int(input("%d번째 숫자 입력(%d~%d):" % (i, min, max)))  #숫자 입력

            while min > n or max < n:
              print("범위 안의 숫자를 입력해주세요.")
              n = int(input("%d번째 숫자 입력(%d~%d):" % (i, min, max)))  #1,2번 조건에 맞는 숫자 입력해야 다음으로 넘어감

            if answer > n :
                print("UP")
                min = n  #입력 값이 정답 값보다 작으면 범위를 (입력값,최대값)으로 수정
            elif answer < n:
                print("DOWN")
                max = n  #입력 값이 정답 값보다 크면  범위를 (최소값,입력값)으로 수정
            else:
                print("정답입니다!!\n%d번째만에 맞추셨습니다." % i)
                print(top)
               
                if top[0] > i:
                    top.insert(0,i) # 최고 기록일 때만 기록에 추가하기
                    print("최고기록 갱신~!")  #top의 첫번째 인덱스 값보다 작으면 최고기록
                    name = input("닉네임을 입력하세요 >> %s" % i)
                    nameSave.insert(0,name)
                    date = datetime.today().strftime("%Y-%m-%d") #현재 년월일
                    dateSave.insert(0,date)
                    print(top)
                    print(nameSave)
                    print(dateSave)
                    
                    for x in range(len(nameSave)):
                        #f=open('record.txt', 'w')
                        f.writelines(str(top[x])+ "  " + str(nameSave[x])+ "  " + str(dateSave[x])+"\n")
                        #print(top[x]+ nameSave[x]+dateSave[x])
                    

                    break
                    
                
                break
     #except Exception as e:
      #  print("error : 입력횟수를 초과하였습니다. 게임오버!")

    elif num == 2:
      f=open('record.txt', 'r')
      while True:
        line = f.readline()
        if line =='':
          break
        print(line, end= '')
      

            

    elif num ==3:#3 선택 시 게임 종료
        print("UP & DOWN 게임이 종료됩니다.")
        #f=open('record.txt','w')
        #for i in range(len(top) -1):
          #f.writelines("%d %s %d %s" % (i + 1 ,nameSave[i], top[i],dateSave[i]))
       # break
        f.close
    else:  #4번 선택지 외의 숫자를 입력했을 경우 다시 메뉴 입력하기
      continue
        