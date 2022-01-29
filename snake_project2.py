import turtle 
import time
import random

# Define Global Variables
delay = 0.2
score = 0
high_score = 0
segments = []
direction = ""

#Setting up the screen, title, background color, width etc.
# must return the window created
def setUpScreen():
    # Set up the screen
    wn = turtle.Screen()
    wn.title('Snake Game')

    # Set background color
    wn.bgcolor('yellow') 
    # Set height and width
    wn.setup(width=1000, height=800)
    # Turns off the screen updates
    return wn
    

# Write score and highscore on the screen
def trackScoreOnScreen():
    pen = turtle.Turtle()
    pen.hideturtle()
    # Set color
    pen.color('lightblue')
    # penup and hide turtle
    pen.penup()
    pen.shape('turtle')
    # Move the score to top of screen
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
    return pen

# Create and return the Head of the snake

def createSnakeHead():
    # Snake head
    head = turtle.Turtle()
    head.shape('square')
    head.color('blue')
    head.speed(0)
    head.penup()
    head.goto(180,0)
    
    # Set speed, shape, color and move it center of the screen
    
   
    
    # Set direction as stop
    return head

# Create and return the first food on the screen
def createFood():
    # Create Snake food
    food = turtle.Turtle()
    food.shape('circle')
    food.color('green')
    food.speed(0)
    food.penup()
    food.goto(100,0)
    
    
    
    
    
     # Set speed, shape, color and move it some location of the screen
    
    return food

# Function to call when up key is pressed
# Snake can go up only when the direction is right or left and not down
def go_up():
    if head.direction != "down":
        head.direction = "up"
    
    # remove print statement after implementing this function
    print("go_up function called")
    
    
# Function to call when down key is pressed
# Snake can go down only when the direction is right or left and not up
def go_down():
     if head.direction != "up":
        head.direction = "down"
   # remove print statement after implementing this function
     print("go_down function called")
   # print


# Function to call when left key is pressed
# Snake can go left only when the direction is up or down and not right
def go_left():
    if head.direction != "right":
        head.direction = "left"
     # remove print statement after implementing this function
    print("go_left function called")

# Function to call when right key is pressed
# Snake can go right only when the direction is up or down and not left
def go_right():
    if head.direction != "left":
        head.direction = "right"
    # remove print statement after implementing this function
    print("go_right function called")
        

# Bind Up, Down, Left and Right keys with their function
def bindKeyboardKeys(win):
    if head.direction == 'up':
           y=head.ycor()    
           head.sety(y+20)
           
    if head.direction == 'down':
           y=head.ycor()    
           head.sety(y+20)
           
    if head.direction == 'left':
           x=head.xcor()
           head.sety(y+20)
     
    if head.direction == 'right':
           x=head.xcor()
           head.sety(y+20)
    # remove print statement after implementing this function
    print("bindKeyboardKeys function called")

# Function to call to move the snake, based on the direction of the snake
# snake body should move automatically in that direction
# should be called from the main loop. 
# Function to call when left key is pressed
# Snake can go left only when the direction is up or down and not right
def go_left():
    if head.direction != "right":
        head.direction = "left"
     # remove print statement after implementing this function
    print("go_left function called")

# Function to call when right key is pressed
# Snake can go right only when the direction is up or down and not left
def go_right():
    if head.direction != "left":
        head.direction = "right"
    # remove print statement after implementing this function
    print("go_right function called")



def moveHead():
    if head.direction=='up':
        y = head.ycor()
        head.sety(y+20)
    
    # remove print statement after implementing this function
    print("moveHead function called")
   
# Move segments

def moveSegments():
    global segments
    
     # Move the end segments first in reverse order
     # Using for loop move the segments
     # For example if there are 3 segments 2, 1, and 0
     # Move second segment to location of first and move first segment to location of zero


     # Move segment 0 to where the head is



# Detect collision of snake head with the screen borders
# If collision detected return True else return False
def detectCollisionWithBorder(head):
    # remove print statement after implementing this function
    print("detectCollisionWithBorder function called")
    
    return False

# Handle the collision if detected true
def handleCollisionWithBorder(head, trackScore):
    global delay
    global score
    
    # Make head goto center of the screen
    # Make head direction dummy so that it do not move
    # Hide the segments
    # Clear the segments list
    # Reset the score
    # Reset the delay
    # Clear trackscore and start from 0

# Detect collision of snake head with food
# If collision detected return True else return False
def detectCollisionWithFood(head, food):
    # remove print statement after implementing this function
    print("detectCollisionWithFood function called")
    
    return False


# Handle the collision if detected true
def handleCollisionWithFood(head, trackScore, food):
    global delay
    global score
    global high_score
    
    # Move the food to a random spot

    # Add a segment, define its shape and color
    # append it to the segments list

    # Shorten the delay, to move snake faster

    # Increase the score by 10

    # check for high score and update it if player made a new high score
    
    # Update trackScore 


# Detect collision of snake head with its body
# needs to check for all segment, thus will use for loop
# If collision detected return True else return False
def detectCollisionOfHeadWithSegment(head):
    # remove print statement after implementing this function
    print("moveHead function called")
    
    return False


####################################
#                                  #
#   Start of the main function     #
#                                  #
####################################

#Call Functions in main program
wn = setUpScreen()
head = createSnakeHead()
food = createFood()
trackScore = trackScoreOnScreen()
bindKeyboardKeys(wn)

# Start of main game loop
while True:
    wn.update()
    
    # Check for a collision of head with the screen border
    if detectCollisionWithBorder(head):
        time.sleep(1)
        handleCollisionWithBorder(head, trackScore)

    # Check for a collision with the food
    if detectCollisionWithFood(head, food):
        handleCollisionWithFood(head, trackScore, food)
        
    moveSegments()
    moveHead()    

    # Detect collision of snake body with its head
    if detectCollisionOfHeadWithSegment(head):
        time.sleep(1)
        handleCollisionWithBorder(head, trackScore)
        
    # Sleep for time equal to delay to add delay
    time.sleep(delay)


wn.mainloop()