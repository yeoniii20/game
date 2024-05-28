import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("공 튀기기 게임")

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)

# 공 속성
ball_pos = [screen_width // 2, screen_height // 2]
ball_radius = 20
ball_color = white
ball_speed = [3, 3]

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 공 위치 업데이트
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # 공이 화면 경계를 벗어나면 반사
    if ball_pos[0] <= ball_radius or ball_pos[0] >= screen_width - ball_radius:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= ball_radius or ball_pos[1] >= screen_height - ball_radius:
        ball_speed[1] = -ball_speed[1]

    # 화면을 검정색으로 채우기
    screen.fill(black)

    # 공 그리기
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60프레임으로 설정
    clock.tick(60)
