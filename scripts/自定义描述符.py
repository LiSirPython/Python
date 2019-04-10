class Room:
    def __init__(self,name,width,length):
        self.name = name
        self.width = width
        self.length = length
    @property
    def area(self):
        return self.width * self.length

r1=Room('厕所',1,2)
print(r1.area)