def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car_0 = make_car('subaru', 'outback', color='blue', tow_package=True)
car_1 = make_car('toyota', 'prius', color='red', tow_package=False)

print(car_0)
print(car_1)