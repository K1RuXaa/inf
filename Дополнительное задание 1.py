import xml.etree.ElementTree as ET
from xmljson import badgerfish as bf
import json

# Задайте путь к вашему XML-файлу
xml_file_path = 'xml__lab4.txt'

# Прочитайте содержимое XML-файла
with open(xml_file_path, 'r', encoding='utf-8') as xml_file:
    xml_data = xml_file.read()

# Создайте объект ElementTree из XML-строки
tree = ET.fromstring(xml_data)

# Преобразуйте XML в JSON с использованием badgerfish
json_data = bf.data(tree)

# Запишите JSON-данные в файл
json_file_path = 'json_libs.txt'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print(f'XML файл успешно преобразован и сохранен в {json_file_path}')
