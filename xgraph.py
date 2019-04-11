import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


class xgraph:

    def graph(self, x1, y1, x2, y2, title, fcontrol):
        rf = plt.figure(fcontrol)
        rf.canvas.set_window_title("#"+str(fcontrol)+" "+title)
        rf.patch.set_facecolor('xkcd:charcoal')
        if x1 is not None and y2 is not None:
            plt.plot(x2, y2, 'b')
        plt.plot(x1, y1, '--r')
        plt.grid(True)
        plt.title(">>"+title+"<<", color='yellow', fontsize = 15)
        plt.xlabel("Tiempo [0:5]", color='orange')
        plt.ylabel("Valores de la señal [0:1]", color='orange')
        plt.tick_params(labelcolor='tab:cyan')

