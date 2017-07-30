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

paso_c16 =("cv cv0cv cvc cvcv cvv cvvcv cv cv0cv")

lista_sec_cv = paso_c17.split()

# Llamar a la lista de palabras literales

lista_palabras = ('la', 'pieza', 'del', 'kine', 'sea', 'caera', 'de', 'cauco')

largo_lista_sec_cv =len(lista_sec_cv)

print(lista_sec_cv, "....", largo_lista_sec_cv)


# Esta es la serie cv cv cv sobre la cual es hará la clasificación


for b in lista_palabras:
    print("8. ",b)

for i in lista_sec_cv:
    print(i)

# dos sílabas	
# aka
if i == "vv":
    print("v v")
if i == "vvc":
    print("v vc")
# akai
if i == "vcv0":
    print("v cv0")
if i == "vcv0c":
    print("v cv0c")
# akia
if i == "vc0v":
    print("v c0v")
if i == "vc0vc":
    print("v c0vc")
# aika
if i == "v0cv":
    print("v0 cv")
if i == "v0cvc":
    print("v0 cvc")
# iaka
if i == "0vcv":
    print("0v cv")
if i == "0vcvc":
    print("0v cvc")
# iakai
if i == "0vcv0":
    print("0v cv0")
if i == "0vcv0c":
    print("0v cv0c")
# iakia
if i == "0vc0v":
    print("0v c0v")
if i == "0vc0vc":
    print("0v c0vc")
# aika
if i == "v0cv":
    print("v0 cv")
if i == "v0cvc":
    print("v0cvc")
# aikai
if i == "v0cv0":
    print("v0 cv0")
if i == "v0cv0c":
    print("v0 cv0c")
# aikia
if i == "v0c0v":
    print("v0 c0v")
if i == "v0c0v0c":
    print("v0 c0vc")
# kaka
if i == "cvcv":
    print("cv cv")
if i == "cvcvc":
    print("cv cvc")
# kakai
if i == "cvcv0":
    print("cv cv0")
if i == "cvcv0c":
    print("cv cv0c")
# kakia
if i == "cvc0v":
    print("cv c0v")
if i == "cvc0vc":
    print("cv c0vc")
# kaika
if i == "cv0cv":
    print("cv0 cv")
if i == "cv0cvc":
    print("cv0 cvc")
# kiaka
if i == "c0vcv":
    print("c0v cv")
if i == "c0vcvc":
    print("c0v cvc")
# kiakai
if i == "c0vcv0":
    print("c0v cv0")
if i == "c0vcv0c":
    print("c0v cv0c")
# kiakia
if i == "c0vc0v":
    print("c0v c0v")
if i == "c0vc0vc":
    print("c0v c0vc")
# kaika
if i == "cv0cv":
    print("cv0 cv")
if i == "cv0cvc":
    print("cv0 cvc")
# kaikai
if i == "cv0cv0":
    print("cv0 cv0")
if i == "cv0cv0c":
    print("cv0 cv0c")
# kaikia
if i == "cv0c0v":
    print("cv0 c0v")
if i == "cv0c0vc":
    print("cv0 c0vc")
# klaka
if i == "c1vcv":
    print("c1v cv")
if i == "c1vcvc":
    print("c1v cvc")
# klakai
if i == "c1vcv0":
    print("c1v cv0")
if i == "c1vcv0c":
    print("c1v cv0c")
# klakia
if i == "c1vc0v":
    print("c1v c0v")
if i == "c1vc0vc":
    print("c1v c0vc")
# klaika
if i == "c1v0cv":
    print("c1v0 cv")
if i == "c1v0cvc":
    print("c1v0 cvc")
# kliaka
if i == "c10vcv":
    print("c10v cv")
if i == "c10vcvc":
    print("c10v cvc")
# kliakai
if i == "c10vcv0":
    print("c10v cv0")
if i == "c10vcv0c":
    print("c10v cv0c")
# kliakia
if i == "c10vc0v":
    print("c10v c0v")
if i == "c10vc0vc":
    print("c10v c0vc")
# klaika
if i == "c1v0cv":
    print("c1v0 cv")
if i == "c1v0cvc":
    print("c1v0 cvc")
# klaikai
if i == "c1v0cv0":
    print("c1v0 cv0")
if i == "c1v0cv0c":
    print("c1v0 cv0c")
# klaikia
if i == "c1v0c0v":
    print("c1v0 c0v")
if i == "c1v0c0vc":
    print("c1v0 c0vc")
# kakla
if i == "cvc1v":
    print("cv c1v")
if i == "cvc1vc":
    print("cv c1vc")
# kaklai
if i == "cvc1v0":
    print("cv c1v0")
if i == "cvc1v0c":
    print("cv c1v0c")
# kaklia
if i == "cvc10v":
    print("cv c10v")
if i == "cvc10vc":
    print("cv c10vc")
# kaikla
if i == "cv0c1v":
    print("cv0 c1v")
if i == "cv0c1vc":
    print("cv0 c1vc")
# kiakla
if i == "c0vc1v":
    print("c0v c1v")
if i == "c0vc1vc":
    print("c0v c1vc")
# kiaklai
if i == "c0vc1v0":
    print("c0v c1v0")
if i == "c0vc1v0c":
    print("c0v c1v0c")
# kiaklia
if i == "c0vc10v":
    print("c0v c10v")
if i == "c0vc10vc":
    print("c0v c10vc")
# kaikla
if i == "cv0c1v":
    print("cv0 c1v")
if i == "cv0c1vc":
    print("cv0 c1vc")
# kaiklai
if i == "cv0c1v0":
    print("cv0 c1v0")
if i == "cv0c1v0c":
    print("cv0 c1v0c")
# kaiklia
if i == "cv0c10v":
    print("cv0 c10v")
if i == "cv0c10vc":
    print("cv0 c10vc")
# klakla
if i == "c1vc1v":
    print("c1v c1v")
if i == "c1vc1vc":
    print("c1v c1vc")
# klaklai
if i == "c1vc1v0":
    print("c1v c1v0")
if i == "c1vc1v0c":
    print("c1v c1v0c")
# klaklia
if i == "c1vc10v":
    print("c1v c10v")
if i == "c1vc10vc":
    print("c1v c10vc")
# klaikla
if i == "c1vc10v":
    print("c1v c10v")
if i == "c1vc10vc":
    print("c1v c10vc")
# kliakla
if i == "c1vc10v":
    print("c1v c10v")
if i == "c1vc10vc":
    print("c1v c10vc")
# kliaklai
if i == "c10vc1v0":
    print("c10v c1v0")
if i == "c10vc1v0c":
    print("c10v c1v0c")
# kliaklia
if i == "c10vc10v":
    print("c10v c10v")
if i == "c10vc10vc":
    print("c10v c10vc")
# klaikla
if i == "c1v0c1v":
    print("c1v0 c1v")
if i == "c1v0c1vc":
    print("c1v0 c1v")
# klaiklai
if i == "c1v0c1v0":
    print("c1v0 c1v0")
if i == "c1v0c1v0c":
    print("c1v0 c1v0c")
# klaiklia
if i == "c1v0c10v":
    print("c1v0 c10v")
if i == "c1v0c10vc":
    print("c1v0 c10vc")
