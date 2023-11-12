import turtle
from turtle import *
import random

kopf = Turtle()
kopf.shape("square")
kopf.color("black")
kopf.penup()
kopf.speed(0)
kopf.goto(0,0)
kopf.direction = "stop"

essen = Turtle()
essen.shape("circle")
essen.color("red")
essen.penup()
essen.speed(0)
essen.goto(0,100)

rechts = Turtle()
rechts.shape("triangle")
rechts.color("green")
rechts.speed(0)
rechts.penup()
rechts.goto(180,-160)

unten = Turtle()
unten.shape("triangle")
unten.color("green")
unten.right(90)
unten.speed(0)
unten.penup()
unten.goto(160,-180)

links = Turtle()
links.shape("triangle")
links.color("green")
links.left(180)
links.speed(0)
links.penup()
links.goto(140,-160)

oben = Turtle()
oben.shape("triangle")
oben.color("green")
oben.left(90)
oben.speed(0)
oben.penup()
oben.goto(160,-140)

def kopf_bewegen():
    global kopf
    if kopf.direction == "down":
        y = kopf.ycor()
        kopf.sety(y - 20)

    elif kopf.direction == "right":
        x = kopf.xcor()
        kopf.setx(x + 20)

    elif kopf.direction == "up":
        y = kopf.ycor()
        kopf.sety(y + 20)

    elif kopf.direction == "left":
        x = kopf.xcor()
        kopf.setx(x - 20)

def nach_unten_ausrichten():
    if kopf.direction != "up":
        kopf.direction ="down"

def nach_rechts_ausrichten():
    if kopf.direction != "left":
        kopf.direction = "right"

def nach_links_ausrichten():
    if kopf.direction != "right":
        kopf.direction = "left"

def nach_oben_ausrichten():
    if kopf.direction != "down":
        kopf.direction = "up"

def interpretiere_eingabe(x,y):
    if(x >= 150 and x <= 170 and y >= -190 and y<=-170):
        nach_unten_ausrichten()
    elif(x >= 170 and x <= 190 and y >= -170 and y<=-150):
        nach_rechts_ausrichten()
    elif(x >= 130 and x <= 150 and y >= -170 and y<=-150):
        nach_links_ausrichten()
    elif(x >= 150 and x <= 170 and y >= -150 and y<=-130):
        nach_oben_ausrichten()

    kopf_bewegen()

onclick(interpretiere_eingabe)


turtle.mainloop()

from turtle import *
from definitionen import *
from random import randint


def checke_kollision_mit_essen():
    if kopf.distance(essen) < 20:

        while True:
            x = random.randint(-9, 9) * 20
            y = random.randint(-9, 9) * 20
        essen.goto(x, y)

        neues_segment = Turtle()
        neues_segment.shape("square")
        neues_segment.color("yellow")
        neues_segment.penup()
        neues_segment.speed(0)

        segmente.append(neues_segment)





