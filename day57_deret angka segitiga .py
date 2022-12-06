print("Program Python Segitiga Deret Angka ")
print()
  
user = int(input('enter the number: '))
print()
 
k = 1
for i in range(user):
  for j in range(i+1):
    print(k,' ',end='',sep='')
    k = k + 1
  print()
		
