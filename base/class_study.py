class My:
    kind = "hello"
    kind2 = [1, 2, 3]

    def __init__(self, msg):
        self.msg = msg


obj = My('li')
print(obj.kind)
obj2 = My('bai')
obj2.kind = 'world'
print(obj.kind)
print(obj2.kind)

print(obj.kind2)
obj2.kind2[len(obj2.kind2):] = [4, 5, 6]
print(obj.kind2)


class My2(My):
    def __init__(self):
        My.__init__(self, 'libai')

    @staticmethod
    def test():
        print('test')


obj3 = My2()
isinstance(obj3, My)
issubclass(My2, My)
print(obj3.msg)


class My3(My):
    def __init__(self):
        super(My3, self).__init__('libai')

    @staticmethod
    def test():
        print('test')


bytes('abc', encoding='utf-8')
bytearray('abc', encoding='utf-8')
