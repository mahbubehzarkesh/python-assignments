name=input("please enter your first name:")
family=input ("please enter your family:")
grade1=float(input("enter grade1:"))
grade2=float(input("enter grade2:"))
grade3=float(input("enter grade3:"))
ave=(grade1+grade2+grade3)/3
if ave>=17: 
    print (" well done dear",name,family,"your average is Great")
if 12<=ave<17: 
    print ("dear",name,family,"your average is Normal")
if ave<12: 
    print ("sorry dear ",name,family," you Failed")
