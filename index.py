def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("함수 호출 전")
        result = func(*args, **kwargs)
        print("함수 호출 후")
        return result
    return wrapper

class Person:
    def __init__(self, name, age):
        self._name = name  # 인스턴스 변수
        self.age = age
    
    @my_decorator
    def say_hello(self):
        print(f"부모, 저는 {self._name}이고 {self.age}살입니다.")

class Police(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def say_hello(self):
        print(f"자식, 저는 {self._name}이고 {self.age}살입니다.")

p1 = Police("paul", 20)
p2 = Police("sean", 30)
p3 = Person("Alice", 23)
persons = {p1,p2,p3}

for p in persons:
    p.say_hello()
    print(f"{p._name}")
    print("")