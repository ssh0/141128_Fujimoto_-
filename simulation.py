#!/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

r = 5.
N = 6
radius = 3

class Person(object):
    
    def __init__(self, name, ideas_num=10, place=(0., 0.)):
        self.link = []
        self.name = name
        self.ideas_num = ideas_num
        self.place = place
        self.ocp = False
        
    def distance(self, p):
        dist = np.sqrt((self.place[0]-p[0])**2 + (self.place[1]-p[1])**2)
        return dist
    
    def linked_to(self, p):
        self.link.append(p.name)
        p.link.append(self.name)
        
        
class meeting(object):
    
    def __init__(self):
        self.ideas = []
        x0 = (0., 0.)
        self.members = []
        deg = np.linspace(0., 360., N+1, endpoint=False)
        for n in range(N+1):
            rad = np.radians(deg[n])
            self.members.append(Person(name=str(n),
                                       place=(radius*np.cos(rad),
                                              radius*np.sin(rad)
                                              )
                                       )
                               )
        
            
    def test_plot(self):
        x = [0.,]
        y = [0.,]
        for n in range(N+1):
            x.append(self.members[n].place[0])
            y.append(self.members[n].place[1])
        return x,y
        
        
a = meeting()
x, y = a.test_plot()
fig = plt.Figure()
ax = fig.add_subplot(111)
ax.set_aspect("equal")
plt.scatter(x, y)
plt.show()
