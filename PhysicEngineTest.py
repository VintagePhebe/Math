import pygame as pg
import pymunk.pygame_util
import pymunk
from random import randrange
import math

pg.init()

RES = WIDTH, HEIGHT = 1200, 1000
FPS = 60

surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 800

# Ball properties with radii multiplied by 7
ball_data = [
    (pg.Color(255, 0, 0), 7 * 7),      # Dimension 1: Red
    (pg.Color(0, 255, 0), 10 * 7),     # Dimension 2: Green
    (pg.Color(0, 0, 255), 13 * 7),     # Dimension 3: Blue
]

ball_shapes = [pymunk.Circle(space.static_body, radius) for _, radius in ball_data]

balls = []

def create_boundary_segment(from_, to_, thickness, space, color):
    segment_shape = pymunk.Segment(space.static_body, from_, to_, thickness)
    segment_shape.color = pg.color.THECOLORS[color]
    segment_shape.elasticity = 0.1
    segment_shape.friction = 0.5
    space.add(segment_shape)

def create_ball(space, position, dimension):
    color, radius = ball_data[dimension]
    ball_mass = 1
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = position
    ball_shape = pymunk.Circle(ball_body, radius)
    ball_shape.elasticity = 0.1
    ball_shape.friction = 10
    space.add(ball_body, ball_shape)
    return color, ball_body, dimension

for i in range(4):
    thickness = 20
    color = 'darkslategray'
    if i == 0:
        from_, to_ = (0, 0), (WIDTH, 0)
    elif i == 1:
        from_, to_ = (0, 0), (0, HEIGHT)
    elif i == 2:
        from_, to_ = (WIDTH, 0), (WIDTH, HEIGHT)
    else:
        from_, to_ = (0, HEIGHT), (WIDTH, HEIGHT)
    create_boundary_segment(from_, to_, thickness, space, color)

while True:
    surface.fill(pg.Color('black'))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_x, mouse_y = pg.mouse.get_pos()
            # Create the smallest ball (dimension 1) when clicking
            color, ball, dimension = create_ball(space, (mouse_x, mouse_y), 0)
            balls.append((color, ball, dimension))  # Store color, body, and dimension

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    # Check for ball merging
    i = 0
    while i < len(balls) - 1:
        color1, ball1, dimension1 = balls[i]
        color2, ball2, dimension2 = balls[i + 1]

        if dimension1 == dimension2:
            # Merge the balls to the next dimension
            new_dimension = dimension1 + 1

            if new_dimension < len(ball_data):
                # Create a new merged ball
                color, new_ball, _ = create_ball(space, ball1.position, new_dimension)
                balls.pop(i)  # Remove the first ball
                balls.pop(i)  # Remove the second ball
                balls.append((color, new_ball, new_dimension))  # Add the merged ball
            else:
                i += 1
        else:
            i += 1

    # Draw the balls
    for color, ball, _ in balls:
        pg.draw.circle(surface, color, (int(ball.position.x), int(ball.position.y)), ball_shapes[0].radius)

    pg.display.flip()
    clock.tick(FPS)
