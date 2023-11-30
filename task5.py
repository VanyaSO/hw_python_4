# Пользователь с клавиатуры вводит четырёхзначное число. 
# Необходимо перевернуть число и отобразить результат. 
# Например, если введено 4512, результат 2154.

number = int(input("Enter please four digit number: "))

# We get all the numbers separately
first_number = number // 1000
second_number = (number // 100) % 10
third_number = (number // 10) % 10
fourth_number = (number // 1) % 10

# Reverse the number
reverse_number = fourth_number*1000 + third_number*100 + second_number*10 + first_number;

print(f"Reversed number {number} = {reverse_number}");