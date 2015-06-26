# Implementation of classic arcade game Pong
# Made by Kartik kapoor

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
TEXT_SIZE=60


# Initialize ball_pos and ball_vel for new bal in middle of table
# If direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction==RIGHT:
        ball_pos=[WIDTH/2,HEIGHT/2]
        ball_vel=[random.randrange(2, 4),-random.randrange(1, 3)]
    elif direction == LEFT:
        ball_pos=[WIDTH/2,HEIGHT/2]
        ball_vel=[-random.randrange(2, 4),-random.randrange(1, 3)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    paddle1_pos=HEIGHT/2
    paddle2_pos=HEIGHT/2
    paddle1_vel=0
    paddle2_vel=0
    global score1, score2  # Initialize to zero
    score1=score2=0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # Draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # Update ball position based on velocity
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    
    # Draw ball        
    canvas.draw_circle(ball_pos,BALL_RADIUS,10,"White","White")
    
    # Reflect ball from the top and bottom walls
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    
    if ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
        
    # Collision detection code for ball and paddle
    
    if ball_pos[0]<=PAD_WIDTH+BALL_RADIUS:
        if (ball_pos[1] >= paddle1_pos-HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos+HALF_PAD_HEIGHT) :
            ball_vel[0]=-ball_vel[0]*1.10
        else:
            spawn_ball(RIGHT)
            score2+=1
        
    if ball_pos[0]>=WIDTH-1-PAD_WIDTH-BALL_RADIUS:
        if (ball_pos[1] >= paddle2_pos-HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos+HALF_PAD_HEIGHT) :
            ball_vel[0]=-ball_vel[0]*1.10
        else:
            score1+=1
            spawn_ball(LEFT)
     
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos-HALF_PAD_HEIGHT+paddle1_vel)>=0 and ((paddle1_pos+HALF_PAD_HEIGHT+paddle1_vel) <=HEIGHT) :
        paddle1_pos+=paddle1_vel
        
    if (paddle2_pos-HALF_PAD_HEIGHT+paddle2_vel)>=0 and ((paddle2_pos+HALF_PAD_HEIGHT+paddle2_vel) <=HEIGHT) :
        paddle2_pos+=paddle2_vel
        
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos-HALF_PAD_HEIGHT],[PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT],[PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT],[0,paddle1_pos+HALF_PAD_HEIGHT]],1,"White","White")
    canvas.draw_polygon([[WIDTH-PAD_WIDTH,paddle2_pos-HALF_PAD_HEIGHT],[WIDTH,paddle2_pos-HALF_PAD_HEIGHT],[WIDTH,paddle2_pos+HALF_PAD_HEIGHT],[WIDTH-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT]],1,"White","White")    
    
    # draw scores
    canvas.draw_text(str(score1),[WIDTH/2 - PAD_HEIGHT,PAD_HEIGHT],TEXT_SIZE,"White")
    canvas.draw_text(str(score2),[WIDTH/2 + PAD_HEIGHT-TEXT_SIZE/2, PAD_HEIGHT],TEXT_SIZE,"White")

# Keydown function to update velocity of paddle
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel-=5
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel+=5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel-=5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel+=5
 
# Key up function to update velocity of Paddle 
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel+=5
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel-=5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel+=5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel-=5


# Create frame, handlers and buttons
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game)


# Start frame
new_game()
frame.start()
