import math

def circle(radius):
    area = math.pi * radius ** 2
    circum = 2 * math.pi * radius
    return area,circum

a, c = circle(4)

print(f'Area {a:.2f}')
print(f"Circumference: {c:.2f}")