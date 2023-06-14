import turtle
loadWindow = turtle.Screen()
turtle.speed(2)
turtle.bgcolor('black')
l = ['red','orange','green','yellow','blue'] 
for i in range(100):
    turtle.color(l[i%5])
    turtle.fillcolor(l[i%5])
    turtle.begin_fill()
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    turtle.end_fill()
turtle.exitonclick()
