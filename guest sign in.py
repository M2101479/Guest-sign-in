guests=[]
cars=[]

def arrival():
    arrival=[]
    name=input('Enter customer name ')
    email=input('Enter customers email address ')
    number=input('Enter customer phone number ')
    time=input('What is your time of arrival ')
    arrival.append(name)
    arrival.append(email)
    arrival.append(number)
    arrival.append(time)
    guests.append(arrival)

def carpark():
    park=[]
    number=input('Enter the cars registration number ')
    name=input('Enter the drivers name ')
    park.append(number)
    park.append(name)
    cars.append(park)



loop = True
while loop == True:
    option = input(' 1. Register a guest arrival \n 2. Register a car in the carpark \n 3. Exit \n 4. Save guests and cars to file \n ')
    if option == '1':
        arrival()
    elif option == '2':
        carpark()
    elif option == '3':
        loop = False
    elif option == '4' :
        file=open('guest sign in.txt' , 'w+')
        file.write('Guests \n')
        for i in guests:
            file.write(str(i) + '\n')
        file.write('\nCars \n')
        for i in cars:
            file.write(str(i) + '\n')
        file.close()
    else:
        print('Invalid input')
