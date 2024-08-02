import main
import spam

def main():
    print("Welcome to the startup screen!")
    print("Please choose which script to run:")
    print("1. Script 1")
    print("2. Script 2")
    choice = input("Enter your choice: ")
    if choice == "1":
        main.main()
    elif choice == "2":
        spam.main()
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()