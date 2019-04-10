import abc   #abc模块可以限制子类继承父类所必须实现的方法

class All_File(abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass
class Disk(All_File):
    def read(self):
        print("disk read")
    def write(self):
        print("disk write")

class Mem(All_File):
    def read(self):
        print("Mem read")
    def write(self):
        print("Mem write")