# Step 1: Ask the user for their current age
# The input() function displays the message in parentheses and waits for the user
# to type something and press Enter. What they type is retrieved as TEXT.
current_age_str = input("How old are you? ")

# Step 2: Convert the age from text to an integer number
# Since input() returns text, we need to convert it into a number (an integer here)
# to perform calculations with it. int() does this conversion.
current_age = int(current_age_str)

# Step 3: Calculate the years to add until 2050
# We're told the current year is 2023. So, 2050 - 2023 = 27 years.
years_to_add = 27

# Step 4: Calculate the future age
# We simply add the years to the current age.
future_age = current_age + years_to_add

# Step 5: Display the result to the user
# We use an f-string (the 'f' before the quotes) to easily insert
# the value of our 'future_age' variable directly into the sentence.
print(f"In 2050, you will be {future_age} years old.")