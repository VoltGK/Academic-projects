from operator import index

participants = []

#function that generate ID automatically
def generate_registration_id(participants):
    return int(1E3 + len(participants) + 1)

#function that ADD participant to system
def register_participant(student, name, age, email, event):
    if len(student) >= 50:
        print("Event capacity already FULL!")
        return
    if name == "" or email =="":
        print("Name and Email MUST complete")
        return
    if age < 0:
        print("Age MUST be greater than one")

    if event == "1":
        event = "Python WorkShop"
    elif event == "2":
        event = "AI Introduction Seminar"
    elif event == "3":
        event = "Web Development Bootcamp"
    elif event == "4":
        event = "Career Guidance Session"

    if email not in student:
        new_id = generate_registration_id(student)
        new_participants = {
            "id": new_id,
            "name": name,
            "age": age,
            "email": email,
            "event": event,
            "payment": "Unpaid"
        }
        student.append(new_participants)
        print("\nRegistration successful!")
        print(f"Registration ID: {new_id}")
    else:
        print(f"There is {email} call email already on database")
        return

#function that view all participant
def view_participant(student):
    if student == []:
        print("First add participant into system")
        print()
    else:
        print("\n<-----View All Participant----->")
        print(f"{'ID':^6} | {'Name':^10} | {'Age':^6} | {'Email':^15} | {'Event':^23} | {'Payment':^10}")
        print("-" * 90)
        for i in range(len(participants)):
            print(
                f"{participants[i]["id"]:^6} | {participants[i]["name"]:^10} | {participants[i]["age"]:^6} | {participants[i]["email"]:^10} | {participants[i]["event"]:^15} | {participants[i]["payment"]:^10}")
            print("-" * 90)
            print()

#function to search participant in system
def search_participant(student, name):
    if student == []:
        print("First add participant into system")
        print()
    else:
        name_str = name.lower()
        for p in student:
            if name_str in p["name"].lower():
                print(f"<-----Participant Found----->"
                      f"\nID {':':>6} {p["id"]}"
                      f"\nName {':':>4} {p["name"]}"
                      f"\nAge {':':>5} {p["age"]}"
                      f"\nEmail {':':>3} {p["email"]}"
                      f"\nEvent {':':>3} {p["event"]}"
                      f"\npayment {':':>1} {p["payment"]}")
                print()
            else:
                print(f"No participant name : {name}")

#function to filter participant by event they joined
def view_event_participants(student, event):
    if student == []:
        print("First add participant to system")
    else:
        event_str = event.lower()
        for j in student:
            if event_str in j["event"].lower():
                print(f"For {event} "
                      f"\n {j["name"]}")
            else:
                print(f"There is no participant for {event} event")



while True:
    print("=====EVENT REGISTRATION SYSTEM=====")
    print("\n1. Register participant"
          "\n2. View all participant"
          "\n3. Search participant"
          "\n4. View event participant"
          "\n5. Update payment status"
          "\n6. Cancel registration"
          "\n7. Show statistics"
          "\n8. Exit")

    choice = int(input("\nWhat do you want to do : "))

    if choice == 1:
        while True:
            user_name = input("\nEnter name : ")
            user_age = int(input("Enter age : "))
            user_email = input("Enter email : ")
            print("\nWhat event participant want to participate"
                  "\n1. Python Workshop"
                  "\n2. AI Introduction Seminar"
                  "\n3. Web Development Bootcamp"
                  "\n4. Career Guidance Session")
            print()
            user_event = input("Enter event number : ")
            register_participant(student=participants, name=user_name, age=user_age, email=user_email, event=user_event)
            to_exit = input("\nDo you want to exit? (type 'yes' to exit): ")
            if to_exit == "yes":
                print()
                break

    if choice == 2:
        view_participant(student=participants)

    if choice == 3:
        search_user_name = input("Enter name of participant you want to see : ")
        search_user_name.lower()
        search_participant(student=participants, name=search_user_name)

    if choice == 4:
        print("\n1. Python Workshop"
             "\n2. AI Introduction Seminar"
             "\n3. Web Development Bootcamp"
             "\n4. Career Guidance Session")
        print()
        filter_user_event = input("Enter the event name for filter the names : ")
        view_event_participants(student=participants, event=filter_user_event)
