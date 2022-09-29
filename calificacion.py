def calcularGrade(score):
    if(score >= 0.9 and score <= 1.0):
        grade = "sobresaliente"
    elif(score >= 0.8 and score < 0.9):
        grade = "Notable"
    elif(score >= 0.7 and score < 0.8):
        grade = "Bien"
    elif(score >= 0.6 and score < 0.7):
        grade = "Suficiente"
    elif(score >= 0 and score < 0.6):
        grade = "Insuficiente"
    else:
        grade = "Score no es valido"
    return grade 
try:
    score = float(input("Ingrese su score(0.01 - 1.0): "))
    grade = calcularGrade(score)
    print("Su calificacion es: ", grade)
except: 
    print("Error, debe ingresar un valor numerico")
    