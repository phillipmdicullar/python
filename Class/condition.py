age = 1
is_baby = 'baby' if age < 2 else 'not a baby'
print(is_baby)
# This is the equivalent of the following if/else statement:

age = 1
if age < 2:
  is_baby = 'baby'
else:
  is_baby = 'not a baby'
# Conditional expressions in Python are always of the format:

# value_if_true if condition else value_if_false