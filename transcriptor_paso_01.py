#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  # transcriptor_fonologico
#  
#  Copyright 2017 mapa <mapa@jules>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#    1. Una entrada literal -------------> una transcripción fonológica
#    2. una transcripción fonológica ----> una secuenca cvcv cvcv cvcvc
#    3. una secuencia cvcv cvcv cvcvc ---> separada por sílabas
#    para cada palabra                      cv cv / cv cv / cv cvc     
#

palabra = input('escribe unas palabras:   ')

# Agrega un especio al final para evitar los AY > ay
espacio_poste = " "
palabra = palabra + espacio_poste

# Separación por palabras
lista_palabras = palabra.split(" ")

# Número de palabras de toda la cadena
n_palabras=len(lista_palabras)

# poner todo en minúsculas
palabra = palabra.lower()

# Elimina acentos
paso_a = palabra.replace("á", "a")
paso_e = paso_a.replace("é", "e")
paso_i = paso_e.replace("í", "i")
paso_o = paso_i.replace("ó", "o")
paso_u = paso_o.replace("ú", "u")

# sustituye V por B
paso_b = paso_u.replace("v", "b")

# sustituye C por S
paso_ce = paso_b.replace("ce", "se")
paso_ci = paso_ce.replace("ci", "si")

# sustituye C por K
paso_ca =paso_ci.replace("ca", "ka")
paso_co =paso_ca.replace("co", "ko")
paso_cu =paso_co.replace("cu", "ku")

# sustituye CH por 
paso_ch = paso_cu.replace("ch", "t͡∫")

# sustituye la X
paso_xks = paso_ch.replace(" x", "s")
paso_x_vxv= paso_xks.replace("x","ks")
paso_cuate= paso_x_vxv.replace("meksi","mexi")

# sustituye GE, GI, J por X
paso_x = paso_cuate.replace("j", "x")
paso_xe = paso_x.replace("ge", "xe")
paso_xi = paso_xe.replace("gi", "xi")

# sustituye diptongos finales con y
paso_oi = paso_xi.replace("oy ", "oi ")
paso_ei = paso_oi.replace("ey ", "ei ")
paso_ui = paso_ei.replace("uy ", "ui ")
paso_ai = paso_ui.replace("ay ", "ai ")

paso_ay = paso_ai.replace("ay", "aʝ")
paso_ey = paso_ay.replace("ey", "eʝ")
paso_oy = paso_ey.replace("oy", "oʝ")
paso_uy = paso_oy.replace("uy", "uʝ")
paso_iy = paso_uy.replace("iy", "iʝ")

paso_y2 = paso_iy.replace("y", "ʝ")

# sustituye LL por Y
paso_y = paso_y2.replace("ll", "ʝ")

# sustituye QU por K
paso_k = paso_y.replace("qu", "k")

# sustituye Z por S
paso_z = paso_k.replace("z", "s")

# sustituye GUE/I por GE/I
paso_ge = paso_z.replace("gue","ge")
paso_gi = paso_ge.replace("gui","gi")

# sustituye ERRES (1)
paso_rr1 = paso_gi.replace("rr","00")

# sustituye casos de ERE

paso_r1 = paso_rr1.replace("ar","aɾ")
paso_r2 = paso_r1.replace("er","eɾ")
paso_r3 = paso_r2.replace("ir","iɾ")
paso_r4 = paso_r3.replace("or","oɾ")
paso_r5 = paso_r4.replace("ur","uɾ")
paso_r6 = paso_r5.replace("gr","gɾ")
paso_r7 = paso_r6.replace("br","bɾ")
paso_r8 = paso_r7.replace("pr","pɾ")
paso_r9 = paso_r8.replace("tr","tɾ")
paso_r10 = paso_r9.replace("dr","dɾ")
paso_r11 = paso_r10.replace("fr","fɾ")
paso_r12 = paso_r11.replace("cr","kɾ")
paso_r13 = paso_r12.replace("cl", "kl")

# sustituye ERRES (2)
paso_rr2 = paso_r13.replace("00","r")

# sustituye EÑE
paso_ñ = paso_rr2.replace("ñ","ɲ")

# Borra H
paso_h = paso_ñ.replace("h","")
paso_coma = paso_h.replace(",","")
paso_pcoma = paso_coma.replace(";","")
paso_2punt = paso_pcoma.replace(";","")

# Escribe Ü como u
transcripcion_final = paso_2punt.replace("ü", "u")

# imprime resultado
print(transcripcion_final)

#########################################
#########################################
# El siguiente paso cambia t͡∫ por un solo
# caracter: "c" para efectos de contar los fonemas
paso_cuenta_fonemas = transcripcion_final.replace("t͡∫","c")
paso_cuenta_fonemas_1 = paso_cuenta_fonemas.replace(" ", "")
ene_de_fonemas = len(paso_cuenta_fonemas_1)
#########################################
#########################################
