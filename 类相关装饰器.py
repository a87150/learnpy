class Student(object):
# @property有.setter、.getter和.deleter三个装饰器，分别对应赋值、取值和删除三种操作。
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @score.deleter #删除
    def score(self):
        del self._score
		
s = Student()

s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()

s.score = 99
print(s.score)

del s.score
print(s.score)
s.score = 9999


class A(object):
    var = 1

    def func(self):
        print(self.var)
        return
# @staticmethod 将类成员方法声明为类静态方法，类静态方法没有 self 参数，可以通过类名或类实例调用。
    @staticmethod
    def static_func():
        print(A.var)
        return

# @classmethod 将类成员方法声明为类方法，类方法所接收的第一个参数不是self，而是cls，即当前的类。
    @classmethod
    def class_func(cls):
        print(cls.var)
        cls().func()
        return

A.static_func()
A.class_func()