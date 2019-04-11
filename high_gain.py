import base as src
import matplotlib.pyplot as plt

#DERIVADOR DE ALTA GANANCIA

class h_gain:
    z = 0
    e = 0
    k = 10
    dz = 0

    init = None

    def __init__(self):
        self.init = src.XBase()
        self.start(self)

    @staticmethod
    def start(self):
        for y in range(2):
            for x in range(int(self.init.xn)):
                if 0 == y:
                    self.init.df1[x] = float(self.routine(self.init.f1[x]))

                else:
                    self.init.df2[x] = float(self.routine(self.init.f2[x]))

            self.z = 0
            self.e = 0
        self.init.print_graph(self.init.t, self.init.df, self.init.t, self.init.df1, "Alta Ganancia: Funcion sin Ruido")

        self.init.print_graph(self.init.t, self.init.df, self.init.t, self.init.df2, "Alta Ganancia: Funcion con Ruido")

        plt.show()

    def routine(self, val):
        self.e = val - self.z
        self.dz = self.k * self.e
        self.z += self.dz * self.init.h
        return self.dz


xx = h_gain()