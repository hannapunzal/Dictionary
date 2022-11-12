while True:

    # display menu
    print("""----------------- M E N U -----------------\n
    Option 1: Add a contact information
    Option 2: Search for existing contact
    Option 3: Exit program\n\n-------------------------------------------
    """)

    # allow user to select (check if valid)
    userOption = int(input("Choose from the options above [1-3]: "))

    if userOption !=1 and userOption!=2 and userOption!=3:
        print("Sorry, you entered an invalid option. Please choose from 1-3 only: ")
        print()
    
     #option 1: personal data
    if userOption == 1:
        inputName = input("Enter your full name: ")
        name = inputName.upper()
        gender = input("Enter your gender [f/m/rather not say)]: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        phone = int(input("Enter your phone number: "))
        vax = input("Are you vaccinated against COVID-19? [yes/no]: ")
        print("\nYour contact info is saved!")
        print()

    # store user info
        contactTracing = {
            name: {"Name": inputName,
                   "Gender" : gender,
                   "Age" : age,
                   "Address" : address,
                   "Phone" :phone,
                   "Vax" :vax}
        }

    # option 2: search full name, display
    if userOption == 2:
        search = input("Enter the full name of contact: ")
        print()
        contactSearch = search.upper()
        if contactSearch in contactTracing:
            print("Here's the contact information you're searching for:\n")
            for key, value in contactTracing.items():
                print("Name: ",value["Name"],"\nGender: ",value["Gender"],"\nAge: ",value["Age"], "\nAddress: ",value["Address"],"\nPhone number: ",value["Phone"],"\nVaccination status: ",value["Vax"])
            print()
        if contactSearch not in contactTracing:
            print("Sorry, you entered a non-existent contact.\n Choose Option 1 if you want to create\n a new contact.\n")
                

    # option 3 exit
    if userOption == 3:
        print("\nThank you for using HF's Contact Tracer!")
        break