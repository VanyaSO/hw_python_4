# Пользователь вводит с клавиатуры количество метров.
# Требуется вывести результат перевода метров в сантиметры, дециметры, миллиметры, мили.

number_metrs = int(input("Enter number of meters: "));

centimeters = number_metrs * 100
decimeters = number_metrs * 10
millimeters = number_metrs * 1000
miles = number_metrs * 0.000621371

print(f"In {number_metrs} meters: \n {centimeters} centimeters \n {decimeters} decimeters \n {millimeters} millimeters \n {miles} miles");