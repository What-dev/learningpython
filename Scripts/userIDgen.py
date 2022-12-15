#add imports 
import random
import os



# Get the full name from the user
full_name = input("Enter your full name: ")

# Use the full name as a seed for the random number generator
random.seed(full_name)

# Generate a random number between 0 and 99999999 (8 digits)
user_id = random.randint(0, 99999999)

# Check if the user ID is already in use
if os.path.exists('used_ids.txt'):
  # If the file exists, open it and read the used IDs
  with open('used_ids.txt', 'r') as f:
    used_ids = f.read().splitlines()
else:
  # If the file doesn't exist, create an empty list of used IDs
  used_ids = []

# Check if the generated user ID is in the list of used IDs
if user_id in used_ids:
  # If the ID is already in use, generate a new one and check again
  while user_id in used_ids:
    user_id = random.randint(0, 99999999)

# Add the user ID to the list of used IDs
used_ids.append(user_id)

# Save the full name and user ID to the file
with open('used_ids.txt', 'a') as f:
  f.write(full_name + ': ' + str(user_id) + '\n')

# Print the user ID
print("Your user ID is:", user_id)

# Pause the script before closing the window
input()