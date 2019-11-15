import tkinter as tk
import random
n = int(input("请输入一个1至200的整数"))
a = list(range(0,n))
b = []
while True:
    if len(b) == n:
        break
    b.append('1')
#print(b)
for i in range(0,n):
    b[i] = "a" + str(a[i]) 
def make(name):
    name = tk.Tk()
    x = random.randint(1, 1200)
    y = random.randint(1, 700)
    con = "400x400" + "+" + str(x) + "+" + str(y)
    name.geometry(con)
def makemore(namelist,nembei):
    for i in range(0,nembei):
        make(namelist[i])
makemore(b,n)

