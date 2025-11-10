import turtle as t
import colorsys as c
t.tracer(200)
t.width(5)
t.setup(1537,865)
t.bgcolor('black')
q=0
for i in range(2000):
    q+=0.01
    color=c.hsv_to_rgb(q,1,1)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(i,121)
    t.circle(120,30)
    t.fd(i)
    t.rt(60)
    t.bk(i)
    t.rt(90)
    t.fd(i)
    t.lt(120)
    t.end_fill()
t.done()
