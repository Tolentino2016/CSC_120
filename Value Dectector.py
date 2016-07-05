
while True:
    value = input ("Value between 0 and 100, inclusive: ")
    try:
        value = int(value)
    except ValueError:
        print('Valid number please')
        continue
    #if value not in range (0,101):
    if 0<value<=100:
        break
    else:
        print("Valid range, please 0-100, inclusive")

print('Value in percent is' , 100*value, '%', sep='')
