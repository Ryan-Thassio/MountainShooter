import pygame

from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.velocity = 0
        self.gravity = 0.4
        self.jump_strength = -12
        self.original_y = self.rect.centery
        self.Jump = False
        self.Jump_frames = []
        for i in range(6):
            image = pygame.image.load(f'Assets/Jump{i}.png').convert_alpha()
            image = pygame.transform.scale(image, (120, 150))
            self.Jump_frames.append(image)
        self.animation_speed = 0.2
        self.Jump_index = 0

        self.frames = []
        for i in range(6):
            image = pygame.image.load(f'Assets/Run{i}.png').convert_alpha()
            image = pygame.transform.scale(image, (120, 150))
            self.frames.append(image)
        self.animation_speed = 0.2
        self.frame_index = 0


        self.surf = self.frames[self.frame_index]

        self.crouch_walk_frames = []
        for i in range(6):
            image = pygame.image.load(f'Assets/Crouch_Walk{i}.png').convert_alpha()
            image = pygame.transform.scale(image, (100, 90))

            self.crouch_walk_frames.append(image)

        self.crouch_walk = False
        self.crouch_walk_index = 0


    def update(self):
        self.animate()

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_SPACE] and not self.Jump:
            self.velocity = self.jump_strength
            self.Jump = True
            self.Jump_index = 0
        if pressed_key[pygame.K_DOWN]:
            self.crouch_walk = True
        else:
            self.crouch_walk_index = 0
            self.crouch_walk = False





        # gravidade sempre atua
        self.velocity += self.gravity
        self.rect.centery += self.velocity

        # chão (voltar pra posição original)
        if self.rect.centery >= self.original_y:
            self.rect.centery = self.original_y
            self.velocity = 0
            self.Jump = False


    def animate(self):
        if self.Jump:
            self.animation_speed = 0.2
            self.Jump_index += self.animation_speed
            if self.Jump_index > len(self.Jump_frames):
                self.Jump_index -= 1
            self.surf = self.Jump_frames[int(self.Jump_index)]


        elif self.crouch_walk:
            self.animation_speed = 0.2
            self.crouch_walk_index += self.animation_speed
            if self.crouch_walk_index >= len(self.crouch_walk_frames):
                    self.crouch_walk_index -= 3

            self.surf = self.crouch_walk_frames[int(self.crouch_walk_index)]
            self.rect.y += 60


        else:
            self.animation_speed = 0.2
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.frames):
                self.frame_index = 0

            self.surf = self.frames[int(self.frame_index)]

