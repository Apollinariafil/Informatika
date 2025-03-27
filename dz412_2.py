# from turtle import *

# size = 30
# tracer(2)


# down()

# for i in range(5):
#     fd(35 * size)
#     rt(90)
#     fd(24 * size)
#     rt(90)

# up()

# for i in range(1):
#     rt(90)
#     fd(7 * size)
#     rt(90)
#     fd(5 * size)

# down()

# for i in range(1001):
#     rt(90)
#     fd(20 * size)
#     rt(90)
#     fd(36 * size)

# up()

# for x in range(-500, 500):
#     for y in range(-500, 500):
#         setpos(x * size, y * size)
#         dot(4, 'red')

# done()
from turtle import*
lt(90)
size = 15
tracer(2)
screensize(2000,2000)
down()

for i in range(36):
    fd(size*1)
    rt(36)

up()

fd(4*size)
rt(90)

down()

for i in range(8):
    fd(size*6)
    rt(90)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * size, y * size)     # переместиться на позицую
        dot(4, 'red') # размер и цвет точки
done()