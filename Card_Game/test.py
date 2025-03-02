import pygame
import sys
import random
from functools import cache
#
pygame.init()
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
back_ground = (174,175,176)
red = (255, 0, 0)
white = (255, 255, 255)
width_display = 1280
height_display = 720
display = pygame.display.set_mode((width_display, height_display))
display.fill(back_ground)
pygame.time.Clock().tick(60)
pygame.display.set_caption("Digital Collectible Card Game")
font = pygame.font.SysFont(None, 36)
#
@cache
def end():
    pygame.quit()
    sys.exit()

#   класс карты
class Card:
    def __init__(self, name, attack, health, cost):
        self.name = name
        self.attack = attack
        self.health = health
        self.cost = cost

    def __repr__(self):
        return f"name: {self.name} (attack: {self.attack} health: {self.health} cost: {self.cost})"

#   класс игрока
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 9
        self.mana = 0
        self.deck = []
        self.hand = []
        self.field = []

    def draw_card(self):
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)

    def play_card(self, card_index, target=None):
        card = self.hand[card_index]
        if self.mana >= card.cost:
            self.mana -= card.cost
            self.field.append(card)
            del self.hand[card_index]
            return True
        return False

#   функция для броска монетки
def coin_toss():
    return random.choice([True, False])

#   функция отображения текста
def draw_text(text, x, y, color=black):
    text_surface = font.render(text, True, color)
    display.blit(text_surface, (x, y))

#   основная функция игры
def main():
    #   создание колоды
    deck1 = [
        Card("Рыцарь", 3, 3, 2),
        Card("Маг", 2, 4, 3),
        Card("Стрелок", 4, 2, 4),
        Card("Воин", 5, 5, 5),
    ] * 5

    deck2 = [
        Card("Огненный элементаль", 4, 3, 3),
        Card("Ледяной голем", 3, 5, 4),
        Card("Дракон", 7, 6, 6),
        Card("Чародей", 2, 6, 5),
    ] * 5

    random.shuffle(deck1)
    random.shuffle(deck2)

    #   создание игроков
    player1 = Player("Игрок 1")
    player2 = Player("Игрок 2")
    player1.deck = deck1
    player2.deck = deck2

    #   бросок монетки
    player1_turn = coin_toss()
    print(f"{'Игрок 1' if player1_turn else 'Игрок 2'} ходит первым.")

    #   начальная раздача карт
    for _ in range(3):
        player1.draw_card()
    for _ in range(4):
        player2.draw_card()

    #   главный цикл игры
    running = True
    current_player = player1 if player1_turn else player2
    while running:
        display.fill(back_ground)

        #   отображение информации о здоровье игроков
        draw_text(f"{player1.name}: {player1.health}", 50, 10, red)
        draw_text(f"{player2.name}: {player2.health}", 50, 50, blue)

        #   отображение карт на руке текущего игрока
        for i, card in enumerate(current_player.hand):
            draw_text(f"{i + 1}. {card}", 50, 100 + i * 30, black)

        #   обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #   конец хода
                    current_player.mana += 1
                    current_player.draw_card()
                    current_player = player2 if current_player == player1 else player1

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
