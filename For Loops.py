#Create a Python file called for_loop_basic1.py that performs the following tasks.
# Basic - Print all integers from 0 to 150.
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

for number in range(151):
    print (number)

for number in range(5,1005,5):
    print (number)

def the_dojo_way():
    for number in range(101):
        if number % 10 == 0:
            print ("Coding Dojo")
        elif number % 5 == 0:
            print ("Coding")
        else:
            print (number)

def that_suckers_huge():
    final_sum = 0
    for number in range(1,500000,2):
        final_sum += number
    print (final_sum)

def countdown_by_four():
    for number in range(2018,0,-4):
        print (number)

def flexible_counter():
lownumber = 2
highnumber = 9
mult = 3
for number in range(lownumber,highnumber + 1):
    if number % mult == 0:
        print (number)
    