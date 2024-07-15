class manyfunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        print("\n Machine Learning \n Neural Networks \n Vision \n Robotics \n Speech \n Processing Natural \n Language Processing")
        
    def OddEven():
        i=int(input("Enter the number"))
        if(i % 2 == 0):
            print(i,"is Even number")
        else:
            print(i,"is Odd number")
    def Elegible():
        gender= input("Enter your gender: M or F: ")
        age=int(input("Enter your age: "))
        if(gender=="M" and age>=20) or (gender=="F" and age>=18):
            return "Eligible"
        else:
            return "Not eligible"
    
    def BMI():
        bmi=int(input("Enter the BMI Index : "))
        if(bmi<18.5):
             message="underweight"
        elif(bmi<24.9):
            message="Normal"
        elif (bmi<29.9):
            message="Overweight"
        else:
            message="Obese"
            return message
