import turtle

def draw_square (some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art ():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    #Create a turtle named George - Draws a square
    george = turtle.Turtle()
    george.shape("turtle")
    george.color("white")
    george.speed(2)
    for i in range(1,37):
        draw_square(george)
        george.right(10)
        
    #Create a turtle named Anne - Draws a circle
    #anne = turtle.Turtle()
    #anne.shape("arrow")
    #anne.color("yellow")
    #anne.circle(100)
        
    #Create a turtle named Tracy - Draws a triangle
    #tracy = turtle.Turtle()
    #tracy.shape("arrow")
    #tracy.color("black")
    #tracy.forward(100)
    #tracy.right(120)
    #tracy.forward(100)
    #tracy.right(120)
    #tracy.forward(100)

    window.exitonclick()

draw_art()

#turtle is a class - like a blueprint
#george, anne, tracy are instances or objects of that class - like buildings
