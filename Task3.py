'''Задача 3: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no'''

num = 123321
FirtTreeNums = num // 1000
LastTreeNums = num % 1000
SumFirstTreeNums = (FirtTreeNums //100) + (FirtTreeNums // 10 % 10) + (FirtTreeNums % 10)
SumLastTreeNums = (LastTreeNums //100) + (LastTreeNums // 10 % 10) + (LastTreeNums % 10)

if SumLastTreeNums == SumFirstTreeNums:
    print("Yes")

else:
    print('No')
