from turtle import *

size = 30
tracer(2)


down()

for i in range(5):
    fd(35 * size)
    rt(90)
    fd(24 * size)
    rt(90)

up()

for i in range(1):
    rt(90)
    fd(7 * size)
    rt(90)
    fd(5 * size)

down()

for i in range(1001):
    rt(90)
    fd(20 * size)
    rt(90)
    fd(36 * size)

up()

for x in range(-500, 500):
    for y in range(-500, 500):
        setpos(x * size, y * size)
        dot(4, 'red')

done()
