                              #if condition task
#-------------------------------------------------------------------------------------------------------------------#
def bmi():                                                           
    Height = float(input("Enter Your Height in metres : "))      
    Weight = float(input("Enter Your Weight in kilograms : "))    

    BMI = (Weight / (Height * 2))                 

    # Starting the If Else ladder or the Nested If Else 

    if BMI >= 30 :                               
        print("Obesity")
    elif BMI > 25 and BMI <= 29 :      
        print("Overweight")
    elif BMI > 18.5 and BMI <= 25 :    
        print("Normal")
    elif BMI < 18.5 :                  
        print("Underweight")
    else :
        print ("Wrong Input")           

bmi()                    

#-----------------------------------------------------------------------------------------------------------------------#   

'''
2. Write a program to determine which country a city belongs to. Given list of cities per country:
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi" 
Output: "Abu Dhabi is in UAE"
'''

Australia = ["sydney", "melbourne", "brisbane", "perth"]   
UAE = ["dubai", "abu dhabi", "sharjah", "ajman"]            
India = ["mumbai", "bangalore", "chennai", "delhi"]               

city = input("Enter a City Name : ")            
city_name = city.lower()                       

# Starting nested loop

if city_name in Australia :                     
    print(f"{city_name} is in Australia")
elif city_name in UAE :                        
    print(f"{city_name} is in UAE")
elif city_name in India :                       
    print (f"{city_name} is in India")
else :
        print ("Wrong Input")           