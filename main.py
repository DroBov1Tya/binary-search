import time
low, high, find = int(input('Enter low list number: ')),int(input('Enter High list number: ')),int(input('Enter number to find: '))
l = list(range(low, high))
l.sort()
mid = len(l) // 2
cycle = 0
start_time = time.time()
try:
    while l[mid] != find and low <= high:
        cycle += 1
        if find < l[mid]:
            high = l[mid] - 1
        else:
            low = l[mid] + 1
        mid = (low + high) // 2
    end_time = time.time() - start_time 
    print(f'ID = {mid}\n[+]Cycle = {cycle}\n[Time] = {end_time}')
except IndexError:
    print('[No Value] Index_Error')