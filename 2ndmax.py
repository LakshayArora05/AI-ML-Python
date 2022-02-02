s=[]
n = int(input("Enter the number of elements: "))
print('Enter ', n, ' elements: ')
for i in range(0,n):
    ele = int(input())
    s.append(ele)
    s.sort()
print('sorted elements: ', s)
print('Second largest element: ',s[i-1])
