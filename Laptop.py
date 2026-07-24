class Laptop:
    def __init__(self , brand , RAMS , storage , processer):
        self.brand = brand
        self.RAMS = RAMS
        self.storage = storage
        self.processer = processer

L = Laptop("Dell " , "14_L" , 256 , 8)

print("brand : " , L.brand)
print("RAMS : " , L.RAMS)
print('Storage : ' , L.storage)
print("Processer : " , L.processer)
