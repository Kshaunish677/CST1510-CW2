#class students 
#one is cyber and it 
#range 80-100 distinction 50-80 pass below 50 fsil

class Students:
    class cyber:
        sname = input("Enter Name: ")
        std_id = input("Enter Student ID: ") 
        mark = int(input("Enter Mark: "))
        if mark >=  80:
            print("DISTINCTION")
        elif mark >= 50:
            print("PASS")
        else:
            print("FAIL")
        print(f"{sname} {std_id} : {mark}")
    class it:
        sname = input("Enter Name: ")
        std_id = input("Enter Student ID: ") 
        mark = int(input("Enter Mark: "))
        if mark >=  80:
            print("DISTINCTION")
        elif mark >= 50:
            print("PASS")
        else:
            print("FAIL")
        print(f"{sname} {std_id} : {mark}")

 

