import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math as mat
import random as ran
import xgraph as grafs


class XBase(grafs.xgraph):
    fcc = None

    h = None
    tf = None
    t = None
    n = None
    f1 = None
    df = None
    df1 = None
    f2 = None
    df2 = None
    xn = None

    NOISE_CONST = .002

    def init_graph(self):
        self.graph(self.t, self.f1, self.t, self.f2, "Funciones de entrada", self.fcc)

    def print_graph(self, x1, y1, x2, y2, title):
        self.fcc += 1
        self.graph(x1, y1, x2, y2, title, self.fcc)

    def __init__(self):
        self.fcc = 1
        self.h = 0.0002
        self.tf = 5
        self.xn = self.tf / self.h
        self.xn += 1
        self.t = np.zeros(int(self.xn))
        self.f1 = np.empty(int(self.xn))
        self.df1 = np.empty(int(self.xn))
        self.f2 = np.empty(int(self.xn))
        self.df2 = np.empty(int(self.xn))
        self.df = np.empty(int(self.xn))
        i = 0
        for x in np.arange(0, self.tf + self.h, self.h):
            self.t[i] = x
            self.f1[i] = mat.sin(x)
            self.df[i] = mat.cos(x)
            #print(str(self.df[i]))
            self.f2[i] = self.f1[i] + self.NOISE_CONST * ((ran.uniform(0, 1)) - 0.5)

            i += 1
            if i == self.xn:
                self.init_graph()
