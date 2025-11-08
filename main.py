import storage


def input_grades(msg = 'Insira as notas do estudante, separadas por espaço: '):
    grades = input(msg).strip().split()
    
    grades = [float(g) for g in grades] # list comprehension

    '''number_list = []
    for g in grades:
        number_list.append(float(g))
    return number_list'''

    return grades


def save_student(name, grades, data, path):
    data[name] = grades
    storage.save_data(path, data)


def delete_student(name, data, path):
    data.pop(name)
    storage.save_data(path, data)


def main():
    print('== CRUD zinho ==')
    path = 'data.json'
    
    while True:
        print('Comandos disponíveis: create, read, update, delete, list, avg, exit')
        cmd = input('Comando: ').strip().lower()

        if cmd == 'exit':
            break

        if cmd == 'create':
            students = storage.load_data(path)
            name = input('Nome do estudante: ').strip()
            grades = input_grades()
            save_student(name, grades, students, path)
        elif cmd == 'update':
            students = storage.load_data(path)
            name = input('Nome do estudante que terá as notas atualizadas: ').strip()
            grades = input_grades('Notas atualizadas, separadas por espaço: ')
            save_student(name, grades, students, path)
            print(f'Notas de {name} atualizadas')
        elif cmd == 'delete':
            students = storage.load_data(path)
            name = input('Nome do estudante que será removido: ').strip()
            delete_student(name, students, path)
            print(f'O estudante {name} foi removido')


if __name__ == '__main__':
    main()
