# Copyright (c) 2024, Francisco Cáceres Colihuil. All rights reserved.
# This code is licensed under the BSD 3-Clause License.

class Informe:

    def __init__(self, variables, resultados, paths_graficos):
        self.variables = variables
        self.resultados = resultados
        self.paths_graficos = paths_graficos

    def generar_informe(self):
        tex_content = r"""
        \documentclass{{article}}
        \usepackage[utf8]{{inputenc}}
        \usepackage[spanish]{{babel}}
        \usepackage{{amsmath}}
        \usepackage{{graphicx}}
        \usepackage{{float}}
        \usepackage{{setspace}}
        \usepackage{{siunitx}}
        \usepackage{{geometry}}
        \geometry{{
            left=1in,
            right=1in,
            top=1in,
            bottom=1in
        }}
        \doublespacing
        \begin{{document}}
        \section{{Modelo de la catapulta}}
        \begin{{figure}}[H]
            \centering
            \includegraphics[width=0.5\textwidth]{{figures/catapulta.jpeg}}
            \caption{{Modelo de la catapulta}}
        \end{{figure}}
        \section{{Variables}}
        Las variables iniciales son:
        \begin{{align*}}
            m &= {m} \si{{kg}} \\
            g &= {g} \si{{m/s^2}} \\
            h_A &= {h_A} \si{{m}} \\
            h_B &= {h_B} \si{{m}} \\
            \theta_B &= {theta} \si{{\degree}} \\
        \end{{align*}}
        """.format(m=self.variables['m'],
                   g=self.variables['g'],
                   h_A=self.variables['h_A'],
                   h_B=self.variables['h_B'],
                   theta=self.variables['theta_B'])

        tex_content += self.seccion_velocidad_en_b()
        tex_content += self.seccion_funciones_posicion()
        tex_content += self.seccion_funciones_energia()
        tex_content += self.seccion_funciones_velocidad()
        tex_content += self.seccion_tiempo_de_vuelo()
        tex_content += self.seccion_alcance()
        tex_content += self.seccion_altura_maxima()

        tex_content += r"""
        \end{document}
        """
        return tex_content

    def seccion_velocidad_en_b(self):
        return r"""
        \section{{Cálculos (sin fricción)}}
        En este caso, se asume que no hay fricción entre el proyectil y la rampa ni entre el proyectil y el aire, por lo que la energía mecánica se conserva a lo largo de todo el trayecto, desde que se suelta el proyectil en el punto $A$ hasta que cae al suelo.
        \subsection{{Velocidad en el punto $B$}}
        Para calcular la velocidad con la que el proyectil sale disparado de la rampa, o la velocidad en el punto $B$,
        se utiliza la conservación de la energía mecánica.
        \begin{{align*}}
            E &= K + U \\
        \end{{align*}}
        Donde:
        \begin{{align*}}
            K &= \frac{{1}}{{2}} m v^2 \\
            U &= m g h \\
        \end{{align*}}
        Como no hay fricción, la energía mecánica se conserva, y la energía en los puntos $A$ y $B$ es la misma:
        \begin{{align*}}
            E_A &= E_B \\
            K_A + U_A &= K_B + U_B \\
            \frac{{1}}{{2}} m v_A^2 + m g h_A &= \frac{{1}}{{2}} m v_B^2 + m g h_B \\
        \end{{align*}}
        Dado que en el punto $A$, el proyectil parte del reposo, $v_A = 0$:
        \begin{{align*}}
            m g h_A &= \frac{{1}}{{2}} m v_B^2 + m g h_B \\
        \end{{align*}}
        Despejando $v_B$:
        \begin{{align*}}
            v_B &= \sqrt{{v_A^2 + 2 g (h_A - h_B)}} \\
        \end{{align*}}
        Sustituyendo los valores, tenemos:
        \begin{{align*}}
            v_B &= \sqrt{{2 \cdot {g} \cdot ({h_A} - {h_B})}} \\
            v_B &= {v_B} \, \si{{m/s}} \\
        \end{{align*}}
        """.format(g=self.variables['g'],
                   h_A=self.variables['h_A'],
                   h_B=self.variables['h_B'],
                   v_B=self.resultados['v_B'])

    def seccion_funciones_posicion(self):
        return r"""
        \subsection{{Funciones de posición}}
        Las funciones de posición en función del tiempo de un movimiento parabólico son:
        \begin{{align*}}
            x(t) &= x_B + v_{{xB}} t \\
            y(t) &= h_B + v_{{yB}} t - \frac{{1}}{{2}} g t^2 \\
        \end{{align*}}
        Para descomponer $v_B$ en sus componentes $v_{{xB}}$ y $v_{{yB}}$, se tiene:
        \begin{{align*}}
            v_{{xB}} &= v_B \cos(\theta_B) \\
            v_{{yB}} &= v_B \sin(\theta_B) \\
        \end{{align*}}
        Sustituyendo los valores, tenemos:
        \begin{{align*}}
            v_{{xB}} &= {v_B} \cos({theta_B}) \\
            v_{{yB}} &= {v_B} \sin({theta_B}) \\
        \end{{align*}}
        Resolviendo, se tiene:
        \begin{{align*}}
            v_{{xB}} &= {v_xB} \si{{m/s}} \\
            v_{{yB}} &= {v_yB} \si{{m/s}} \\
        \end{{align*}}
        Sustiyendo las velocidades en las funciones de posición, se obtiene:
        \begin{{align*}}
            x(t) &= {v_xB} t \\
            y(t) &= {h_B} + {v_yB} t - \frac{{1}}{{2}} {g} t^2 \\
        \end{{align*}}
        Para graficar la trayectoria, parametrizamos las funciones de posición en función del tiempo:
        \[
        \begin{{cases}}
            x(t) = {v_xB} t \\
            y(t) = {h_B} + {v_yB} t - \frac{{1}}{{2}} {g} t^2 \\
        \end{{cases}}
        \]
        Graficando la ecuación paramétrica, se obtiene:
        \begin{{figure}}[H]
            \centering
            \includegraphics[width=0.8\textwidth]{{{grafico_trayectoria}}}
            \caption{{Trayectoria del proyectil}}
        \end{{figure}}
        """.format(g=self.variables['g'],
                   h_B=self.variables['h_B'],
                   theta_B=self.variables['theta_B'],
                   v_B=self.resultados['v_B'],
                   v_xB=self.resultados['v_xB'],
                   v_yB=self.resultados['v_yB'],
                   grafico_trayectoria=self.paths_graficos['trayectoria'])

    def seccion_funciones_energia(self):
        return r"""
        \subsection{{Funciones de energía}}
        Las funciones de energía en función del tiempo del proyectil son:
        \begin{{align*}}
            K(t) &= \frac{{1}}{{2}} m (v_x(t)^2 + v_y(t)^2) \\
            U(t) &= m g y(t) \\
            E(t) &= K(t) + U(t) \\
        \end{{align*}}
        Graficando las energías:
        \begin{{figure}}[H]
            \centering
            \includegraphics[width=0.8\textwidth]{{{grafico_energia}}}
            \caption{{Energías del proyectil}}
        \end{{figure}}
        Como se observa en el gráfico, la energía mecánica se conserva a lo largo de todo el trayecto.
        """.format(grafico_energia=self.paths_graficos['energia'])

    def seccion_funciones_velocidad(self):
        return r"""
        \subsection{{Funciones de velocidad}}
        Para calcular la velocidad en función del tiempo, derivamos las funciones de posición con respecto al tiempo:
        \begin{{align*}}
            v_x(t) &= \frac{{dx}}{{dt}} = v_{{xB}} \\
            v_y(t) &= \frac{{dy}}{{dt}} = v_{{yB}} - g t \\
        \end{{align*}}
        Sustituyendo los valores:
        \begin{{align*}}
            v_x(t) &= {v_xB} \\
            v_y(t) &= {v_yB} - {g} t \\
        \end{{align*}}
        Graficando las velocidades:
        \begin{{figure}}[H]
            \centering
            \includegraphics[width=0.8\textwidth]{{{grafico_vx}}}
            \caption{{Velocidad en x del proyectil}}
        \end{{figure}}
        \begin{{figure}}[H]
            \centering
            \includegraphics[width=0.8\textwidth]{{{grafico_vy}}}
            \caption{{Velocidad en y del proyectil}}
        \end{{figure}}
        """.format(g=self.variables['g'],
                   v_xB=self.resultados['v_xB'],
                   v_yB=self.resultados['v_yB'],
                   grafico_vx=self.paths_graficos['velocidad_x'],
                   grafico_vy=self.paths_graficos['velocidad_y'])

    def seccion_tiempo_de_vuelo(self):
        tiempo_vuelo = self.resultados['tiempo_de_vuelo']
        return r"""
        \subsection{{Tiempo de vuelo}}
        El tiempo de vuelo del proyectil es:
        \[
        t = \frac{{v_{{yB}} + \sqrt{{v_{{yB}}^2 + 2 g h_B}}}}{{g}}
        \]
        Sustituyendo los valores:
        \begin{{align*}}
        t &= \frac{{ {v_yB} + \sqrt{{ {v_yB}^2 + 2 \cdot {g} \cdot {h_B} }} }}{{ {g} }} \\
        t &= {tiempo} \, \si{{s}}
        \end{{align*}}
        """.format(v_yB=self.resultados['v_yB'],
                   g=self.variables['g'],
                   h_B=self.variables['h_B'],
                   tiempo=tiempo_vuelo)

    def seccion_alcance(self):
        alcance = self.resultados['alcance']
        return r"""
        \subsection{{Alcance}}
        El alcance del proyectil es:
        \[
        R = v_{{xB}} \frac{{v_{{yB}} + \sqrt{{v_{{yB}}^2 + 2gh_B}}}}{{g}}
        \]
        Sustituyendo los valores:
        \begin{{align*}}
        R &= {v_xB} \frac{{ {v_yB} + \sqrt{{ {v_yB}^2 + 2 \cdot {g} \cdot {h_B} }} }}{{ {g} }} \\
        R &= {alcance} \, \si{{m}}
        \end{{align*}}
        """.format(g=self.variables['g'],
                   h_B=self.variables['h_B'],
                   v_xB=self.resultados['v_xB'],
                   v_yB=self.resultados['v_yB'],
                   alcance=alcance)

    def seccion_altura_maxima(self):
        altura_max = self.resultados['altura_maxima']
        return r"""
        \subsection{{Altura máxima}}
        La altura máxima alcanzada por el proyectil es:
        \[
        h_{{\text{{max}}}} = h_B + \frac{{v_B^2 \sin^2(\theta_B)}}{{2 g}}
        \]
        Sustituyendo los valores:
        \begin{{align*}}
        h_{{\text{{max}}}} &= {h_B} + \frac{{ {v_B}^2 \sin^2({theta_B})}}{{2 \cdot {g}}} \\
        h_{{\text{{max}}}} &= {altura_max} \, \si{{m}}
        \end{{align*}}
        """.format(h_B=self.variables['h_B'],
                   v_B=self.resultados['v_B'],
                   theta_B=self.variables['theta_B'],
                   g=self.variables['g'],
                   altura_max=altura_max)
