upper=int(input("enter upper limit :"))
lower=int(input("enter lower limit :"))
print("prime number between",lower,"and",upper,"are :")
for i in range(lower,(upper+1)):
	if i==0 or i==1:
		continue
	j=2
	flag=0
	while j<=i/2:
		if i%j==0:
			flag=1
			break
		j=j+1
	if flag==0:
		print(i)
		
