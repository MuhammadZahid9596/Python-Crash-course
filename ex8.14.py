def make_cars(manufacturer_name,modelno,**car_info):
  car={}
  car['man_name']=manufacturer_name.title()
  car['model'] = modelno.title()
  for key,value in car_info.items():
      car[key]= value.title()
  return car
car_profile= make_cars(
    'honda','2017',color='blue',tech='hybrid'
)
print(car_profile)