# Задание: Вариант 21
# Хеш-функция К - Первые k символов ключа последовательно преобразуются в десятичные числа, суммируются,
# результат делится по mod m (все ключи имеют одинаковую длину). В качестве m берется n (длина вектора)
# или некоторое простое число p, ближайшее к n (p<n).

# Метод разрешения конфликтов (1): открытого перемешивания
# Метод определения вторичного индекса (2): линейных проб с простым шагом р

class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value, key_hash]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        print('---PHONEBOOK----')
        for item in self.map:
            if item is not None:
                print(str(item))


h = HashMap()
h.add('Bobsf', '567-8888')
h.add('Bobsf', '567-8888')
h.add('Bobsf', '567-8888')
h.add('Mingf', '333-8233')
h.add('Ankif', '293-8625')
h.add('Aditf', '852-6551')
h.add('Alicf', '632-4123')
h.add('Mikef', '567-2188')
h.add('Adiqf', '777-8888')
h.print()
print(h.keys())