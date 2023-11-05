print("This program is for the calculation of Accelration and Distance travelled by and object")
x = str(input("Press A for accelration, S for distance - "))
if x=='a' or x=='A':
	a1 = float(input("Enter the Initial speed (u) of the object (in m/s) - "))
	b1 = float(input("Enter the Final speed (v) of the object (in m/s) - "))
	c1 = float(input("Enter the time taken (t) by the object (in sec.) - "))
	acc1 = (b1-a1)/c1
	print("The accelration of the object is ",acc1,"m/s sq.")
elif x=='s' or x=='S':
	a2 = float(input("Enter the Initial speed (u) of the object (in m/s) - "))
	b2 = float(input("Enter the Final speed (v) of the object (in m/s) - "))
	c2 = float(input("Enter the time taken (t) by the object (in sec.) - "))
	acc2 = (b2-a2)/c2
	s1 = (a2*c2)+((acc2*c2*c2)/2)
	print("The distance travelled by the object is ",s1,"meters")