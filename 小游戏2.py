import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("迷信射击 - PyCharm版")
clock = pygame.time.Clock()


class Target:
    def __init__(self):
        self.radius = 30
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.color = (255, 0, 0)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # 边界反弹
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.speed_x *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        # 绘制靶心
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius - 5)
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius - 10)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius - 15)

    def is_hit(self, pos):
        distance = math.sqrt((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2)
        return distance <= self.radius


# 游戏设置
targets = [Target() for _ in range(5)]
score = 0
shots = 0
font = pygame.font.Font(None, 36)
running = True

print("🎯 靶心射击游戏！")
print("用鼠标点击红色的靶心")
print("每击中一个得10分")
print("总共有20次射击机会")

while running and shots < 20:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shots += 1
            mouse_pos = pygame.mouse.get_pos()
            for target in targets[:]:
                if target.is_hit(mouse_pos):
                    score += 10
                    targets.remove(target)
                    targets.append(Target())

    # 更新
    for target in targets:
        target.update()

    # 绘制
    screen.fill((0, 0, 0))
    for target in targets:
        target.draw(screen)

    # 显示分数
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    shots_text = font.render(f"Shots: {shots}/20", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(shots_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

# 游戏结束画面
screen.fill((0, 0, 0))
game_over_text = font.render("GAME OVER!", True, (255, 0, 0))
final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 50))
screen.blit(final_score_text, (WIDTH // 2 - 80, HEIGHT // 2))
pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()