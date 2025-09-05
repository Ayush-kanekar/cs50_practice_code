while True:
	try:
	    x,y = (input("Fraction: ")).split("/")
	    x = int(x)
	    y = int(y)
	    z = (x / y)*100
	    rounded_z = round(z)
	    if x > y or x < 0:
	        continue
	    if rounded_z <= 1:
	        print("E")
	    elif rounded_z >= 99:
	        print("F")
	    else:
	        print(f"{rounded_z}%")
	    break
	except (ValueError,ZeroDivisionError):
	    pass


# the answer was rejected cause of the comment I made in the first if statement
