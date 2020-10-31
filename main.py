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

    # Tick clock to limit FPS
    clock = pygame.time.Clock()

    # 3D object to render
    poly = polyhedron.create_cube()

    # State variables
    running = True
    mouse_dragging = False
    mouse_x, mouse_y = (0, 0)

    while running:
        for event in pygame.event.get():

            # Quit button
            if event.type == pygame.QUIT:
                running = False

            # Mouse down
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_dragging = True
                mouse_x, mouse_y = event.pos

            # Mouse up
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_dragging = False

            # Mouse dragging
            elif event.type == pygame.MOUSEMOTION and mouse_dragging:
                # Get new mouse position
                new_mouse_x, new_mouse_y = event.pos

                # Calculate mouse position delta
                delta_x, delta_y = (
                    new_mouse_x - mouse_x, new_mouse_y - mouse_y
                )

                # Apply rotation based on mouse position delta
                vector.apply_rotation(poly, delta_y, (1, 0, 0))
                vector.apply_rotation(poly, -delta_x, (0, 1, 0))

                # Store new mouse position as old mouse position
                mouse_x, mouse_y = (new_mouse_x, new_mouse_y)

        # Handle key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            vector.apply_rotation(poly, 1, (0, 1, 0))
        if keys[pygame.K_RIGHT]:
            vector.apply_rotation(poly, -1, (0, 1, 0))
        if keys[pygame.K_UP]:
            vector.apply_rotation(poly, -1, (1, 0, 0))
        if keys[pygame.K_DOWN]:
            vector.apply_rotation(poly, 1, (1, 0, 0))

        # Clear screen for redraw
        screen.fill(config.BACKGROUND_COLOR)

        # Draw cube
        draw_polyhedron(screen, config.COLOR, poly)

        pygame.display.flip()

        # Clock tick
        clock.tick(config.TICK_RATE)

    pygame.quit()
