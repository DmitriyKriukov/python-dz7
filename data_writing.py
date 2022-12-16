def get_info():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = input('Введите номер телефона: ')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info


def writing_txt(info):
    with open('db.txt', 'a', encoding='utf-8') as data:
        data.write(
            f'\nФамилия: {info[0]}; Имя: {info[1]}; Номер телефона: {info[2]}; Описание: {info[3]}')
