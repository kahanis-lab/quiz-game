name=input("이름이 뭐예요?")
print(f"{name}님,환영합니다!")
print("퀴즈 게임을 시작합니다!")
score=0
while True:
    print("""
========================================
        🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================""")
    menu=input("번호 골라: ")
    if menu=="5":
        print("게임을 종료합니다.")
        break
    elif menu == "1":
        print("""코디세이 오는데 걸리는 시간?
        1. 10분 
        2. 30분
        3. 1시간
        4. 1시간 30분
        5. 그 이상""")
        try:
           o=int(input("정답 입력:"))
           if o==4:
              print("정답입니다")
              score+=1
                     
           else:
              print("다시 골라")
        except ValueError:
            print("숫자만 입력해요.")
        
    elif menu =="2":
        newquiz=input("퀴즈 추가해:")
        
    elif menu=="3":
        print(newquiz)
    elif menu=="4":
        print(score)
    else:
        print("1~5번까지 고르라니까")


 