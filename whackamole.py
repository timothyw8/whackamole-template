import pygame
import random

def main():
    def draw_grid():
        for i in range(1, 16):
            pygame.draw.line(screen, (0, 0, 0), (0, i*(512/16)), (640, i*(512/16)), width=1)
        for x in range(1,20):
            pygame.draw.line(screen, (0, 0, 0), (x*(640/20), 0), (x*(640/20), 512), width=1)
    try:
        pygame.init()

        screen = pygame.display.set_mode((640, 512))
        screen.fill("light green")

        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))


        clock = pygame.time.Clock()
        running = True
        draw_grid()
        mole_coordX = 0
        mole_coordY = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_coord = event.pos[0]
                    y_coord = event.pos[1]
                    if x_coord < (mole_coordX+32) and y_coord < (mole_coordY+32) and x_coord>mole_coordX and y_coord>mole_coordY:
                        pygame.draw.rect(screen, "light green", pygame.Rect(mole_coordX, mole_coordY, 25,25))
                        mole_coordX = random.randrange(2,640,32)
                        mole_coordY = random.randrange(2,512,32)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_coordX,mole_coordY)))

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
