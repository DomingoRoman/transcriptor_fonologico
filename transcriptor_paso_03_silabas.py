#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silabificador.py
#  
#  Copyright 2017 Pedro Domingo Roman <historiadores@iMac-de-Pedro.local>
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
#  Parte de paso_c18 del tipo cvcvcvc cvcvcvc cvc cv cvcvcv

paso_c18 =("cv cv0cv cvc cvcv cvv cvvcv cv cv0cv")

lista_sec_cv = paso_c18.split()

# Llamar a la lista de palabras literales

lista_palabras = ('la', 'pieza', 'del', 'kine', 'sea', 'caera', 'de', 'cauco')

largo_lista_sec_cv =len(lista_sec_cv)

print(lista_sec_cv, "....", largo_lista_sec_cv)

for i in lista_sec_cv:
    print(i)

# dos sílabas	
# casa
    if i == "cvcv":
        print("cv cv")
# casas
    if i == "cvcvc":
        print("cv cvc")
# causa
    if i == "cv0cv":
        print("cv0 cv")
# causas
    if i == "cv0cvc":
        print("cv0 cvc")
# cuasa
    if i == "c0vcv":
        print("c0v cv")
# cuasas
    if i == "c0vcvc":
        print("c0v cvc")
# cuansa
    if i == "cv0ccv":
        print("cv0c cv")
# cuansas
    if i == "cv0ccvc":
        print("cv0c cvc")
# aa
    if i == "vv":
        print("v v")
    if i == "vvc":
        print("v vc")
 # cae       
    if i == "cvv":
        print("cv v")
    if i == "cvvc":
        print("cv vc")
#cansas
    if i == "cvccvc":
        print("cvc cvc")      
    if i == "cvccv":
        print("cvc cv")  
    if i == "ccvcv":
        print("ccv cv")
#clase
    if i == "ccvcv":
        print("ccv cv")
    if i == "ccvcvc":
        print("ccv cvc")
# *trampla *tracra*
    if i == "ccvcccv":
        print("ccvc ccv")
    if i == "ccvcccvc":
        print("ccvc ccvc")
# trampa trampas
     if i == "ccvccv":
        print("ccvc cv")
# trampa trampas
     if i == "ccvccvc":
        print("ccvc cvc")
# ala
    if i == "vcv":
        print("v cv")
# casio
    if i == "cvc0v":
        print("cv c0v")
# cautra
    if i == "cv0ccv":
        print("cv0c cv")   
    if i == "vcvc":
        print("v cvc")
    if i == "c0vccv":
        print("c0vc cv")	       
    if i == "c0vccvc":
        print("c0vc cvc")	       
# crueles
    if i == "cc0vcvc":
        print("cc0v cvc")
# siempre
    if i == "c0vcccv":
        print("c0vc ccvc")

# flaite
    if i == "ccv0cv":
        print("ccv0 cv") 
    if i == "ccv0cvc":
        print("ccv0 cvc")  
# coigüe
    if i == "cv0c0v":
        print("cv0 c0v")  
    if i == "cv0c0vc":
        print("cv0 cvc")
# abre
    if i == "vccvc":
        print("v ccvc")
    if i == "cv0c0vc":
        print("v ccvc")
