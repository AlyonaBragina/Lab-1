#TASK1
# RED = '\u001b[41m'
# WHITE = '\u001b[47m'
# END = '\u001b[0m'
# for i in range(10):
#     if i<2 or i>7:
#         print(f'{RED}{"  " * (14)}{END}')
#     elif (i>1 and i<4) or (i>5 and i<8):
#         print(f'{RED}{"  " * (6)}{WHITE}{"  " * (2)}{RED}{"  " * (6)}{END}')
#     elif i>3 and i<6:
#         print(f'{RED}{"  " * (4)}{WHITE}{"  " * (6)}{RED}{"  " * (4)}{END}')
#     

#TASK2
# BLUE = '\u001b[44m'
# WHITE = '\u001b[47m'
# END = '\u001b[0m'
# for i in range(4):
#     if i==0 or i==3:
#         print(f'{WHITE}{"  " * (2)}{BLUE}{"  " * (2)}{WHITE}{"  " * (1)}{BLUE}{"  " * (2)}{WHITE}{"  " * (2)}{END}')
#     elif i==1 or i==2:
#         print(f'{WHITE}{"  " * (1)}{BLUE}{"  " * (1)}{WHITE}{"  " * (2)}{BLUE}{"  " * (1)}{WHITE}{"  " * (2)}{BLUE}{"  " * (1)}{WHITE}{"  " * (1)}{END}')

#TASK3
# BLUE = '\u001b[44m'
# WHITE = '\u001b[47m'
# END = '\u001b[0m'
# n=7
# for i in range(n):
#     if i<6:
#         print(n-(i+1),f'{WHITE}{"  " * (n-(i+1))}{BLUE}{"  " * (1)}{WHITE}{"  " * (i)}{END}')
#     if i==6:
#         print(0,'  ','3 6 9121518')

#TASK4
file = open('sequence.txt')
lst = []
listnew=[]
for number in file:
    lst.append(float(number))
for i in range(len(lst)):
    if int(lst[i])>-3 and  int(lst[i])<3:
        listnew.append(i)
file.close()
print(listnew)