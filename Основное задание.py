xml_file = open('xml__lab4.txt','r',encoding='UTF-8')
json_file = open('jsontry.txt','w')


for el in xml_file:
    el = (
    el.replace('<?xml version="1.0" encoding="UTF-8"?>', "")
    .replace('</dayname>','",')
    .replace('<dayname>','"dayname": "')
    .replace('<professor>','"professor": "')
    .replace('</professor>','",')
    .replace("<day>",'"day": {')
    .replace("</day>",'}')
    .replace("<week>", "{")
    .replace("</week>", "}")
    .replace("<lessons>", '"lessons": {')
    .replace("</lessons>", "    }")
    .replace("<lesson1>", '"lesson1": {')
    .replace("</lesson1>", "   },")
    .replace("<lesson2>", '"lesson2": {')
    .replace("</lesson2>", '    }')
    .replace("<name>", '"name": "')
    .replace("</name>", '",')
    .replace("<professor>", '"prfessor": "')
    .replace("</professor>", '",')
    .replace("<place>", '"place": "')
    .replace("</place>", '",')
    .replace("<time>", '"time": "')
    .replace("</time>", '",')
    .replace("<format>", '"format": "')
    .replace("</format>", '"')
)
    json_file.write(el)




print(json_file)
