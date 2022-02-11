#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import sys

sys.path.append(".")
from .rotation import rotate as rt

global P
P = np.array([1,0,0])
global frame
frame = np.array([[1,0,0],[0,1,0],[0,0,1]])
global omega
omega = np.array([1,2,2])

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

def get_arrow_1(t):
    x = 0
    y = 0
    z = 0
    u = frame[0][0]
    v = frame[1][0]
    w = frame[2][0]
    return [u,v,w]

def get_arrow_2(t):
    x = 0
    y = 0
    z = 0
    u = frame[0][1]
    v = frame[1][1]
    w = frame[2][1]
    return [u,v,w]

def get_arrow_3(t):
    x = 0
    y = 0
    z = 0
    u = frame[0][2]
    v = frame[1][2]
    w = frame[2][2]
    return [u,v,w]

def get_arrow(t):
    x = [0,0,0]
    y = [0,0,0]
    z = [0,0,0]
    i = get_arrow_1(t)
    j = get_arrow_2(t)
    k = get_arrow_3(t)
    u = [i[0],j[0],k[0]]
    v = [i[1],j[1],k[1]]
    w = [i[2],j[2],k[2]]
    return x,y,z,u,v,w


quiver = ax.quiver(*get_arrow(0))

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

def update(t):
    global frame
    frame = rt(np.array([1,2,2]),t,frame)
    global quiver
    quiver.remove()
    quiver = ax.quiver(*get_arrow(t))

ani = FuncAnimation(fig, update, frames=np.linspace(0,0.1,1000), interval=50)
plt.show()
