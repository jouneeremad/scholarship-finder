```python
scholarships = []

try:
    with open("scholarships.txt", "r") as file:
        for line in file:
            scholarships.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print("\n===== Scholarship Finder =====")
    print("1. Add Scholarship")
    print("2. View Scholarships")
    print("3. Search Scholarship")
    print("4. Filter By Country")
    print("5. Exit")

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
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
```
