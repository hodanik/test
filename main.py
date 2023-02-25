
# this is the second test for githyb
# this is the third test for github
# this is the forth test for git hub
# this is the fifth test
# jadi tutorial
# this is the sixth

# first session intro

# comment
# tu python semicollumn ; akhare dastoor ha nemikhaeem, age bezari ham error nemide warning mide..
#type() is a build in fuction to show the variables type
#print() is a build in function to print the results
#input() is a build in function to get input from the user as a string
#isinstance(variable or value, type) is a build in boolean function to chech the type of variables or values.
# isinstance(variable or value, type) function result will be True or False
# variable (moteghaer): x. value (meghdar): 2.
# variable is a name that points to a value.
# tu python moteghayere x ba X fargh dare. case sensitive ast.
# statement: har ghesmate ghabele ejra dar python ra statement goyim.
# statment examples: 1. x=1, 2. print(x), 3. x=x-1
# amalgar (operators) in python. +,-, ** (tavan), *,/ (taghsim), and, or, not, ==, <>, !=, <=,
# edame amalgar: // (taghsim bedune baghimande), % (baghi mande taghsim), 17//3=5, 17%3=2
# expression: har tarkibi ke dar an variable va value va operator vojood dashte bashad,
# yek expression ast. mesal: 1. x=x*2, 2.
# myname='Hoda', lastname='nikpour', print(myname+ ''+lastname), result: Hoda Nikpour
# to convert types in python: we have following functions: int('1') result: 1, float('1.1') result: 1.1,
# Boolean: True, False. ba T va B bozorg
# if in python: if x%2==0: new line, 4 space,now you are in the if print('even'), enter, enter now you are out of if
x = 41
if x % 2 == 0:
    print('even')
elif x % 3 == 0:
    print('to 3')
else:
    print('not even not 3')



name = input()
print(name)

print('Hello World!')

first = int(input())
second = int(input())
print(first*second)

num = int(input())
if num > 99 and num < 1000:
    print(2*((num%10)*100+(((num//10)%10))*10+num//100))
elif num < 100 or num >= 1000:
    print('not in range')

num1 = int(input())
print(((num1+10)//10)*10)

num2 = input()
num3 = input()
if int(num2) >= int(num3):
        print(num2)
elif int(num3) >= int(num2):
        print(num3)

### this is for test the github
# this is the fifth test for git hub
num5 = input()
print(isinstance(int(num5), int))


num4 = input()
if 0 <= int(num4) < 6:
    print('khordsal')
elif 6 <= int(num4) < 10:
    print('koodak')
elif 10 <= int(num4) < 14:
    print('nojavan')
elif 14 <= int(num4) < 24:
    print('javan')
elif 24 <= int(num4) < 40:
    print('bozorgsal')
elif 40 <= int(num4):
    print('miansal')

