print("\n\n\n\t\t\t\t\tWelocome to DVS Technologies")
ch=1
while ch!=0:
	print("\n\t----------DVS Dashboard----------\n")
	print("\t1. Courses Offered")
	print("\t2. Fees Details")	
	print("\t3. DVS Faculties")
	print("\t4. Location of DVS")
	print("\t5. Exit from Portal")
	try:
		ch=int(input("\n\tEnter your choice:"))
	except:
			print("\tPlese select only available choices")
			continue
	if ch==1:
		print("\t----Courses----\n")
		print("\t1. Python 2 Months")
		print("\t2. Scala 3 Months")
		print("\t3. Hadoop 1.5 Months")
		print("\t4. Sparks 2.5 Months")
	elif ch==2:
		print("\t----Fee Details----\n")
		print("\t1. Python: 7000 INR")
		print("\t2. Scala: 8000 INR")
		print("\t3. Hadoop: 9000 INR")
		print("\t4. Sparks: 10000 INR")
		global crs_choice
		while crs_choice!=0:
		
			try:
				crs_choice=int(input("\n\tEnter the Course no. to join:"))
			except:
				print("Please enter valid course number.")
				continue
			if crs_choice==1:
				print("\tYou have choosed 'Python'")
				dec=input("\tDo you want to take admission. Reply by 'Yes|No':")
				if dec.lower()=="yes":
					name=input("\tEnter your name:")
				
					while True:
						amt=int(input("\tEnter the amount:"))
						if amt>=8000:
							print("\tPlease collect your change:", amt-8000)
							print("\tThank you {}. DVS Technology welcomes you :)".format(name.capitalize()))
							print("\tClass Timings: Mon-Sat, 7:00-9:00")
							break
				
						else:
							print("\tEnter the exact course amount")
	elif ch==3:
		print("\t----Faculty Details----\n")
		print("\tNireekshan: Python")
		print("\tShahid: Scala")
		print("\tAbishek: Hadoop")
		print("\tPraveen: Sparks")
	elif ch==4:
		address='''\n\tDVS Technologies
\tMarathahalli outer ring road
\tBeside Biryani Zone
\tBengaluru-560040'''
		print("\t----Location Details----")
		print(address)
	elif ch==5:
		print("\tThank you....Hope we meet again!")
		exit()
	else:
		print("\tInvalid choice...Try again")
		ch=1
		continue
		
