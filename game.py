import pygame, sys

# Khởi tạo game
pygame.init()
# Khởi tạo cửa sổ game
SCREEN_WITH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))
# clock = pygame.time.Clock()
# Tựa game
pygame.display.set_caption('Hero techx')
# Load surface text (văn bản)
    # B1: Tạo font (1 font có thể tạo nhiều surface text) => tạo 1 lần
f_game = pygame.font.Font('KnightWarrior.otf', 32)
    # B2: từ font tạo ra surface text
title_new_game = f_game.render('New game', True, 'Yellow')
title_introduce = f_game.render('Introduce', True, 'Yellow')
title_setting = f_game.render('Setting', True, 'Yellow')
    # B3: thiết lập tọa độ cho surface text
line_height = 15
x_title_new_game = SCREEN_WITH/2 - title_new_game.get_width()//2
y_title_new_game = SCREEN_HEIGHT/2 - title_new_game.get_height()//2
x_title_introduce = x_title_new_game
y_title_introduce = y_title_new_game + line_height + title_new_game.get_height()
x_title_setting = x_title_introduce
y_title_setting = y_title_introduce + line_height + title_introduce.get_height()

# Load image surface (hình ảnh)
hero_image = pygame.image.load('hero_pygame.png')
hero_image = pygame.transform.scale(hero_image, (hero_image.get_width()/5, hero_image.get_height()/5))
x_hero = 100
y_hero = 100
# Setup background image
bg_image = pygame.image.load('bg_pygame.jpg')
bg_image = pygame.transform.scale(bg_image, (bg_image.get_width()/3, bg_image.get_height()/3.3))
x_bg = 0
y_bg = 0
# Tạo rect:
    # Cách 1
# hero_rect = pygame.Rect(x_hero, y_hero, hero_image.get_width(),hero_image.get_height())
    # Cách 2
hero_rect = hero_image.get_rect()
hero_rect.x = 100
hero_rect.y = 100
# Load nhạc nền
sound_bg_game = pygame.mixer.Sound('sound_game.wav')
sound_bg_game.play(-1)

# Vòng lặp game
running = True
while running:
    # Thời gian
        # Tạo ra 1 text chứa thời gian
    time = pygame.time.get_ticks()
    title_time = f_game.render(f'Time: {time}', True, 'Red')
    # Xử lý thoát game
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    # Xử lý background
    # screen.fill('White')
    # Xử lý background image
    screen.blit(bg_image, (x_bg, y_bg))        
    # Xử lý kịch bản game
    screen.blit(title_new_game, (x_title_new_game, y_title_new_game))
    screen.blit(title_introduce, (x_title_introduce, y_title_introduce))
    screen.blit(title_setting, (x_title_setting, y_title_setting))
    # Xử lý hero
    pygame.draw.rect(screen, 'Red', hero_rect)
    screen.blit(hero_image, (hero_rect.x, hero_rect.y))
    screen.blit(title_time,(SCREEN_WITH/2,0))
    # Cập nhật game
    pygame.display.flip()

pygame.quit()
sys.exit()