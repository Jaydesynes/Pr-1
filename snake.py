import turtle
import time
import random

#screen
screen =turtle.Screen()
screen.title("cobra")
screen.setup(width=1000,height=1000)
screen.bgcolor("cyan")
screen.tracer(0)

#creating head
head =turtle.Turtle()
head.penup()
head.shape("square")
head.color("black")
head.goto(0,0)
head.direction = "stop"
head.speed(0)

#food
food = turtle.Turtle()
food.penup()
food.direction ="stop"
food.shape("triangle")
food.color("green")
x = random.randint(-400,400)
y = random.randint(-400,400)
food.goto(x,y)

#creating body
snake =[]

#function
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y-10)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x+10)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x-10)

#keybinding
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")


#main game loop
while True:
    screen.update()
    if head.distance(food) < 20:
        x = random.randint(-400,400)
        y = random.randint(-400,400)  
        food.goto(x,y) 
        body =turtle.Turtle()
        body.penup()
        body.shape("circle")
        body.color("red")
        body.speed(0)
        snake.append (body)

        #moving the end segments first in reverse order
    for index in range(len(snake)-1,0,-1):
        x = snake[index-1].xcor()
        y = snake[index-1].ycor()
        snake[index].goto(x,y)

        #moving segment 0 to where the head is
    if len(snake) >0:
        x = head.xcor()
        y = head.ycor()
        snake[0].goto(x,y)


    move()
    time.sleep(0.1)


screen.mainloop()