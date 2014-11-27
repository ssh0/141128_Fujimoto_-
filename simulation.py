#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto, 2014.


import matplotlib.pyplot as plt
import numpy as np


N = 6
radius = 3

def accumulate(iterable):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    total = next(it)
    yield total
    for element in it:
        total += element
        yield total

class Person(object):
    
    def __init__(self, ideas_num=10, place=(0., 0.), **kwargs):
        self.ideas = list(np.random.random(ideas_num))
        self.place = place
        for (k, v) in kwargs.items():
            setattr(self, k, v)
        
    def distance(self, p):
        d = np.sqrt((self.place[0]-p[0])**2 + (self.place[1]-p[1])**2)
        return d
    
class meeting(object):
    
    def __init__(self):
        self.ideas = []
        self.speaker = []
        self.k = 0
        self.links = []
        x0 = 0.
        self.ideas.append(x0)
        self.speaker.append(0)
        self.members = {0: Person(place=(0., 0.)),}
        deg = np.linspace(0., 360., N, endpoint=False)
        for n in range(1, N+1):
            rad = np.radians(deg[n-1])
            self.members[n] = Person(place=(radius*np.cos(rad), radius*np.sin(rad)))
            
    def linked_to(self, p):
        self.link.append(p.name)
        p.link.append(self.name)

    def weight(self, x):
        return 1./(1.+x)
        
    def p(self, i):
        weight = []
        _N = []
        for k, v in self.members.items():
            if len(v.ideas):
                _N.append(k)
        for n in _N:
            d = self.members[n].distance(i.place)
            weight.append(self.weight(d))
        weight = np.array(weight)
        sum_ = np.sum(weight)
        _p = list(weight/sum_)
        p = accumulate(_p)
        rn = np.random.rand()
        nm = 0
        while True:
            if _N[nm] > rn:
                break
            else:
                nm += 1
        return _N[nm]
    
    def q(self, j):
        x_j = self.members[j]
        return x_j.ideas.pop()
        
    def progress(self):      
        j = self.p(self.members[self.speaker[-1]])
        self.ideas.append(self.q(j))
        
    
    def test_plot(self):
        x = [0,]
        y = [0,]
        for n in range(N+1):
            x.append(self.members[n].place[0])
            y.append(self.members[n].place[1])
        return x,y

