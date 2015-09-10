# Implementation of classic arcade game Pong
#author -Bhuvan

import simplegui
import random


WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0.0,0.0]
timek=0
Hit=False
Left=False
Right=False


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos=[WIDTH/2,HEIGHT/2]
    if direction==RIGHT:
      ball_vel[0]=random.randrange(120, 240)/60
      ball_vel[1]=-random.randrange(60,180)/60
      
    elif direction==LEFT:
      ball_vel[0]=-random.randrange(120,240)/60
      ball_vel[1]=-random.randrange(60,180)/60
    
      

# define event handlers
def new_game():
    global Hit,paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.randrange(0,2))
    paddle1_pos=[0,HEIGHT/2-HALF_PAD_HEIGHT]
    paddle2_pos=[WIDTH-1,HEIGHT/2-HALF_PAD_HEIGHT]
    paddle1_vel=0
    paddle2_vel=0
    score1=0
    score2=0
    ball_pos=[WIDTH/2,HEIGHT/2]
    Hit=False
    
    
               
               
               
               
               
               
               
               
               
               
            

def draw(canvas):
    global Left,Right,Hit,score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel,RIGHT,LEFT
    
    
      
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
   
    
    
    # update ball
    if ball_pos[1]<=BALL_RADIUS:
      
       ball_vel[1]=-ball_vel[1]
    
    
    if ball_pos[1]>=HEIGHT-BALL_RADIUS:
      
       ball_vel[1]=-ball_vel[1]
    
    elif ball_pos[0]<=BALL_RADIUS+PAD_WIDTH+10 and ( ball_pos[1]>=paddle1_pos[1] and ball_pos[1]<=paddle1_pos[1]+PAD_HEIGHT):
         
        
         if Left==False:
           ball_vel[0]=-ball_vel[0]
           
           Left=True
           Hit=True
           Right=False
         
    
       
         print "paddle1",ball_vel
    
          
    elif ball_pos[0]>=WIDTH-1-PAD_WIDTH-10-BALL_RADIUS and (ball_pos[1]>=paddle2_pos[1] and ball_pos[1]<=paddle2_pos[1]+PAD_HEIGHT):
        if Right==False:
           ball_vel[0]=-ball_vel[0]
           Hit=True
           Right=True
           Left=False
               
        print "paddle2",ball_vel
         
    elif ball_pos[0]<=BALL_RADIUS+PAD_WIDTH:
        paddle1_pos=[0,HEIGHT/2-HALF_PAD_HEIGHT]
        paddle2_pos=[WIDTH-1,HEIGHT/2-HALF_PAD_HEIGHT]
        score2+=1
        timek=0
        spawn_ball(RIGHT)
        Hit=False
        Left=False
        Right=False
    elif ball_pos[0]>=WIDTH-1-PAD_WIDTH-BALL_RADIUS:
        paddle1_pos=[0,HEIGHT/2-HALF_PAD_HEIGHT]
        paddle2_pos=[WIDTH-1,HEIGHT/2-HALF_PAD_HEIGHT]
        score1+=1
        timek=0
        spawn_ball(LEFT)
        Hit=False
        Left=False
        Right=False
        
        
    
    if Hit:
       ball_vel[0]+=float(6*ball_vel[0]/100)
       ball_vel[1]+=float(1.5*ball_vel[1]/100)
       Hit=False
     
        
        
           
    
    ball_pos[0]+=float(ball_vel[0])
    ball_pos[1]+=float(ball_vel[1])
    
    if paddle1_pos[1]<=0:
       paddle1_pos[1]=0
    
    if paddle1_pos[1]+PAD_HEIGHT>=HEIGHT:
       paddle1_pos[1]=HEIGHT-PAD_HEIGHT
    
    if paddle2_pos[1]<=0:
       paddle2_pos[1]=0
        
    if paddle2_pos[1]+PAD_HEIGHT>=HEIGHT:
       paddle2_pos[1]=HEIGHT-PAD_HEIGHT
    
    
    
    
        
        
    
            
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,3,'Black','Green')
    
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1]+=paddle1_vel
    paddle2_pos[1]+=paddle2_vel
  
        
    # draw paddles
    canvas.draw_line(paddle1_pos,[0,paddle1_pos[1]+PAD_HEIGHT], PAD_WIDTH+10, 'White')
    canvas.draw_line(paddle2_pos,[WIDTH-1,paddle2_pos[1]+PAD_HEIGHT],PAD_WIDTH+10,'White')
    
   #scores
    canvas.draw_text(str(score1), (WIDTH/2-100,HEIGHT/2-100), 55, 'Blue')
    canvas.draw_text(str(score2),(WIDTH/2+100,HEIGHT/2-100),55,'Blue')   
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
       paddle1_vel-=5
    
    if key==simplegui.KEY_MAP["s"]:
       paddle1_vel+=5
        
    if key==simplegui.KEY_MAP["up"]:
       paddle2_vel-=5
    
    if key==simplegui.KEY_MAP["down"]:
       paddle2_vel+=5
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
       paddle1_vel+=5
    
    if key==simplegui.KEY_MAP["s"]:
       paddle1_vel-=5
        
    if key==simplegui.KEY_MAP["up"]:
       paddle2_vel+=5
    
    if key==simplegui.KEY_MAP["down"]:
       paddle2_vel-=5


    
    
     


       
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1=frame.add_button("Restart",new_game)



# start frame
new_game()

frame.start()

