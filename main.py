start_digit = 0
last_digit = 0
searchdigit = 0
try: 
    start_digit = int(input('First number:'))
    last_digit = int(input('last number:'))
    searchdigit = int(input('Искомое число:'))


    start_digit = int(start_digit)
    last_digit = int(last_digit)
    searchdigit = int(searchdigit)
except ValueError:
    print('Необходимо ввести целое число.')


digit_dict = [i for i in range(start_digit,last_digit)]
digit_dict.sort()

low = start_digit
mid = len(digit_dict) // 2
high = len(digit_dict) - 1

cycles = 0
while digit_dict [mid] != searchdigit and low < high:
    if searchdigit > mid:
        low = mid + 1
        
        cycles = cycles + 1
    else:
        high = mid - 1
        cycles = cycles + 1
    mid = (low + high) // 2
    

if low > high:
    print("No value")
else:
    print("ID =", mid)

if searchdigit == digit_dict[mid]:
    print('done')
else:
    print('error')
print('Cycles = ', cycles)
