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

# sustituye CH por t͡∫
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

# sustituye ERRES (2)
paso_rr2 = paso_r12.replace("00","r")

# sustituye EÑE
paso_ñ = paso_rr2.replace("ñ","ɲ")

# Borra H
paso_h = paso_ñ.replace("h","")
paso_coma = paso_h.replace(",","")
paso_pcoma = paso_coma.replace(";","")
paso_2punt = paso_pcoma.replace(";","")

# Escribe Ü como u
paso_u_cre = paso_2punt.replace("ü", "u")

#########################################
# El siguiente paso cambia t͡∫ por un solo
# caracter: c
# para efectos de contar los fonemas
paso_cuenta_fonemas = paso_u_cre.replace("t͡∫","c")
paso_cuenta_fonemas_1 = paso_cuenta_fonemas.replace(" ", "")

ene_de_fonemas = len(paso_cuenta_fonemas_1)

#####################
######################
####
####
paso_tript_uai = paso_cuenta_fonemas.replace("uai", "0v0")
paso_tript_iai = paso_tript_uai.replace("iai", "0v0")
paso_tript_iei = paso_tript_iai.replace("iei", "0v0")
paso_tript_uau = paso_tript_iei.replace("uau", "0v0")
paso_tript_iau = paso_tript_uau.replace("iau", "0v0")
paso_tript_uei = paso_tript_iau.replace("uei", "0v0")

## diptongos

paso_dipt_ui = paso_tript_uei.replace("ui", "v0")
paso_dipt_iu = paso_dipt_ui.replace("iu", "v0")
paso_dipt_ai = paso_dipt_iu.replace("ai", "v0")
paso_dipt_ei = paso_dipt_ai.replace("ei", "v0")
paso_dipt_oi = paso_dipt_ei.replace("ei", "v0")
paso_dipt_au = paso_dipt_oi.replace("au", "v0")
paso_dipt_eu = paso_dipt_au.replace("eu", "v0")
paso_dipt_ia = paso_dipt_eu.replace("ia", "0v")
paso_dipt_ie = paso_dipt_ia.replace("ie", "0v")
paso_dipt_io = paso_dipt_ie.replace("io", "0v")
# coigüe
paso_dipt_oi = paso_dipt_ie.replace("oi", "v0")
paso_dipt_ue = paso_dipt_oi.replace("ue", "0v")
paso_dipt_uo = paso_dipt_ue.replace("uo", "0v")
paso_dipt_ua = paso_dipt_uo.replace("ua", "0v")

paso_c0va = paso_dipt_ua.replace("a","v")
paso_c0ve = paso_c0va.replace("e","v")
paso_c0vi = paso_c0ve.replace("i","v")
paso_c0vo = paso_c0vi.replace("o","v")
paso_c0vu = paso_c0vo.replace("u","v")

# sustituye consonantes por C
paso_c01 = paso_c0vu.replace("b","c")
paso_c02 = paso_c01.replace("c","c")
paso_c03 = paso_c02.replace("d","c")
paso_c04 = paso_c03.replace("f","c")
paso_c05 = paso_c04.replace("g","c")
paso_c06 = paso_c05.replace("x","c")
paso_c07 = paso_c06.replace("k","c")
paso_c08 = paso_c07.replace("l","c")
paso_c09 = paso_c08.replace("m","c")
paso_c10 = paso_c09.replace("n","c")
paso_c11 = paso_c10.replace("ɲ","c")
paso_c12 = paso_c11.replace("p","c")
paso_c13 = paso_c12.replace("ɾ","c")
paso_c14 = paso_c13.replace("s","c")
paso_c15 = paso_c14.replace("t","c")
paso_c16 = paso_c15.replace("ʝ","c")
paso_c17 = paso_c16.replace("r","c")

# Esta es la serie cv cv cv sobre la cual es hará la clasificación
print(paso_u_cre)
print(paso_c17)
print(paso_cuenta_fonemas)
print(ene_de_fonemas)
print(lista_palabras,":  ", n_palabras-1)


lista_sec_cv = paso_c17.split()
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
# aas
    if i == "vvc":
        print("v vc")
        
    if i == "cvv":
        print("cv v")

    if i == "cvvc":
        print("cv vc")

    if i == "cvccvc":
        print("cvc cvc")      

    if i == "ccvcv":
        print("ccv cv")

    if i == "ccvcv":
        print("ccv cv")

    if i == "ccvcvc":
        print("ccv cvc")

# trampa tracra*
    if i == "ccvccv":
        print("ccv ccv")

    if i == "vcv":
        print("v cv")

# trenza y troglo*
    if i == "ccvccv":
        print("ccvc cv")

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

# cerdo
    if i == "cvccv":
        print("cc0v cvc")

# siempre
    if i == "c0vcccv":
        print("c0vc ccvc")

# flaite
    if i == "ccv0cv":
        print("ccv0 cv") 

# flaites
    if i == "ccv0cvc":
        print("ccv0 cvc")  
# coigüe
    if i == "cv0c0v":
        print("cv0 c0v")  
# coigües
    if i == "cv0c0vc":
        print("cv0 cvc")
