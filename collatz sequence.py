large=1;
sav=1;
for i in range(1,1000000):
	temp=i
	flag=1;
	while(i>1):	
		if(i%2==0):
			i=i/2;
		else:		
			i=(3*i) + 1
		flag=flag+1;
	if(flag>large):
		sav=temp;
		large=flag;
		

print sav

	
