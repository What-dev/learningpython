# Get the input from the user
user_input = input("Enter a name or ID: ")

# Open the file and read the used IDs and names
with open('used_ids.txt', 'r') as f:
  used_ids = f.read().splitlines()

# Search for the input in the list of used IDs and names
found = False
for entry in used_ids:
  name, id = entry.split(': ')
  if id == user_input or name == user_input:
    # If the input is found, print the corresponding name or ID
    if id == user_input:
      print("The user ID", user_input, "is associated with the name", name)
    else:
      print("The name", user_input, "is associated with the user ID", id)
    found = True
    break


if not found:
  # If the input is not found, print an error message
  print("The input", user_input, "was not found in the file.")

# Pause the script before closing the window
input()
