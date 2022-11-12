while True:

    # display menu
    print("""----- M E N U -----\n
    Option 1: Add a contact information
    Option 2: Search for existing contact
    Option 3: Exit program\n
    -------------------
    """)

    # allow user to select (check if valid)
    userOption = int(input("Choose from the options above [1-3]: "))

    #option 1: personal data
    if userOption == 1:
        inputName = input("Enter your full name: ")
        name = inputName.upper()
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        phone = int(input("Enter your phone number: "))
        vax = input("Are you vaccinated against COVID-19? [yes/no]: ")

    # store user info
    contactTracing = {
        name: [age,address,phone,vax]
    }

    # option 2: search full name, display
    if userOption == 2:
        search = input("Enter the full name of contact: ")
        contactSearch = search.upper()
        if contactSearch in contactTracing:
            print("Here's the contact information you're searching for: ", contactTracing[contactSearch])

    # option 3 exit
    if userOption == 3:
        break
