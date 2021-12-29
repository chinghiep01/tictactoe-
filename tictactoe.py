import random
import sys
class tictactoe : 
    board = []
    board_restart = []
    def __init__(self , number ) :
        self.board_size = number 
        self.win_system =  0    
    def  initalise_board (self):
      for i  in range (self.board_size): 
        row = [] 
        for j  in range (self.board_size):
            row.append(' ') 
        tictactoe.board.append(row)
    def  initalise_board_restart (self):
      for i  in range (self.board_size): 
        row = [] 
        for j  in range (self.board_size):
            row.append('P') 
        tictactoe.board_restart.append(row)
    def create_board(self):
      for r in tictactoe.board:
        for c in r:
           print(c , end = ' |  ') 
        print("\n" + '==+=='*len(r))
    def set_player_turn (self):       
       return random.randint(0,1)
    def player_choose (self,row, column, choose): 
        tictactoe.board[row][column] = choose
    def swap_player (self , player):
        if player == 'O':
            print ('')
            print ("player X turn") 
            return   'X' 
        else: 
           print ('')
           print ('player O turn')
           return    'O'
    def row_check (self , location_x , location_y ): 
      a = 0
      
      count_win_X  = 0 
      count_win_O  = 0  
      count_P_left = 0
      count_P_right= 0  
      try : 
       while tictactoe.board [location_x ][location_y ]  ==  tictactoe.board [location_x ][location_y + a ] :
         a = a + 1 
         if tictactoe.board [location_x][location_y] == 'X':
          count_win_X = count_win_X  + 1 
         elif tictactoe.board [location_x][location_y] == 'O' : 
          count_win_O = count_win_O + 1
       else : 
         if tictactoe.board [location_x ][location_y + a] == ' ': 
            count_P_left  = count_P_left + 1 
      except: 
          pass    
      try :     
       while tictactoe.board [location_x ][location_y ]  ==  tictactoe.board [location_x  ][location_y - a ] :
         a = a + 1 
         if tictactoe.board [location_x][location_y] == 'X':  
          count_win_X  = count_win_X + 1
         elif tictactoe.board [location_x][location_y] == 'O' : 
           count_win_O = count_win_O + 1  
       else : 
         if tictactoe.board [location_x ][location_y - a] == ' ': 
            count_P_right  = count_P_right + 1 
      except:
         pass  
      
      
      if count_win_X > 3 : 
          print ("X win Row ")
          self.win_system = 1
      elif count_win_O > 3: 
          print ("O win Row")
          self.win_system = 1
      elif count_win_X > 3 and count_P_left > 0 and count_P_right > 0: 
          print ("X win Row")
          self.win_system = 1
      elif count_win_O > 3 and count_P_left > 0 and count_P_right > 0 : 
          print ("O win Row ")
          self.win_system = 1
      print (count_win_X)
      print (count_win_O)

    def column_check(self, location_x, location_y): 
      a = 0
      
      count_win_X  = 0 
      count_win_O  = 0  
      count_P_left = 0
      count_P_right= 0  
      try : 
       while tictactoe.board [location_x ][location_y ]  ==  tictactoe.board [location_x + a][location_y ] :
         a = a + 1 
         if tictactoe.board [location_x][location_y] == 'X':
          count_win_X = count_win_X  + 1 
         elif tictactoe.board [location_x][location_y] == 'O' : 
          count_win_O = count_win_O + 1
       else : 
         if tictactoe.board [location_x + a ][location_y ] == ' ': 
            count_P_left  = count_P_left + 1 
      except: 
          pass    
      try :     
       while tictactoe.board [location_x ][location_y ]  ==  tictactoe.board [location_x - a ][location_y ] :
         a = a + 1 
         if tictactoe.board [location_x][location_y] == 'X':  
          count_win_X  = count_win_X + 1
         elif tictactoe.board [location_x][location_y] == 'O' : 
           count_win_O = count_win_O + 1  
       else : 
         if tictactoe.board [location_x - a][location_y ] == ' ': 
            count_P_right  = count_P_right + 1 
      except:
         pass  
      
      
      if count_win_X > 3 : 
          print ("X win Column ")
          self.win_system = 1
      elif count_win_O > 3: 
          print ("O win Column ")
          self.win_system = 1
      elif count_win_X > 3 and count_P_left > 0 and count_P_right > 0: 
          print ("X win Column ")
          self.win_system = 1
      elif count_win_O > 3 and count_P_left > 0 and count_P_right > 0 : 
          print ("O win Column ")
          self.win_system = 1

      
    def diagonal_check (self , location_x , location_y ):
      a = 0
      
      count_win_X_right = 0  
      count_win_O_right = 0
      count_win_O_left  = 0 
      count_win_X_left  = 0  
      count_P_left      = 0
      count_P_right     = 0  
      try : 
       while tictactoe.board [location_x ][location_y ]  ==  tictactoe.board [location_x + a ][location_y + a ] :
        a = a + 1 
        if tictactoe.board [location_x][location_y] == 'X':
         count_win_X_left = count_win_X_left + 1 
        elif tictactoe.board [location_x][location_y] == 'O' : 
          count_win_O_left = count_win_O_left + 1
       else : 
         if tictactoe.board [location_x + a][location_y + a] == '': 
            count_P_left  = count_P_left + 1 
      except: 
          pass    
      try :     
       while tictactoe.board [location_x ][location_y ]  ==  tictactoe.board [location_x - a ][location_y - a ] :
         a = a + 1 
         if tictactoe.board [location_x][location_y] == 'X':  
          count_win_X_left = count_win_X_left + 1
         elif tictactoe.board [location_x][location_y] == 'O' : 
          count_win_O_left = count_win_O_left + 1  
       else : 
         if tictactoe.board [location_x - a][location_y - a] == '': 
            count_P_left  = count_P_left + 1 
      except:
         pass  
       # check nguoc
      try :  
       while tictactoe.board [location_x ][location_y ]  ==  tictactoe.board [location_x + a ][location_y - a ] :
         a = a + 1 
         if tictactoe.board [location_x][location_y] == 'X': 
          count_win_X_right = count_win_X_right + 1 
         elif tictactoe.board [location_x][location_y] == 'O' : 
          count_win_O_right = count_win_O_right + 1
       else : 
         if tictactoe.board [location_x + a][location_y - a] == '': 
            count_P_right  = count_P_right + 1 
      except :
           pass
      try:    
       while tictactoe.board [location_x ][location_y ]  ==  tictactoe.board [location_x - a ][location_y + a ] :
         a = a + 1 
         if tictactoe.board [location_x][location_y] == 'X': 
          count_win_X_right = count_win_X_right + 1 
         elif tictactoe.board [location_x][location_y] == 'O' : 
          count_win_O_right = count_win_O_right + 1    
       else : 
         if tictactoe.board [location_x - a][location_y + a] == '': 
            count_P_right  = count_P_right + 1 
      except: 
          pass

      if count_win_X_right > 4 : 
          print ("X win diagonal")
          self.win_system = 1
      elif count_win_O_right > 4: 
          print ("O win diagonal")
          self.win_system = 1
      elif count_win_X_right >= 4 and count_P_left > 2: 
          print ("X win diagonal")
          self.win_system = 1
      elif count_win_O_right >= 4 and count_P_left > 2: 
          print ("O win diagonal")
          self.win_system = 1

      if count_win_X_left > 4 : 
          print ("X win diagonal")
          self.win_system = 1
      elif count_win_O_left > 4: 
          print ("O win diagonal")
          self.win_system = 1
      elif count_win_O_left >= 4 and count_P_left > 2: 
          print ("O win diagonal")
          self.win_system = 1
      elif count_win_X_left >= 4 and count_P_left > 2: 
          print ("X win diagonal")
          self.win_system = 1
    def draw (self):
        x = "P"
        count_for_P = 0 
        check_system_finish  = 0 
        #check thang :  
        for i in range (self.board_size):
            count_for_P = 0
            check_system_finish = 1
            for j in range (self.board_size):
              x =  tictactoe.board[j][i]
              if x == '':
                count_for_P = count_for_P + 1
              
        if count_for_P == 0 and check_system_finish > 1: 
          print ("draw")
    
                
    def start_game (self): 
      whi_loop = 2 
      self.initalise_board()
      
      player_turn = ''
      if self.set_player_turn() == 1:
          print ('') 
          print ("Player X turn")
          player_turn = 'X'
      else: 
          print ('')
          print ("Player O turn ")
          player_turn = 'O'
      while whi_loop > 1 :
            self.create_board()
            print (""*20)
            row = int (input("please input the row "))
            col = int (input ("please input the postion of column")) 
            while row > self.board_size or col > self.board_size :
                print ("please choose the correct input") 
                row = int (input("please input the row "))
                col = int (input ("please input the postion of column"))
            else :
                check_for_filled_spot = tictactoe.board[row - 1][col - 1]
                if check_for_filled_spot == 'X' or  check_for_filled_spot == 'O': 
                    print ("Invalid position ")
                else: 
                    self.player_choose (row - 1 , col - 1 , player_turn)
                    self.row_check(row-1, col-1)
                    self.column_check(row-1, col-1)
                    self.diagonal_check (row-1, col-1)
                    player_turn = self. swap_player ( player_turn)
                    if self.win_system == 1:
                      self.create_board()
                      choose_continue = int (input ("choose 1 to stop and choose 2 to continue")) 
                      if choose_continue == 1 : 
                       sys.exit()  
                      elif choose_continue == 2 : 
                        whi_loop == 0
                        tictactoe.board = []
                        self.win_system = 0
                        break 
                    elif self.win_system == 0 : 
                      self.draw()


          
            




n = 2
while n > 1 :
 print ("New game let play ")
 print ("="*200)

 size_of_board = int(input ("please input the size of board"))
 game = tictactoe(size_of_board)
 game.start_game()
