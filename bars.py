import json
import sys


def load_data(file_path):
    with open(file_path, 'r') as opened_file:
        loaded_data = json.load(opened_file)
    return loaded_data


def get_biggest_bar(bars):
    return max(
        bars,
        key=lambda bar:
        bar['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(bars):
    return min(
        bars,
        key=lambda bar:
        bar['properties']['Attributes']['SeatsCount']
    )


def get_closest_bar(bars, user_longitude, user_latitude):
    return min(
        bars,
        key=lambda bar:
        get_distance(
            user_longitude,
            bar['geometry']['coordinates'][0],
            user_latitude,
            bar['geometry']['coordinates'][1]
        )
    )


def get_distance(user_longitude, bar_longitude, user_latitude, bar_latitude):
    distance = ((user_longitude - bar_longitude)
                + (user_latitude - bar_latitude))
    return abs(distance)

if __name__ == '__main__':
    try:
        loaded_data = load_data(sys.argv[1])
        bars = loaded_data['features']
        print("Критерий для поиска бара: \n "
              "1. Самый большой бар \n "
              "2. Самый маленький бар \n "
              "3. Ближайший бар")
        search_criteria = int(
            input('Задайте критерий для поиска цифрой от 1го до 3х: \n'))
        if (search_criteria == 1):
            print('Cамый большой бар: ',
                  get_biggest_bar(
                      bars
                  )['properties']['Attributes']['Name'])
        elif (search_criteria == 2):
            print('Самый маленький бар: ',
                  get_smallest_bar(
                      bars
                  )['properties']['Attributes']['Name'])
        elif (search_criteria == 3):
            print('Ввведите координаты вашего местоположения \n')
            user_longitude = float(input('Ввведите долготу: \n'))
            user_latitude = float(input('Ввведите широту: \n'))
            print('Ближайший бар: ',
                  get_closest_bar(
                      bars,
                      user_longitude,
                      user_latitude
                  )['properties']['Attributes']['Name'])
        else:
            print("Неккоректно задан критерий поиска. Попробуйте снова")
    except FileNotFoundError:
        print('Некорректный путь к файлу.')
    except IndexError:
        print('Укажите путь к файлу.')
    except ValueError:
        print('Некорректный формат ввода данных.')
