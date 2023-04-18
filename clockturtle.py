import turtle
import datetime

def skip(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()

def mkHand(name, length):
    turtle.reset()
    skip(-length*0.1)
    turtle.begin_poly()
    turtle.forward(length*1.1)
    turtle.end_poly()
    handForm = turtle.get_poly()
    turtle.register_shape(name, handForm)


def init():
    global secHand, minHand, horHand, printer

    turtle.mod('logo')
    mkHand('secHand',135)
    mkHand('minHand',125)
    mkHand('horHand',90)
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    horHand = turtle.Turtle()
    horHand.shape("horHand")


    for hand in secHand, minHand, horHand:
        hand.shape(1,1,3)
        hand.speed(0)

    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()

def setupClock(radius):
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            turtle.forward()
            skip(-radius-20)
            skip(radius+20)
            if i == 0:
                turtle.write(int(12),align='center',font=('Courier',14,'bold'))
            elif i == 30:
                skip(25)
                turtle.write(int(i/5),align='center',font=('Courier',14,'bold'))
                skip(-25)
            elif (i == 25 or i ==35):
                skip(20)
                turtle.write(int(i/5),align='center',font=('Courier',14,'bold'))
                skip(-20)
            else:
                turtle.write(int(i/5),align='center',font=('Courier',14,'bold'))
                skip(-radius-20)
        else:
            turtle.dot(5)
            skip(-radius)
        turtle.right(6)
def Week(t):
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return week[t.weekday()]

def Date(t):
    y = t.year()
    m = t.month()
    d = t.day()
    return '%s %d%d' %(y, m,d)

def Tick():
    t = datetime.today()
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    secHand.setheading(6*second)
    minHand.setheading(6*minute)
    horHand.setheading(30*hour)

    turtle.tracer(False)
    printer.forward(65)
    printer.write(Week(t),align='center',font = ('Courier',14,'bold'))
    printer.back(130)
    printer.write(Date(t),align='center',font = ('Courier',14,'bold'))
    printer.home()
    turtle.tracer(True)

    turtle.ontimer(Tick,100)

def main():
    turtle.tracer(False)
    init()
    setupClock(160)
    turtle.tracer(True)
    Tick()
    turtle.mainloop()

if __name__ == '__main__':
    main()
