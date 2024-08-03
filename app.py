from time import localtime, strftime, time
from logger import Logger

def get_timestamp():
    return strftime("[%Y-%m-%d %H:%M:%S]", localtime())

def main():
    logger = Logger()

    while True:
        print("------------------ Menu ------------------")
        print("1. Log a message")
        print("2. Clean the logger")
        print("3. Current logger size")    
        print("Enter 'q' to quit")    
        choice = input("Enter your choice (1, 2, 3 or q): ")
        
        print()
        if choice == "1":    
            message = input("Enter a message: ")
            if logger.shouldPrintMessage(int(time()), message):
                print(f"{get_timestamp()} Message {message} logged!")
            else:
                print(f"{get_timestamp()} Message {message} cannot be logged at this time. Please try again later.")
        elif choice == "2":
            print(f"Current size: {logger.loggerSize()}")
            if logger.clean(int(time())):
                print(f"{get_timestamp()} Logger cleaned! Size after cleaning: {logger.loggerSize()}")
            else:
                print(f"{get_timestamp()} Logger was not cleaned. Please try again later.")
        elif choice == "3":
            print(f"{get_timestamp()} Current size: {logger.loggerSize()}")
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")
        
        print("\n")
    
    print("Goodbye!")


if __name__ == "__main__":
    main()