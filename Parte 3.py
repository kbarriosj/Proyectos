import math
def list_divide(a, b):
    c = []
    for i in range(len(a)):  # Aqui el ciclo debe ir hasta la cantidad de elementos del vector a
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
        initial_data = input().split(' ') # Aqui debes leer los datos y hacer un split por espacios
        n, m = int(initial_data[0]), int(initial_data[1])
    acum_ant, acum_a_ant = [], []
    for i in range(n):
        acum_ant.append(0)    # Aqui debes inicializar el vector en 0
        acum_a_ant.append(0)  # Aqui debes inicializar el vector en 0
    area_old = 16600 # Aqui debes asignar el valor del rango de las antenas previamente instaladas
    for i in range(m):
        ant_old = -1
        while ant_old < 0:
            input_data = input().split(' ')
            depart, area, ant_old, type_new = int(input_data[0]), float(input_data[1]), int(input_data[2]), input_data[3]
        if 0 < depart <= n:
            if type_new == 'a':  # Aqui debes realizar el calculo de las antenas de tipo a con su rango respectivo
                acum_a_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 50600))
                acum_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 50600))
            elif type_new ==  'b':  # Aqui debes verificar que el tipo de antena nueva sea 'b'
                acum_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 19200))
            elif type_new == 'c':  # Aqui debes verificar que el tipo de antena nueva sea 'c'
                acum_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 36900))
            elif type_new == 'd':
                acum_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 40500))  # Aqui debes realizar el calculo de las antenas de tipo d con su rango respectivo
            elif type_new == 'e':
                acum_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 34200))  # Aqui debes realizar el calculo de las antenas de tipo e con su rango respectivo
    
    
    min_, index_min = get_elem_index(acum_ant, elem='min')
    max_, index_max = get_elem_index(acum_ant, elem='max')
    print(index_min + 1, min_)
    print(index_max + 1, max_)
    
    porc_a_ant = list_divide(acum_a_ant, acum_ant)  # Aqui debes dividir la listas que acumula las antenas de tipo 'a' sobre la lista que acumula todas las antenas 
    for i in range(n):
        print('{:} {:.2f}%'.format(i + 1, porc_a_ant[i] * 100))
if __name__ == "__main__":
    main()