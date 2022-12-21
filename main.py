import turtle
import time
import random

delay = 0.1
penalty_delay = 1.0

# Score
score = 0
high_score = 0


# set un the screen

wn = turtle.Screen()
wn.title("Snake Game by @Abdou")
wn.bgcolor("orange")
wn.setup(width=600, height=600)
# turns off the screen updats
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food +10
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

# Snake poison -10
poison = turtle.Turtle()
poison.speed(0)
poison.shape("circle")
poison.color("red")
poison.penup()
poison.goto(100, 0)

segments = []

# Pen ( Scoring )
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("courier", 22, "bold"))

# Penalty ( + or - 10 )
penalty = turtle.Turtle()
penalty.speed(0)
penalty.shape("square")
penalty.penup()
penalty.hideturtle()
penalty.goto(-260, 260)

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

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "z")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "q")
wn.onkeypress(go_right, "d")


# Main game loop
while True:
    wn.update()
    # Check for collision with the head
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segment list
        for seg in segments:
            seg.goto(1000, 1000)

        # Clear the segment
        segments.clear()

        # Reset the score
        score = 0
        pen.clear()
        pen.color("red")
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier", 22, "bold"))

        # Reset the delay
        delay = 0.1

    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food on random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Move the poison on random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        poison.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay (speed ++)
        delay -= 0.001

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.color("green")
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier", 22, "bold"))
        penalty.clear()
        penalty.color("green")
        penalty.write("+10", align="center", font=("courier", 20, "bold"))


    elif head.distance(poison) < 20:
        # Move the poison on random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        poison.goto(x, y)

        # Move the food on random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Delete one segment from the snake
        # Check if there are a snake body on the segments or not
        if len(segments) > 0:
            segments[-1].goto(1000, 1000)
            segments.pop()
            # Decrease the score
            score -= 10
            # Shorten the delay (speed ++) zkara !
            delay -= 0.001

            # Affichage
            pen.color("red")
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier", 22, "bold"))
            penalty.clear()
            penalty.color("red")
            penalty.write("-10", align="center", font=("courier", 20, "bold"))
        else:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Reset the score
            score = 0
            # Reset the delay
            delay = 0.1

            # Affichage
            pen.color("red")
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier", 22, "bold"))
            penalty.clear()
            penalty.color("red")
            penalty.write("-10", align="center", font=("courier", 20, "bold"))

    # Move the end segments first in reverse order
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Rest the score
            score = 0
            pen.color("red")
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier", 22, "bold"))

            # Hide the segment list
            for seg in segments:
                seg.goto(1000, 1000)

            # Clear the segment
            segments.clear()

            # Reset the delay
            delay = 0.1

    time.sleep(delay)

wn.mainloop()