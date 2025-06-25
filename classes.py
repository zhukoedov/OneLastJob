import vars
import preloads
import pygame


class Icon(pygame.sprite.Sprite):
    def __init__(self, image, x, y,):
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = vars.glblt.speed

    def blit(self):
        preloads.screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.y += self.speed


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False

    def draw(self, surface):
        # Определяем текущий цвет кнопки (при наведении или нет)
        current_color = self.hover_color if self.is_hovered else self.color

        # Рисуем прямоугольник кнопки
        pygame.draw.rect(surface, current_color, self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2)  # Обводка

        # Рендерим текст
        text_surface = preloads.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Отображаем текст на кнопке
        surface.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_click):
        return self.rect.collidepoint(mouse_pos) and mouse_click
