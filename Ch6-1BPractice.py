##Robert Fernandez
##Complete
####Read a file with your name, someone else's name, and your age.

def main():
    # Open the file for reading
    file = open("my_name.txt", "r")
    
    # Read lines from the file
    lines = file.readlines()
    
    # Strip newline characters and store names and age
    name1 = lines[0].strip()
    name2 = lines[1].strip()
    age = int(lines[2].strip())

    # Display the names
    print(f"Name 1: {name1}")
    print(f"Name 2: {name2}")
    
    # Compute age divided by 2
    age_divided_by_2 = age / 2
    
    # Print age and age divided by 2
    print(f"Age: {age}")
    print(f"Age divided by 2: {age_divided_by_2}")
    
    # Close the file
    file.close()

if __name__ == "__main__":
    main()
