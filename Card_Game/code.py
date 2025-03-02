"""Card Game"""
from importlib import import_module
from functools import cache
asyncio, random, sys = import_module('asyncio'), import_module('random'), import_module('sys')
pygame = import_module('pygame')
#
pygame.init()
#   цвета
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
back_ground = (174,175,176)
red = (255, 0, 0)
white = (255, 255, 255)
#   дисплей
width_display = 1280
height_display = 720
display = pygame.display.set_mode((width_display, height_display))
display.fill(back_ground)
pygame.time.Clock().tick(60)
#   название
pygame.display.set_caption("Digital Collectible Card Game")
#   кнопки
left_button = width_display/(2*1.5+1)*1.5
top_button = height_display/(2*1.5+5+4*0.5)*1.5
width_button = width_display/(2*1.5+1*1)
height_button = height_display/(2*1.5+5+4*0.5)
size = 70
font = pygame.font.Font(None, size)
#   кнопки текст
text_surface_play = font.render("Играть", True, white)
text_surface_settings = font.render("Настройки", True, white)
text_surface_rules = font.render("Правила", True, white)
text_surface_about = font.render("Об игре", True, white)
text_surface_exit = font.render("Выход", True, white)
text_surface_about_ON = font.render("", True, white)
#   функции
@cache
def end():
    """exit"""
    pygame.quit()
    sys.exit()
#   кнопки блоки
button_play = pygame.Rect(left_button, top_button, width_button, height_button)
button_settings = pygame.Rect(left_button, top_button*2, width_button, height_button)
button_rules = pygame.Rect(left_button, top_button*3, width_button, height_button)
button_about = pygame.Rect(left_button, top_button*4, width_button, height_button)
button_exit = pygame.Rect(left_button, top_button*5, width_button, height_button)
button_about_ON = pygame.Rect(0,0,1280,720)
#   текст на кнопках
text_rect_play = text_surface_play.get_rect(topleft=(left_button, top_button))
text_rect_settings = text_surface_settings.get_rect(topleft=(left_button, top_button*2))
text_rect_rules = text_surface_rules.get_rect(topleft=(left_button, top_button*3))
text_rect_about = text_surface_about.get_rect(topleft=(left_button, top_button*4))
text_rect_exit = text_surface_exit.get_rect(topleft=(left_button, top_button*5))
#   тело программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_play.collidepoint(event.pos):
                print("Играть")
            if button_settings.collidepoint(event.pos):
                print("Настройки")
            if button_rules.collidepoint(event.pos):
                print("Правила")
            if button_about.collidepoint(event.pos):
                print("Об игре")
            if button_exit.collidepoint(event.pos):
                end()
    #   кнопки
    pygame.draw.rect(display, black, button_play)
    pygame.draw.rect(display, black, button_settings)
    pygame.draw.rect(display, black, button_rules)
    pygame.draw.rect(display, black, button_about)
    pygame.draw.rect(display, black, button_exit)
    pygame.draw.rect(display, back_ground, button_about_ON)
    #   текст на кнопках
    display.blit(text_surface_play, text_rect_play)
    display.blit(text_surface_settings, text_rect_settings)
    display.blit(text_surface_rules, text_rect_rules)
    display.blit(text_surface_about, text_rect_about)
    display.blit(text_surface_exit, text_rect_exit)
    #
    pygame.display.flip()
