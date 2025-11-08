def main():
    print('== CRUD zinho ==')
    
    while True:
        print('Comandos disponíveis: create, read, update, delete, list, avg, exit')
        cmd = input('Comando: ').strip().lower()

        if cmd == 'exit':
            break


if __name__ == '__main__':
    main()
