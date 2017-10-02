## --- PASO 2---
######################
####. Las I y las U se convierten en "v".
####  0 = semivocal o semiconsonante
####  1 = líquida combinada
####

# Separación silábica de la cadena sin espacios
# Punto de partida:::: s_e_transcripcion_final_ipa_pausas

## Estructuras silábicas con triptongos
s_e_paso_tript_uai = s_e_transcripcion_final_ipa_pausas.replace("uai", "0v0")
s_e_paso_tript_iai = s_e_paso_tript_uai.replace("iai", "0v0")
s_e_paso_tript_iei = s_e_paso_tript_iai.replace("iei", "0v0")
s_e_paso_tript_uau = s_e_paso_tript_iei.replace("uau", "0v0")
s_e_paso_tript_iau = s_e_paso_tript_uau.replace("iau", "0v0")
s_e_paso_tript_uei = s_e_paso_tript_iau.replace("uei", "0v0")

## Estructuras silábicas con diptongos
s_e_paso_dipt_ui = s_e_paso_tript_uei.replace("ui", "v0")
s_e_paso_dipt_iu = s_e_paso_dipt_ui.replace("iu", "v0")
s_e_paso_dipt_ai = s_e_paso_dipt_iu.replace("ai", "v0")
s_e_paso_dipt_ei = s_e_paso_dipt_ai.replace("ei", "v0")
s_e_paso_dipt_oi = s_e_paso_dipt_ei.replace("ei", "v0")
s_e_paso_dipt_au = s_e_paso_dipt_oi.replace("au", "v0")
s_e_paso_dipt_eu = s_e_paso_dipt_au.replace("eu", "v0")
s_e_paso_dipt_ia = s_e_paso_dipt_eu.replace("ia", "0v")
s_e_paso_dipt_ie = s_e_paso_dipt_ia.replace("ie", "0v")
s_e_paso_dipt_io = s_e_paso_dipt_ie.replace("io", "0v")
s_e_paso_dipt_oi = s_e_paso_dipt_io.replace("oi", "v0")
s_e_paso_dipt_ou = s_e_paso_dipt_oi.replace("ou", "v0")
s_e_paso_dipt_ue = s_e_paso_dipt_ou.replace("ue", "0v")
s_e_paso_dipt_uo = s_e_paso_dipt_ue.replace("uo", "0v")
s_e_paso_dipt_ua = s_e_paso_dipt_uo.replace("ua", "0v")

## VOCALES a "V"
s_e_paso_c0va = s_e_paso_dipt_ua.replace("a","v")
s_e_paso_c0ve = s_e_paso_c0va.replace("e","v")
s_e_paso_c0vi = s_e_paso_c0ve.replace("i","v")
s_e_paso_c0vo = s_e_paso_c0vi.replace("o","v")
s_e_paso_c0vu = s_e_paso_c0vo.replace("u","v")

# LÍQUIDAS
s_e_paso_liq_01 = s_e_paso_c0vu.replace("bɾ","c1")
s_e_paso_liq_02 = s_e_paso_liq_01.replace("bl","c1")
s_e_paso_liq_03 = s_e_paso_liq_02.replace("kɾ","c1")
s_e_paso_liq_04 = s_e_paso_liq_03.replace("kl","c1")
s_e_paso_liq_05 = s_e_paso_liq_04.replace("dɾ","c1")
s_e_paso_liq_06 = s_e_paso_liq_05.replace("fɾ","c1")
s_e_paso_liq_07 = s_e_paso_liq_06.replace("fl","c1")
s_e_paso_liq_08 = s_e_paso_liq_07.replace("gɾ","c1")
s_e_paso_liq_09 = s_e_paso_liq_08.replace("gl","c1")
s_e_paso_liq_10 = s_e_paso_liq_09.replace("pl","c1")
s_e_paso_liq_11 = s_e_paso_liq_10.replace("pɾ","c1")
s_e_paso_liq_12 = s_e_paso_liq_11.replace("tɾ","c1")
s_e_paso_liq_13 = s_e_paso_liq_12.replace("tl","c1")

# sustituye consonantes por C
s_e_paso_c01 = s_e_paso_liq_13.replace("b","c")
s_e_paso_c02 = s_e_paso_c01.replace("d","c")
s_e_paso_c03 = s_e_paso_c02.replace("f","c")
s_e_paso_c04 = s_e_paso_c03.replace("g","c")
s_e_paso_c05 = s_e_paso_c04.replace("x","c")
s_e_paso_c06 = s_e_paso_c05.replace("k","c")
s_e_paso_c07 = s_e_paso_c06.replace("l","c")
s_e_paso_c08 = s_e_paso_c07.replace("m","c")
s_e_paso_c09 = s_e_paso_c08.replace("n","c")
s_e_paso_c10 = s_e_paso_c09.replace("ɲ","c")
s_e_paso_c11 = s_e_paso_c10.replace("p","c")
s_e_paso_c12 = s_e_paso_c11.replace("ɾ","c")
s_e_paso_c13 = s_e_paso_c12.replace("s","c")
s_e_paso_c14 = s_e_paso_c13.replace("t","c")
s_e_paso_c15 = s_e_paso_c14.replace("ʝ","c")
s_e_paso_c16 = s_e_paso_c15.replace("I","v")
s_e_paso_c17 = s_e_paso_c16.replace("U","v")

s_e_estructura_silabica_palabras = paso_c17.replace("r","c")

transcripcion_final_ipa_pausas = transcripcion_final_ipa_pausas.replace("I", "i")
transcripcion_final_ipa_pausas = transcripcion_final_ipa_pausas.replace("U", "u")

transcripcion_final_c = transcripcion_final_c.replace("I", "i")
transcripcion_final_c = transcripcion_final_c.replace("U", "u")

estructura_silabica_cadena = estructura_silabica_palabras.replace(" ","")

print(transcripcion_final_ipa_pausas)
print(transcripcion_final_c)
print(estructura_silabica_palabras)
print(estructura_silabica_cadena)





# Estas son las dos series cv cv cv sobre las cuales se hará la separación silábica
