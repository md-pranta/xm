class Star_cinema:
    _hall_list = []

    def entry_hall(self,hall_object):
        self._hall_list.append(hall_object)


class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

    
    def entry_show(self, id, movie_name, time):
        self._show_list.append((id, movie_name, time))

        self._seats[id] = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, show_id, num, seat_list):
        if show_id not in self._seats:
            print(f"invalid show id '{show_id}'\n")
            return

        seats = self._seats[show_id]

        for row, col in seat_list:
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                print(f"invalid seat ({row}, {col})\n")
                continue

            if seats[row - 1][col - 1] == 1:
                print(f"seat ({row}, {col}) is not available\n")
            else:
                seats[row - 1][col - 1] = 1
                num -= 1
                print(f"seat ({row}, {col}) is booked\n")

        if num > 0:
            print(f"\n{num} seat\'s couldn't be booked.")
    def view_show_list(self):
        print('.....SHOW LIST.....')
        for show in self._show_list:
            print(f"id:{show[0]}, Movie:{show[1]}, Time:{show[2]}")
    
    def view_available_seats(self, id):
        if id not in self._seats:
            print("incorrect ID!!\n")
            return
        
        seat = self._seats[id]
        for r in seat:
            print(" ".join(map(str, r)))
        
cinema = Star_cinema()

h1 = Hall(5, 5, 1)

h1.entry_show('m1', 'killing me softly', '9:00 PM')
h1.entry_show('m2', 'Ancient Secrets Of The Kama Sutra', '12:00 AM')

while True:
    print("\n1:View all shows today")
    print("2:View available seats")
    print("3:Book ticket")
    print("4:Exit\n")
    choice = input("Select an option: ")

    if choice == '1':
        h1.view_show_list()

    elif choice == '2':
        movie_id = input("enter id to view available seats: ")
        h1.view_available_seats(movie_id)
    elif choice == '3':
        movie_id = input("enter id to book a ticket: ")
        num = int(input("number of seats to book: "))
        li = []
        for _ in range(num):
            row = int(input("enter row: "))
            col = int(input("enter column: "))
            li.append((row, col))
        h1.book_seats(movie_id, num, li)
    elif choice == '4':
        break
    else:
        print("invalid option!!")


