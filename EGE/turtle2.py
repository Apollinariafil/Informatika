from turtle import*

lt(90)
size = 15
tracer(0)
screensize(2000,2000)
down()

# for i in range(3):
#     fd(size*5)
#     rt(90)
#     fd(size*12)
#     rt(90)

# up()

# fd(3*size)
# rt(90)
# fd(2*size)
# rt(90)
# down()

# for i in range(4):
#     fd(size*5)
#     rt(90)
#     fd(size*12)
# up()

# for x in range(-20, 20):
#     for y in range(-20, 20):
#         setpos(x * size, y * size)     # переместиться на позицую
#         dot(4, 'red') # размер и цвет точки
# done()

#№4
# for i in range(5):
#     fd(35*size)
#     rt(90)
#     fd(size*24)
#     rt(90)
    
# up()
# rt(90)   
# fd(7*size)
# rt(90)
# fd(size*5)
# down()

# for i in range(1001):
#     rt(90)   
#     fd(20*size)
#     rt(90)
#     fd(size*36)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         setpos(x * size, y * size)   
#         dot(4, 'red')
# done()
#№5
rt(135)
for i in range(7):
    fd(7*size)
    rt(45)
    fd(8*size)
    rt(135)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * size, y * size)   
        dot(4, 'red')
done()
       