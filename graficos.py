##Biblioteca para padronização da criação de gráficos
##Autor: Thiago William Machado (github: thimac)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def cria_figura(figs=(6,8)):
    plt.style.use('seaborn-whitegrid')
    #plt.style.use('ggplot')
    fig = plt.figure(figsize=(figs))
    return fig

def cria_axes (fig=plt.figure(), titulo="", labelx="", labely="", lci=[1,1,1], ticks=True):
    ax = fig.add_subplot(lci[0], lci[1], lci[2])
    ax.set_title(titulo)
    ax.xaxis.grid(True, color ="grey", lw = .05)
    ax.yaxis.grid(True, color ="grey", lw = .05)
    if ticks:
        ax.set_xticklabels(labelx, rotation=45, ha='right')
    ax.set_ylabel(labely)
    ax.set_xlabel(labelx)
    #ax.set_yticks(ranges)
    ax.set_frame_on(False)
    return ax

def plot_variaveis_categoricas (df=None, lci=[1,1,1], lista_vars=[], figs=(6,8), lista_titulo=[], color='#0F2D49', labely=""):
    fig = cria_figura(figs=figs)
    for i, column in enumerate(lista_vars):
        lci[-1:] = [i+1]
        ax = cria_axes (fig=fig,titulo=lista_titulo[i], lci=lci)
        sns.countplot(x=column, data=df, order = df[column].value_counts().index, color=color, ax=ax).set(ylabel="", xlabel="")
    
def plot_variaveis_numericas (df, lci, lista_vars, figs, lista_titulo, bins, logscale):
    fig = cria_figura(figs=figs)
    for i, column in enumerate(lista_vars):
        lci[-1:] = [i+1]
        ax = cria_axes (fig=fig,titulo=lista_titulo[i], lci=lci)
        sns.histplot(data=df, x=column, bins=bins, log_scale=logscale, ax=ax, color="#0F2D49")
        
def plot_linhas_group (df, lci, lista_vars, figs, titulo, ylabel="", xlabel="", colors=["#0F2D49", "#F1C232"]):
    fig = cria_figura(figs=figs)
    ax = cria_axes (fig=fig,titulo=titulo, ticks=False)
    for i, column in enumerate(df.columns):
        sns.lineplot(x=df[column].index.values, y=df[column], ax=ax, color= colors[i]).set(ylabel=ylabel, xlabel=xlabel)
        
    plt.legend(labels=lista_vars, facecolor='white')

def plot_variaveis_barras (df=None, titulo = "", ylabel="", palette = "cividis", lim = 101, figs = (6,8), y = "", x = "index", hue=None, palle=True):
    fig = cria_figura(figs)
    ax = cria_axes (fig=fig, titulo=titulo)
    if(palle==True):
        sns.barplot(data = df, x = x, y = y, hue = hue, palette=palette, ax=ax).set(ylabel="Porcentagem", xlabel="")
    else:
        sns.barplot(data = df, x = x, y = y, color="#0F2D49", ax=ax).set(ylabel=ylabel)

def plot_variaveis_caixa (df, lci, lista_vars, figs):
    fig = cria_figura(figs=figs)
    #if len(lci) == 0:
    for i, column in enumerate(lista_vars):
        lci[-1:] = [i+1]
        ax = cria_axes (fig=fig, lci=lci)
        sns.boxplot(y=column, data=df, ax=ax, color="#0F2D49")

#pd.melt(df[lista_vars]
def calcula_porcentagem (df, col):
    ser_aux = df[col].value_counts()
    ser_aux = ser_aux/ser_aux.sum()*100
    return ser_aux.to_frame().reset_index()