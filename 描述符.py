class Integer(object):

    def __get__(self, instance, owner):
        print(instance, owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(self, instance, value)
        if value < 0:
            raise ValueError('Negative value not allowed')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        print(owner, name)
        self.name = name


class Movie(object):
    score = Integer()
    amount = Integer()

movie = Movie()
movie.score = 9

print(movie.score)


'''
描述符是一种在多个属性上重复利用同一个存取逻辑的方式，他能”劫持”那些本对于self.__dict__的操作。
描述符通常是一种包含__get__、__set__、__delete__三种方法中至少一种的类，给人的感觉是「把一个类的操作托付与另外一个类」。
静态方法、类方法、property都是构建描述符的类。
'''