# Continúa del paso 01
#
#####################
######################
####
####  0 = semivocal o semiconsonante
####  1 = líquida combinada
####
## TRIPTONGOS
paso_tript_uai = paso_cuenta_fonemas.replace("uai", "0v0")
paso_tript_iai = paso_tript_uai.replace("iai", "0v0")
paso_tript_iei = paso_tript_iai.replace("iei", "0v0")
paso_tript_uau = paso_tript_iei.replace("uau", "0v0")
paso_tript_iau = paso_tript_uau.replace("iau", "0v0")
paso_tript_uei = paso_tript_iau.replace("uei", "0v0")

## DIPTONGOS
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
paso_dipt_oi = paso_dipt_ie.replace("oi", "v0")
paso_dipt_ue = paso_dipt_oi.replace("ue", "0v")
paso_dipt_uo = paso_dipt_ue.replace("uo", "0v")
paso_dipt_ua = paso_dipt_uo.replace("ua", "0v")

## VOCALES a "V"
paso_c0va = paso_dipt_ua.replace("a","v")
paso_c0ve = paso_c0va.replace("e","v")
paso_c0vi = paso_c0ve.replace("i","v")
paso_c0vo = paso_c0vi.replace("o","v")
paso_c0vu = paso_c0vo.replace("u","v")

# LÍQUIDAS
paso_liq_01 = paso_c0vu.replace("bɾ","c1")
paso_liq_02 = paso_liq_01.replace("bl","c1")
paso_liq_03 = paso_liq_02.replace("kɾ","c1")
paso_liq_04 = paso_liq_03.replace("kl","c1")
paso_liq_05 = paso_liq_04.replace("dɾ","c1")
paso_liq_06 = paso_liq_05.replace("fɾ","c1")
paso_liq_07 = paso_liq_06.replace("fl","c1")
paso_liq_08 = paso_liq_07.replace("gɾ","c1")
paso_liq_09 = paso_liq_08.replace("gl","c1")
paso_liq_10 = paso_liq_09.replace("pl","c1")
paso_liq_11 = paso_liq_10.replace("pɾ","c1")
paso_liq_12 = paso_liq_11.replace("tɾ","c1")
paso_liq_13 = paso_liq_12.replace("tl","c1")

# sustituye consonantes por C
paso_c01 = paso_liq_13.replace("b","c")
paso_c02 = paso_c01.replace("d","c")
paso_c03 = paso_c02.replace("f","c")
paso_c04 = paso_c03.replace("g","c")
paso_c05 = paso_c04.replace("x","c")
paso_c06 = paso_c05.replace("k","c")
paso_c07 = paso_c06.replace("l","c")
paso_c08 = paso_c07.replace("m","c")
paso_c09 = paso_c08.replace("n","c")
paso_c10 = paso_c09.replace("ɲ","c")
paso_c11 = paso_c10.replace("p","c")
paso_c12 = paso_c11.replace("ɾ","c")
paso_c13 = paso_c12.replace("s","c")
paso_c14 = paso_c13.replace("t","c")
paso_c15 = paso_c14.replace("ʝ","c")
paso_c16 = paso_c15.replace("r","c")

# Esta es la serie cv cv cv sobre la cual es hará la clasificación

print("1. Tiene", ene_de_fonemas, "fonemas")
print("2. Estructura silábica:", paso_c16)

lista_sec_cv = paso_c16.split()
largo_lista_sec_cv =len(lista_sec_cv)
