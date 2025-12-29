import turtle
import time
import random

# === Config ===
delay = 0.11
score = 0
high_score = 0

# === Setup Screen ===
wn = turtle.Screen()
wn.title("Snake Game by Shreya 🐍")
wn.bgcolor("pink")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off auto screen updates

# === Snake Head ===
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# === Food ===
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

# === Segments List ===
segments = []

# === Scoreboard ===
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# === Update Score Function ===
def update_score():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# === Direction Functions ===
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

# === Move Function ===
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

# === Keyboard Bindings ===
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# === Main Game Loop ===
while True:
    wn.update()

    # === Border Collision ===
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide and reset segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset score
        score = 0
        update_score()

    # === Food Collision ===
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Update score
        score += 10
        if score > high_score:
            high_score = score
        update_score()

        # Fun message
        print(random.choice([
            "Nom nom 🍎", 
            "Snack acquired 😋", 
            "That hit the spot 🐍", 
            "10 points for Shreya 🏆", 
            "Mmmm... crunchy pixels!"
        ]))

    # === Move Segments in Reverse Order ===
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move first segment to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # === Self Collision ===
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide and reset segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset score
            score = 0
            update_score()
            break

    time.sleep(delay)

# Run the game loop
wn.mainloop()
