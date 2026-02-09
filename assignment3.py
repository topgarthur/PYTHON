income=8000
if(income>=0 and income<=5999):
    print(150)
elif(income>5999 and income<=7999):
    print(300)  
elif(income>7999 and income<=11999):
    print(400)      
elif(income>11999 and income<=14999):
    print(500)
elif(income>14999 and income<=19999):
    print(600)   
elif(income>19999 and income<=24999):
    print(750)   
elif(income>24999 and income<=29999):
    print(850) 
elif(income>29999 and income<=49999):
    print(1000)
elif(income>49999 and income<=99999):
    print(1500)   
elif(income>100000):
    print(2000)
else:
    print("invalid income")    




