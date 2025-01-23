def ispravlenie(phone_book):
    for i in range(len(phone_book)):
        phone_book[i] = phone_book[i].replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        if len(phone_book[i]) == 11 and phone_book[i].startswith('8'):
            phone_book[i] = '+7' + phone_book[i][1:]
        if len(phone_book[i]) == 7:
            phone_book[i] = '+7495' + phone_book[i]
    return phone_book

def proverka(num, phone):
    return "YES" if num == phone else "NO"

nomera_strip = []

with open('nomera.txt', 'r') as f:
    new_phone = f.readline().strip()
    for line in f:
        ls = line.strip()
        nomera_strip.append(ls)

phone_book = ispravlenie(nomera_strip)
new_phone = ispravlenie([new_phone])[0]

with open('вывод.txt', 'w') as f:
    for phone in phone_book:
        f.write(proverka(new_phone, phone) + '\n')
