def edad():
    year=int(input("ingrese el año en curso;"))
    persona_1=list()
    persona_2=list()
    persona_3=list()
    persona_1.append(input("ingrese nombre de la persona:"))
    persona_1.append(int(input("ingrese año de nacimiento de la persona:")))
    persona_2.append(input("ingrese nombre de la persona:"))
    persona_2.append(int(input("ingrese año de nacimiento de la persona:")))
    persona_3.append(input("ingrese nombre de la persona:"))
    persona_3.append(int(input("ingrese año de nacimiento de la persona:")))
    persona_1.append(year-persona_1[1])
    persona_2.append(year-persona_2[1])
    persona_3.append(year-persona_3[1])
    print(persona_1,persona_2,persona_3)
edad()
        