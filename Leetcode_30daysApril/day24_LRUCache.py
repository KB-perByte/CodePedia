class LRUCache:
    def __init__(self, capacity):
        self.__size = capacity
        self.__cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.__cache:
            self.__cache.move_to_end(key)
            return self.__cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.__cache:
            if len(self.__cache) == self.__size:
                self.__cache.popitem(last=False)
        else:
            self.__cache.move_to_end(key)
        self.__cache[key] = value       
