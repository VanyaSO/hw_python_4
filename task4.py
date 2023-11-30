# Напишите программу, вычисляющую площадь треугольника. 
# Пользователь с клавиатуры вводит размер основания треугольника и размер высоты.


#Height and length of the tri-wall base
triangle_height = float(input("Enter the height of the triangle: "));
triangle_base = float(input("Enter the base of the triangle: "));

# Calculation behind the formula
area_triangle = .5 * triangle_base * triangle_height

print(f"S = {area_triangle}")