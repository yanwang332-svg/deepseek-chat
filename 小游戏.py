import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D旋转立方体 - PyCharm")
clock = pygame.time.Clock()

# 立方体的8个顶点
vertices = [
    [-1, -1, -1],  # 0
    [1, -1, -1],  # 1
    [1, -1, 1],  # 2
    [-1, -1, 1],  # 3
    [-1, 1, -1],  # 4
    [1, 1, -1],  # 5
    [1, 1, 1],  # 6
    [-1, 1, 1]  # 7
]

# 12条棱的连接关系
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # 底面
    (4, 5), (5, 6), (6, 7), (7, 4),  # 顶面
    (0, 4), (1, 5), (2, 6), (3, 7)  # 垂直棱
]

# 6个面的颜色（RGBA，带透明度）
faces = [
    ([0, 1, 2, 3], (255, 0, 0, 100)),  # 底面 - 红
    ([4, 5, 6, 7], (0, 255, 0, 100)),  # 顶面 - 绿
    ([0, 1, 5, 4], (0, 0, 255, 100)),  # 前面 - 蓝
    ([2, 3, 7, 6], (255, 255, 0, 100)),  # 后面 - 黄
    ([0, 3, 7, 4], (255, 0, 255, 100)),  # 左面 - 紫
    ([1, 2, 6, 5], (0, 255, 255, 100))  # 右面 - 青
]


def project_3d_to_2d(x, y, z, fov=500, viewer_distance=5):
    """3D投影到2D"""
    factor = fov / (viewer_distance + z)
    x2d = x * factor + WIDTH // 2
    y2d = -y * factor + HEIGHT // 2
    return int(x2d), int(y2d)


def rotate_point(x, y, z, angle_x, angle_y, angle_z):
    """绕三个轴旋转"""
    # 绕X轴旋转
    cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
    y1 = y * cos_x - z * sin_x
    z1 = y * sin_x + z * cos_x
    y, z = y1, z1

    # 绕Y轴旋转
    cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
    x1 = x * cos_y + z * sin_y
    z1 = -x * sin_y + z * cos_y
    x, z = x1, z1

    # 绕Z轴旋转
    cos_z, sin_z = math.cos(angle_z), math.sin(angle_z)
    x1 = x * cos_z - y * sin_z
    y1 = x * sin_z + y * cos_z
    x, y = x1, y1

    return x, y, z


# 旋转角度
angle_x = angle_y = angle_z = 0
auto_rotate = True

print("🎲 3D旋转立方体！")
print("按空格键 - 切换自动/手动旋转")
print("方向键 - 手动控制旋转")
print("鼠标拖动 - 多维度旋转")
print("ESC - 退出")

# 鼠标控制
mouse_down = False
last_mouse_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                auto_rotate = not auto_rotate
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            last_mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        if event.type == pygame.MOUSEMOTION and mouse_down:
            if last_mouse_pos:
                dx = pygame.mouse.get_pos()[0] - last_mouse_pos[0]
                dy = pygame.mouse.get_pos()[1] - last_mouse_pos[1]
                angle_y += dx * 0.01
                angle_x += dy * 0.01
                last_mouse_pos = pygame.mouse.get_pos()

    # 自动旋转
    if auto_rotate:
        angle_x += 0.01
        angle_y += 0.015
        angle_z += 0.005

    # 键盘控制
    keys = pygame.key.get_pressed()
    if not auto_rotate:
        if keys[pygame.K_LEFT]:
            angle_y -= 0.05
        if keys[pygame.K_RIGHT]:
            angle_y += 0.05
        if keys[pygame.K_UP]:
            angle_x -= 0.05
        if keys[pygame.K_DOWN]:
            angle_x += 0.05
        if keys[pygame.K_q]:
            angle_z -= 0.05
        if keys[pygame.K_e]:
            angle_z += 0.05

    screen.fill((0, 0, 0))

    # 旋转并投影所有顶点
    projected_points = []
    for vertex in vertices:
        x, y, z = rotate_point(vertex[0], vertex[1], vertex[2], angle_x, angle_y, angle_z)
        x, y = project_3d_to_2d(x, y, z)
        projected_points.append((x, y))

    # 绘制面（带透明度）
    for face, color in faces:
        points = [projected_points[i] for i in face]
        # 创建临时表面用于透明度
        s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.polygon(s, color, points)
        screen.blit(s, (0, 0))

    # 绘制棱
    for edge in edges:
        pygame.draw.line(screen, (255, 255, 255),
                         projected_points[edge[0]],
                         projected_points[edge[1]], 2)

    # 绘制顶点
    for point in projected_points:
        pygame.draw.circle(screen, (255, 255, 0), point, 4)

    # 显示信息
    font = pygame.font.Font(None, 24)
    info = f"模式: {'自动旋转' if auto_rotate else '手动控制'}"
    if not auto_rotate:
        info += " | 方向键旋转 | Q/E绕Z轴"
    text = font.render(info, True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()