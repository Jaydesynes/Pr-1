import turtle as t
import time
import random

playerAscore=0
playerBscore=0

window=t.Screen()
window.title("pong Game")
window.bgcolor("cyan")
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
leftpaddle=t.Turtle
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("green")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(350,0)

#creating right paddle
rightpaddle=t.Turtle
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating ball
ball=t.Turtle
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

#creating scorecard
pen = t.Turtle
pen.speed(0)
pen.color("Green")
pen.penup()
pen.hideturtle()
pen.goto(0.260)
pen.write("score",align="center",font=('Arial',24,'normal'))

#moving the left paddle



window.mainloop()