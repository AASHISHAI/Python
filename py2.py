'''Rounding off a number'''
x = float(input('enter the number : '))
int_part = int(x)
dec_part = x - int_part
if dec_part >= 0.50:
   print(int_part + 1)
else:
  print(int_part)