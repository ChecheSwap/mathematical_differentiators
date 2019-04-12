import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math as mat
import xgraph as gr
import base as src

#DERIVADOR "DERIVADA SUCIA"

class DirtyDerivative:
    init = None

    def __init__(self):
        self.init = src.XBase()
        self.start(self)

    @staticmethod
    def start(self):

        for y in range(2):
            for x in range(2, int(self.init.xn)):
                if 0 == y:
                    self.init.df1[x] = (self.init.f1[x] - self.init.f1[x - 1]) / self.init.h

                else:
                    self.init.df2[x] = (self.init.f2[x] - self.init.f2[x - 1]) / self.init.h
                    print(str(self.init.f2[x])+ "   "+ str(self.init.f2[x-1]) + "   " + str(self.init.df2[x]))

        self.init.print_graph(self.init.t, self.init.df, self.init.t, self.init.df1, "Derivada Sucia: Funcion sin Ruido")

        self.init.print_graph(self.init.t, self.init.df, self.init.t, self.init.df2, "Derivada Sucia: Funcion con Ruido")

        plt.show()


xx = DirtyDerivative()
