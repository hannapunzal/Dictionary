import time
import sys

def greet():
    greet = "\033[1;32mHi! Welcome to HF's \033[1;33mContact Tracer\n"
    for i in greet: # this is to put a delay per letter in the printed output to give a typing effect
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.04),
    print()

def loading():
    loading = " . \n .\n .\n"
    for i in loading: # loading dots with delay effect 
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.20),
    print()
    

def firstOption():
    global inputName, name, gender,age,address, phone, vax, comorbidity
    inputName = input("\033[1;32mEnter your full name: \033[1;37m")
    name = inputName.upper()
    gender = input("\033[1;32mEnter your gender \n\033[1;36m[f/m/rather not say]\033[1;32m: \033[1;37m")        
    age = int(input("\033[1;32mEnter your age: \033[1;37m"))
    address = input("\033[1;32mEnter your address: \033[1;37m")
    phone = int(input("\033[1;32mEnter your phone number: \033[1;37m"))
    vax = input("\033[1;32mAre you vaccinated against COVID-19? \033[1;36m[yes/no]\033[1;32m: \033[1;37m")
    comorbidity = input("\033[1;32mDo you have existing health condition? \n\033[1;36m[If yes, enter it. If no, type none]\033[1;32m: \033[1;37m")
    loading()
    print("\033[1;33m\nYour contact info is saved!\n")
    time.sleep(0.9)

def storeContact():
    global contactTracing
    contactTracing = {
            name: {"Name": inputName,
                   "Gender" : gender,
                   "Age" : age,
                   "Address" : address,
                   "Phone" :phone,
                   "Vax" :vax,
                   "Comorbidity" : comorbidity
                   }
            }

def secondOption():
    global contactSearch
    search = input("\033[1;32mEnter the full name of contact: \033[1;37m")
    print()
    contactSearch = search.upper()
    if contactSearch in contactTracing:
        display = "\033[1;36mHere's the contact information we retrieved:\n"
        for i in display: # this is to put a delay per letter in the printed output to give a typing effect
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.06),
        print()
        loading()
        time.sleep(0.9)
        for key, value in contactTracing.items():
            print("\033[1;33mName: \033[1;37m",value["Name"],"\n\033[1;33mGender: \033[1;37m",value["Gender"],"\n\033[1;33mAge: \033[1;37m",value["Age"], "\n\033[1;33mAddress: \033[1;37m",value["Address"],"\n\033[1;33mPhone number: \033[1;37m",value["Phone"],"\n\033[1;33mVaccination status: \033[1;37m",value["Vax"],"\n\033[1;33mComorbidity: \033[1;37m", value["Comorbidity"])
        time.sleep(5)
        print("\033[1;37m")
    if contactSearch not in contactTracing:
        print("\033[1;31mSorry, you entered a non-existent contact.\n Choose Option 1 if you want to create\n a new contact.\n")

def thirdOption():
    print("\033[1;32m\nThank you for using \033[1;33mHF's Contact Tracer\033[1;32m!")
    print("\033[1;37m")

def contactTracer():
    greet()
    while True:

        # display menu
        menu ="""\033[1;37m----------------- M E N U -----------------\n
        Option 1: Add a contact information
        Option 2: Search for existing contact
        Option 3: Exit program\n\n-------------------------------------------
        """
        for i in menu: # this is to put a delay per letter in the printed output to give a typing effect
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02),
        print()
        time.sleep(0.4)

        # allow user to select (check if valid)
        userOption = int(input("\033[1;32mChoose from the options above [1-3]:\033[1;37m "))

        if userOption !=1 and userOption!=2 and userOption!=3:
            print("\033[1;31m\nSorry, you entered an invalid option. Please choose from 1-3 only: \033[1;37m")
            print("\033[1;37m")
            time.sleep(1)
        
        #option 1: personal data
        if userOption == 1:
            firstOption()

        # store user info
            storeContact()

        # option 2: search full name, display
        if userOption == 2:
            secondOption()
                    
        # option 3 exit
        if userOption == 3:
            thirdOption()
            break

contactTracer()