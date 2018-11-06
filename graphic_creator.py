# uncompyle6 version 3.2.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
# [GCC 5.4.0 20160609]
# Embedded file name: /home/dlopezc/Escritorio/machineAR/graphic_creator.py
# Size of source mod 2**32: 1384 bytes
import pandas as pd
from pandas import Series, DataFrame
from matplotlib.pyplot import pyplot as plt
import numpy as np, statistics as st
from statistics import mode

def creador_graficas(df, num, valor1, valor2):
    x = df[[valor1, 'timestamp']]
    y = df[[valor2, 'timestamp']]
    resultado = pd.merge(x, y, on='timestamp')
    fig = resultado.plot(x='timestamp', figsize=(20, 20))
    fig.set_title(valor1 + ' vs ' + valor2)
    plt.savefig('grafica ' + str(num) + '.png')
    return resultado


def get_promedio(df, valor):
    x = df[valor].values
    return str('El promedio de ' + valor + ' fue de ' + str(sum(x) / float(len(x))))


def get_pico(df, valor):
    x = df[[valor, 'timestamp']]
    x2 = df[valor].values
    maxv = max(x2)
    pos_maxv = list(x2).index(maxv)
    tiempo_m = x.at[(pos_maxv, 'timestamp')]
    return str('Valor maximo de ' + valor + ': ' + str(maxv) + ', en el timestamp ' + str(tiempo_m))


def get_moda(df, valor):
    x1 = df[valor].values
    x2 = list(filter((0.0).__ne__, x1))
    try:
        moda = st.mode(x2)
        return str('La moda de ' + valor + ' fue de ' + str(moda))
    except st.StatisticsError as e:
        try:
            return 'Hay multiples modas en el valor ' + valor
        finally:
            e = None
            del e


def get_media(df, valor):
    x1 = df[valor].values
    x2 = list(filter((0.0).__ne__, x1))
    x3 = st.median(x2)
    return str('La media de ' + valor + ' fue de ' + str(x3))
# okay decompiling graphic_creator.cpython-37.pyc
