import pygame as pg
from random import randrange
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 1200, 1000
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 8000
ball_mass, ball_radius = 1, 7
segment_thickness = 6

a, b, c, d = 10, 100, 18, 40
x1, x2, x3, x4 = a, WIDTH // 2 - c, WIDTH // 2 + c, WIDTH - a
y1, y2, y3, y4, y5 = b, HEIGHT // 4 - d, HEIGHT // 4, HEIGHT // 2 - 1.5 * b, HEIGHT - 4 * b
L1, L2, L3, L4 = (x1, -100), (x1, y1), (x2, y2), (x2, y3)
R1, R2, R3, R4 = (x4, -100), (x4, y1), (x3, y2), (x3, y3)
B1, B2 = (0, HEIGHT), (WIDTH, HEIGHT)
bottom_barrier = (B1, B2)  # Bottom barrier segment

# Function to create boundary segments
def create_boundary_segment(from_, to_, thickness, space, color):
    segment_shape = pymunk.Segment(space.static_body, from_, to_, thickness)
    segment_shape.color = pg.color.THECOLORS[color]
    segment_shape.elasticity = 0.1
    segment_shape.friction = 0.5
    space.add(segment_shape)

# Create boundary segments to enclose the screen
create_boundary_segment((0, 0), (WIDTH, 0), 20, space, 'darkslategray')
create_boundary_segment((0, 0), (0, HEIGHT), 20, space, 'darkslategray')
create_boundary_segment((WIDTH, 0), (WIDTH, HEIGHT), 20, space, 'darkslategray')
create_boundary_segment(*bottom_barrier, 20, space, 'darkslategray')  # Add the bottom barrier

def create_ball(space):
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = randrange(x2, x3), randrange(y2, y4)  # Ensure balls are within the box
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.1
    ball_shape.friction = 10
    space.add(ball_body, ball_shape)
    return ball_body

# Rest of your code...

# balls
balls = [([randrange(256) for i in range(3)], create_ball(space)) for j in range(6)]

while True:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    # [pg.draw.circle(surface, color, ball.position, ball_radius) for color, ball in balls]
    [pg.draw.circle(surface, color, (int(ball.position[0]), int(ball.position[1])),
                    ball_radius) for color, ball in balls]

    pg.display.flip()
    clock.tick(FPS)
