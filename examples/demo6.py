class A(object):
    name = 'wukt'
    age = 18
    nodeDatas = []
    def __init__(self):
        self.gender = 'male'
        self.nodeDatas = []

    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        return ['name', 'age', 'gender', 'nodeDatas']

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)

a = A()
r = dict(a)
print(r)

class HierarchyData():
    # name = ''
    # age = 18
    # nodeDatas = []
    def __init__(self):
        self.nodeDatas = []
        # self.gender = 'male'

    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        # return ('gender','nodeDatas')
        return ['nodeDatas']
        

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)

a = HierarchyData()
r = dict(a)
print(r, r["nodeDatas"])


class NodeData():
    def __init__(self):
        self.positionChannels = []
        self.rotationChannels = []
        self.positionData = []
        self.rotationData = []
    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        return ["rotationChannels", "positionData", "rotationData"]

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)
a = NodeData()
r = dict(NodeData())
print(r, r["rotationData"])

b = []

b.append(r)
b.append(r)
print(b)
