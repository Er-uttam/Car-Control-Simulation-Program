print('---PROGRAM TO START, STOP, AND CONTROL CAR---')
print("---YOU CAN TYPE HELP FOR WHAT TO DO!---")

car_started = False
car_locked = True
headlights_on = False
speed = 0

def show_help():
    print('''
start - to start the car
stop - to stop the car
lock - to lock the car
unlock - to unlock the car
headlights on - to turn on the headlights
headlights off - to turn off the headlights
horn - to honk the horn
fuel - to check the fuel level
speed [number] - to set the speed of the car
park - to set the car to park mode
drive - to set the car to drive mode
ac on - to turn on the air conditioning
ac off - to turn off the air conditioning
radio on - to turn on the radio
radio off - to turn off the radio
quit - to terminate
''')

def check_fuel():
    print("Fuel level is at 75%")

while True:
    command = input('Enter a Command:').lower()
    
    if command == 'start':
        if not car_started:
            car_started = True
            print("Car started, ready to go.")
        else:
            print("Car is already started.")
    
    elif command == 'stop':
        if car_started:
            car_started = False
            speed = 0
            print("Car stopped.")
        else:
            print("Car is already stopped.")
    
    elif command == 'lock':
        if not car_locked:
            car_locked = True
            print("Car locked.")
        else:
            print("Car is already locked.")
    
    elif command == 'unlock':
        if car_locked:
            car_locked = False
            print("Car unlocked.")
        else:
            print("Car is already unlocked.")
    
    elif command == 'headlights on':
        if not headlights_on:
            headlights_on = True
            print("Headlights turned on.")
        else:
            print("Headlights are already on.")
    
    elif command == 'headlights off':
        if headlights_on:
            headlights_on = False
            print("Headlights turned off.")
        else:
            print("Headlights are already off.")
    
    elif command == 'horn':
        print("Honking horn. Beep beep!")
    
    elif command == 'fuel':
        check_fuel()
    
    elif command.startswith('speed '):
        try:
            speed = int(command.split()[1])
            print(f"Speed set to {speed} km/h.")
        except ValueError:
            print("Invalid speed. Please enter a number.")
    
    elif command == 'park':
        speed = 0
        print("Car set to park mode.")
    
    elif command == 'drive':
        print("Car set to drive mode.")
    
    elif command == 'ac on':
        print("Air conditioning turned on.")
    
    elif command == 'ac off':
        print("Air conditioning turned off.")
    
    elif command == 'radio on':
        print("Radio turned on.")
    
    elif command == 'radio off':
        print("Radio turned off.")
    
    elif command == 'help':
        show_help()
    
    elif command == 'quit':
        print("Program terminated successfully!")
        break
    
    else:
        print("Sorry, I don't understand that.")
