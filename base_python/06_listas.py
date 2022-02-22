


lista = [5,6,7,8,]  # elementos de la lista empiezan x 0, 1, 2
print(lista)

# le pasamos un index que queremos que muestre
print(lista[1])  # 6

# para eliminar un elemento de la lista
del lista[3]
print(lista) # [5, 6, 7]

# ######## metodo append() para agregar a la lista 
lista.append('string')
print(lista) # [5, 6, 7, 'string']

# ######## metodo remove() para borrar un elemento con su referencia 
lista.remove(7) 
print(lista)  # [5, 6, 'string']

# para que te diga el index 
print(lista.index(6))  # 1