
# purchase_amount = float(input("Enter your purchase amount: "))

# if purchase_amount >= 1000:
#   discount = 0.1  # 10% discount
# elif purchase_amount >= 500:
#   discount = 0.05  # 5% discount
# else:
#   discount = 0  # No discount

# final_price = purchase_amount * (1 - discount)

# print(final_price)


# User Input Validation:
# age = 0

# while age < 18:
#   age = int(input("Enter your age (must be 18 or older): "))

# print("You are old enough to proceed.")



# Guessing Game:
# secret_number = 7

# guess_count = 0
# guess = 0

# while guess != secret_number:
#   guess_count += 1
#   guess = int(input("Guess a number between 1 and 10: "))

# print(f"You guessed it in {guess_count} tries!")


# Iterating Until a Specific Condition:

# shopping_list = ["apples", "bread", "milk", "cheese"]
# item_found = False

# while not item_found:
#   item = input("Search for an item in your list (or 'q' to quit): ")
#   if item.lower() == "q":
#     break  # Exit the loop if user enters 'q'
#   if item in shopping_list:
#     item_found = True
#     print(f"{item} is on your shopping list.")
#   else:
#     print(f"{item} is not on your list.")

# outer_count = 5

# while outer_count > 0:
#   # Outer loop controls the number of times the inner loop runs
#   inner_count = 1
#   while inner_count <= outer_count:
#     # Inner loop repeats for each outer loop iteration
#     print(inner_count, end=" ")
#     inner_count += 1
#   print()  # Move to a new line after each outer loop iteration
#   outer_count -= 1

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:    
#           print(f"{n} equal {x} * {n//x}")
        
#           break


# def user_info(name, age=None):
#      """Prints user information."""
#      print(f"Name: {name}")
#      if age:
#           print(f"Age: {age}")

# user_info(name ="Bob", age="")
     

# def square(number):
#     return number * number
# square_value = square(4)
# print(square_value)

count = 0

def increment_global():
  count = count
  count += 1
increment_global()
print(count)
                     
     
   




 