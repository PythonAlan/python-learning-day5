#!/usr/bin/env python3
#antuor:Alan

class Person:
    def __init__(self,name,gen,age,fight):
        self.name = name
        self.gen = gen
        self.age = age
        self.fight = fight
    def greenglass(self):
        self.fihgt = self.fight - 100
    def practice(self):
        self.fight = self.fight + 300
    def multiplay(self):
        self.fight = self.fight - 500
    def detail(self):
        temp = "人物:%s , 性别:%s ,年龄:%s,战斗值:%s" % (self.name,self.gen,self.age,self.fight)
        print(temp)

CangJin = Person("苍井","femal",28,1000)
DongNi = Person("Dongni","male",20,1500)
BallDD = Person("BallDD","femal",24,1600)



CangJin.multiplay()
DongNi.greenglass()
BallDD.practice()

CangJin.detail()
DongNi.detail()
BallDD.detail()

"""
人物:苍井 , 性别:femal ,年龄:28,战斗值:500
人物:Dongni , 性别:male ,年龄:20,战斗值:1500
人物:BallDD , 性别:femal ,年龄:24,战斗值:1900
"""