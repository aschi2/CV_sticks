#Game states
#The first entry describes the current players turn
i=0
while(i<10):
    print(i)
    i+=1

#(something) constructs a tuple, {} constructs a set

#List out all 15 hands for one player:
i = 0
j = 0
while(i < 5):
    while(j<5):
        hand = [i,j]
        print(hand)
        j+=1
    i+=1
    j=i


#We want to first define a turn in a way where we can edit the turn
class state:
    def __init__(self,turn, myhand, opphand):
        self.turn = turn
        self.myhand = myhand
        self.opphand = opphand
    def game_state(self):
        return(state(self.turn,self.myhand,self.opphand))
    def __str__(self):
        return(f"{(self.turn,self.myhand,self.opphand)}")


    
def change_turn(state):
    if(state.turn==1):
        state.turn = 2
    else:
        state.turn = 1

def attackhand(state,attacking,defending):
    if state.turn == 1:
        if state.myhand[attacking]==0 or state.opphand[defending]==0:
            raise Exception("That is not valid, go away")
        state.opphand[defending] = state.opphand[defending] + state.myhand[attacking]
        if state.opphand[defending] >=5:
            state.opphand[defending] = state.opphand[defending] - 5
        
    else:
        if state.opphand[attacking]==0 or state.myhand[defending]==0:
            raise Exception("That is not valid, go away")
        state.myhand[defending] = state.myhand[defending] + state.opphand[attacking]
        if state.myhand[defending]>=5:
            state.myhand[defending] = state.myhand[defending] - 5
    change_turn(state)
    if(state.myhand==[0,0]):
        print("Player 2 wins, suck it player 1")
    if(state.opphand==[0,0]):
        print("Player 1 wins, go rub it in player 2's face")
    print(state)

def split_helper(hand):
    if (hand[0] == 2 or hand[0]==4) and hand[1] ==0:
        hand = [int(hand[0]/2),int(hand[0]/2)]
        return(hand)
    elif (hand[1] == 2 or hand[1]==4) and hand[0] ==0:
        hand = [int(hand[1]/2),int(hand[1]/2)]
        return(hand)
    else:
        raise Exception("That is not valid, go away")
    print(hand)

def split(state):
    if state.turn==1:
        state.myhand = split_helper(state.myhand)    
    else:
        state.opphand = split_helper(state.opphand)
    change_turn(state)
    print(state)


new_game = state(1,[1,1],[1,1])
attackhand(new_game,0,0)
attackhand(new_game,1,0)
attackhand(new_game,1,1)
attackhand(new_game,0,0)
attackhand(new_game,1,0)
attackhand(new_game,0,1)
attackhand(new_game,0,0)
attackhand(new_game,1,1) #We have a loop!!!
attackhand(new_game,1,0)
attackhand(new_game,1,0)
attackhand(new_game,0,0)
attackhand(new_game,0,0)
attackhand(new_game,1,0)
split(new_game)
attackhand(new_game,1,0)
attackhand(new_game,0,1)
attackhand(new_game,1,0)
attackhand(new_game,1,1)
attackhand(new_game,1,1) #Player 1 wins, go rub it in player 2s face
print(game.turn)
print(game.opphand)
print(game)

#Next steps: Flask to create a web app
#Teach html, css, javascript