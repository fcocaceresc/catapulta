# Copyright (c) 2024, Francisco Cáceres Colihuil. All rights reserved.
# This code is licensed under the BSD 3-Clause License.

import math


class Rampa:
    def __init__(self, g, h1, h2):
        self.g = g
        self.h1 = h1
        self.h2 = h2

    def velocidad_final(self):
        return math.sqrt(2 * self.g * (self.h1 - self.h2))
