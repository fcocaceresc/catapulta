# Copyright (c) 2024, Francisco Cáceres Colihuil. All rights reserved.
# This code is licensed under the BSD 3-Clause License.

from catapulta import Rampa, Proyectil, Informe, graficar_trayectoria, graficar_energia, graficar_velocidad
import json


def main():
    with open("data/config.json") as f:
        config = json.load(f)

    m = config["m"]
    g = config["g"]
    hA = config["hA"]
    hB = config["hB"]
    thetaB = config["thetaB"]

    rampa = Rampa(g, hA, hB)
    vB = rampa.velocidad_final()

    proyectil = Proyectil(m, vB, thetaB, g, hB)

    graficar_trayectoria(proyectil, filename="reports/figures/trayectoria.png")
    graficar_energia(proyectil, filename="reports/figures/energia.png")
    graficar_velocidad(proyectil, filename_vx="reports/figures/velocidad_x.png", filename_vy="reports/figures/velocidad_y.png")

    resultados = {
        "v_B": round(vB, 2),
        "v_xB": round(proyectil.velocidad_x(), 2),
        "v_yB": round(proyectil.velocidad_y(0), 2),
        "tiempo_de_vuelo": round(proyectil.tiempo_de_vuelo(), 2),
        "alcance": round(proyectil.alcance(), 2),
        "altura_maxima": round(proyectil.altura_maxima(), 2),
    }

    variables = {
        "m": round(m, 2),
        "g": round(g, 2),
        "h_A": round(hA, 2),
        "h_B": round(hB, 2),
        "theta_B": round(thetaB, 2)
    }

    graficos = {
        "trayectoria": "figures/trayectoria.png",
        "energia": "figures/energia.png",
        "velocidad_x": "figures/velocidad_x.png",
        "velocidad_y": "figures/velocidad_y.png",
    }

    informe = Informe(variables, resultados, graficos)
    documento = informe.generar_informe()

    with open("reports/informe.tex", "w") as f:
        f.write(documento)


if __name__ == "__main__":
    main()
