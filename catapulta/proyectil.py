# Copyright (c) 2024, Francisco Cáceres Colihuil. All rights reserved.
# This code is licensed under the BSD 3-Clause License.

import numpy as np


class Proyectil:
    def __init__(self, m, v0, theta, g, h):
        self.m = m
        self.v0 = v0
        self.theta = np.deg2rad(theta)
        self.g = g
        self.h = h

    def energia_cinetica(self, t):
        return 0.5 * self.m * (self.velocidad_x() ** 2 + self.velocidad_y(t) ** 2)

    def energia_potencial(self, t):
        return self.m * self.g * self.posicion_y(t)

    def energia_total(self, t):
        return self.energia_cinetica(t) + self.energia_potencial(t)

    def posicion_x(self, t):
        return self.v0 * np.cos(self.theta) * t

    def posicion_y(self, t):
        return self.h + self.v0 * np.sin(self.theta) * t - 0.5 * self.g * t ** 2

    def velocidad_x(self):
        return self.v0 * np.cos(self.theta)

    def velocidad_y(self, t):
        return self.v0 * np.sin(self.theta) - self.g * t

    def tiempo_de_vuelo(self):
        a = -0.5 * self.g
        b = self.v0 * np.sin(self.theta)
        c = self.h
        discriminante = b ** 2 - 4 * a * c
        t1 = (-b + np.sqrt(discriminante)) / (2 * a)
        t2 = (-b - np.sqrt(discriminante)) / (2 * a)
        return max(t1, t2)

    def alcance(self):
        return self.velocidad_x() * self.tiempo_de_vuelo()

    def altura_maxima(self):
        return self.h + (self.v0 * np.sin(self.theta)) ** 2 / (2 * self.g)
