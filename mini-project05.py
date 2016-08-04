# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH/2, HEIGHT/2]
    horizontal_vel = random.randrange(120, 240)/60
    vertical_vel = -random.randrange(60, 180)/60

    if direction == "LEFT":
        ball_vel = [horizontal_vel, vertical_vel]
    else:
        ball_vel = [-horizontal_vel, vertical_vel]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2

    paddle1_pos, paddle2_pos = (HEIGHT - PAD_HEIGHT)/2, (HEIGHT - PAD_HEIGHT)/2
    paddle1_vel = paddle2_vel = 0
    score1, score2 = 0, 0
    direction = random.choice(["LEFT","RIGHT"])
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_line([PAD_WIDTH/2, paddle1_pos],[PAD_WIDTH/2, paddle1_pos+PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH/2, paddle2_pos],[WIDTH- PAD_WIDTH/2, paddle2_pos+PAD_HEIGHT], PAD_WIDTH, "White")

    # determine whether paddle and ball collide
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            spawn_ball("LEFT")
            score2 += 1
    if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            spawn_ball("RIGHT")
            score1 += 1
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]

    # draw scores
    canvas.draw_text(str(score1), (150, 50), 60, "White", "monospace")
    canvas.draw_text(str(score2), (415, 50), 60, "White", "monospace")

def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 3
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 5
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -5
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

def restart_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart_handler, 100)

# start frame
new_game()
frame.start()

http://www.codeskulptor.org/#user41_VoGZTf5hOe7otdE.py
