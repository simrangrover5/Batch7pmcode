class One:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def perimeter(self):
        print("Perimeter is {}",format(self.height*2+self.width*2))

    def show(self):
        print("Height : ",self.height)
        print("Width : ",self.width)


