from math import ceil, sqrt
from os import path
def read_file(path):
    data = []
    with open(path, 'r') as f:
        i = 0
        for line in f.readlines():
            if i != 0:
                line = line.split(',')  # Aqui debes realizar el split por comas (,)
                line[0], line[2], line[3], line[4] = int(line[0]), float(line[2]), int(line[3]), line[4][0]
                data.append(line)  # Aqui debes añadir la linea (line) a la lista data
            i += 1
    return data
def filter_by_id(data, id_):
    filter_data = []
    for d in data:
        if d[0] == id_:
            filter_data.append(d)
    return filter_data
def mean(data):
    return sum(data) / len(data) # Aqui debes dividir entre la cantidad de elementos del vector data
def std(data):
    mean = sum(data) / len(data)  # Aqui debes dividir entre la cantidad de elementos del vector data
    return sqrt((sum(list(map(lambda x: (x - mean) ** 2, data)))) / (len(data) - 1))
def main():
    data = read_file('data.csv')  # Aqui debes colocar el nombre del archivo csv que contiene los datos
    ids = list(set(list(map(lambda x: int(x), input().split(' ')))))
    ids.sort()
    area_old = 16600 # Aqui debes asignar el valor del rango de las antenas previamente instaladas
    
    for id_ in ids:
        depart_data = filter_by_id(data, id_)
        
        acum_type_ant = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0
        }
        
        varea, vant_old, vtype_new = [d[2] for d in depart_data], [d[3] for d in depart_data], [d[4] for d in depart_data]
        for i in range(len(varea)):  # Aqui el ciclo debe ir hasta la cantidad de elementos del vector varea
            area, ant_old, type_new = varea[i], vant_old[i], vtype_new[i]
            if type_new == 'a':
                acum_type_ant[type_new] += max(0, ceil((area - area_old * ant_old) / 50600))  # Aqui debes realizar el calculo de las antenas de tipo a con su rango respectivo
            elif type_new == 'b':  # Aqui debes verificar que el tipo de antena nueva sea 'b'
                acum_type_ant[type_new] += max(0, ceil((area - area_old * ant_old) / 19200))
            elif type_new == 'c':
                acum_type_ant[type_new] += max(0, ceil((area - area_old * ant_old) / 36900))  # Aqui debes realizar el calculo de las antenas de tipo a con su rango respectivo
            elif type_new == 'd':  # Aqui debes verificar que el tipo de antena nueva sea 'd'
                acum_type_ant[type_new] += max(0, ceil((area - area_old * ant_old) / 40500))  # Aqui debes realizar el calculo de las antenas de tipo a con su rango respectivo
            elif type_new == 'e':  # Aqui debes verificar que el tipo de antena nueva sea 'e'
                acum_type_ant[type_new] += max(0, ceil((area - area_old * ant_old) / 34200))  # Aqui debes realizar el calculo de las antenas de tipo a con su rango respectivo
                
        print(id_, depart_data[0][1])
        print('terrain area')
        print('mean {:.2f}'.format(mean(varea)))
        print('std {:.2f}'.format(std(varea)))
        print('min {:.2f}'.format(min(varea)))  # Aqui debes obtener el valor minimo del vector varea
        print('max {:.2f}'.format(max(varea)))
        print('total {:.2f}'.format(sum(varea)))
        
        print('old antenna')
        print('mean {:.2f}'.format(mean(vant_old)))
        print('std {:.2f}'.format(std(vant_old)))
        print('min {:.0f}'.format(min(vant_old)))
        print('max {:.0f}'.format(max(vant_old)))  # Aqui debes obtener el valor maximo del vector vant_old
        print('total {:.0f}'.format(sum(vant_old)))  # Aqui debes obtener la suma de todos los valores del vector vant_old
        
        print('new antenna')
        print('a {:}'.format(acum_type_ant['a']))
        print('b {:}'.format(acum_type_ant['b']))  # Aqui debes mostrar la informacion que hay en acum_type_ant en la posicion 'b'
        print('c {:}'.format(acum_type_ant['c']))  # Aqui debes mostrar la informacion que hay en acum_type_ant en la posicion 'c'
        print('d {:}'.format(acum_type_ant['d']))
        print('e {:}'.format(acum_type_ant['e']))  # Aqui debes mostrar la informacion que hay en acum_type_ant en la posicion 'e'
        
if __name__ == "__main__":
    main()