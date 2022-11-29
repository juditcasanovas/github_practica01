def corona(): # 10 Judit C
    print("Càlcul de l'àrea i del perímetre d'una corona circular ")
    R = float(input("Radi major = "))
    r = float(input("radi menor = "))
    area = PI * (R*R - r*r)
    perimetre = 2 * PI * (R + r)
    return area, perimetre