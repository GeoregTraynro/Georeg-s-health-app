#menu

    #Ask weather to print BMI or BMR
output = str(input('Calulate BMI or BMR or Exit:   '))
print (output)


#BMI
if output == 'BMI' or 'bmi':

    #Get height and weight values
    height = float(input('Please enter your height in inches: '))
    weight = float(input('Please enter your weight in pounds: '))
    #Do the first steps of the formula
    heightSquared = (height * height)
    finalWeight = (weight * 703)
    
    #Fiqure out and print the BMI
    bmi = finalWeight / heightSquared

    if bmi < 18:
        text = 'Underweight'

    if bmi <= 24: # we already know that bmi is >=18 
        text = 'Ideal'

    if bmi <= 29:
        text = 'Overweight'

    if bmi <= 39:
        text = 'Obese'

    else:
        text = 'Extremely Obese'
    print ('Your BMI is: ' + str(bmi))    
    print ('This is: ' + text)

#bmr

if output == 'bmr' or 'BMR':

    gender = input('Are you male (M) or female (F) ')
    if gender == 'M' or 'm':
        
        #Get user's height, weight and age values.
        height = float(input('Please enter your height in inches'))
        weight = float(input('Please enter your weight in pounds'))
        age = int(input('Please enter your age in years'))
        
        #Figure out and print the BmR
        bmr = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
        print (bmr)
    
    if gender == 'F' or 'f':
        #Get user's height, weight and age values.
        height = float(input('Please enter your height in inches'))
        weight = float(input('Please enter your weight in pounds'))
        age = int(input('Please enter your age in years'))
        
        #Figure out and print the BmR
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
        print (bmr)
 

#exit
if output == 'exit' or 'Exit' or 'EXIT':
   exit()
