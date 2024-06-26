import pygame


class SpriteSheet():
    def __init__(self, image, frames, width, height, scale, colour, running, total_frame, left):
        self.sheet = image
        self.frames = frames
        self.width = width
        self.height = height
        self.scale = scale
        self.colour = colour
        self.running = running
        self.total_frame = total_frame
        self.left = left

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_image(self, frame, scale):
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA).convert_alpha()
        image.blit(pygame.image.load(self.sheet).convert_alpha(), (0, 0),((frame * self.width), 0, self.width, self.height))
        image = pygame.transform.scale(image, (self.width * scale, self.height * scale))
        if self.left == True:
            image = pygame.transform.flip(image, True, False)
        image.set_colorkey(self.colour)
        return image

    def start_animation(self, scale, display, x=0, y=0, frame=0):
        if self.running == False:
            self.frames = frame
            self.running = True
        self.running = True
        self.scale = scale
        if self.running == False:
            return
        if self.frames == self.total_frame - 1:
            self.frames = 0
            image_xy = (x, y)
            image = self.get_image(self.frames, self.scale)
            display.blit(image, image_xy)
            self.frames += 1
        else:
            display.blit(self.get_image(self.frames, self.scale), (x, y))
            self.frames += 1

        pygame.display.update()

    def stop_animation(self):
        self.running = False
