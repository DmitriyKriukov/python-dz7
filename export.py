def from_file():
    last_name = input('Введите искомую фамилию: ')
    with open('db.txt', 'r', encoding='utf-8') as data:
        phonebook = data.read().splitlines()
        for i in range(0, len(phonebook)):
            if last_name in phonebook[i]:
                find_name = str(phonebook[i])
                break
            else:
                find_name = ('Такой фамилии не найдено')
    return find_name
