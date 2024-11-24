class Star_Cinema:
    __hall_list=[]
    
    def entry_hall(self,hall_object):
        Star_Cinema.__hall_list.append(hall_object)
        
class Hall(Star_Cinema):
    
    def __init__(self,rows,cols,hall_no):
        self.__seats={}
        self.__show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        
        self.entry_hall(self)
        
    def entry_show(self,id,movie_name,time):
        tpl=(id,movie_name,time)
        self.__show_list.append(tpl)
        
        two_d_list=[[0 for i in range(self.cols)] for j in range(self.rows)]
        self.__seats[id]=two_d_list
        
    def book_seats(self,id,row_col):
        if id not in self.__seats:
            print('Invalid id!')
            return
        for row,col in row_col:
            if self.__seats[id][row][col]==1:
                continue
            elif row>=self.rows or col>=self.cols or row<0 or col<0:
                print('Invalid row or column!')
                return
            else:
                self.__seats[id][row][col]=1
                print('Seat booked successfully!')
                return
        print('Seat not available!')
        
    def view_show_list(self):
        for id,movie_name,time in self.__show_list:
            print(f'{id} {movie_name} {time}')
            
    def view_available_seats(self,id):
        if id not in self.__seats:
            print('Invalid id!')
            return
        for row_number,row in enumerate(self.__seats[id]):
            print(f'Row {row_number} : {row}')
            
    
hall=Hall(3,3,1)
hall.entry_show(1,'3 Idiots','10:00 AM')
hall.entry_show(2,'Inception','12:00 PM')
hall.entry_show(3,'Interstellar','2:00 PM')

hall.book_seats(1,[(0,0),(0,1),(0,2)])
hall.book_seats(1,[(0,0),(0,1),(0,2)])
hall.book_seats(1,[(0,0),(0,1),(0,2)])
hall.book_seats(1,[(0,0),(0,1),(0,2)])
hall.book_seats(1,[(0,0),(0,1),(0,2)])
hall.book_seats(1,[(0,0),(0,1),(0,2)])


hall.view_available_seats(1)

hall.view_show_list()
