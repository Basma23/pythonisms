import functools
import time

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item) 

    def __iter__(self):
        def values_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return values_generator()

    def __str__(self):
        out = ""
        for value in self:
            out += f"[{value}] -> "
        return out + "None"

    def __len__(self):
        return len(list(iter(self)))

    def __eq__(self, other):
        return list(iter(self)) == list(iter(other))

    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def factors(n):
    results = []
    for k in range(1, n + 1):
        if n % k == 0: results.append(k)
    return results

@slow_down
def factors1(n):
    for k in range(1, n + 1):
        if n % k == 0: 
            yield k
print(factors(100))
for factor in factors1(200):
    print(factor)

def lowerize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_value = func(*args, **kwargs)
        return original_value.lower()
    return wrapper

def camelize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_value = func(*args, **kwargs)
        return original_value.title()
    return wrapper
    
def fun_with_words(first_noun, second_noun, verb):
    return f"{first_noun}s love tO {verb} ALL the {second_noun}s"
print(fun_with_words('Programmer','Time','Code'))