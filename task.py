def all_contacts():
    with open ('phones.txt', 'r', encoding='utf8') as data:
        for line in data:
            print(line)

def find_contact(name):
    with open ('phones.txt', 'r', encoding='utf8') as data:
        for line in data:
            if name in line:
                print(line)    

def add_contact(new_contact):
    with open ('phones.txt', 'a', encoding='utf8') as data:
        data.write('\n'+new_contact)
        print('Запись создана')

def edit_contact():
    with open ('phones.txt', 'r+', encoding='utf8') as data:
        old_name = input('Введите искомый контакт: ')
        new_name = input('Новые данные: ')
        lines = data.read()
        new_lines = lines.replace(old_name, new_name)
    with open ('phones.txt', 'w', encoding='utf8') as data:       
        data.write(new_lines)
        print('Запись изменена') 

def delete_contact(contact):
    with open ('phones.txt', 'r', encoding='utf8') as data:
        lines = data.readlines()
        with open ('phones.txt', 'w', encoding='utf8') as data:
            for line in lines:
                if contact in line:
                    print('Удаление выполнено успешно') 
                else:
                    print(line)
                    data.write(line)  

def main_menu(numb):
    if numb == 1:
        all_contacts()
    elif numb == 2:
        name = input('Введите искомый контакт: ')
        find_contact(name)
    elif numb == 3:
        data = input('Введите новый контакт: ')
        add_contact(data)
    elif numb == 4:
        edit_contact()
    elif numb == 5:
        contact = input('Введите контакт для удаления: ')
        delete_contact(contact)