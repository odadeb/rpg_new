# -*- coding: utf-8 -*-

class GoblinData:
    def __init__(self, height, width, HealthPoint, MagicPoint, type):
        self.type = type
        self.height = height
        self.width = width
        self.healthPoint = HealthPoint
        self.MagicPoint = MagicPoint       
        print(f'{self.type}, hoje cedo')