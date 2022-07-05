'''
Задача №1.
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)
def task(array):
    pass

print(task("111111111110000000000000000"))
# >> OUT: 10
…

'''


def array_to_string(array):
    if type(array) is list:
        return "".join(map(str, array))


def task(array):
    if len(array) < 1:
        raise ValueError("Need more elements in array")
    if type(array) is list:
        array = array_to_string(array)
    if not array.isdigit():
        raise ValueError("Array must be digits")
    if not array.startswith("1"):
        raise ValueError("Array must start with 1")
    if "0" not in array:
        raise ValueError("Array must contain 0")
    return array.index("0") - 1
