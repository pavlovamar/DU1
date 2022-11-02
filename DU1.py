from turtle import left, right, forward, speed, circle, exitonclick, setpos, penup, pendown, back, home
import math
from math import sqrt
# rychlost, počet řádků a sloupců, velikost strany
speed(15)
a = int(input ("Zvolte počet řádků:"))
while a < 1:
        print("Chyba! Zadaný záporný počet řádků. Zkus to znovu.")
        a = int(input ("Zvolte počet řádků: "))
b = int(input ("Zvolte počet sloupců:"))
while b < 1:
        print("Chyba! Zadaný záporný počet sloupců. Zkus to znovu.")
        b = int(input ("Zvolte počet sloupců: "))
c = 50
# čtvercová síť
for k in range (b):
    for l in range (a):
        for i in range (4):
            forward (c)
            right (90)
        forward (c)
    left (180)
    forward (a*c)
    left(90)
    forward(c)
    left(90)
# Střídání hráčů 
d = int((a*b)/2)
for m in range (d):
    # Hráč 1
    penup ()
    home()
    x = int(input ("Hráči 1 zadej řádek: "))
    while x < 1:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        x = int(input ("Hráči 1 zadej řádek: "))
    while x > a:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        x = int(input ("Hráči 1 zadej řádek: "))
    if x == 1:
        setpos(0,0)
    if x > 1:
        setpos(0,(x-1)*(-100))
    y = int(input ("Hráči 1 zadej sloupec: "))  
    while y < 1:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        y = int(input ("Hráči 1 zadej řádek: "))
    while y > b:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        y = int(input ("Hráči 1 zadej řádek: "))
    forward((y-1)*c)
    # křížek
    pendown()
    right(45)
    forward(sqrt(c**2 + c**2))
    back(sqrt(c**2 + c**2)/2)
    right(90)
    forward(sqrt(c**2 + c**2)/2)
    back(sqrt(c**2 + c**2))
    penup ()
    home ()
    # Hráč 2
    w = int(input ("Hráči 2 řádek: "))
    while w > a:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        w = int(input ("Hráči 2 zadej řádek: "))
    while w < 1:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        w = int(input ("Hráči 2 zadej řádek: "))
    setpos(0, w*(-100))
    z = int(input ("Hráči 2 sloupec: "))
    while z > b:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        z = int(input ("Hráči 2 zadej řádek: "))
    while z < 1:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        z = int(input ("Hráči 2 zadej řádek: "))
    forward((z*100)-50)
    pendown ()
    # kolečko
    circle(c/2)
# Pokud je počet polí lichý, musí hru zakončit první hráč --> po cyklu následuje ještě jedna otázka na souřadnice
if (a*b) % 2 != 0:
    penup ()
    home()
    x = int(input ("Hráči 1 zadej řádek: "))
    while x > a:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        x = int(input ("Hráči 1 zadej řádek: "))
    while x < 1:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        x = int(input ("Hráči 1 zadej řádek: "))
    if x == 1:
        setpos(0,0)
    if x > 1:
        setpos(0,(x-1)*(-100))
    y = int(input ("Hráči 1 zadej sloupec: "))  
    while y > b:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        y = int(input ("Hráči 1 zadej řádek: "))
    while y < 1:
        print("Chyba! Špatně zadaná souřadnice. Zkus to znovu.")
        y = int(input ("Hráči 1 zadej řádek: "))
    forward((y-1)*c)
    # křížek
    pendown()
    right(45)
    forward(sqrt(c**2 + c**2))
    back(sqrt(c**2 + c**2)/2)
    right(90)
    forward(sqrt(c**2 + c**2)/2)
    back(sqrt(c**2 + c**2))
    penup ()
    home ()
exitonclick ()