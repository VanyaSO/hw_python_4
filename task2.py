# Пользователь вводит с клавиатуры число, состоящее из четырех цифр. 
# Требуется найти произведение цифр. 
# Например, если с клавиатуры введено 1324, тогда результат произведения 1*3*2*4 = 24.

number = int(input("Enter please four digit number: "))

first_number = number // 1000
second_number = (number // 100) % 10
third_number = (number // 10) % 10
fourth_number = (number // 1) % 10

print(first_number * second_number * third_number * fourth_number); 