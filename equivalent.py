import base as src
import math as mat
import matplotlib.pyplot as plt
import numpy as np

#DERIVADOR EQUIVALENTE (ALDO J. MUNOZ-VAZQUEZ)

class equivalent:

    L = 100

    z = 0
    z1 = 0
    dz = 0
    dz1 = 0
    e = 0
    k1 = 3
    k2 = 10
    k3 = 20
    k4 = 50

    beta1 = 20
    beta2 = 1000

    u1 = 0
    u2 = 0

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
            self.z1 = 0

        self.init.print_graph(self.init.t, self.init.df, self.init.t, self.init.df1, "Derivador Equivalente: Funcion sin Ruido")

        self.init.print_graph(self.init.t, self.init.df, self.init.t, self.init.df2, "Derivador Equivalente: Funcion con Ruido")

        plt.show()

    def routine(self, val):
        self.e = val - self.z
        self.u1 = self.k1 * mat.tanh(self.beta1*self.e)+self.k3*self.e
        self.u2 = self.k2  * mat.tanh(self.beta2*self.u1) + self.k4 * self.u1
        self.dz = self.z1 + self.u1
        self.dz1 = self.u2
        self.z += self.dz * self.init.h
        self.z1 += self.dz1 * self.init.h
        return self.z1


xx = equivalent()