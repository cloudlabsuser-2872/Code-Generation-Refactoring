# Optimized program to sum user-provided integers
MAX_ELEMENTS = 100


   try:
      n = int(input(f"Enter the number of elements (1-{MAX_ELEMENTS}): "))
      if not 1 <= n <= MAX_ELEMENTS:
         print(f"Invalid input. Please provide a number from 1 to {MAX_ELEMENTS}.")
         return

      print(f"Enter {n} integers (space-separated):")
      arr_input = input().split()
      if len(arr_input) != n:
         print(f"Expected {n} integers, but got {len(arr_input)}.")
         return
      try:
         arr = list(map(int, arr_input))
      except ValueError:
         print("Invalid input. Please enter valid integers.")
         return

      total = sum(arr)
      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")

if __name__ == "__main__":
   main()
      print("Sum of the numbers:", total)
