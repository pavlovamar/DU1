from turtle import left, right, forward, speed, circle, exitonclick, setpos, penup, pendown, back, home
import math
from math import sqrt
# rychlost, a = počet řádků, b = počet sloupců, s = velikost strany
speed(8)
a = int(input ("Zvolte počet řádků:"))
while a < 1:
        print("Chyba! Zadaný záporný počet řádků. Zkus to znovu.")
        a = int(input ("Zvolte počet řádků: "))
b = int(input ("Zvolte počet sloupců:"))
while b < 1:
        print("Chyba! Zadaný záporný počet sloupců. Zkus to znovu.")
        b = int(input ("Zvolte počet sloupců: "))
s = 50
# čtvercová síť
for k in range(b):
    for l in range(a):
        for i in range(4):
            forward(s)
            right(90)
        forward(s)
    left(180)
    forward(a*s)
    left(90)
    forward(s)
    left(90)
# Střídání hráčů 
d = (a*b//2)
for m in range (d):
    # Hráč 1
    penup()
    home()
    x = int(input ("Hráči 1 zadej řádek: "))
    while x < 1 or x > a:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        x = int(input ("Hráči 1 zadej řádek: "))
    if x == 1:
        setpos(0,0)
    if x > 1:
        setpos(0,(x-1)*(-s))
    y = int(input ("Hráči 1 zadej sloupec: "))  
    while y < 1 or y > b:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        y = int(input ("Hráči 1 zadej řádek: "))
    forward((y-1)*s)
    # křížek
    pendown()
    right(45)
    forward(sqrt(s**2 + s**2))
    back(sqrt(s**2 + s**2)/2)
    right(90)
    forward(sqrt(s**2 + s**2)/2)
    back(sqrt(s**2 + s**2))
    penup()
    home()
    # Hráč 2
    w = int(input ("Hráči 2 řádek: "))
    while w > a or w < 1:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        w = int(input ("Hráči 2 zadej řádek: "))
    setpos(0, w*(-s))
    z = int(input ("Hráči 2 sloupec: "))
    while z > b or z < 1:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        z = int(input ("Hráči 2 zadej řádek: "))
    forward((z*s)-(0.5*s))
    pendown ()
    # kolečko
    circle(s/2)
# Pokud je počet polí lichý, musí hru zakončit první hráč --> po cyklu následuje ještě jedna otázka na souřadnice
if (a*b) % 2 != 0:
    penup ()
    home()
    x = int(input ("Hráči 1 zadej řádek: "))
    while x > a or x < 1:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        x = int(input ("Hráči 1 zadej řádek: "))
    if x == 1:
        setpos(0,0)
    if x > 1:
        setpos(0,(x-1)*(-s))
    y = int(input ("Hráči 1 zadej sloupec: "))  
    while y > b or y < 1:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        y = int(input ("Hráči 1 zadej řádek: "))
    forward((y-1)*s)
    # křížek
    pendown()
    right(45)
    forward(sqrt(s**2 + s**2))
    back(sqrt(s**2 + s**2)/2)
    right(90)
    forward(sqrt(s**2 + s**2)/2)
    back(sqrt(s**2 + s**2))
    penup ()
    home ()
exitonclick ()