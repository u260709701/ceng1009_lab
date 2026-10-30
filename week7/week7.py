import turtle
import math
# def sumTo(n):
#     result = n*(n+1)/2
#     return result
#
# print(sumTo(10))
#
#
# def draw (t, n, size):
#     angle = 180 / n
#     for i in range(n):
#     t.forward(size)
#     t.left(angle)





wn = turtle.Screen()
tess = turtle.Turtle()
tess . color("red")
# drawstar(tess, 9, 200)


# def sumTo(n):
#     countr = 0
#     for i in range(n + 1):
#         countr += 1
#
#     return counteref sumTo(n):
#     countr = 0
#     for i in range(n + 1):
#         countr += 1
#
#     return count
# print(sumTo(10))
#
#
# def mysqrt(n):
#     guess = n //2
#     new= (1/2)*(guess + (n/guess))








def sprite ( t , leg , length ):
    angle = 360 / leg
    for i in range(leg):
        t.forward(length)
        t.backward(length)
        t.left(angle)

def square ( t , size):
        for i in range (4):
                sprite (tess ,15 , 20)
                t.forward(size)
                t.left(90)

square (tess, 150 )















def drawBar( t , h , gap):
    t.left(90)
    t.forward(h +gap)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(h+gap)
    t.left(90)

    x=[33,45,66,77,89,100,150,200]
    maxh = max(x)
    num = len(x)
    n = 10
    wn.setworldcoordinates(0-b,0-b ,40*num + b , maxh + b )
    





def checksign (n):
    if n > 0:
        return "positive"
    elif n < 0 :
        return "negative"
    else:"zero"

    num = [-7 , 5 , 0]
    for n in num:
        print(checksign(n))

