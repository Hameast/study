import turtle
import random
from time import sleep

# 전역 변수 설정
# 맵 관련 변수
map_n = 10  # n * n 크기의 맵, test 용 10, 과제는 100
map_size = 800  # 바둑판 크기
one_point = map_size // map_n  # 한 칸의 크기
start_point = (int(-map_size / 2) - (map_size // 4), int(-map_size / 2))  # user 시작 지점, 맵 남서 끝 지점
end_point = (-start_point[0] - (map_size // 2), int(map_size / 2))  # 맵 북동 끝 지점
center_point = (- map_size // 4, 0)  # 맵 중간 지점

# 게임 관련 변수
player_list = [('---', 10000) for _ in range(10)]
play_time = 1  # user 가 기록 하기 까지 플레이 할 횟수
user_try_cnt = 0  # 한 게임 에서 시도한 횟수
user_try_cnt_total = 0  # 5 게임의 시도 횟수 총합
user_game_cnt = 0  # 게임 횟수
click_buffer = False  # 클릭 이벤트 조절용

# turtle 관련 변수
turtle_speed = 4  # target 과 user 객체의 속도
turtle_size = 1.5  # target 과 user 객체의 크기
turtle_color = ('red', 'orange', 'gold', 'green', 'cyan', 'blue', 'purple')
turtle_shape = ('arrow', 'turtle', 'circle', 'square', 'triangle', 'classic')

# turtle 객체 생성
scr = turtle.Screen()
scr.tracer(0)  # 최초 설정 전까지 화면 변화 표시 안함
scr.title("Team4's Turtle Game")
scr.setup(width=1280, height=880)

printer0 = turtle.Turtle()
printer1 = turtle.Turtle()
printer2 = turtle.Turtle()
user = turtle.Turtle()
target = turtle.Turtle()
up_btn = turtle.Turtle()
down_btn = turtle.Turtle()
left_btn = turtle.Turtle()
right_btn = turtle.Turtle()


def easter_egg():
    if turtle.textinput("Link...Link...", "Who am I?").lower() == "zelda":
        scr.bgcolor('#01A049')
    else:
        scr.bgcolor('white')


def turn360(t):
    t.speed(3)
    t.right(360)
    t.speed(turtle_speed)


def customize_user_color(x, y):
    next_color = turtle_color.index(user.color()[0]) + 1  # 현재 값의 인덱스에 + 1
    if next_color >= len(turtle_color):  # 인덱스가 최댓값을 넘으면 0으로
        next_color = 0
    color = turtle_color[next_color]  # 색상 결정
    user.color(color)  # 색상 설정
    return x, y


def customize_user_shape(x, y):
    next_shape = turtle_shape.index(user.shape()) + 1
    if next_shape >= len(turtle_shape):
        next_shape = 0
    shape = turtle_shape[next_shape]
    user.shape(shape)
    return x, y


def customize_target_color(x, y):
    next_color = turtle_color.index(target.color()[0]) + 1
    if next_color >= len(turtle_color):
        next_color = 0
    color = turtle_color[next_color]
    target.color(color)
    return x, y


def customize_target_shape(x, y):
    next_shape = turtle_shape.index(target.shape()) + 1
    if next_shape >= len(turtle_shape):
        next_shape = 0
    shape = turtle_shape[next_shape]
    target.shape(shape)
    return x, y


def btn_right(x, y):
    global click_buffer
    click_buffer = True  # 버튼 클릭이 아닌 키보드 입력일 땐 False
    right_btn.color("black")  # 버튼이 눌림을 표현하기 위해 색상 변경
    unset_game_key()  # 이동중에 새로운 입력을 받지 못하게 event 끄기

    if round(user.pos()[0]) >= round(end_point[0]):  # user 위치가 맵 가장자리에 위치한 경우
        turn360(user)  # 이동 불가를 표현하기 위해 한 바퀴 돌기
        right_btn.color("gray")  # 버튼 색상 원래대로
        set_game_key()  # 다시 입력 받을 수 있게 event 켜기
        return

    user.setheading(0)  # turtle 객체가 오른쪽을 바라보도록
    user.forward(one_point)  # 앞으로 이동
    right_btn.color("gray")  # 버튼 색상 원래대로
    if check_continue():
        set_game_key()  # 다시 입력 받을 수 있게 event 켜기
    return x, y


def btn_up(x, y):
    global click_buffer
    click_buffer = True
    up_btn.color("black")
    unset_game_key()
    if round(user.pos()[1]) >= round(end_point[1]):
        turn360(user)
        up_btn.color("gray")
        set_game_key()
        return

    user.setheading(90)
    user.forward(one_point)
    up_btn.color("gray")
    if check_continue():
        set_game_key()
    return x, y


def btn_left(x, y):
    global click_buffer
    click_buffer = True
    left_btn.color("black")
    unset_game_key()
    if round(user.pos()[0]) <= round(start_point[0]):
        turn360(user)
        left_btn.color("gray")
        set_game_key()
        return

    user.setheading(180)
    user.forward(one_point)
    left_btn.color("gray")
    if check_continue():
        set_game_key()
    return x, y


def btn_down(x, y):
    global click_buffer
    click_buffer = True
    down_btn.color("black")
    unset_game_key()
    if round(user.pos()[1]) <= round(start_point[1]):
        turn360(user)
        down_btn.color("gray")
        set_game_key()
        return

    user.setheading(270)
    user.forward(one_point)
    down_btn.color("gray")
    if check_continue():
        set_game_key()
    return x, y


def btn_none(x, y):
    return x, y


def right():
    global click_buffer
    click_buffer = False
    unset_game_key()
    if round(user.pos()[0]) >= round(end_point[0]):
        turn360(user)
        set_game_key()
        return

    user.setheading(0)
    user.forward(one_point)
    if check_continue():
        set_game_key()


def up():
    global click_buffer
    click_buffer = False
    unset_game_key()
    if round(user.pos()[1]) >= round(end_point[1]):
        turn360(user)
        set_game_key()
        return

    user.setheading(90)
    user.forward(one_point)
    if check_continue():
        set_game_key()


def left():
    global click_buffer
    click_buffer = False
    unset_game_key()
    if round(user.pos()[0]) <= round(start_point[0]):
        turn360(user)
        set_game_key()
        return

    user.setheading(180)
    user.forward(one_point)
    if check_continue():
        set_game_key()


def down():
    global click_buffer
    click_buffer = False
    unset_game_key()
    if round(user.pos()[1]) <= round(start_point[1]):
        turn360(user)
        set_game_key()
        return

    user.setheading(270)
    user.forward(one_point)
    if check_continue():
        set_game_key()


def none():
    pass


# 방향키 입력 설정
def set_game_key():
    printer1.clear()
    printer1.goto(start_point[0], end_point[1] + 20)
    printer1.write(f"Game {user_game_cnt + 1} , Try {user_try_cnt + 1} , Total {user_try_cnt_total + 1}",
                   move=False, align="left", font=("arial", 10, "bold"))

    up_btn.onclick(btn_up, btn=1, add=None)
    down_btn.onclick(btn_down, btn=1, add=None)
    left_btn.onclick(btn_left, btn=1, add=None)
    right_btn.onclick(btn_right, btn=1, add=None)
    scr.onkey(up, 'Up')
    scr.onkey(down, 'Down')
    scr.onkey(left, 'Left')
    scr.onkey(right, 'Right')
    scr.listen()


# 방향키 입력 중지
def unset_game_key():
    up_btn.onclick(btn_none, btn=1, add=None)
    down_btn.onclick(btn_none, btn=1, add=None)
    left_btn.onclick(btn_none, btn=1, add=None)
    right_btn.onclick(btn_none, btn=1, add=None)
    scr.onkey(none, 'Up')
    scr.onkey(none, 'Down')
    scr.onkey(none, 'Left')
    scr.onkey(none, 'Right')
    scr.listen()


# 엔터키 감지, 게임 시작
def press_enter():
    printer1.clear()
    scr.onclick(btn_none, btn=1, add=None)
    scr.onkey(none, 'q')
    scr.onkey(none, 'Return')
    scr.listen()

    init_game()
    target_run()
    set_game_key()


# 클릭 감지, 게임 시작
def screen_clicked(x, y):
    global click_buffer
    if click_buffer:
        click_buffer = False
        return

    printer1.clear()
    scr.onclick(btn_none, btn=1, add=None)
    scr.onkey(none, 'q')
    scr.onkey(none, 'Return')
    scr.listen()

    init_game()
    target_run()
    set_game_key()
    return x, y


# 이동후 확인
def check_continue():
    global user_try_cnt_total, user_try_cnt, user_game_cnt
    user_try_cnt += 1
    user_try_cnt_total += 1
    user_pos = user.pos()
    target_pos = target.pos()

    # catch
    if int(round(user_pos[0])) == int(round(target_pos[0])) and \
            int(round(user_pos[1])) == int(round(target_pos[1])):
        user_game_cnt += 1
        user_try_cnt = 0
        target.hideturtle()
        turn360(user)
        # game over and wait new game
        if user_game_cnt >= play_time:
            nickname = turtle.textinput("Game Clear!!", "Enter your 3-digit initials")
            if nickname:
                player_list.append((nickname, user_try_cnt_total))
            else:
                player_list.append(("___", user_try_cnt_total))
            user_try_cnt_total = 0
            user_try_cnt = 0
            user_game_cnt = 0
            draw_rank()
            set_standby()
            return False
        init_game()
        target_run()
    elif user_try_cnt % 3 == 0:
        target_run()

    return True


# 타겟 도망 가기
def target_run():
    # user, target 위치 저장
    user_pos = user.pos()
    target_pos = target.pos()
    # 2번 움직여 갈 수 있는 모든 경우의 수 (9개)
    target_hope = target_pos
    target_movable_pos = [(target_pos[0] + one_point, target_pos[1] + one_point),
                          (target_pos[0] + one_point, target_pos[1] - one_point),
                          (target_pos[0] - one_point, target_pos[1] + one_point),
                          (target_pos[0] - one_point, target_pos[1] - one_point),
                          (target_pos[0] + one_point * 2, target_pos[1]),
                          (target_pos[0] - one_point * 2, target_pos[1]),
                          (target_pos[0], target_pos[1] + one_point * 2),
                          (target_pos[0], target_pos[1] - one_point * 2)]
    distance = abs(user_pos[0] - target_hope[0]) + abs(user_pos[1] - target_hope[1])

    # user 로 부터 가장 멀리 있는 지점 선택
    # 이동할 위치와 현재 위치가 같다면, 코너에 몰린 것 입니다.
    # 코너에 몰리면 제 자리를 유지 합니다.
    for pos in target_movable_pos:
        if pos[0] < start_point[0] or pos[0] > end_point[0] \
                or pos[1] < start_point[1] or pos[1] > end_point[1]:
            continue
        this_distance = abs(user_pos[0] - pos[0]) + abs(user_pos[1] - pos[1])
        if this_distance >= distance:
            distance = this_distance
            target_hope = pos

    temp_pos = target_pos

    # 갈 수 있는 가장 먼 지점 으로 이동
    if target_hope != target_pos:
        # x 축 이동
        for _ in range(int(abs(round(temp_pos[0] - target_hope[0])) // one_point)):
            if target_hope[0] - temp_pos[0] > 0:
                target.setheading(0)  # 오른쪽 이동
                target.goto(target_pos[0] + one_point, target_pos[1])
            else:
                target.setheading(180)  # 왼쪽 이동
                target.goto(target_pos[0] - one_point, target_pos[1])
            target_pos = target.pos()

        # y 축 이동
        for _ in range(int(abs(round(temp_pos[1] - target_hope[1])) // one_point)):
            if target_hope[1] - temp_pos[1] > 0:
                target.setheading(90)  # 위쪽 이동
                target.goto(target_pos[0], target_pos[1] + one_point)
            else:
                target.setheading(270)  # 아래쪽 이동
                target.goto(target_pos[0], target_pos[1] - one_point)
            target_pos = target.pos()
    else:
        turn360(target)


# target, user 위치 초기화
def init_game():
    user.hideturtle()  # 터틀 안 보이게
    target.hideturtle()  # 터틀 안 보이게

    user.speed(0)  # speed 0가장 빠름
    user.goto(start_point)  # start point = (-600, -400)
    user.speed(turtle_speed)  # 설정된 속도로 바꿈
    user.setheading(0)  # 터틀의 머리가 오른쪽을 향하도록

    # 2차 평면 에서 user 는 왼쪽 아래 즉 3사 분면에 존재 한다.
    # target 과 적당한 거리를 두기 위해서
    # 3사 분면을 제외한 1,2,4사 분면에 랜덤 하게 타겟이 배치 되도록 한다.
    xy_zone = int(random.random() * 10) % 3
    x = int(random.random() * 10) % (map_n // 2 + 1) * one_point
    y = int(random.random() * 10) % (map_n // 2 + 1) * one_point
    if xy_zone == 1:  # 2사분면 x는 음수
        x = x * -1
    elif xy_zone == 2:  # 4사분면 y는 음수
        y = y * -1

    target.speed(0)  # speed 0가장 빠름
    target.goto(x - 200, y)  # 터틀 이동
    target.speed(turtle_speed)  # 설정된 속도로 바꿈
    target.setheading(0)  # 터틀의 머리가 오른쪽을 향하도록

    user.showturtle()  # 터틀 보이게
    target.showturtle()  # 터틀 보이게

    # blink
    for _ in range(2):
        sleep(0.2)  # 0.2초 대기
        user.hideturtle()  # 터틀 안보이게
        target.hideturtle()  # 터틀 안보이게
        sleep(0.2)  # 0.2초 대기
        user.showturtle()  # 터틀 보이게
        target.showturtle()  # 터틀 보이게


# 터틀 객체 설정
def init_turtle():
    # 터틀 객체 안 보이게
    for t in scr.turtles():
        t.hideturtle()

    scr.onkey(easter_egg, 'h')

    # 바둑판 그리기 용
    printer0.speed(0)  # 가장 빠름 0, 느린 순서로 1 ~ 10
    printer0.penup()  # 커서의 이동 경로 표시 X
    printer0.goto(start_point)  # 해당 좌표로 이동
    printer0.pendown()  # 커서의 이동 경로 표시 O

    # 게임 상태 표시용
    printer1.speed(0)
    printer1.penup()  # 커서의 이동 경로 표시 X
    printer1.goto(center_point[0] - 60, 0)

    # 게임 로딩 %표시 및 랭킹 표시용
    printer2.speed(0)
    printer2.penup()  # 커서의 이동 경로 표시 X
    printer2.goto(center_point[0] + 130, 0)

    # 유저
    user.shape("turtle")  # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
    user.color("blue")
    user.penup()
    user.shapesize(turtle_size, turtle_size, 1)
    user.onclick(customize_user_color, btn=1)  # 좌클릭
    user.onclick(customize_user_shape, btn=3)  # 우클릭

    # 목표 지점
    target.shape("square")
    target.color("red")
    target.penup()
    target.shapesize(turtle_size, turtle_size, 1)
    target.onclick(customize_target_color, btn=1)  # 좌클릭
    target.onclick(customize_target_shape, btn=3)  # 우클릭

    # 버튼
    up_btn.speed(0)
    up_btn.penup()  # 커서의 이동 경로 표시 X
    up_btn.goto(end_point[0] + 120, start_point[1] + 140)
    up_btn.shapesize(4, 4, 4)
    up_btn.color("gray")
    up_btn.setheading(90)

    down_btn.speed(0)
    down_btn.penup()  # 커서의 이동 경로 표시 X
    down_btn.goto(end_point[0] + 120, start_point[1] + 10)
    down_btn.shapesize(4, 4, 4)
    down_btn.color("gray")
    down_btn.setheading(270)

    left_btn.speed(0)
    left_btn.penup()  # 커서의 이동 경로 표시 X
    left_btn.goto(end_point[0] + 50, start_point[1] + 75)
    left_btn.shapesize(4, 4, 4)
    left_btn.color("gray")
    left_btn.setheading(180)

    right_btn.speed(0)
    right_btn.penup()  # 커서의 이동 경로 표시 X
    right_btn.goto(end_point[0] + 190, start_point[1] + 75)
    right_btn.shapesize(4, 4, 4)
    right_btn.color("gray")
    right_btn.setheading(0)


# 맵 그리기
def draw_map():
    # 가로선 그리기
    for row in range(map_n + 1):
        printer0.goto(end_point[0], start_point[1] + row * one_point)
        printer0.penup()
        printer0.goto(start_point[0], start_point[1] + (row + 1) * one_point)
        printer0.pendown()
    printer0.penup()
    printer0.goto(end_point)
    printer0.pendown()
    # 세로선 그리기
    for col in range(map_n + 1):
        printer0.goto(end_point[0] - col * one_point, start_point[1])
        printer0.penup()
        printer0.goto(end_point[0] - (col + 1) * one_point, end_point[1])
        printer0.pendown()

    printer0.penup()
    printer0.goto(end_point[0] + 30, end_point[1])
    printer0.pendown()
    printer0.pensize(5)

    printer0.setheading(270)
    printer0.forward(620)
    printer0.setheading(0)
    printer0.forward(350)
    printer0.setheading(90)
    printer0.forward(620)
    printer0.setheading(180)
    printer0.forward(350)

    printer0.penup()
    printer0.goto(end_point[0] + 30, end_point[1] - 650)
    printer0.pendown()

    printer0.setheading(270)
    printer0.forward(150)
    printer0.setheading(0)
    printer0.forward(350)
    printer0.setheading(90)
    printer0.forward(150)
    printer0.setheading(180)
    printer0.forward(350)

    printer0.penup()
    printer0.setheading(0)
    printer0.forward(185)
    printer0.setheading(270)
    printer0.forward(100)
    printer0.write("조작 방법\n1. 좌측의 버튼 클릭\n2. 키보드의 방향키 입력",
                   move=False, align="left", font=("arial", 10, "bold"))

    up_btn.showturtle()
    down_btn.showturtle()
    left_btn.showturtle()
    right_btn.showturtle()


# 10등까지 랭킹 표시
def draw_rank():
    global player_list
    player_list.sort(key=lambda x: x[1])  # 시도 횟수 적은 순으로 정렬
    player_list = player_list[:10]  # 메모리 절약겸 10등 까지만 저장

    printer2.clear()  # printer2로 그린 것들 전체 삭제
    printer2.goto(end_point[0] + 50, end_point[1] - 100)
    printer2.write("Ranking", move=False, align="left",
                   font=("Freestyle Script", 50, "bold"))

    # 10등 까지의 유저를 등수 대로 화면 우측에 표시
    # 1등은 다른 색으로 표시
    # 닉네임 은 3글자의 대문자 로만 표시
    for rank, player in enumerate(player_list):
        printer2_pos = printer2.pos()
        printer2.goto(printer2_pos[0], printer2_pos[1] - 50)
        printer2.pencolor('purple') if rank == 0 else None
        printer2.write(f"{str(rank + 1).rjust(2, '0')}등:" +
                       f" {player[0][:3].upper().rjust(3, '_')} ," +
                       f" {str(player[1]).rjust(4, '0') if player[1] < 10000 else '----'}회",
                       move=False, align="left", font=("Consolas", 25, "bold"))
        printer2.pencolor('black') if rank == 0 else None


# 대기 화면 세팅
def set_standby():
    user.hideturtle()
    target.hideturtle()

    printer1.clear()
    printer1.pencolor('green')
    printer1.goto(center_point)
    printer1.write("Click Screen or Press Enter", move=False, align="center", font=("Courier", 30, "bold"))
    printer1.goto(center_point[0], center_point[1] - 50)
    printer1.write("To Start", move=False, align="center", font=("Courier", 30, "bold"))
    printer1.pencolor('black')

    scr.onclick(screen_clicked, btn=1, add=None)
    scr.onkey(press_enter, 'Return')
    scr.onkey(scr.bye, 'q')
    scr.onkey(none, 'Up')
    scr.onkey(none, 'Down')
    scr.onkey(none, 'Left')
    scr.onkey(none, 'Right')
    scr.listen()


# 초기 세팅
def first_init():
    init_turtle()  # 터틀 객체 설정
    draw_map()  # 맵 그리기
    draw_rank()  # 랭크 표시
    set_standby()  # 대기 화면 세팅
    scr.tracer(1)  # 최초 설정 완료, 다시 화면 변화 표시 할 수 있도록


# main
if __name__ == '__main__':
    print("게임 시작")
    first_init()
    scr.mainloop()
    print("게임 종료")
