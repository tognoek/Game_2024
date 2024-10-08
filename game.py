import pygame, sys
from ENV import WINDOWS_SCREEN, DISPLAY_SIZE
from models.game_scenes.gamecanvas import GameCanvas

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(WINDOWS_SCREEN, pygame.NOFRAME)

pygame.mouse.set_visible(False)

icon = pygame.image.load("data/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Tog")

display = pygame.Surface(DISPLAY_SIZE)

ratio = (DISPLAY_SIZE[0] / WINDOWS_SCREEN[0], DISPLAY_SIZE[1] / WINDOWS_SCREEN[1])

class Game:
    def __init__(self):
        self.GameCanvas = GameCanvas(display=display, ratio=ratio)
        self.running = True
    def run(self):
        while self.running:
            clock.tick(65)
            self.GameCanvas.run(pygame.mouse.get_pos(), clock.get_fps())
            
            for event in pygame.event.get():
                if self.GameCanvas.event(event, pygame.mouse.get_pos()):
                    self.running = False
                    pygame.quit()
                    sys.exit()
                    
            screen.blit(pygame.transform.scale(display, WINDOWS_SCREEN), (0, 0))
            pygame.display.update()
        
if __name__ == "__main__":
    game = Game()
    game.run()

pygame.quit()
sys.exit()
