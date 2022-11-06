import turtle
import random

# 전역 변수 설정
map_size = 800  # 바둑판 크기
map_n = 10  # n * n 크기의 맵
turtlesize = 10 / map_n # 객체 크기 지정
move_error_message = "그 방향으로는 움직일 수 없습니다."
start_point = (int(-map_size / 2), int(-map_size / 2))  # user 시작지점
move_speed = 4  # target과 user 객체의 속도
one_point = map_size // map_n  # 한 칸의 크기

# turtle 객체 초기화
turtle.setup(width=int(map_size * 1.1), height=int(map_size * 1.1))  # 바둑판 크기에 10% 여유 추가
setter = turtle.Turtle()
setter.hideturtle()  # 안보이게
setter.speed(0)  # 가장 빠름
setter.penup()
setter.goto(start_point)
setter.pendown()

user = turtle.Turtle()
user.hideturtle()
user.shape("circle")  # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
user.color("blue")
user.penup()  # 커서의 이동경로 표시 X
user.speed(move_speed)
user.resizemode("user")
user.shapesize(turtlesize, turtlesize, 1)
user.shapesize()

target = turtle.Turtle()
target.hideturtle()
target.shape("square")
target.color("red")
target.penup()
target.speed(move_speed)
target.resizemode("user")
target.shapesize(turtlesize, turtlesize, 1)
target.shapesize()


# target, user 초기화
def init_game():
    user.hideturtle()
    user.speed(0)
    user.goto(start_point)
    user.speed(move_speed)
    user.showturtle()

    target.hideturtle()
    target.speed(0)
    # 2차평면에서 user는 왼쪽 아래 즉 3사분면에 존재한다.
    # 따라서 3사분면을 제외한 1,2,4사분면에 랜덤하게 타겟이 배치되도록 한다.
    xy_zone = int(random.random() * 10) % 3
    x = int(random.random() * 10) % int(map_n / 2) * one_point
    y = int(random.random() * 10) % int(map_n / 2) * one_point
    if xy_zone == 1:  # 2사분면 x는 음수
        x = x * -1
    elif xy_zone == 2:  # 4사분면 y는 음수
        y = y * -1
    target.goto(x, y)
    target.speed(move_speed)
    target.showturtle()


# 맵 그리기
def draw_map():
    '''# 사각형 하나씩 그리면서 바둑판 깔기
    # for j in range(1, 101):
    #     for i in range(100):
    #         setpos = setter.pos()
    #         setter.goto(setpos[0] + one_point, setpos[1])
    #         setter.goto(setpos[0] + one_point, setpos[1] + one_point)
    #         setter.goto(setpos[0], setpos[1] + one_point)
    #         setter.goto(setpos[0], setpos[1])
    #         setter.goto(setpos[0] + one_point, setpos[1])
    #     setter.penup()
    #     setter.goto(start_point[0], start_point[1] + one_point * j)
    #     setter.pendown()'''

    # 가로선 그리기
    for i in range(1, map_n + 2):
        setpos = setter.pos()
        setter.goto(-start_point[0], setpos[1])
        setter.penup()
        setter.goto(start_point[0], start_point[1] + one_point * i)
        setter.pendown()

    setter.penup()
    setter.goto(-start_point[0], -start_point[1])
    setter.pendown()
    # 세로선 그리기
    for i in range(1, map_n + 2):
        setpos = setter.pos()
        setter.goto(setpos[0], start_point[1])
        setter.penup()
        setter.goto(setpos[0] - one_point, setpos[1])
        setter.pendown()


# play game
def game1(cnt):
    print()
    print(cnt, "번째 시도입니다.\n", end="")
    game_cnt = 0
    while user.pos() != target.pos():
        game_cnt += 1
        # 유저 움직이기
        for _ in range(3):
            user_pos = user.pos()

            while True:
                key = input("가고자 하는 방향을 입력하세요 : ")
                if key == 'a':
                    if user_pos[0] <= start_point[0]:
                        print(move_error_message)
                        continue
                    else:
                        user.goto(user_pos[0] - one_point, user_pos[1])
                elif key == 's':
                    if user_pos[1] <= start_point[1]:
                        print(move_error_message)
                        continue
                    else:
                        user.goto(user_pos[0], user_pos[1] - one_point)
                elif key == 'd':
                    if user_pos[0] >= -start_point[0]:
                        print(move_error_message)
                        continue
                    else:
                        user.goto(user_pos[0] + one_point, user_pos[1])
                elif key == 'w':
                    if user_pos[1] >= -start_point[1]:
                        print(move_error_message)
                        continue
                    else:
                        user.goto(user_pos[0], user_pos[1] + one_point)
                else:
                    print("잘못된 입력입니다.\na = 왼쪽, s = 아래쪽, d = 오른쪽, w = 위쪽")
                    continue
                break

            if user.pos() == target.pos():
                break
        if user.pos() == target.pos():
            break

        user_pos = user.pos()
        target_pos = target.pos()

        # 타겟 움직이기
        print("타겟이 도망갑니다.")
        # 2번 움직여 갈 수 있는 모든 경우의 수
        target_movable_pos = [target_pos,
                              (target_pos[0] + one_point, target_pos[1] + one_point),
                              (target_pos[0] + one_point, target_pos[1] - one_point),
                              (target_pos[0] - one_point, target_pos[1] + one_point),
                              (target_pos[0] - one_point, target_pos[1] - one_point),
                              (target_pos[0] + one_point * 2, target_pos[1]),
                              (target_pos[0] - one_point * 2, target_pos[1]),
                              (target_pos[0], target_pos[1] + one_point * 2),
                              (target_pos[0], target_pos[1] - one_point * 2)]
        target_hope = target_pos
        distance = abs(user_pos[0] - target_hope[0]) + abs(user_pos[1] - target_hope[1])

        # user로 부터 가장 멀리 있는 지점 선택
        for pos in target_movable_pos:
            if pos[0] < start_point[0] or pos[0] > -start_point[0] \
                    or pos[1] < start_point[1] or pos[1] > -start_point[1]:
                pos = target_pos

            will_distance = abs(user_pos[0] - pos[0]) + abs(user_pos[1] - pos[1])
            if will_distance > distance:
                distance = will_distance
                target_hope = pos

        temp_pos = target_pos
        # 이동할 위치와 현재위치가 같다면, 코너에 몰린 것입니다.
        # 제자리를 유지합니다.
        if target_hope != target_pos:
            for i in range(int(abs(temp_pos[0] - target_hope[0]) // one_point)):
                if target_hope[0] - temp_pos[0] > 0:
                    target.goto(target_pos[0] + one_point, target_pos[1])
                else:
                    target.goto(target_pos[0] - one_point, target_pos[1])
                target_pos = target.pos()

            for i in range(int(abs(temp_pos[1] - target_hope[1]) // one_point)):
                if target_hope[1] - temp_pos[1] > 0:
                    target.goto(target_pos[0], target_pos[1] + one_point)
                else:
                    target.goto(target_pos[0], target_pos[1] - one_point)
                target_pos = target.pos()
        else:
            print("타겟이 코너에 몰렸습니다!")

    print(game_cnt, "번만에 타겟을 잡았습니다!!\n", end="")
    return game_cnt


if __name__ == '__main__':
    draw_map()
    player_list = []
    print("타켓 쫒기 게임에 오신 걸 환영합니다!!\n")
    while True:
        if input("시작하려면 아무키나 누르세요(종료 q)") == 'q':
            break

        try_cnt = 0
        for i in range(1):
            init_game()
            try_cnt += game1(i + 1)

        print("축하합니다. 총", try_cnt, "회 만에 성공하셨습니다.\n", end="")
        nickname = input("닉네임을 입력해주세요 : ")
        player_list.append((nickname, try_cnt))

        # TODO: player_list 정렬후 순위대로 출력할 것
        print(player_list)

    print("게임을 종료합니다.")
