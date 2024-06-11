import turtle

def draw_mandala(num_circles, radius):
    turtle.speed(9000000)
    turtle.pensize(2)
#100
    for _ in range(num_circles):
        turtle.circle(radius)
        turtle.left(360 / num_circles)
        
        for _ in range(num_circles // 2):
            turtle.forward(radius)
            turtle.circle(radius / 4)
            turtle.backward(radius)
            turtle.left(360 / num_circles)

    for _ in range(num_circles):
        turtle.circle(radius)
        turtle.left(360 / num_circles)
        radius = radius-10
        for _ in range(num_circles // 2):
            turtle.forward(radius)
            turtle.circle(radius / 4)
            turtle.backward(radius)
            turtle.left(360 / num_circles)
#150

    for _ in range(num_circles):
        turtle.circle(12)
        turtle.left(360 / num_circles)
        
        for _ in range(num_circles // 2):
            turtle.forward(150)
            turtle.circle(150 / 4)
            turtle.backward(150)
            turtle.left(360 / num_circles)

    
#160

    for _ in range(num_circles):
        turtle.circle(12)
        turtle.left(360 / num_circles)
        
        for _ in range(num_circles // 2):
            turtle.forward(160)
            turtle.circle(160 / 4)
            turtle.backward(160)
            turtle.left(360 / num_circles)

#170
    for _ in range(num_circles):
        turtle.circle(12)
        turtle.left(360 / num_circles)
        
        for _ in range(num_circles // 2):
            turtle.forward(170)
            turtle.circle(170 / 4)
            turtle.backward(170)
            turtle.left(360 / num_circles)


#180
    for _ in range(num_circles):
        turtle.circle(12)
        turtle.left(360 / num_circles)
        
        for _ in range(num_circles // 2):
            turtle.forward(180)
            turtle.circle(180 / 4)
            turtle.backward(180)
            turtle.left(360 / num_circles)
#200
    for _ in range(num_circles):
        turtle.circle(12)
        turtle.left(360 / num_circles)
        
        for _ in range(num_circles // 2):
            turtle.forward(200)
            turtle.circle(200 / 4)
            turtle.backward(200)
            turtle.left(360 / num_circles)


#190
    for _ in range(num_circles):
        turtle.circle(12)
        turtle.left(360 / num_circles)
        
        for _ in range(num_circles // 2):
            turtle.forward(190)
            turtle.circle(190 / 4)
            turtle.backward(190)
            turtle.left(360 / num_circles)
            
    for _ in range(num_circles):
        turtle.circle(12)
        turtle.left(360 / num_circles)
        
        for _ in range(num_circles // 2):
            turtle.forward(210)
            turtle.circle(210 / 4)
            turtle.backward(210)
            turtle.left(360 / num_circles)

    for _ in range(num_circles):
        turtle.circle(12)
        turtle.left(360 / num_circles)
        
        for _ in range(num_circles // 2):
            turtle.forward(220)
            turtle.circle(220 / 4)
            turtle.backward(220)
            turtle.left(360 / num_circles)


            
    turtle.done()

# Set the number of circles and radius
num_circles = 12
radius = 100

# Draw the mandala
draw_mandala(num_circles, radius)
