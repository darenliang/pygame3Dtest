from typing import Tuple

import pygame

import config
import polyhedron
import vector


def draw_polyhedron(
        screen,
        color: Tuple[int, int, int],
        polyhedron: polyhedron.Polyhedron
):
    """
    Draw polyhedron
    :param screen: Pygame screen to draw on
    :param color: Color to draw with
    :param polyhedron: Polyhedron to draw
    """
    for line in polyhedron.edges:
        pygame.draw.line(
            screen,
            color,
            (
                vector.adjust_coordinate(line[0].coordinates[0]),
                vector.adjust_coordinate(line[0].coordinates[1])
            ),
            (
                vector.adjust_coordinate(line[1].coordinates[0]),
                vector.adjust_coordinate(line[1].coordinates[1])
            )
        )


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(config.TITLE)

    screen = pygame.display.set_mode(
        (config.DISPLAY_LENGTH, config.DISPLAY_LENGTH)
    )

    clock = pygame.time.Clock()

    poly = polyhedron.create_cube()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # handle key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            vector.apply_rotation(poly, 1, (0, 1, 0))
        if keys[pygame.K_RIGHT]:
            vector.apply_rotation(poly, -1, (0, 1, 0))
        if keys[pygame.K_UP]:
            vector.apply_rotation(poly, -1, (1, 0, 0))
        if keys[pygame.K_DOWN]:
            vector.apply_rotation(poly, 1, (1, 0, 0))

        # clear screen for redraw
        screen.fill(config.BACKGROUND_COLOR)

        # draw cube
        draw_polyhedron(screen, config.COLOR, poly)

        pygame.display.flip()

        # clock tick
        clock.tick(config.TICK_RATE)

    pygame.quit()
