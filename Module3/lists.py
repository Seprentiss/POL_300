"""

Fix the return statement so that the function returns the 4th element in the list.
Remember lists start at index 0 so you're looking for the element at index 3.

"""

def access_list():
   list_of_names = ["Sam","Paul","Dan","Luke"]

   # Fix this return statement

   return list_of_names[3]

"""

Add the number 4 to the list_of_numbers at index 3.
Add the name George to the list_of_names

Hint) Try using the insert and append methods.
"""
def add_to_list():
  # Fix this statement. Add what's needed to the insert method
  list_of_numbers = [1,2,3,5,6]

  list_of_names = ["Sam","Paul","Dan","Luke"]


  # Put code here

  list_of_numbers.insert(3,4)
  list_of_names.append("George")



  # DON"T TOUCH THIS RETURN STATEMENT
  return list_of_numbers, list_of_names


"""

Remove the name Dan from the list_of_names

Hint) Try using the remove method.

"""

def remove_from_list():
  list_of_names = ["Sam", "Paul", "Dan", "Luke"]

  # Put code here
  list_of_names.remove("Dan")



  # DON"T TOUCH THIS RETURN STATEMENT
  return list_of_names


# DO NOT CHANGE BELOW THIS LINE! THIS IS FOR YOU TO SEE AND COMPARE YOUR OUTPUT!

print(access_list()) # Output should be Luke

print(add_to_list()) # Output should be ([1, 2, 3, 4, 5, 6], ['Sam', 'Paul', 'Dan', 'Luke', 'George'])

print(remove_from_list()) # Output should be ['Sam', 'Paul', 'Luke']

