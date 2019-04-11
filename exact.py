import base as src
import math as mat
import matplotlib.pyplot as plt
import numpy as np

#DERIVADOR EXACTO (ARIE LEVANT)

class exact:

    L = 100

    z = 0
    z1 = 0
    dz = 0
    dz1 = 0
    oz1 = 0
    e = 0
    k0 = 1.1*L
    k1 = 1.5 * mat.sqrt(L)

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

        self.init.print_graph(self.init.t, self.init.df, self.init.t, self.init.df1, "Derivador Exacto: Funcion sin Ruido")

        self.init.print_graph(self.init.t, self.init.df, self.init.t, self.init.df2, "Derivador Exacto: Funcion con Ruido")

        plt.show()

    def routine(self, val):
        self.e = val - self.z
        self.dz = self.k1 * mat.sqrt(mat.fabs(self.e))*np.sign(self.e)+self.z1
        self.dz1 = self.k0 * np.sign(self.e)
        self.oz1 = self.z1
        self.z += self.dz * self.init.h
        self.z1 += self.dz1 * self.init.h
        return self.oz1


xx = exact()