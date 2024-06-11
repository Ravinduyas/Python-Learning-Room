import turtle

def draw_flower():
    turtle.color("orange")
    turtle.fillcolor("lightblue")

    turtle.begin_fill()
    for _ in range(36):
        turtle.forward(100)
        turtle.right(45)
        turtle.forward(100)
        turtle.right(135)
        turtle.forward(100)
        turtle.right(45)
        turtle.forward(100)
        turtle.right(135)
        
        turtle.right(10)  # Rotate slightly for the next petal

    turtle.end_fill()

def main():
    turtle.speed(200)
    turtle.pensize(2)
    turtle.bgcolor("black")

    draw_flower()

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
