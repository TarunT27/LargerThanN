def find_greater_numbers(num_list, n):
  """Finds all numbers in a list that are greater than a given number.

  Args:
    num_list: A list of numbers.
    n: The number to compare the list elements to.

  Returns:
    A list of numbers from the input list that are greater than n.
  """

  return [num for num in num_list if num > n]

def main():
  """Gets user input for the list and number, and then displays the results."""


  num_list_str = input("Enter a list of numbers separated by commas: ")
  try:
    num_list = [float(num) for num in num_list_str.split(",")]
  except ValueError:
    print("Invalid input. Please enter a comma-separated list of numbers.")
    return


  while True:
    try:
      n = float(input("Enter a number: "))
      break
    except ValueError:
      print("Invalid input. Please enter a number.")


  greater_numbers = find_greater_numbers(num_list, n)
  if greater_numbers:
    print(f"Numbers greater than {n} in the list are: {greater_numbers}")
  else:
    print(f"No numbers in the list are greater than {n}.")

if __name__ == "__main__":
  main()
