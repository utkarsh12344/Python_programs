import time as t

print(t.time())#returns from January 1, 1970, how many seconds has passed.

print(t.localtime())#returns local time

print(t.asctime())#retuns day,month,time and year

print(t.strftime('%c'))#the other methods to take date and time 

'''
        *Date Formers*
% a: abbreviated name of the week day
% A: full name of the week day
% b: abbreviated name of the month
% B: full name of the month
% c: full date, time, and time
% d: a number of days as a character string
% j: a number between 1-366, indicating that a certain date is the day of the year
% m: month as a character string
% U: a number between 0-53, indicating that a certain date has reached the year of the year
% y: the last two digits of the year
% Y: four digit full year
% x: full date information
% X: full time information
'''

print(t.strftime("%Y"))

print(t.strftime("%B"))

print(t.strftime("%A"))

print(t.strftime("%d/%m/%Y"))#returns formated date

t.sleep(2)#This code will stop our program for 2 seconds.

for i in range(0,5): #Using this function, we can interrupt the operation of our codes for certain periods of time.
    t.sleep(3)
    print("utkarsh bondade")
    