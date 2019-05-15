print("=====MARKSHEET FOR CLASS IX")

a =int(input ("Enter marks of English : \n"))
b = int(input ("Enter marks of Sindhi: \n"))
c = int(input ("Enter marks of Pak.studies: \n"))
d = int(input ("Enter marks of Biology: \n"))
e = int(input ("Enter marks of Chemistry: \n"))
f = a + b + c + d + e 
print("Total marks :" + str(f))
g = (f/425) * 100
print("per% : " + str (g))
g= str(g)
if g >="80":
    print(" congrates your Grade is A+ ")
else:
    if g < '80' and g >= '70':
        print('''your grade is "A"''')
    else:
        if g < '70' and g >= '60':
            print('''your grade is "B" ''')
        else:
            if g < '60' and g >= '50':
                print('''your grade is "C"''')
            else:
                if g < '50':
                    print('''your grade is "D"''')
                else:
                    print ("oh! you are fail please try again")
        
        