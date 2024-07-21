import math
def circle_stats(radius):
    area=math.pi * radius ** 2
    circumference=2 * math.pi * radius
    return(area,circumference)
a,c=circle_stats(3)
rounded_area=round(a,2)
rounded_circumference=round(a,2)
print('area: ',rounded_area, 'circumference:', rounded_circumference)
