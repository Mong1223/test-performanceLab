# python .\task2\task2.py .\task2\center.txt .\task2\coord.txt

"""
Напишите программу, которая рассчитывает положение точки относительно
окружности.
Координаты центра окружности и его радиус считываются из файла 1.
    Пример:
    1 1
    5
Координаты точек считываются из файла 2.
    Пример:
    0 0
    1 6
    6 6
Вывод для данных примеров файлов:
    1
    0
    2
файл с координатами и радиусом окружности - 1 аргумент;
    ● файл с координатами точек - 2 аргумент;
    ● координаты - рациональные числа в диапазоне от 10^-38 до 10^38;
    ● количество точек от 1 до 100;
    ● вывод каждого положения точки заканчивается символом новой строки;
    ● соответствия ответов:
        ○ 0 - точка лежит на окружности
        ○ 1 - точка внутри
        ○ 2 - точка снаружи
"""

import sys


def check_point(center, points):
    r = center[1][0]
    result = []
    for point in points:
        distance_squared = (point[0] - center[0][0]) ** 2 + (point[1] - center[0][1]) ** 2
        if distance_squared == r * r:
            result.append(0)
        elif distance_squared > r * r:
            result.append(2)
        elif distance_squared < r * r:
            result.append(1)
    return result


def read_circle(cicle_f, coords_f):
    try:
        center = []
        with open(cicle_f, 'r') as f:
            line = f.readline().replace('\n', '')
            while line:
                center.append(list(map(int, line.split())))
                line = f.readline().replace('\n', '')
        f.close()

        coord = []
        with open(coords_f, 'r') as f:
            line = f.readline().replace('\n', '')
            while line:
                coord.append(list(map(int, line.split())))
                line = f.readline().replace('\n', '')
        f.close()
        return center, coord
    except FileNotFoundError:
        print("Ошибка: один или оба файла не найдены.")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Использование: python script.py <file1> <file2>")
        sys.exit(1)

    try:
        center_f = sys.argv[1]
        points_f = sys.argv[2]
        center_data, coord_data = read_circle(center_f, points_f)
        print(*check_point(center_data, coord_data), sep='\n')

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        sys.exit(1)
