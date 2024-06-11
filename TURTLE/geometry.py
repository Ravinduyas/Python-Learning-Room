import turtle

def draw_symmetric_circles(num_circles, radius):

    turtle.speed(50)
    turtle.pensize(0.2)
    
    for _ in range(12):
        turtle.circle(125)
        turtle.left(360 / num_circles)




    turtle.speed(50)
    turtle.pensize(0.2)
    
    for _ in range(num_circles):
        turtle.circle(radius)
        turtle.left(360 / num_circles)

    

    turtle.speed(50)
    turtle.pensize(0.5)
    
    for _ in range(12):
        turtle.circle(50)
        turtle.left(360 / num_circles)




    turtle.speed(50)
    turtle.pensize(0.5)
    
    for _ in range(12):
        turtle.circle(25)
        turtle.left(360 / num_circles)



    turtle.speed(50)
    turtle.pensize(0.5)
    
    for _ in range(12):
        turtle.circle(20)
        turtle.left(360 / num_circles)

    turtle.done()

# Set the number of circles and radius
num_circles = 12
radius = 100

# Draw the symmetric circles pattern
draw_symmetric_circles(num_circles, radius)
