p = input ("Escribe una palabra: ")
v=0
for l in p.lower():
    if l in "aeiou":
        v +=1
print ("Tines", v,"vocales")

