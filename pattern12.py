'''Katarua Rohita Reddy'''
Pattern 12

 1  6 11 16 21
 2  7 12 17 22
 3  8 13 18 23
 4  9 14 19 24
 5 10 15 20 25

'''

n = 5
for i in range(1, n+1):
    count = i
    for j in range(1, n+1):
        print('{:2d}'.format(count), end=' ')
        count += 5
    print()
