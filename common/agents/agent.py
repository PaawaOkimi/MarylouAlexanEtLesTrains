import random
from common.base_agent import BaseAgent
from common.move import Move
#from server.train import Train # this is where the train position is
#from server.game import Game # this is where the game size is
# Student scipers, will be automatically used to evaluate your code
SCIPERS = ["390899", "445566"]


class Agent(BaseAgent):

    def get_move(self):
        #self.logger.debug(self.all_trains)
        moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
        previous_move = self.all_trains['Bob']['direction'] #[0,1] -> [0,-1]
        print("PREVIOUS MOVE", previous_move)
        previous_move = [-(i) for i in previous_move] # -> [1,0]
        print("PREVIOUS", previous_move)
        previous_move = tuple(previous_move)
        print("PREVIOUS_MOVE", previous_move)
        moves.remove(Move(tuple(previous_move)))
        print("MOVES", moves)
        move = random.choice(moves) #Move(tuple(self.all_trains['Bob']['direction'])) #Move.DOWN #random.choice(moves)
        position = self.all_trains['Bob']['position'] 
        print("POSSIBLE_MOVE", move)
        if move == Move.UP:
            #checks if wall above
            if position[1] - self.cell_size < 0: 
                #checks if in top left corner
                if position[0] - self.cell_size < 0:
                    move = Move.turn_right(Move.UP)
                    print("MOVE", move)
                    return move
                else:
                    move = Move.turn_left(Move.UP)
                    print("MOVE", move)
                    return move
        elif move == Move.DOWN:
            #checks if wall below
            if position[1] + self.cell_size > 400:
                #checks if bottom left corner
                if position[0] - self.cell_size < 0:
                    move = Move.turn_left(Move.DOWN)
                    print("MOVE", move)
                    return move
                else:
                    move = Move.turn_right(Move.DOWN)
                    print("MOVE", move)
                    return move
        elif move == Move.LEFT:
            #checks if wall to the left
            if position[0] - self.cell_size < 0:
                #checks if bottom left corner
                if position[1] + self.cell_size > 400:
                    move = Move.turn_right(Move.LEFT)
                    print("MOVE", move)
                    return move
                else:
                    move = Move.turn_left(Move.LEFT)
                    print("MOVE", move)
                    return move
        elif move == Move.RIGHT:
            #checks if wall to the left
            if position[0] + self.cell_size > 400:
                #checks if bottom right corner
                if position[1] + self.cell_size > 400:
                    move = Move.turn_left(Move.RIGHT)
                    print("MOVE", move)
                    return move
                else:
                    move = Move.turn_right(Move.RIGHT)
                    print("MOVE", move)
                    return move
        return move

    #def is_wall(self, move):
    #    """
    #    Determines the position of walls around the player
    #    
    #    IN: wanted movement
    #    OUT: 0 if no wall, 1 if wall for each direction (list of int)
    #    """
    #    current_position = self.all_trains['Bob']['position']   
    #    movement = move.value 
    #    wanted_x_pos = current_position[0] + movement[0]*self.cell_size
    #    wanted_y_pos = current_position[1] + movement[1]*self.cell_size
    #    up, down, left, right = (0, 0, 0, 0)
    #    #check if new position is on a wall
    #    if wanted_x_pos > 400 :
    #        #checks if there is a wall to the right
    #        right = 1
    #    if wanted_x_pos < 0 :
    #        #checks if there is a wall to the left
    #        left = 1
    #    if wanted_y_pos > 400 :
    #        #checks if there is a wall above
    #        up = 1
    #    if wanted_y_pos < 0 :
    #        #checks if there is a wall below
    #        down = 1
    #    walls = [up, down, left, right]
    #    return walls
#
#
    #def get_move(self):
    #    """ 
    #    Determines where the train will move next
    #    """
    #    moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
    #    while True:
    #        move = random.choice(moves)
    #        possible_move = self.is_wall(move)
    #        if 1 not in possible_move:
    #            return move
    #        #checks if wall above
    #        elif possible_move[0] == 1:
    #            #checks if on top left corner
    #            if possible_move[2] == 1:
                































    #def get_move(self):
    #    pos = self.all_trains['Bob']['position']
    #    print('POS', pos)
    #    move = Move.turn_left(Move.UP)
    #    return move
    #def get_move(self):
    #    moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
    #    return random.choice(moves)

    #def is_wall(self, pos, move):
    #    """
    #    Determines if there are walls around the train
    #    
    #    IN: x,y coordinates (list of int) and dx,dy movement (tuple with int)
    #    OUT: list of int (0 if no wall, 1 if wall)
    #    """
#
    #    #postion the train is trying to go on
    #    new_x_pos = pos[0] + move[0]*self.cell_size
    #    new_y_pos = pos[1] + move[1]*self.cell_size
#
    #    #where walls are present around player
    #    up, down, left, right = (0, 0, 0, 0)
    #    if new_x_pos > 400 :
    #        #checks if there is a wall to the right
    #        right = 1
    #    if new_x_pos < 0 :
    #        #checks if there is a wall to the left
    #        left = 1
    #    if new_y_pos > 400 :
    #        #checks if there is a wall above
    #        up = 1
    #    if new_y_pos < 0 :
    #        #checks if there is a wall below
    #        down = 1
    #    walls = [up, down, left, right]
#
    #    #PRINTS FOR CODE TESTING/UNDERSTANDING
    #    print ("POS", pos)
    #    print ("WALLS", walls)
#
    #    return walls
    #
    #def get_move(self):
    #    #return Move.LEFT
    #    """
    #    Determines next train movement
    #    
    #    IN:
    #    OUT:
    #    """
    #    current_pos = self.all_trains['Bob']['position']
    #    moves = [Move.UP, Move.DOWN, Move.RIGHT]
    #    while True: #loops until valid move is chosen
    #        wanted_move = random.choice(moves)
    #        #PRINTS FOR CODE TESTING/UNDERSTANDING
    #        print (wanted_move, wanted_move.value)
    #        #checks if move is valid
    #        walls = self.is_wall(current_pos, wanted_move.value)
    #        #corner cases 
    #        if walls[0] and walls[2]:
    #            Move.turn_left(wanted_move)
    #        
    #        if 1 in walls:
    #            
    #            possible_move = 1
    #            still_walls = self.is_wall(current_pos, wanted_move).value
    #            return Move.turn_left(Move.wanted_move)
    #            continue
    #        else:
    #            print("NEW MOVE ###########")
    #            return wanted_move
    #        
    #        
    #        
    #    
    #        
#
#
#
#
    ##def is_wall(self, pos, move):
    ##    """
    ##    returns True if the position the player is trying to go to is in the grid
    #    
    #    IN: train position (tuple) with x,y coordinates (int) _ movement (tuple) with dx,dy (int)
    #    OUT: Boolean
    #    """
    #    pos[0] = pos[0] + (move[0])*self.cell_size 
    #    pos[1] = pos[1] + (move[1])*self.cell_size
    #    print(self.cell_size)
    #    print('POS', pos)
    #    up, down, left, right = (0, 0, 0, 0)
    #    if pos[0] > 400:
    #        right = 1
    #    if pos[0] < 0:
    #        left = 1
    #    if pos[1] > 400:
    #        up = 1
    #    if pos[1] < 0:
    #        down = 1
    #    walls = [up, down, left, right] 
    #    #print('WALLS', walls)
    #    return walls
    #
    #def is_other_player():
    #    pass
#
    #def get_move(self):
    #    """
    #    Called regularly called to get the next move for your train. Implement
    #    an algorithm to control your train here. You will be handing in this file.
#
    #    For now, the code simply picks a random direction between UP, DOWN, LEFT, RIGHT
#
    #    This method must return one of moves.MOVE
    #    """
#
#
#
#
#
#
#
    #    pos = self.all_trains['Bob']['position']
    #    move = self.all_trains['Bob']['direction']
    #    moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
    #    walls = self.is_wall(pos, move) # [up, down, left, right]

        #match move:
        #    case []

        #pos = self.all_trains['Bob']['position']
        #moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
        #walls = self.is_wall(pos, move) # [up, down, left, right]
        #move = Move.UP #random.choice(moves)
        ##print ('MOVE', move)
        #if walls[0] == 1 : #wall above
        #    #checks for corner situations
        #    if walls[2] == 1:
        #        return Move.RIGHT
        #    return Move.LEFT
        #elif walls[1] == 1: # wall below
        #    #checks for corner situations
        #    if walls[2] == 1:
        #        return Move.RIGHT
        #    return Move.LEFT
        #elif walls[2] == 1:
        #    Move.turn_right(move) #return Move.RIGHT
        #elif walls[3] == 1:
        #    Move.turn_left(move) #return Move.LEFT
        ##print("HAHA")
        #return Move.UP


        #pos = self.all_trains['Bob']['position']
        #move = self.all_trains['Bob']['direction']
        #moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
        #print(move)
        #if self.is_wall(pos, move) == "wall_above":
        #    if self.is_wall(pos, move) == "wall_left":
        #        return Move.RIGHT
        #elif self.is_wall(pos, move) == "wall_above":
        #    if self.is_wall(pos, move) == "wall_right":
        #        return Move.LEFT
        #elif self.is_wall(pos, move) == "wall_below":
        #    if self.is_wall(pos, move) == "wall_right":
        #        return Move.LEFT
        #      
        #else:
        #    return moves[1]
        
       
