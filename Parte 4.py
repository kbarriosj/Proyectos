import math

def convert_type_to_int(type_):
    type_list = ['a', 'b', 'c', 'd', 'e']
    return type_list.index(type_)
def list_divide(a, b):
    c = []
    for i in range(len(a)): # Aqui el ciclo debe ir hasta la cantidad de elementos del vector a
        c.append(0) if b[i] == 0 else c.append(a[i] / b[i])
    return c
def get_elem_index(a, elem=None):
    if elem == 'min':
        return min(a), a.index(min(a))
    elif elem == 'max':
        return max(a), a.index(max(a))
    else:
        return elem, a.index(elem)
def main():
    n = 0
    while n < 1:
        initial_data = input().split(' ')  # Aqui debes leer los datos y hacer un split por espacios
        n, m = int(initial_data[0]), int(initial_data[1])
    acum_type_ant = [] # Aqui debes declarar un vector / lista vacio
    for i in range(n):  # Aqui el ciclo debe ir hasta la cantidad de departamentos (n)
        acum_type_ant.append([0 for i in range(5)])
    area_old = 16600 # Aqui debes asignar el valor del rango de las antenas previamente instaladas
    for i in range(m):  # Aqui el ciclo debe ir hasta la cantidad de terrenos a analizar (m)
        ant_old = -1
        while ant_old < 0:
            input_data = input().split(' ')
            depart, area, ant_old, type_new = int(input_data[0]), float(input_data[1]), int(input_data[2]), input_data[3]
        if 0 < depart <= n:
            if type_new == 'a':  # Aqui debes verificar que el tipo de antena nueva sea 'a'
                acum_type_ant[depart - 1][convert_type_to_int(type_new)] += max(0, math.ceil((area - area_old * ant_old) / 50600))  # Aqui debes realizar el calculo de las antenas de tipo a con su rango respectivo
            elif type_new == 'b':
                acum_type_ant[depart - 1][convert_type_to_int(type_new)] += max(0, math.ceil((area - area_old * ant_old) / 19200))  # Aqui debes realizar el calculo de las antenas de tipo b con su rango respectivo
            elif type_new == 'c':  # Aqui debes verificar que el tipo de antena nueva sea 'c'
                acum_type_ant[depart - 1][convert_type_to_int(type_new)] += max(0, math.ceil((area - area_old * ant_old) / 36900))  # Aqui debes realizar el calculo de las antenas de tipo c con su rango respectivo
            elif type_new == 'd':  # Aqui debes verificar que el tipo de antena nueva sea 'd'
                acum_type_ant[depart - 1][convert_type_to_int(type_new)] += max(0, math.ceil((area - area_old * ant_old) / 40500))
            elif type_new == 'e':
                acum_type_ant[depart - 1][convert_type_to_int(type_new)] += max(0, math.ceil((area - area_old * ant_old) / 34200))  # Aqui debes realizar el calculo de las antenas de tipo e con su rango respectivo
    types = ['a', 'b', 'c', 'd', 'e']
    for i in range(n):  # Aqui el ciclo debe ir hasta la cantidad de departamentos (n)
        min_, index_min = get_elem_index(acum_type_ant[i], elem='min')
        max_, index_max = get_elem_index(acum_type_ant[i], elem='max')
        print(i + 1)
        print(sum(acum_type_ant[i]))  # Aqui se debe sumar los valores del vector acum_type_ant en la posicion i
        print(types[index_min], min_)
        print(types[index_max], max_)
    for i in range(len(types)):  # Aqui el ciclo debe ir hasta la cantidad de elementos del vector types
        actual_type = [t_ant[i] for t_ant in acum_type_ant]
        min_, index_min = get_elem_index(actual_type, elem='min')
        max_, index_max = get_elem_index(actual_type, elem='max')
        print(index_min + 1, types[i], min_)
        print(index_max + 1, types[i], max_)
        
if __name__ == "__main__":
    main()