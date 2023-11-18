import re


# Указать путь к файлу с XML-данными
xml_file_path = 'xml__lab4.txt'

# Чтение XML-данных из файла
with open(xml_file_path, 'r', encoding='utf-8') as file:
    xml_data = file.read()

# Пример использования регулярных выражений
dayname_match = re.search(r'<dayname>\s*(.*?)\s*</dayname>', xml_data)
lesson_matches = re.findall(r'<lesson\d+>(.*?)</lesson\d+>', xml_data, re.DOTALL)

# Создаем словарь вручную
result_dict = {'week': {'day': {'dayname': dayname_match.group(1), 'lessons': []}}}

for lesson_match in lesson_matches:
    name_match = re.search(r'<name>(.*?)</name>', lesson_match)
    professor_match = re.search(r'<professor>(.*?)</professor>', lesson_match)
    place_match = re.search(r'<place>(.*?)</place>', lesson_match)
    time_match = re.search(r'<time>(.*?)</time>', lesson_match)
    format_match = re.search(r'<format>(.*?)</format>', lesson_match)

    lesson_dict = {
        'name': name_match.group(1),
        'professor': professor_match.group(1),
        'place': place_match.group(1),
        'time': time_match.group(1),
        'format': format_match.group(1)
    }

    result_dict['week']['day']['lessons'].append(lesson_dict)

# Конвертируем словарь в JSON
def format_json_like(data, tabs=0):
    result = ''
    indent = ' ' * (tabs * 2)

    if isinstance(data, dict):
        result += '{\n'
        for key, value in data.items():
            result += f'{indent}"{key}": {format_json_like(value, level + 1)},\n'
        result = result.rstrip(',\n')  # Убираем лишнюю запятую
        result += '\n' + ' ' * (level - 1) * 2 + '}'
    elif isinstance(data, list):
        result += '[\n'
        for item in data:
            result += f'{indent}{format_json_like(item, level + 1)},\n'
        result = result.rstrip(',\n')  # Убираем лишнюю запятую
        result += '\n' + ' ' * (tabs - 1) * 2 + ']'
    elif isinstance(data, str):
        result += f'"{data}"'
    else:
        result += str(data)

    return result
json_format = format_json_like(result_dict)

# Запись JSON-данных в файл
json_file_path = 'json_re.txt'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_format)

print(f'Conversion completed. JSON data saved to {json_file_path}')
