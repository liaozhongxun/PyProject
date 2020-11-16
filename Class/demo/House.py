# 房子 户型,总面积,剩余面积,家具列表
class House(object):
    def __init__(self, house_type, total_area, fru_list=None):
        if fru_list is None:
            fru_list = []
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list

    def add_fru(self, x):
        if self.free_area >= x.area:
            self.fru_list.append(x.name)
            self.free_area -= x.area
            print('成功添加' + x.name)
        else:
            print('剩余面积不足无法添加-' + x.name)

    def __str__(self):
        return '户型={},总面积={},剩余面积={},家具列表={}'.format(self.house_type,self.total_area,self.free_area,self.fru_list)

# 家具
class Furniturn(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


house = House('两室一厅', 100)
bed = Furniturn('家具一', 10)
bed2 = Furniturn('家具二', 10)
bed3 = Furniturn('家具三', 20)
bed4 = Furniturn('家具四', 30)
bed5 = Furniturn('家具五', 20)

house.add_fru(bed)
house.add_fru(bed2)
house.add_fru(bed3)
house.add_fru(bed4)
house.add_fru(bed5)

print(house)
