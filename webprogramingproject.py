import turtle
import keyboard
 
t1 = turtle.Turtle() #빨간색 거북이 (1번 주자)
t2 = turtle.Turtle() #파란색 거북이 (2번 주자)
line = turtle.Turtle() #맵을 그리고 결과를 출력하기 위한 터틀

line.shape('circle')
line.pensize(3)
line.hideturtle()
line.speed(0)
line.penup()
line.goto(-70, 150)
line.write("거북이 경주", font=("",20))
line.goto(-250, 100)
line.pendown()
line.goto(250, 100)
line.goto(250, -100)
line.goto(-250, -100)
line.goto(-250, 100)
line.goto(-250, 0)
line.goto(250, 0) #직사각형의 경주맵을 그림 (500x200)
 
t1.shape('turtle')
t1.color('red') 
t1.penup()
t1.speed(0)
t1.goto(-250, 50) #1번 주자의 위치를 지정
 
t2.shape('turtle')
t2.color('blue')
t2.penup()
t2.speed(0)
t2.goto(-250, -50) #2번 주자의 위치를 지정

result = "" #결과를 저장할 문자열
 
def t1space(): #스페이스 바를 눌렀을 때 1번 주자를 앞으로 보내는 함수
    t1.forward(5)

def t2rightarrow(): #오른쪽 방향키를 눌렀을 때 2번 주자를 앞으로 보내는 함수
    t2.forward(5)
 
while(True):
    if(keyboard.read_key() == "space"): #스페이스 바 입력이 감지되면 함수 실행
        t1space() 
    if(keyboard.read_key() == "right"): #오른쪽 방향키 입력이 감지되면 함수 실행
        t2rightarrow()

    if(t1.position() == (250,50)): #1번 주자가 이겼을 시 결과 문자열을 지정해주고, while을 빠져나옴
        result = "1번 주자가 이겼습니다."
        line.color('red')
        break
    elif(t2.position() == (250, -50)): #2번 주자가 이겼을 시 결과 문자열을 지정해주고, while을 빠져나옴
        result = "2번 주자가 이겼습니다."
        line.color('blue')
        break

line.penup()
line.goto(-100, -200)
line.write(result, font=("", 20)) #결과 출력
line.mainloop() #프로그램 자동 종료 막기