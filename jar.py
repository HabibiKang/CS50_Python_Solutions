class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0 or int(capacity) > 12:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n > self.capacity or (n + self.size) > self.capacity:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if int(n) > self.size:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(6)
jar.withdraw(5)
print(jar.capacity)
print(jar.size)

