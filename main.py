import turtle
import winsound


window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width= 800, height=600)
window.tracer(0)


#Pad A
pad_A = turtle.Turtle()
pad_A.speed(0)

pad_A.shape("square")
pad_A.color("blue")
pad_A.shapesize(stretch_wid=6, stretch_len=1)

pad_A.penup()
pad_A.goto(-350,0)


#Pad B
pad_B = turtle.Turtle()
pad_B.speed(0)

pad_B.shape("square")
pad_B.color("red")
pad_B.shapesize(stretch_wid=6, stretch_len=1)

pad_B.penup()
pad_B.goto(350,0)



#Ball
ball = turtle.Turtle()
ball.speed(0)

ball.shape("circle")
ball.color("white")

ball.penup()
ball.goto(0,0)

ball.dx = 0.2
ball.dy = 0.1



#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,280)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 14, "bold"))


#Score

score_a = 0
score_b = 0


#Function
def pad_a_up():
    y = pad_A.ycor()
    y += 30
    pad_A.sety(y)

def pad_a_down():
    y = pad_A.ycor()
    y -= 30
    pad_A.sety(y)

def pad_b_up():
    y = pad_B.ycor()
    y += 30
    pad_B.sety(y)

def pad_b_down():
    y = pad_B.ycor()
    y -= 30
    pad_B.sety(y)

#Keyboard binding

window.listen()
window.onkeypress(pad_a_up, "z")
window.onkeypress(pad_a_down, "s")
window.onkeypress(pad_b_up, "Up")
window.onkeypress(pad_b_down, "Down")


#Main game loop
while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        score_a +=1
        ball.dx *= -1
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        ball.dx = 0.2
        ball.dy = 0.1
        pad_A.goto(-350, 0)
        pad_B.goto(350, 0)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 14, "bold"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        score_b += 1
        ball.dx *= -1
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        ball.dx = 0.2
        ball.dy = 0.1
        pad_A.goto(-350, 0)
        pad_B.goto(350, 0)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 14, "bold"))

    #Pad and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and ( ball.ycor() < pad_B.ycor() + 60  and ball.ycor() > pad_B.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
        ball.dx *= 1.2
        ball.dy *= 1.2
        winsound.PlaySound("bounce3.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and ( ball.ycor() < pad_A.ycor() + 60  and ball.ycor() > pad_A.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
        ball.dx *= 1.2
        ball.dy *= 1.2
        winsound.PlaySound("bounce3.wav", winsound.SND_ASYNC)


    #pad limit
    if pad_A.ycor() > 260:
        pad_A.sety(250)
    if pad_A.ycor() < -260:
        pad_A.sety(-250)
    if pad_B.ycor() > 260:
        pad_B.sety(250)
    if pad_B.ycor() < -260:
        pad_B.sety(-250)


    if score_a == 5 or score_b == 5:
        winsound.PlaySound("vict.wav", winsound.SND_ASYNC)
        score_a = 0
        score_b = 0
        pad_B.goto(350, 0)
        pad_A.goto(-350, 0)
        ball.dx = 0.2
        ball.dy = 0.1
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 14, "bold"))