# Define a function to add (concatenate) two strings
def add_strings(str1, str2):
    return str1 + str2

# Get user input for the strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the function to concatenate the strings
result = add_strings(string1, string2)

# Display the result
print("The concatenated string is:", result)
