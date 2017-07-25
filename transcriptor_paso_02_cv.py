#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pru2.py
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
#  

paso_c0 = "derecos sediendos puel el gueito de tuelno"
## triptongos

paso_tript_uai = paso_c0.replace("uai", "0v0")
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
paso_dipt_ue = paso_dipt_io.replace("ue", "0v")
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
print(paso_c18)
