command = ""
started = False

while True:
    command = input("Enter command words >> ").lower()
    if command == "start":
        if started:
            print("Car already started !")
        else:
            started = True
            print("Cars started !")
    elif command == "stop":
        if not started:
            print("Car already stopped !")
        else:
            started = False
            print("Cars stopped !")
    elif command == "help":
        print(""" 
start - to start a car
stop  - to stop a car
quit  - to quit
        """)
    elif command == "quit" or "q":
        print("Quit car game!")
        break
    else:
        print(f"I don't understand this {command} command")


