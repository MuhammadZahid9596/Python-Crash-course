class Resturant:

    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def open_resturant(self):
        print('The Resturtant is Open'.lower().title())

    def describe_resturant(self):
        print('Resturant Name is ',self.resturant_name.title(),'largess',self.cuisine_type.title())

    def increment_number_served(self,served):
        self.number_served=served
        print('A happy food day!')

    def set_number_served(self):
        print('The Resturant has served ', self.number_served, 'costumers \n')



res1=Resturant('a','b')

res1.describe_resturant()
res1.open_resturant()
res1.increment_number_served(10)
res1.set_number_served()

class IceCreamStand(Resturant):
    def __init__(self,resturant_name,cuisine_type):
        super().__init__(resturant_name,cuisine_type)
        self.flavours= ['vanila','strawberry']
    def disp_flavours(self):
        for i in self.flavours:
            print(i)

obj=IceCreamStand('Largess','ice cream')
obj.describe_resturant()
obj.disp_flavours()