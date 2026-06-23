scholarships = []
favorites = []

# Load scholarships
try:
    with open("scholarships.txt", "r") as file:
        for line in file:
            scholarships.append(line.strip())
except FileNotFoundError:
    pass

# Load favorites
try:
    with open("favorites.txt", "r") as file:
        for line in file:
            favorites.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print("\n===== Scholarship Finder =====")
    print("1. Add Scholarship")
    print("2. View Scholarships")
    print("3. Search Scholarship")
    print("4. Filter By Country")
    print("5. Add To Favorites")
    print("6. View Favorites")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Scholarship Name: ")
        country = input("Country: ")
        deadline = input("Deadline (YYYY-MM-DD): ")

        scholarship = f"{name} - {country} - {deadline}"

        scholarships.append(scholarship)

        with open("scholarships.txt", "a") as file:
            file.write(scholarship + "\n")

        print("Scholarship added successfully!")

    elif choice == "2":
        print("\nScholarships:")

        if not scholarships:
            print("No scholarships found.")
        else:
            for scholarship in scholarships:
                print("-", scholarship)

    elif choice == "3":
        keyword = input("Enter scholarship name: ").lower()

        found = False

        for scholarship in scholarships:
            if keyword in scholarship.lower():
                print(scholarship)
                found = True

        if not found:
            print("No results found.")

    elif choice == "4":
        country = input("Enter country: ").lower()

        found = False

        for scholarship in scholarships:
            if country in scholarship.lower():
                print(scholarship)
                found = True

        if not found:
            print("No scholarships found.")

    elif choice == "5":
        scholarship = input("Enter scholarship name to favorite: ")

        favorites.append(scholarship)

        with open("favorites.txt", "a") as file:
            file.write(scholarship + "\n")

        print("Added to favorites!")

    elif choice == "6":
        print("\nFavorite Scholarships:")

        if not favorites:
            print("No favorites yet.")
        else:
            for scholarship in favorites:
                print("-", scholarship)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
        
