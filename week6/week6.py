import turtle

#--setup--

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


#--functions--

def drawPoly(someturtle, somesides, somesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)



def drawSpiral(someturtle, angle):
    size = 1
    for i in range(100):
        someturtle.forward(size)
        someturtle.left(angle)
        size = size + 1


def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)







def drawstar(someturtle, size):
    for i in range(5):
        someturtle.forward(size)
        someturtle.right(144)



# --Exersices--


#exercise 1

# tess . color("hotpink")
# drawPoly(tess,8, 50)

# #exercise 2
# tess.color("blue")
# for i in range (20):
#     drawPoly(tess,4, 100)
#     tess.left(18)

#exercise 3

# tess.pencolor("blue")
# tess.penup()
# tess.goto(-200,200)
# tess.pendown()
# drawSpiral(tess,90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess,89)

#exercise 4
# drawEquitriangle(tess,100)
# drawPoly(tess,3, 100)

#exercise 5

# for i in range(5):
#     drawstar(tess,100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()



# def drawSprite(someturtle, somelegs, length):
#     angle =360 / somelegs
#     for i in range(somelegs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
#
# drawSprite(tess,15,120)
#
#
#
#
#
#
#
#
#
# #--finish--
# turtle.exitonclick()