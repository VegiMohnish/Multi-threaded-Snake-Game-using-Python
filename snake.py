#### Snake game in python       --- mohnish vegi
import turtle
import time
import random
import threading

# import tkinter
delay = 0.1
final = 0
# Score
flag = 0
score = 0
high_score = 0
a = 1000
b = 1000
n = 1000
m = 1000
z = 0
i = 0
t = 0

eat = 0
# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("light blue")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"
st = 1
# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
# food.shapesize(2, 2, 1)
food.color("red")
food.penup()
food.goto(0, 100)
a1 = food.xcor()
b1 = food.ycor()

ff = 0
food1 = turtle.Turtle()
food1.speed(0)
food1.shape("circle")
food1.shapesize(2, 2, 1)
food1.color("brown")
food1.penup()
food1.goto(1000, 1000)
segments = []
""""
last = turtle.Turtle()
last.speed(0)
last.direction = "stop"
last.hideturtle()
last.goto(a1, b1)
last.penup()
last.shape("circle")
last.color("light blue")

"""
# Pen
load = turtle.Turtle()
load.speed(0)
load.shape("circle")
load.shapesize(0.2, 0.2, 1)
load.color("black")
load.penup()
load.goto(0, -25)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
#wn.update()
pen.write("welcome to my world!! \n                -python", align="center", font=("Courier", 24, "normal"))

time.sleep(1.5)
pen.clear()
load.goto(1000,1000)
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    # print("he;llo")
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def coll_border():
    global score, delay, head, z, final
    if head.xcor() > 280 or head.xcor() < -290 or head.ycor() > 260 or head.ycor() < -290:
        z = 1
        final = score
        score = 0

        # Reset the delay
        delay = 0.1


def coll_food():
    global delay, score, high_score, food, head, a, b, flag, i, m, n, t, eat, a1, b1
    # pen.write(": {} ".format(head.distance(food)), align="center", font=("Courier", 24, "normal"))
    # print("hii")
    for j in segments:
        if j.distance(a1, b1) < 5:
            j.shapesize(1.5, 1.5, 1)
            #j.color("black")
        else:
            j.shapesize(1, 1, 1)
            #j.color("green")
    if head.distance(food) < 50 or head.distance(food1) < 30:
        head.shapesize(1.5, 1.5, 1)
    else:
        head.shapesize(1, 1, 1)

        # wn.update()

    if head.distance(food) < 15:
        # Move the food to a random spot

        head.shapesize(1, 1, 1)
        a1 = food.xcor()
        b1 = food.ycor()
        a = random.randint(-280, 280)
        b = random.randint(-280, 220)
        # print("bye")

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
    if flag != 1:
        ran = random.randint(1, 10)

        if i % ran == 0 and i % 70 == 0 and i != 0 and head.xcor() != 0:
            while True:
                m = random.randint(-280, 280)
                n = random.randint(-280, 220)
                if m != food.xcor() and n != food.ycor():
                    t = 1
                    flag = 1
                    break

    if flag == 1:
        if head.distance(food1) < 25:
            # Move the food to a random spot
            flag = 0
            t = 0
            eat = 1
            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 20

            if score > high_score:
                high_score = score


def coll_body():
    global z, score, delay, segments, final
    for segment in segments:
        if segment.distance(head) < 20:
            z = 1

            # Reset the score
            final = score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display


def do1():
    global z
    head.goto(0, 0)
    head.direction = "stop"
    # time.sleep(1)

    for i in segments:
        i.goto(1000, 1000)

    segments.clear()

    pen.clear()
    head.color("light blue")
    food.color("light blue")
    food1.color("light blue")

    pen.goto(0, 0)

    wn.update()

    pen.write("Game Over!! \n Score:{}".format(final), align="center",
              font=("Courier", 24, "normal"))
    time.sleep(1.5)
    food.goto(0, 100)

    head.color("black")
    food.color("red")
    food1.color("brown")

    pen.goto(0, 260)
    # score = 0
    pen.clear()

    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
              font=("Courier", 24, "normal"))

    z = 0


def do2():
    global a, b, a1, b1

    #last.goto(a1, b1)
    food.goto(a, b + 1)

    # Add a segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("circle")
    new_segment.color("green")
    new_segment.penup()
    segments.append(new_segment)
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
              font=("Courier", 24, "normal"))
    a = 1000
    b = 1000


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
if __name__ == "__main__":
    while True:
        wn.update()

        t1 = threading.Thread(target=coll_border)
        t2 = threading.Thread(target=coll_food)
        t3 = threading.Thread(target=coll_body)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
        if z == 1:
            do1()

        if a < 600:
            do2()

        if flag == 1:
            if m < 600:
                food1.goto(m, n)
                m = 1000
                n = 1000
            else:
                t = t + 1

            if t > 40:
                food1.goto(1000, 1000)
                flag = 0
                t = 0
                pen.clear()
                pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))
        if eat == 1:
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))
            eat = 0
            food1.goto(1000, 1000)

        if t != 0:
            pen.clear()
            if t:
                if ff == 0:
                    if st == 1:
                        food1.shapesize(1.75, 1.75, 1)
                        st = 2
                    elif st == 2:
                        food1.shapesize(1.5, 1.5, 1)
                        st = 3
                    else:
                        food1.shapesize(1, 1, 1)
                        ff = 1 
                else:
                    if st == 3:
                        food1.shapesize(1.5, 1.5, 1)
                        st = 2
                    elif st == 2:
                        food1.shapesize(1.75, 1.75, 1)
                        st = 1
                    else:
                        food1.shapesize(2, 2, 2)
                        ff = 0 


          

            pen.write("Score:{} HighScore:{} time:{}".format(score, high_score, 40 - t), align="center",
                      font=("Courier", 24, "normal"))

        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()

            segments[index].goto(x, y)
            #wn.update()

            # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
            if segments[0].distance(a1, b1) < 5:
                segments[0].shapesize(1.5, 1.5, 1)
            else:
                segments[0].shapesize(1, 1, 1)

        move()
        i = i + 1
        time.sleep(delay)

wn.mainloop()
