a = 30

print(type(a))

print('Hello \nWorld')

S = "Satyajit Das"

print(S[-1-2-3])
print(S[1])

print(S[0:-1])
print(S[0:])

My_string = 'I am a good boy with no skills'

#Finding the length of a string.
print(len(My_string))

#Reservsing a string

print(My_string[::-1])

#How to convert a string to a list using split method of string.

List = My_string.split()
print(List)
print(type(List))

print('{0:=<8} | {1:-^8} | {2:=>8}'.format('Left','Center','Right'))

num = 3.4567899
num1 = 4.54678

print('This is my ten-character, two-decimal number:{1:0.5f}'.format(num,num1))