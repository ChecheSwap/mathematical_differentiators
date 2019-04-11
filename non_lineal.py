import base as src
import math as mat
import matplotlib.pyplot as plt

#DERIVADOR NO LINEAL (UTKIN)

class n_lineal:

    z = 0
    dz = 0
    e = 0
    k = 3
    beta = 10

    init = None

    def __init__(self):
        self.init = src.XBase()
        self.start(self)

    @staticmethod
    def start(self):
        for y in range(2):
            for x in range(int(self.init.xn)):
                if 0 == y:
                    self.init.df1[x] = self.routine(self.init.f1[x])
                else:
                    self.init.df2[x] = self.routine(self.init.f2[x])
            self.z = 0
            self.e = 0

        self.init.print_graph(self.init.t, self.init.df, self.init.t, self.init.df1, "Derivador No Lineal: Funcion sin Ruido")

        self.init.print_graph(self.init.t, self.init.df, self.init.t, self.init.df2, "Derivador No Lineal: Funcion con Ruido")

        plt.show()

    def routine(self, val):
        self.e = val - self.z
        self.dz = self.k * mat.tanh(self.beta*self.e)
        self.z = self.z + self.dz * self.init.h
        return self.dz


xx = n_lineal()