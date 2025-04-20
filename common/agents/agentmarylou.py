import random
from common.base_agent import BaseAgent
from common.move import Move

# Student scipers, will be automatically used to evaluate your code
SCIPERS = ["390899", "Ton sciper"]

#INFO:
#J'ai créé une première fonction pour éviter de devoir remettre les coordonnées a chaque nouvelle fonction
#Je suis en train de faire qu'il aille chercher les passager ou les déposer. Mon idée'
#c'est qu'on mette ensuite le choix de mouvement dans le get_move() du style, si c'est le plus proche on fait passenger sinon delivery...'


class Agent(BaseAgent):
    def positions(self):
        """
        Coordinates which a reused several times to determine the train's next move
        """

        #Train Coordinates
        self.x_train_position = self.all_trains['Bob']['position'][0]
        self.y_train_position = self.all_trains['Bob']['position'][1]
        
        #passenger Coordinates
        self.x_passenger_position = self.passengers[0]['position'][0]
        self.y_passenger_position = self.passengers[0]['position'][1]

        #previous train movement
        self.current_move = Move(tuple(self.all_trains['Bob']['direction']))

        #delivery zone coordinates
        self.x_delivery_position = self.delivery_zone['position'][0]
        self.y_delivery_position = self.delivery_zone['position'][1]
        self.delivery_zone_height = self.delivery_zone['height']
        self.delivery_zone_width = self.delivery_zone['width']
        self.passed_on_delivery_zone = 0

    def walls_around(self, move):
        
        self.positions()
        
        wanted_move = list(move.value)
        wanted_x_pos = self.x_train_position + wanted_move[0]*self.cell_size
        wanted_y_pos = self.y_train_position + wanted_move[1]*self.cell_size
        if wanted_x_pos > 400 :
            #checks if there is a wall to the right
            return 1
        if wanted_x_pos < 0 :
            #checks if there is a wall to the left
            return 1
        if wanted_y_pos > 400 :
            #checks if there is a wall above
            return 1
        if wanted_y_pos < 0 :
            #checks if there is a wall below
            return 1
        
    def move_if_walls(self, move):

        self.positions()

        print("MOOOOOOVE", move)
        moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
        previous_move = tuple([ -i for i in list(self.current_move.value)])
        moves.remove(Move(previous_move))
        if move == Move.UP:
            #checks if wall above
            print("MOOOVVVVVVVVVVE", move)
            if self.y_train_position - self.cell_size < 0:
                print("MOOOOOOVE", move) 
                #checks if in top left corner
                if self.x_train_position - self.cell_size < 0:
                    move = Move.turn_right(Move.UP)
                    print("MOVE_UP", move)
                    return move
                else:
                    move = Move.turn_left(Move.UP)
                    print("MOVE_UP", move)
                    return move
                
        elif move == Move.DOWN:
            #checks if wall below
            if self.y_train_position + self.cell_size > 400:
                #checks if bottom left corner
                if self.x_train_position - self.cell_size < 0:
                    move = Move.turn_left(Move.DOWN)
                    print("MOVE_DOWN", move)
                    return move
                else:
                    move = Move.turn_right(Move.DOWN)
                    print("MOVE_DOWN", move)
                    return move
        elif move == Move.LEFT:
            #checks if wall to the left
            if self.x_train_position - self.cell_size < 0:
                #checks if bottom left corner
                if self.y_train_position + self.cell_size > 400:
                    move = Move.turn_right(Move.LEFT)
                    print("MOVE_LEFT", move)
                    return move
                else:
                    move = Move.turn_left(Move.LEFT)
                    print("MOVE_LEFT", move)
                    return move
        elif move == Move.RIGHT:
            #checks if wall to the left
            if self.x_train_position + self.cell_size > 400:
                #checks if bottom right corner
                if self.y_train_position + self.cell_size > 400:
                    move = Move.turn_left(Move.RIGHT)
                    print("MOVE_RIGHT", move)
                    return move
                else:
                    move = Move.turn_right(Move.RIGHT)
                    print("MOVE_RIGHT", move)
                    return move
        



    def path_to_passenger(self):
        """
        Determines possible path to collect passenger (not yet optimized)
        """

        self.positions()

        #how to move towards passengers depending on current move
        if self.current_move in (Move.UP, Move.DOWN):
            if self.x_train_position == self.x_passenger_position:
                return self.current_move
            elif self.x_train_position > self.x_passenger_position:
                return Move.LEFT
            elif self.x_train_position < self.x_passenger_position:
                return Move.RIGHT
        if self.current_move in (Move.RIGHT, Move.LEFT):
            if self.y_train_position == self.y_passenger_position:
                return self.current_move
            elif self.y_train_position > self.y_passenger_position:
                return Move.UP
            elif self.y_train_position < self.y_passenger_position:
                return Move.DOWN
    
    def deliver_passengers(self): ##Je suis en train d'ecrire cette fonction
        """
        - self.delivery_zone_width / 2 
        + self.delivery_zone_width / 2
        + self.delivery_zone_width / 2
        - self.delivery_zone_width / 2

        - self.delivery_zone_height / 2
+ self.delivery_zone_height / 2
+ self.delivery_zone_height / 2
- self.delivery_zone_width / 2
        """
        
        self.positions()
        #print(type(self.x_delivery_position), type(self.delivery_zone_width), type(self.x_train_position))
        if self.current_move in (Move.UP, Move.DOWN):
            if (self.x_delivery_position  ) <= self.x_train_position <= (self.x_delivery_position ):
                self.passed_on_delivery_zone = 0
                return self.current_move
            elif self.x_train_position > (self.x_delivery_position ) :
                return Move.LEFT
            elif self.x_train_position < (self.x_delivery_position ) :
                return Move.RIGHT
        if self.current_move in (Move.RIGHT, Move.LEFT):
            if (self.y_delivery_position  ) <= self.y_train_position <= (self.y_delivery_position ):
                self.passed_on_delivery_zone = 1
                return self.current_move
            elif self.y_train_position > (self.y_delivery_position ):
                return Move.UP
            elif self.y_train_position < (self.y_delivery_position ):
                return Move.DOWN


    def avoid_wagons(self):
        #QUESTION: est-ce qu'on fait une fonction pour éviter ses propres wagons et une pour éviter les autres trains ou on combine les deux?
        """
        Moves possible to avoid running into other trains/into the trains own wagons
        """
        pass

    def get_move(self):
        
        ######
        #self.logger.debug(self.all_trains)
        #self.logger.debug(self.passengers)
        #self.logger.debug(self.delivery_zone)
        #####
        """
        Determines Train's next position
        """
        #A rajouter: des conditions if,elif,else qui determinent si le train va en direction des passager/évite d'autres trains/dépose des passager,...
        if len(self.all_trains['Bob']['wagons']) > 4: # and self.passed_on_delivery_zone == 0:
            move = self.deliver_passengers()
            walls = self.walls_around(move)
            if walls:
                print("MOVEEEEEE", move)
                move = self.move_if_walls(move)
        else:
            move = self.path_to_passenger()
            walls = self.walls_around(move)
            if walls:
                print("MOVEEEEEE", move)
                move = self.move_if_walls(move)
        print("MOVEEEEEE", move, "WAGONS", len(self.all_trains['Bob']['wagons']))
        return move



            

