o#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  secuenciador_cv.py
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
#  Convierte una entrada transdcrita fonológicamente en serie de cv
#  según sea consonante o vocal el tipo de segmento
#
#  El punto de partida es "paso_c0" del transcriptor fonológico

## sustituye vocales por V
paso_c0 = "derecos sediendos pol el gueito de tulno"
## diptongos y triptongos

paso_tript_uai = paso_c0.replace("uai", "0v0")
paso_tript_iai = paso_tript_uai.replace("iai", "0v0")
paso_tript_iei = paso_tript_iai.replace("iei", "0v0")
paso_tript_uau = paso_tript_iei.replace("uau", "0v0")
paso_tript_iau = paso_tript_uau.replace("iau", "0v0")
paso_tript_uei = paso_tript_iau.replace("uei", "0v0")

paso_c0va = paso_tript_uei.replace("a","v")
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
paso_c18 = paso_c17.replace("c","c")

# Esta es la serie cv cv cv sobre la cual es hará la clasificación

print(paso_c18)
