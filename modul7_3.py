def custom_write(file_name, strings):
    strings_positions = {}
    file_wr = open(file_name, 'w', encoding= 'utf-8')
    number = 1
    for string in strings:
        byte_position = file_wr.tell()
        file_wr.write(string + '\n')
        strings_positions[(number, byte_position)] = string
        number += 1
    file_wr.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
 print(elem)


