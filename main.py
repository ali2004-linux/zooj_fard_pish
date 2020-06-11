from random import randint

one = int(input("Enter Start Number : "))
two = int(input("Enter End Number : "))
ch = input("Zooj Or Fard? [fard=n, zooj=y] : ")
y = input("Do Save number to file txt ?[y=yes, n=no] : ")

if y.lower() == "y":
	nf = randint(0,10000)
	with open(f"{nf}.txt","w+") as f:
		for i in range(one, two+1):
		        if i%2==0:
		                if ch.lower() == "y":
		                        f.write(f"{str(i)}\n")
        		        else: pass
		        else:
	        	        if ch.lower() == "n":
	        	                f.write(f"{str(i)}\n")
	       		        else: pass		
		print(f"saved to file {nf}.txt")

if y.lower() == "n":	
	for i in range(one, two+1):
		if i%2==0:
			if ch.lower() == "y":
				print(i)
			else: pass
		else:
			if ch.lower() == "n":
				print(i)
			else: pass

