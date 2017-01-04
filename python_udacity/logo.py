import turtle
import math


count=0

def forward(houzz, distance):
    global count
    count +=1
    speed=(10*math.sin(count * (math.pi/9)))
    print speed
    houzz.forward(distance)
    houzz.speed(speed)
    
def draw_logo():
    window = turtle.Screen()
    window.bgcolor("black")
    window.colormode(255)
   
    houzz = turtle.Turtle()
    houzz.pen(fillcolor=(137,192,53), pencolor=(137,192,53), pensize=1)
    houzz.shape("turtle")
    houzz.shapesize(1,1)
    houzz.speed(0)
    
    houzz.right(150)
    forward(houzz, 96)
    houzz.right(120)
    houzz.forward(192)
    houzz.right(60)
    forward(houzz, 96)
    houzz.right(120)
    forward(houzz, 288)
    houzz.right(240)
    forward(houzz, 96)
    houzz.left(60)
    forward(houzz, 192)
    houzz.right(240)
    forward(houzz, 192)
    houzz.right(240)
    forward(houzz, 96)
    houzz.right(300)
    forward(houzz, 96)
    houzz.right(240)
    forward(houzz, 96)




#for count in range(10):
    
    
    window.exitonclick()

draw_logo()
