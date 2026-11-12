
positions = [1.2, 3.5, 2.1, 7.8, 4.6, 0.4, 8.3, 2.9]


def find_particle(positions, target):
    for i, elemento in enumerate(positions):
        if elemento == target:
            return i
    return -1



result = find_particle(positions, 4.6)

print(result)


#pregunta 1
#    pues en el peor de los casos buscara en todos en los elemetos de la lista por lo tanto recorrera los 1000 elementos por lo que hara 1000 comparaciones

#pregunta 2
#   si tenemos 1 000 000 particulas como estamos recorriendo toda la lista tendra una complejidad lineal  

#pregunta 3 
#   yo diria que si porque el ordenado es como un indice intrinseco? creo aun no estoy seguro de entender lo de ordenado