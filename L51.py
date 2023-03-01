#Vinni Paradiso and Katherine O'Roark
import turtle

riley = turtle.Turtle()
riley.width(5)
riley.speed(0)

def draw_star(color):
    for side in range(6):
        riley.forward(100)
        riley.right(144)
        riley.color(color)

def mood(mood):
    if mood == "happy":
        draw_star("pink")
    elif mood == "sad":
        draw_star("blue")
    elif mood == "sleepy":
        draw_star("green")
    else:
        draw_star("red")
mood("happy")
mood("sad")
mood("sleepy")
mood("angry")
