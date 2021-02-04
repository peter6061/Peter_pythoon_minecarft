a = [372468,48327,237,425,642,53,64634]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t
print (a)