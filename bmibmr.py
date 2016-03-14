# Menu
# Ask whether to print BMI, BMR, or to exit
output = str(input('Calulate BMI or BMR or Exit: '))
print ('You entered: ' + output) # Try not to print 'random' info

# Exit, I put it up here to make sure the next step doesn't trigger
if output == 'exit' or output == 'Exit' or output == 'EXIT':
   print('Exiting...') # Try to always notify the user about what is going on
   exit()

# Check if the input is valid
if output != 'BMI' and output != 'bmi' and output != 'BMR' and output != 'bmr':
   print('Please enter a valid choice.')
   exit()

# Get user's height, weight and age values
# Never write code more than once, either place it in a function or
# take it elsewhere where it will be used once only
height = float(input('Please enter your height in inches: '))
weight = float(input('Please enter your weight in pounds: '))

# BMI
if output == 'BMI' or output == 'bmi':

   # Do the first steps of the formula
   heightSquared = (height * height)
   finalWeight = (weight * 703)

   # Figure out and print the BMI
   bmi = finalWeight / heightSquared

   if bmi < 18: # First step, is it less than 18?
      text = 'Underweight'

   elif bmi <= 24: # If it isn't is it less than or equal to 24?
      text = 'Ideal'

   elif bmi <= 29: # If not is it less than or equal to 29?
      text = 'Overweight'

   elif bmi <= 39: # If not is it less than or equal to 39?
      text = 'Obese'

   else: # If none of the above work, i.e. it is greater than 39, do this.
      text = 'Extremely Obese'

   print ('Your BMI is: ' + str(bmi))
   print ('This is: ' + text)

# BMR
elif output == 'bmr' or output == 'BMR':

   gender = str(input('Are you male (M) or female (F): '))
   age = int(input('Please enter your age in years: '))
   bmr = 0 # Initialize the bmr 

   if gender == 'M' or gender == 'm':
      # Figure out and print the BMR
      bmr = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)

   if gender == 'F' or gender == 'f':
      # Figure out and print the BMR
      bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

   print ('Your BMR is: ' + str(bmr))
