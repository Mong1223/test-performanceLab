import json
import sys

# python .\task3\task3.py .\task3\values.json .\task3\tests.json .\task3\report.json

"""
На вход в качестве аргументов программы поступают три пути к файлу (в приложении
к заданию находятся примеры этих файлов):
    ● values.json содержит результаты прохождения тестов с уникальными id
    ● tests.json содержит структуру для построения отчета на основе прошедших
    тестов (вложенность может быть большей, чем в примере)
    ● report.json - сюда записывается результат.
Напишите программу, которая формирует файл report.json с заполненными полями
value для структуры tests.json на основании values.json.
Структура report.json такая же, как у tests.json, только заполнены поля “value”.
"""


def load_json_file(file_path):
    """Загружает JSON файл."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка при парсинге файла {file_path}.")
        sys.exit(1)


def create_values_dict(values_data):
    values_dict = {}
    for value in values_data['values']:
        values_dict[value['id']] = value['value']
    return values_dict


def fill_nested_items(nested_list, values_dict):
    for item in nested_list:
        if isinstance(item, dict) and item.get('id') in values_dict:
            item['value'] = values_dict[item['id']]
        elif isinstance(item, list):
            fill_nested_items(item, values_dict)


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Использование: python script.py <values.json> <tests.json> <report.json>")
        sys.exit(1)

    try:

        values_f = sys.argv[1]
        tests_f = sys.argv[2]
        report_f = sys.argv[3]

        # Загрузка входных данных
        values_data = load_json_file(values_f)
        tests_data = load_json_file(tests_f)

        # Создание словаря значений
        values_dict = create_values_dict(values_data)

        # Заполнение значений
        for test in tests_data['tests']:
            if isinstance(test, dict) and test.get('id') in values_dict:
                test['value'] = values_dict[test['id']]
            elif isinstance(test, list):
                for item in test:
                    if isinstance(item, dict) and item.get('id') in values_dict:
                        item['value'] = values_dict[item['id']]
                    elif isinstance(item, list):
                        fill_nested_items(item, values_dict)

        # Сохранение результата
        with open(report_f, 'w', encoding='utf-8') as file:
            json.dump(tests_data, file, indent=2)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        sys.exit(1)
