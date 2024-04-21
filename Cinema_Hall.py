class Star_Cinema:
    __hall_list = []

    def __init__(self) -> None:
        pass

    def entry_hall(self,rows,cols,hall_no):
        hall_details = Hall(rows,cols,hall_no)
        self.__hall_list.append(hall_details)

class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self,id,movie_name,time):
        t = (id,movie_name,time)
        self.__show_list.append(t)

        self.__seats[id] = []
        for i in range(self.__rows):
            seat_col = []
            for j in range(self.__cols):
                seat_col.append("Free")
            self.__seats[id].append(seat_col)

    def book_seats(self,id,booking_seats):
        for row,col in booking_seats:
            if row<0 or col<0:
                print('Invalid Seat Number')
            elif self.__seats[id][row][col] == "Free":
                self.__seats[id][row][col] = "Booked"
                print(f'Seat {row, col} booked for show {id}')
                return True
            elif self.__seats[id][row][col] == "Booked":
                print(f'Seat {row, col} is already Booked!')
                return False

    def view_shows(self):
        for ans in self.__show_list:
            print(f'Show Name : {ans[1]}  Show Time : {ans[2]} Show ID : {ans[0]}')

    def view_available_seats(self,id):
        print("Available Seats : \n")
        for row in range(self.__rows):
            for col in range(self.__cols):
                print(self.__seats[id][row][col],end = " ")
            print("\n")

movie = Hall(20,20,1)
movie.entry_show("101","Escape Room","2:30")
movie.entry_show("102","3 Idiots","3:30")
movie.entry_show("103","Fast and Furious","4:30")

while True:
    print("Option 1 : View Available Shows")
    print("Option 2 : View Available Seats")
    print("Option 3 : Book a Show")
    print("Option 4 : Exit")

    op = int(input("Enter an option :"))

    if(op == 1):
        movie.view_shows()
    elif(op == 2):
        id = input("Enter the Id of the Show : ")

        try:
            movie.view_available_seats(id)
        except:
            print(f'No shows are available with this id {id}')
        
    elif(op == 3):
        id = input("Enter the Id of the Show : ")
        try:
            movie.view_available_seats(id)
        except:
            print(f'No shows are available with this show_id : {id}')
            continue
        tickets = int(input("Enter total number of tickets : "))
        while tickets > 0:
            booking_seats = [] 
            row = int(input("Enter seat Row No. : "))
            col = int(input("Enter seat Column No. : "))
            try:
                booking_seats.append((row,col)) 
                flag = movie.book_seats(id,booking_seats) 
                if flag == True:    
                    tickets -= 1
            except:    
                print('Invalid Seat Number')
                continue
    elif(op == 4):
        break
    else:
        print("Invalid Option")
    print( "\n")