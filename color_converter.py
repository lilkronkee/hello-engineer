#ФИО: Ермаков_Роман_Алексеевич
#Вариант: 9
def rgb_to_hex():
    print('Конвертер RGB в HEX')
    try:
        r = int(input('Введите R (0-255): '))
        g = int(input('Введите G (0-255): '))
        b = int(input('Введите B (0-255): '))

        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print('Ошибка: значения должны быть от 0 до 255!')
            return

        hex_color = f'#{r:02X}{g:02X}{b:02X}'
        print(f'HEX: {hex_color}')

    except ValueError:
        print('Ошибка: введите целые числа!')


if __name__ == '__main__':
    rgb_to_hex()