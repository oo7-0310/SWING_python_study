import random  #answer값을 랜덤으로 받아와야 함

top = [11]  # top리스트 초기화, 비교값 설정해주려고 임의로 값 넣어줌
while (1):  #게임종료를 누르지 않는 이상 게임은 계속 진행된다.
    answer = random.randrange(1, 101)  #1~100까지의 랜덤 수를 정답으로 지정
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    num = int(input(">>"))  #기능 선택
    max = 100
    min = 1
    if num == 1:
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
               
                if top[0] > i:
                    top.append(i) # 최고 기록일 때만 기록에 추가하기
                    print("최고기록 갱신~!")  #top의 첫번째 인덱스 값보다 작으면 최고기록
                break

    elif num == 2:
        top.sort()  #기록확인 시 top 리스트 안의 값들을 순서대로 정렬함(작은수 -> 큰수)
        for i in range(
                len(top) -
                1):  #처음에 list의 첫번째 인덱스 값을 11로 해주었기 때문에 마지막 숫자를 제외하고 출력되도록 함
            print("%d %d" % (i + 1, top[i]))  #i부터 하면 0부터이므로 i+1
    elif num ==3:#3 선택 시 게임 종료 
        break
    else:  #4번 선택지 외의 숫자를 입력했을 경우 다시 메뉴 입력하기
      continue
        
