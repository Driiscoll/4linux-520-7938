#for i in range(10, -1, -1):
#    print(i)

for i in range(10):
    if i % 3 == 0:
        continue

    if  i % 2 == 0:
        print(i)
    
    if i % 5 == 0:
        break

else:
    print("Fora do loop")