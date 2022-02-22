integer = 11
float = 3.141
string = "Texto"

print("My Texto {:d}".format(integer))
print("My Texto {:b}".format(integer))
print("My Texto {:x}".format(integer))
print("My Texto {:f}".format(float))
print("My Texto {:s}".format(string))

string = "Mi nombre es {name} y tengo un {what}".format(
    name= "Andres",
    what="curso"
)

print(string)