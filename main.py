def check_choice(db, vote):
    if vote in db:
        return True
    return False


def voting(db):
    max_count = 0
    number_votes = {}
    best_choice = ''
    while True:
        choice = input('Ваш выбор?: ').upper()
        if choice == '0':
            print('Голосование завершено!')
            for model, count in number_votes.items():
                if max_count < count:
                    max_count = count
                    best_choice = model
            print('Лучший автомобиль года:', best_choice)
            print('Количество голосов:', max_count)
            break
        else:
            if check_choice(db, choice):
                if choice in number_votes:
                    number_votes[choice] += 1
                else:
                    number_votes[choice] = 1
                print('Ваш голос принят!\n')
            else:
                print('Такой марки нет в списке!\n')


def main():
    database = []
    print('Голосование за автомобиль года!\n')
    num = int(input('Сколько моделей авто учавствует в голосовании?: '))
    for i_model in range(1, num + 1):
        database.append(input(f'Введите модель {i_model}-го автомобиля: ').upper())
    database = set(database)
    print('Голосование создано!')
    print('Выберите модель из списка:', end=' ')
    for model in database:
        print(model, end='; ')
    print('\nДля подсчета голосов введите 0\n')
    voting(database)


if __name__ == '__main__':
    main()
