def calcularScore(grade):
    if(grade >= 0.9 and score <= 1.00):
        grade = "Sobresaliente" 
    elif(grade >= 0.8 and score < 0.9):
        grade = "Notable"
    elif(grade >=0.7 and score < 0.8):
        grade = "Bien"
    elif(grade >= 0.6 and score < 0.7):
        grade = "Suficiente" 
    elif(grade <= 0 and score < 0.6):
        grade = "Insuficiente"
    else:
        grade = "Score no es valido"
    return grade
try:
    score = float(input("Ingreso su score (0.01 - 1.00): "))
    grade = calcularGrade(score)
    print("Su calificacion es: ", grade)
except:
    print("Su califacion: ", grade)