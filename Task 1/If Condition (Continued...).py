#-------------------------------------------------------------------------------------------------------------------------#

'''
3. Write a program to check if two cities belong to the same country. 
Ask the user to enter two cities and print whether they belong to the same country or not.
Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"
Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"
'''
Australia = ["sydney", "melbourne", "brisbane", "perth"]       
UAE = ["dubai", "abu dhabi", "sharjah", "ajman"]                 
India = ["mumbai", "bangalore", "chennai", "delhi"]        


city1 = input("Enter the first City Name : ")           
city2 = input("Enter the second City Name : ")            
city1_name = city1.lower()                        
city2_name = city2.lower()                         

# Starting the loop

if city1_name in Australia and city2_name in Australia :              
    print("Both cities are in Australia")
elif city1_name in UAE and city2_name in UAE :                        
    print("Both cities are in UAE")
elif city1_name in India and city2_name in India :                   
    print ("Both cities are in India")
else :
    print ("They don't belong to the same country")           

