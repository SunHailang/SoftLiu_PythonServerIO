'''
    __author__ = Sun Hai Lang
    __date__ = 2019-09-17

    create singleton model
'''

from functools import wraps

'''
    使用 __new__
    more times call __new__() method
'''
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        print('Singleton')
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance 



'''
    使用装饰器
    我们定义了一个装饰器 singleton，
    它返回了一个内部函数 getinstance，该函数会判断某个类是否在字典 instances 中，
    如果不存在，则会将 cls 作为 key，cls(*args, **kw) 作为 value 存到 instances 中，否则，直接返回 instances[cls]。
'''
def singleton(cls):
    instances = {}
    @wraps(cls)
    def getInstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getInstance

'''
    使用 metaclass
    元类（metaclass）可以控制类的创建过程，它主要做三件事：
        1. 拦截类的创建
        2. 修改类的定义
        3. 返回修改后的类
'''
class mSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(mSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Python2
# class MyClass(object):
#    __metaclass__ = mSingleton

# Python3
@singleton
class MyClass(object):
# class MyClass(metaclass=mSingleton):

    '''
        对象创建时首先调用 __ new (self) 构造函数生成对象，然后调用 init __(self) 函数初始化数据
        __ new __(cls)
        创建对象
        参数是 cls (类)，不是 self
        必须要有返回值
        如果__new__()方法中没有返回值，将不会执行__init__()方法
    '''
    def __new__(cls, *args, **kwargs):
       print('MyClass new')
       return object.__new__(cls)

    '''
        初始化函数
        有了__init__方法，在创建实例的时候，就不能传入空的参数了，
        必须传入与__init__方法匹配的参数，但self不需要传
    '''
    def __init__(self):
        print('MyClass init')

    '''
        使实例能够像函数一样被调用，同时不影响实例本身的生命周期（call()不影响一个实例的构造和析构）
        可以用来改变实例的内部成员的值
    '''
    def __call__(self):
        print('MyClass call')

    '''
        当删除对象时，Python解析器会默认调用__del__()方法
        销毁（释放）内存中的对象时回调__del__()方法
    '''
    def __del__(self):
        print('MyClass del')

if __name__ == "__main__":
    one = MyClass() # __new__ and __init__
    one() # __call__
    print(id(one))
    two = MyClass()
    print(id(two))
    print(one == two)
