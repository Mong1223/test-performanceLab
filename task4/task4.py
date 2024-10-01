import sys

# python .\task4\task4.py .\task4\data.txt

"""
Дан массив целых чисел nums.
Напишите программу, выводящую минимальное количество ходов, требуемых для
приведения всех элементов к одному числу.
За один ход можно уменьшить или увеличить число массива на 1.
Пример:
nums = [1, 2, 3]
Решение: [1, 2, 3] => [2, 2, 3] => [2, 2, 2].
Минимальное количество ходов: 2.

"""


def func(arr):
    res = 0
    m = sorted(arr)[len(arr) // 2]
    return sum(abs(v - m) for v in arr)


def read_vals(values_f):
    try:
        values = []
        with open(values_f, 'r') as f:
            line = f.readline().replace('\n', '')
            while line:
                values.append(int(line))
                line = f.readline().replace('\n', '')
        f.close()

        return values

    except FileNotFoundError:
        print("Ошибка: файл не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Использование: python script.py <data.txt>")
        sys.exit(1)

    try:
        values_f = sys.argv[1]
        # Загрузка входных данных
        values_data = read_vals(values_f)
        print(func(values_data))

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        sys.exit(1)
