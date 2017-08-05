# Este FOR servirá para ver dónde está el acento gráfico
# en la palabra.
# por el momento no se usa

#for b in lista_palabras:
#    print("8. ",b)

# comienza la separación silábica por la estructura

for i in lista_sec_cv:
    print(i)
    n_v = i.count("v")
    print(n_v, "sílabas")

    if n_v == 1:
        if i == "v":
            print("v")
        elif i == "cv": 
           print("cv")
        elif i == "vc":
           print("vc")
        elif i == "cvc": 
           print("cvc")
 ## con diptongo
        elif i == "0v": 
           print("0v")
        elif i == "v0": 
           print("v0")
        elif i == "0vc": 
           print("0vc")
        elif i == "c0v0": 
           print("c0v0")
        elif i == "0v0": 
           print("c0v0")
        elif i == "c1v": 
           print("c1v")
        elif i == "c1vc": 
           print("c1vc")
        elif i == "c1v0": 
           print("c1v0")   
        elif i == "c1v0c": 
           print("c1v0")
        elif i == "c0v":
           print("c0v")
        elif i == "c0vc":
           print("c0vc")
    elif n_v == 2:
# dos sílabas	
        if i == "vv":
            print("v v")
        elif i == "vvc":
            print("v vc")
        elif i == "cvv":
            print("cv v")
        elif i == "cvvc":
            print("cv vc")
# akai
        elif i == "vcv0":
            print("v cv0")
        elif i == "vcv0c":
            print("v cv0c")
# akia
        elif i == "vc0v":
            print("v c0v")
        elif i == "vc0vc":
            print("v c0vc")
# akra
        elif i == "vc1v":
            print("v c1v")
        elif i == "vc1vc":
            print("v c1vc")
# aika
        elif i == "v0cv":
            print("v0 cv")
        elif i == "v0cvc":
            print("v0 cvc")
# iaka
        elif i == "0vcv":
            print("0v cv")
        elif i == "0vcvc":
            print("0v cvc")
# iakai
        elif i == "0vcv0":
            print("0v cv0")
        elif i == "0vcv0c":
            print("0v cv0c")
# iakia
        elif i == "0vc0v":
            print("0v c0v")
        elif i == "0vc0vc":
            print("0v c0vc")
# aika
        elif i == "v0cv":
            print("v0 cv")
        elif i == "v0cvc":
            print("v0cvc")
# aikai
        elif i == "v0cv0":
            print("v0 cv0")
        elif i == "v0cv0c":
            print("v0 cv0c")
# aikia
        elif i == "v0c0v":
            print("v0 c0v")
        elif i == "v0c0v0c":
            print("v0 c0vc")
# kaka
        elif i == "cvcv":
            print("cv cv")
        elif i == "cvcvc":
            print("cv cvc")
# kansa
        elif i == "cvccv":
            print("cvc cv")
        elif i == "cvccvc":
            print("cvc cvc")
# kainsa
        elif i == "cv0ccv":
            print("cv0c cv")
        elif i == "cv0ccvc":
            print("cv0c cvc")
# kiansa
        elif i == "c0vccv":
            print("c0vc cv")
        elif i == "c0vccvc":
            print("c0vc cvc")
# kansai
# kansia
# kakai
        elif i == "cvcv0":
            print("cv cv0")
        elif i == "cvcv0c":
            print("cv cv0c")
# kakia
        elif i == "cvc0v":
            print("cv c0v")
        elif i == "cvc0vc":
            print("cv c0vc")
# kaika
        elif i == "cv0cv":
            print("cv0 cv")
        elif i == "cv0cvc":
            print("cv0 cvc")
# kiaka
        elif i == "c0vcv":
            print("c0v cv")
        elif i == "c0vcvc":
            print("c0v cvc")
# kiakai
        elif i == "c0vcv0":
            print("c0v cv0")
        elif i == "c0vcv0c":
            print("c0v cv0c")
# kiakia
        elif i == "c0vc0v":
            print("c0v c0v")
        elif i == "c0vc0vc":
            print("c0v c0vc")
# kaikai
        elif i == "cv0cv0":
            print("cv0 cv0")
        elif i == "cv0cv0c":
            print("cv0 cv0c")
# kaikia
        elif i == "cv0c0v":
            print("cv0 c0v")
        elif i == "cv0c0vc":
            print("cv0 c0vc")
# kleo
        elif i == "c1vv":
            print("c1v v")
        elif i == "c1vvc":
            print("c1v vc")
# klaka
        elif i == "c1vcv":
            print("c1v cv")
        elif i == "c1vcvc":
            print("c1v cvc")
# klakai
        elif i == "c1vcv0":
            print("c1v cv0")
        elif i == "c1vcv0c":
            print("c1v cv0c")
# klakia
        elif i == "c1vc0v":
            print("c1v c0v")
        elif i == "c1vc0vc":
            print("c1v c0vc")
# klaika
        elif i == "c1v0cv":
            print("c1v0 cv")
        elif i == "c1v0cvc":
            print("c1v0 cvc")
# kliaka
        elif i == "c10vcv":
            print("c10v cv")
        elif i == "c10vcvc":
            print("c10v cvc")
# kliakai
        elif i == "c10vcv0":
            print("c10v cv0")
        elif i == "c10vcv0c":
            print("c10v cv0c")
# kliakia
        elif i == "c10vc0v":
            print("c10v c0v")
        elif i == "c10vc0vc":
            print("c10v c0vc")
# klaika
        elif i == "c1v0cv":
            print("c1v0 cv")
        elif i == "c1v0cvc":
            print("c1v0 cvc")
# klaikai
        elif i == "c1v0cv0":
            print("c1v0 cv0")
        elif i == "c1v0cv0c":
            print("c1v0 cv0c")
# klaikia
        elif i == "c1v0c0v":
            print("c1v0 c0v")
        elif i == "c1v0c0vc":
            print("c1v0 c0vc")
# kakla
        elif i == "cvc1v":
            print("cv c1v")
        elif i == "cvc1vc":
            print("cv c1vc")
# kaklai
        elif i == "cvc1v0":
            print("cv c1v0")
        elif i == "cvc1v0c":
            print("cv c1v0c")
# kaklia
        elif i == "cvc10v":
            print("cv c10v")
        elif i == "cvc10vc":
            print("cv c10vc")
# kaikla
        elif i == "cv0c1v":
            print("cv0 c1v")
        elif i == "cv0c1vc":
            print("cv0 c1vc")
# kiakla
        elif i == "c0vc1v":
            print("c0v c1v")
        elif i == "c0vc1vc":
            print("c0v c1vc")
# kiaklai
        elif i == "c0vc1v0":
            print("c0v c1v0")
        elif i == "c0vc1v0c":
            print("c0v c1v0c")
# kiaklia
        elif i == "c0vc10v":
            print("c0v c10v")
        elif i == "c0vc10vc":
            print("c0v c10vc")
# kaikla
        elif i == "cv0c1v":
            print("cv0 c1v")
        elif i == "cv0c1vc":
            print("cv0 c1vc")
# kaiklai
        elif i == "cv0c1v0":
            print("cv0 c1v0")
        elif i == "cv0c1v0c":
            print("cv0 c1v0c")
# kaiklia
        elif i == "cv0c10v":
            print("cv0 c10v")
        elif i == "cv0c10vc":
            print("cv0 c10vc")
# klakia
        elif i == "c1vc0v":
            print("c1v c0v")
        elif i == "c1vc0vc":
            print("c1v c0vc")
# klakla
        elif i == "c1vc1v":
            print("c1v c1v")
        elif i == "c1vc1vc":
            print("c1v c1vc")
# klaklai
        elif i == "c1vc1v0":
            print("c1v c1v0")
        elif i == "c1vc1v0c":
            print("c1v c1v0c")
# klaklia
        elif i == "c1vc10v":
            print("c1v c10v")
        elif i == "c1vc10vc":
            print("c1v c10vc")
# klaikla
        elif i == "c1vc10v":
            print("c1v c10v")
        elif i == "c1vc10vc":
            print("c1v c10vc")
# kliakla
        elif i == "c1vc10v":
            print("c1v c10v")
        elif i == "c1vc10vc":
            print("c1v c10vc")
# kliaklai
        elif i == "c10vc1v0":
            print("c10v c1v0")
        elif i == "c10vc1v0c":
            print("c10v c1v0c")
# kliaklia
        elif i == "c10vc10v":
            print("c10v c10v")
        elif i == "c10vc10vc":
            print("c10v c10vc")
# klaikla
        elif i == "c1v0c1v":
            print("c1v0 c1v")
        elif i == "c1v0c1vc":
            print("c1v0 c1v")
# klaiklai
        elif i == "c1v0c1v0":
            print("c1v0 c1v0")
        elif i == "c1v0c1v0c":
            print("c1v0 c1v0c")
# klaiklia
        elif i == "c1v0c10v":
            print("c1v0 c10v")
        elif i == "c1v0c10vc":
            print("c1v0 c10vc")
# klanka
        elif i == "c1vccv":
            print("c1vc cv")
        elif i == "c1vccvc":
            print("c1vc cvc")
# klainka
        elif i == "c1v0ccv":
            print("c1v0c cv")
        elif i == "c1v0ccvc":
            print("c1v0c cvc")
# klankia
        elif i == "c1vcc0v":
            print("c1vc c0v")
        elif i == "c1vcc0vc":
            print("c1vc c0vc")
# klainklia
        elif i == "c1v0cc10v":
            print("c1v0c c10v")
        elif i == "c1v0cc10vc":
            print("c1v0c c10vc")
# kliankla
        elif i == "c10vcc1v":
            print("c1v0cc c1v")
        elif i == "c1v0cc1vc":
            print("c1v0c c1vc")
# kiankla
        elif i == "c0vcc1v":
            print("c0vc c1v")
        elif i == "c0vcb1vc":
            print("c0vc c1vc")
    elif n_v == 3:
        print("Es una palabra de",n_v,"sílabas")
        
