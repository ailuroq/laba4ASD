# Задание: Вариант 21
# Хеш-функция К - Первые k символов ключа последовательно преобразуются в десятичные числа, суммируются,
# результат делится по mod m (все ключи имеют одинаковую длину). В качестве m берется n (длина вектора)
# или некоторое простое число p, ближайшее к n (p<n).

# Метод разрешения конфликтов (1): открытого перемешивания
# Метод определения вторичного индекса (2): линейных проб с простым шагом р

class HashMap:
    def __init__(self):
        self.size = 7
        self.map = [None] * self.size

    def get_map(self):
        return self.map

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value, key_hash]
        hash2 = key_hash
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return self.map
        else:
            while True:
                hash2 = self.secondary_hash(hash2)
                if self.map[hash2] is None:
                    self.map[hash2] = list([key_value])
                    return self.map
                counter = 0
                for item in self.map:
                    if item is not None:
                        counter += 1
                        if counter == 7:
                            print("фул таблица")
                            return 0

            # for pair in self.map[key_hash]:
            #    if pair[0] == key:
            #        pair[1] = value
            #        return True
            # self.map[key_hash].append(key_value)
            return self.map

    def secondary_hash(self, hash):
        hash2 = (hash + 2) % 7
        return hash2

    def clear_map(self):
        self.map = [None] * self.size

    def get_value(self, key):
        key_hash = self._get_hash(key)
        hash2 = key_hash
        if self.map[key_hash] is not None:
            array = self.map[key_hash][0]
            if array[0] == key:
                return array
            else:
                while True:
                    try:
                        hash2 = self.secondary_hash(hash2)
                        array = self.map[hash2][0]
                        if array[0] == key:
                            return array
                    except:
                        return 0
        else:
            while True:
                try:
                    hash2 = self.secondary_hash(hash2)
                    array = self.map[hash2][0]
                    if array[0] == key:
                        return array
                except:
                    return 0

    def delete(self, key):
        key_hash = self._get_hash(key)
        hash2 = key_hash
        if self.map[key_hash] is not None:
            array = self.map[key_hash][0]
            if array[0] == key:
                self.map[key_hash] = None
                return self.map
            else:
                while True:
                    try:
                        counter = 0
                        hash2 = self.secondary_hash(hash2)
                        array = self.map[hash2][0]
                        if array[0] == key:
                            self.map[hash2] = None
                            return self.map
                        else:
                            counter += 1
                            if counter == 7:
                                return 0
                    except:
                        return 0
        else:
            while True:
                try:
                    counter = 0
                    hash2 = self.secondary_hash(hash2)
                    array = self.map[hash2][0]
                    if array[0] == key:
                        self.map[hash2] = None
                        return self.map
                    else:
                        counter += 1
                        if counter == 7:
                            return 0
                except:
                    return 0

    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr
