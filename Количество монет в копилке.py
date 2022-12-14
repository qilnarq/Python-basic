'''Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством 
монет, которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет 
в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить 
в копилку ещё какое-то количество монет, не превышая ее вместимость.

Класс должен иметь следующий вид

class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        # положить v монет в копилку
При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.'''


class MoneyBox:

    def __init__(self, capacity):
        self.count=0
        self.capasity=capacity
    
    def can_add(self, v):
        self.v=v
        return self.count+self.v <= self.capasity
      
    def add(self, v):
        self.v=v
        if MoneyBox.can_add(self,v)==True:
            self.count +=self.v
        
x = MoneyBox(15)
print(x.can_add(5))
print(x.can_add(9))
print(x.can_add(3))   