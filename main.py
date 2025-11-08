import storage


def input_grades(msg = 'Insira as notas do estudante, separadas por espaço: '):
    grades = input(msg).strip().split()

    if len(grades) != 4:
        print('Precisa ter exatamente 4 nota!')
        return
    
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


def avg_grades(grades):
    return sum(grades) / len(grades)


def read_student(name, data):
    grades = data.get(name)
    return grades, avg_grades(grades)


def list_students(data):
    for name, grades in data.items():
        print(f'- {name} \t{grades}\t{avg_grades(grades)}')


def main():
    print('== CRUD zinho ==')
    path = 'data.json'
    
    while True:
        print('Comandos disponíveis: create, read, update, delete, list, exit')
        cmd = input('Comando: ').strip().lower()

        if cmd == 'exit':
            break

        if cmd == 'create':
            students = storage.load_data(path)
            name = input('Nome do estudante: ').strip()
            grades = input_grades()
            save_student(name, grades, students, path)
        elif cmd == 'read':
            students = storage.load_data(path)
            name = input('Nome do estudante pesquisado: ').strip()
            grades, avg = read_student(name, students)
            print(f'O estudante {name} possuis as seguintes notas: {grades} (média = {avg})')
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
        elif cmd == 'list':
            students = storage.load_data(path)
            list_students(students)


if __name__ == '__main__':
    main()
