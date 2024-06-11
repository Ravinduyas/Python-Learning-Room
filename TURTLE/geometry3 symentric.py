import turtle

def draw_special_mandala(num_circles, radius):
    turtle.speed(100)
    turtle.pensize(2)

    for _ in range(num_circles):
        turtle.circle(radius)
        turtle.left(360 / num_circles)

        for _ in range(num_circles // 2):
            turtle.forward(radius)
            turtle.circle(radius / 4)
            turtle.backward(radius)
            turtle.left(360 / num_circles)

            for _ in range(num_circles // 4):
                turtle.forward(radius / 2)
                turtle.circle(radius / 1)
                turtle.backward(radius / 2)
                turtle.left(360 / (num_circles // 2))

    turtle.done()

# Set the number of circles and radius
num_circles = 12
radius = 100

# Draw the symmetric special mandala
draw_special_mandala(num_circles, radius)
