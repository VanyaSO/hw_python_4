# Пользователь вводит с клавиатуры три цифры. 
# Необходимо создать число, содержащее эти цифры.
# Например, если с клавиатуры введено 1, 5, 7, тогда нужно сформировать число 157.

number1 = int(input("Enter first number : "));
number2 = int(input("Enter second number : "));
number3 = int(input("Enter thrid number : "));

print(number1 * 100 + number2 * 10 + number3);