

string = '''
Esto es un texto, comillas multiples 
... :)
'''
# ######## metodo replace()  reemplaza texto
string = string.replace('Esto', 'Aquello')
print(string)

# ######## metodo count() cuenta lo q le pases en ()
print(string.count('a'))

# ######## format() para dar formato a concatenaciones
integer = 11
float = 3.14159265358979
string ="texto"

# formato que le damos {:d} (significa numerico)
print("my texto numerico{:d}".format(integer))
# formato que le damos {:x} (significa hexadecimal)
print("my texto hexadecimal {:x}".format(integer))
# formato que le damos {:b} (significa binario)
print("my texto binario{:b}".format(integer))
# formato que le damos {:f} (significa nº flotante)
print("my texto flotante {:f}".format(float))
# formato que le damos {:s} (significa string)
print("my texto string{:s}".format(string))

# otra forma de concatenar:
print("Mi nombre es {name} y tengo un {what}".format(
    name= "Aroa",
    what= "curso"
))

# igualmente se puede hacer asi
string = "Mi nombre es {name} y tengo un {what}".format(
    name= "Aroa",
    what= "curso"
)
print(string)

