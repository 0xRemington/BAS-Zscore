# importing libraries
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib.animation import FuncAnimation
import datetime as dt

#plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    zscore = stats.zscore(data['spread'], nan_policy='omit')
    x = data['time']
    y1 = zscore
    x = x[-50:]
    y1 = y1[-50:]

    plt.clf()

    plt.plot(x, y1, label='Channel 1')


    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.autoscale(False)
plt.tight_layout()
plt.show()