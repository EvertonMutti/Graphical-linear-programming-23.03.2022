# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:41:08 2022

@author: Everton 
"""
import matplotlib.pyplot as plt

# PRIMEIRA RESTRIÇÃO

x1FirstRest = int(input('Digita sua primeira restrição (x1) ex: 4.x1 + 4.x2 <= 400  '))
x1FirstSecon = int(input('Digita sua segunda restrição (x2) ex: 4.x1 + 4.x2 <= 400  '))
LimiteFrist = int(input('Digita o menor ou igual da sua primeira restrição ex: 4.x1 + 4.x2 <= 400  '))

#..............................................................................................
#SEGUNDA RESTRIÇÃO

x1SecondRest = int(input('Digita sua primeira restrição (x1) ex: 4.x1 + 4.x2 <= 450  '))
x2SecondSecon = int(input('Digita sua segunda restrição(x2) ex: 4.x1 + 4.x2 <= 450  '))
LimiteSecond = int(input('Digita o menor ou igual da sua segunda restrição ex: 4.x1 + 4.x2 <= 450  '))

#..............................................................................................

Lucrox1 = int(input('Digita o lucro de (x1) ex: L = 180.x1 + 320x2  '))
Lucrox2 = int(input('Digita o lucro (x2) ex: L = 180.x1 + 320x2  '))


x2 = x1FirstRest * 0 + LimiteFrist / x1FirstSecon
x1 = x1FirstSecon * 0 + LimiteFrist / x1FirstRest
#print(x1, x2)

#----------------------------------------------------------------------------------------------

x2_2 = x1SecondRest * 0  + LimiteSecond / x2SecondSecon
x1_1 = LimiteSecond * 0  + LimiteSecond / x1SecondRest
#print(x1_1, x2_2)

#----------------------------------------------------------------------------------------------
# SOLUÇÃO PERFEITA (INTERCEÇÃO)

x_TEMP = ((x1FirstRest) * (-2) + x1SecondRest) + ((x1FirstSecon) * (-2) + x2SecondSecon) 
xRestricao = ((LimiteFrist) * (-2) + LimiteSecond)
x2_SOLUCAOOTIMA = xRestricao / x_TEMP

x1_SOLUCAOOTIMA = LimiteFrist - (x1FirstSecon * x2_SOLUCAOOTIMA) 
x1_SOLUCAOOTIMA = x1_SOLUCAOOTIMA / x1FirstRest

#print(x1_SOLUCAOOTIMA, x2_SOLUCAOOTIMA)

#----------------------------------------------------------------------------------------------
#Lucro

Lucro1 = Lucrox1 * 0 + Lucrox2 * x2 #(0,20)
Lucro2 = Lucrox1 * x1_1 + Lucrox2 * 0 #(45, 0)
LucroSOLUCAOOTIMA = Lucrox1 * x1_SOLUCAOOTIMA + Lucrox2 * x2_SOLUCAOOTIMA

if Lucro1 > (Lucro2 and LucroSOLUCAOOTIMA):
    print('O maior lucro é {}' .format(int(Lucro1)))
    print('A solução ótima é ({},{})' .format(int(x2), int(x1)))
    plt.plot([1, x2], [x1, 0] )
elif Lucro2 > (Lucro1 and LucroSOLUCAOOTIMA):
    print('O maior lucro é {}' .format(int(Lucro2)))
    print('A solução ótima é ({},{})' .format(int(x2_2), int(x1_1)))
    plt.plot([1, x2_2], [x1_1, 0] )
elif LucroSOLUCAOOTIMA > (Lucro1 and Lucro2):
    print('O maior lucro é {}' .format(int(LucroSOLUCAOOTIMA)))
    print('A solução ótima é ({},{})' .format(int(x1_SOLUCAOOTIMA), int(x2_SOLUCAOOTIMA)))
    plt.plot([1, x2_SOLUCAOOTIMA], [x1_SOLUCAOOTIMA, 0] )

plt.show()

#print(Lucro1, Lucro2, LucroSOLUCAOOTIMA)



