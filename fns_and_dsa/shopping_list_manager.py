def display_menu():
  print("Shopping List Manager ")
  print('1. Add Item')
  print("2. Remove Item")
  print("3. View List")
  print('4. Exit')


def main():
  shopping_list = []

  while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
      name = input("Enter name of item: ")

      shopping_list.append(name)

    elif choice == '2':
      name = input("Enter name of item: ")

      shopping_list.remove(name)
    
    elif choice == '3':
      for item in shopping_list:
        print(item)
    
    elif choice == '4':
      print("Goodbye!")
      break

    else:
      print("Invalid choice. Please try again!")


main()