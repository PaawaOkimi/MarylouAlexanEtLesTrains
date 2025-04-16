import random
from common.base_agent import BaseAgent
from common.move import Move

# Student scipers, will be automatically used to evaluate your code
SCIPERS = ["112233", "445566"]


class Agent(BaseAgent):
        
    nickname='Bernard'
    """ 
    Instructions on structure of code :  
    position - self.all_trains['AgentDetest']['position']
    direction - self.all_trains['AgentDetest']['direction']
    same score, color of agent, alive, boost_cooldown, wagons
    # clé = nom du train 
    obtenir nom adverse : récupérer la clef qui n'est pas dans celles de base et notre nom à nom
     
    ATTENTION : ORIGINE BIZARRE HAUT à -20 et LARGEUR à 420
    """
    def get_the_food(self):#function to find the closest point of food
        positionsoffood=[]
        for x in range(len(self.passengers)):
            positionsoffood.append(self.passengers[x]["position"])
        closestdis=1000000
        for x in positionsoffood:
            pos=x
            distance=abs(pos[0]-self.all_trains[self.nickname]['position'][0])+abs(pos[1]-self.all_trains[self.nickname]['position'][1])
            if distance < closestdis:
                closestdis=distance
                closestpos=pos
            #below: checks in which direction to go depending on the position
        if closestpos[0]-self.all_trains[self.nickname]['position'][0]<0:
            newdirection=Move.LEFT
        if closestpos[0]-self.all_trains[self.nickname]['position'][0]==0:
            if closestpos[1]-self.all_trains[self.nickname]['position'][1]<0:
                newdirection=Move.UP
            if closestpos[1]-self.all_trains[self.nickname]['position'][1]>0:
                newdirection=Move.DOWN

        if closestpos[0]-self.all_trains[self.nickname]['position'][0]>0:
            newdirection=Move.RIGHT


        return newdirection


    def avoid_walls(self):
        actualdirection=list(self.all_trains[self.nickname]['direction'])#gets the actual direction of the train
        listactualdirection=[x*self.cell_size for x in actualdirection]#modifies the direction to fit a displacement of cell
        nextposition=[a + b for a, b in zip(listactualdirection,self.all_trains[self.nickname]['position'])] #calculating the incoming position with the 2 variables
        
        if nextposition[0]==self.game_width:#looks for the east wall
            newdirection=Move.UP
            return newdirection

        if nextposition[0]==-self.cell_size: # looks for the west wall
            newdirection=Move.DOWN
            return newdirection

        if nextposition[1]==self.game_height: #looks for the south wall
            newdirection=Move.RIGHT
            return newdirection


        if nextposition[1]==-self.cell_size: #looks for the north wall

            newdirection=Move.LEFT
            return newdirection
        if nextposition in self.all_trains[self.nickname]['wagons']:#future fix to prevent the train from killing itself, not done yet
            if actualdirection==[0,1]:
                newdirection=Move.UP
            if actualdirection==[0,-1]:
                newdirection=Move.DOWN

            if actualdirection==[1,0]:
                newdirection=Move.LEFT

            if actualdirection==[0,1]:
                newdirection=Move.UP





        else :
            newdirection=0
            if self.all_trains[self.nickname]['position'][0]==self.game_width-self.cell_size:#east
                newdirection=Move.LEFT
            if self.all_trains[self.nickname]['position'][0]==0:#west
                newdirection=Move.RIGHT

            if self.all_trains[self.nickname]['position'][1]==self.game_height-self.cell_size:#south
                newdirection=Move.UP

            if self.all_trains[self.nickname]['position'][1]==-self.cell_size:#north
                newdirection=Move.DOWN
                


            return newdirection
    def depose_passengers(self):
            targetdir=self.delivery_zone["position"]
            if targetdir[0]-self.all_trains[self.nickname]['position'][0]<0:
                newdirection=Move.LEFT
            if targetdir[0]-self.all_trains[self.nickname]['position'][0]==0:
                if targetdir[1]-self.all_trains[self.nickname]['position'][1]<0:
                    newdirection=Move.UP
                if targetdir[1]-self.all_trains[self.nickname]['position'][1]>0:
                    newdirection=Move.DOWN
#similar to detecting where the food is and choosing the direction, but for the goal
            if targetdir[0]-self.all_trains[self.nickname]['position'][0]>0:
                newdirection=Move.RIGHT
            else:
                newdirection=Move.DOWN
            return newdirection





    def get_move(self):
        """
        Called regularly called to get the next move for your train. Implement
        an algorithm to control your train here. You will be handing in this file.

        For now, the code simply picks a random direction between UP, DOWN, LEFT, RIGHT

        This method must return one of moves.MOVE
        """

        move = self.avoid_walls()
        if move==0:
            move=self.get_the_food()
        
        if len(self.all_trains[self.nickname]['wagons'])>10:
            move=self.depose_passengers()
        #moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
        #return random.choice(moves)
        #return Move.RIGHT
        return move
    





