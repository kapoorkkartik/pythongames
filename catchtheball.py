# http://www.codeskulptor.org/#user40_5DlLxPVEQF_5.py


import simplegui
import random

GROUND_HEIGHT=0
FRAME_WIDTH=STAGE_WIDTH=GROUND_WIDTH=821
STAGE_HEIGHT=498
FRAME_HEIGHT=STAGE_HEIGHT+GROUND_HEIGHT

image=simplegui.load_image("http://mrnussbaum.com/calendarclowns1/images/game_background.png")

list_of_balls=[]

colors=['Aqua','Blue','Fuchsia','Gray',
        'Green','Lime','Maroon','Navy','Olive',
        'Orange','Purple','Red','Silver','Teal',
        'White','Yellow']


class Ball:
    def __init__(self,color,radius,x_location):
        self.radius=radius
        self.color=color
        self.location=[x_location,0]
        

def timer():
    radius = 10
    color = random.choice(colors)
    x_location = random.randint(20, STAGE_WIDTH-20)
    new_ball = Ball(color,radius, x_location)
    list_of_balls.append(new_ball)
    
        
def draw(canvas):
    canvas.draw_image(image,[STAGE_WIDTH/2,STAGE_HEIGHT/2],[STAGE_WIDTH,STAGE_HEIGHT],[STAGE_WIDTH/2,STAGE_HEIGHT/2],[STAGE_WIDTH,STAGE_HEIGHT])
    for ball in list_of_balls:
        ball.location[1]+=10
        canvas.draw_circle(ball.location,ball.radius,10,ball.color,ball.color)

ball=Ball("Red",10,50)   
    
frame=simplegui.create_frame("ball",FRAME_WIDTH,FRAME_HEIGHT)
timer=simplegui.create_timer(500,timer)
frame.set_draw_handler(draw)
frame.start()
timer.start()
