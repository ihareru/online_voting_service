def check_choice(db, vote):
    if vote in db:
        return True
    return False


def tally_votes(num_votes):
    max_count = 0
    best_choice = ''
    for model, count in num_votes.items():
        if max_count < count:
            max_count = count
            best_choice = model
    display_results(max_count, best_choice)


def display_results(max, best):
    print('Лучший автомобиль года:', best)
    print('Количество голосов:', max)


def get_user_input(prompt):
    return input(prompt).upper()


def collect_votes(db):
    number_votes = {}
    while True:
        choice = get_user_input('Ваш выбор?: ')
        if choice == '0':
            print('Голосование завершено!\n')
            tally_votes(number_votes)
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
    num = int(get_user_input('Сколько моделей авто учавствует в голосовании?: '))
    for i_model in range(1, num + 1):
        database.append(get_user_input(f'Введите модель {i_model}-го автомобиля: '))
    database = set(database)
    print('\nГолосование создано!')
    print('Выберите модель из списка:', end=' ')
    for model in database:
        print(model, end='; ')

    print('\nДля подсчета голосов введите 0\n')
    collect_votes(database)


if __name__ == '__main__':
    main()
