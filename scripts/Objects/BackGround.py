import pygame

class Background:
    def __init__(self, images, frame_size = 2):
        self.frame_size = frame_size
        self.fram = 0
        self.images = images
        self.pos = (0, 0)

    def update(self):
        self.fram = self.fram + 1
        if self.fram > self.frame_size:
            self.fram = 0
            self.pos = (self.pos[0] - 1, 0)
            if self.pos[0] < -1 * self.images[self.name].get_width():
                self.pos = (0, 0)

    def create(self, name, size = (0, 0)):
        self.name = name
        self.image = pygame.Surface((size[0] + self.images[self.name].get_width() * 3,size[1] + self.images[self.name].get_height() * 3))
        for i in range(int(size[1] / self.images[name].get_width()) + 3):
            for t in range(int(size[0] / self.images[name].get_height()) + 3):
                self.image.blit(self.images[name], (t * self.images[name].get_height(), i * self.images[name].get_width()))

    def render(self, surface : pygame.Surface):
        self.update()
        surface.blit(self.image, self.pos)
