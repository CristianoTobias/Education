frase = "Curso em Video Python"
#fatiamento
print(frase)
print(len(frase))
print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(frase[::-1])
#Análise
print(frase.count("o"))
print(frase.count("o", 0, 13))
print(frase.find("deo"))
print(frase.find("android"))
print( "Curso" in frase)
print(frase.replace("Python", "Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase = "  Aprenda Python   "
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
#Divisão
frase = "Curso em Video Python"
print(frase.split())
#Junção
print("-".join(frase.split()))






