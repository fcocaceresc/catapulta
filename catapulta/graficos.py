# Copyright (c) 2024, Francisco Cáceres Colihuil. All rights reserved.
# This code is licensed under the BSD 3-Clause License.

import numpy as np
import matplotlib.pyplot as plt


def graficar_trayectoria(proyectil, filename="trayectoria.png"):
    tiempo_total = proyectil.tiempo_de_vuelo()
    t = np.linspace(0, tiempo_total, 100)
    x = proyectil.posicion_x(t)
    y = proyectil.posicion_y(t)
    plt.plot(x, y)
    plt.title("Trayectoria del Proyectil")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.grid()
    plt.savefig(filename)
    plt.close()


def graficar_energia(proyectil, filename="energia.png"):
    tiempo_total = proyectil.tiempo_de_vuelo()
    t = np.linspace(0, tiempo_total, 100)
    energia_cinetica = proyectil.energia_cinetica(t)
    energia_potencial = proyectil.energia_potencial(t)
    energia_total = energia_cinetica + energia_potencial

    plt.plot(t, energia_cinetica, label="Energía Cinética")
    plt.plot(t, energia_potencial, label="Energía Potencial")
    plt.plot(t, energia_total, label="Energía Total")
    plt.title("Energías del Proyectil")
    plt.xlabel("t (s)")
    plt.ylabel("E (J)")
    plt.grid()
    plt.legend()
    plt.savefig(filename)
    plt.close()


def graficar_velocidad(proyectil, filename_vx="velocidad_x.png", filename_vy="velocidad_y.png"):
    tiempo_total = proyectil.tiempo_de_vuelo()
    t = np.linspace(0, tiempo_total, 100)
    vx = proyectil.velocidad_x()
    vy = proyectil.velocidad_y(t)

    plt.plot(t, vx * np.ones_like(t))
    plt.title("Velocidad en x del Proyectil")
    plt.xlabel("t (s)")
    plt.ylabel("v (m/s)")
    plt.grid()
    plt.savefig(filename_vx)
    plt.close()

    plt.plot(t, vy, color="orange")
    plt.title("Velocidad en y del Proyectil")
    plt.xlabel("t (s)")
    plt.ylabel("v (m/s)")
    plt.grid()
    plt.savefig(filename_vy)
    plt.close()
