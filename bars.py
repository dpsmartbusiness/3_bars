import json
import sys


def load_data(file_path):
    with open(file_path, 'r') as opened_file:
        unstructured_data = json.loads(opened_file.read())
    return unstructured_data


def get_biggest_bar(bars):
    b_bar = dict()
    for bar in bars["features"]:
        b_bar[bar["properties"]["Attributes"]["SeatsCount"]] = \
            bar["properties"]["Attributes"]["Name"]
    return b_bar.get(max(b_bar))


def get_smallest_bar(bars):
    s_bar = dict()
    for bar in bars["features"]:
        s_bar[bar["properties"]["Attributes"]["SeatsCount"]] = \
            bar["properties"]["Attributes"]["Name"]
    return s_bar.get(min(s_bar))


def get_closest_bar(bars, longitude, latitude):
    bar_coord = dict()
    for bar in bars["features"]:
        bar_coord[bar["properties"]["Attributes"]["Name"]] = \
            bar['geometry']['coordinates']
    c_bar = dict()
    for bar_key in bar_coord.keys():
        c_bar[get_min(bar_coord[bar_key], [longitude, latitude])] = bar_key
    return c_bar.get(min(c_bar.keys()))


def get_min(l1, l2):
    a = l2[0] - l1[0]
    b = l2[1] - l1[1]
    return abs(a + b)


if __name__ == '__main__':
    print("Критерий для поиска бара: \n "
          "1. Самый большой бар \n "
          "2. Самый маленький бар \n "
          "3. Ближайший бар")
    answ = int(
        input("Задайте требуемый критерий для поиска цифрой от 1го до 3х: \n"))

    if (answ == 1):
        print("Cамый большой бар: ",
              get_biggest_bar(load_data(sys.argv[1])))
    elif (answ == 2):
        print("Самый маленький бар: ",
              get_smallest_bar(load_data(sys.argv[1])))
    elif (answ == 3):
        user_Coord = [float(u_coord) for u_coord in
                      input('Ввведите координаты через запятую: ').split(',')]
        print("Ближайший бар: ",
              get_closest_bar(load_data(sys.argv[1]), user_Coord[0],
                              user_Coord[1]))
    else:
        print("Некорректный формат ввода данных")
