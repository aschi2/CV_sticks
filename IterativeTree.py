



class sTree:
    def __init__(self,game_state):
        self.LL = None
        self.LR = None
        self.RL = None
        self.RR = None
        self.split = None
        self.game_state = game_state
        self.p_turn,self.L0,self.R0,self.L1,self.R1 = game_state
        self.L1 = self.check_bust(self.L1)
        self.R1 = self.check_bust(self.R1)
        self.L2 = self.check_bust(self.L2)
        self.R2 = self.check_bust(self.R2)
        self.playing = True
        if self.L0 == 0 and self.R0 ==0:
            self.playing = False
            self.winner = 0
            self.score = 10
        elif self.L1 == 0 and self.R1 == 0:
            self.playing = False
            self.winner = 1
            self.score = -10
        else:
            pass

    def all_children(self):
        nxt_p = (self.p_turn+1)%2
        L1_shift = self.L1*self.p_turn
        L0_shift = self.L0*(1-self.p_turn)
        R1_shift = self.L1*self.p_turn
        R0_shift = self.R0*self.p_turn
        if self.L1!= 0 and self.L2 != 0:
            self.LL = sTree((nxt_p , self.L0 + L1_shift , self.R0 , self.L1+L0_shift ,self.R1))
        if self.R1!=0 and self.R2 != 0:
            self.RR = sTree((nxt_p , self.L0, self.R0+R1_shift, self.L1, self.R1+R0_shift))
        if (self.L1!=0 and self.R0 != 0 and self.p_turn == 1) or (self.R1!=0 and self.L0 !=0 and self.p_turn==0):
            self.LR = sTree((nxt_p , self.L0 , self.R0 + L1_shift , self.L1 , self.R1 + L0_shift))
        if (self.L0!=0 and self.R1 != 0 and self.p_turn == 1) or (self.R0!=0 and self.L1 !=0 and self.p_turn==0):
            self.RL = sTree((nxt_p , self.L0 + R1_shift, self.R0, self.L1 + R0_shift,self.R1))

        if self.p_turn==1:
            self.splitb,self.splitw = self.check_split(self.L0,self.R0)
            if self.splitb:
                if self.wsplit == 'L':
                    self.split = stree((0, self.L0, self.R0, int(self.L1/2), int(self.L1/2)))
                else
                    self.split = stree((0,))
        if self.p_turn==1:
            self.splitb,self.splitw = self.check_split(self.L1,self.R1)
        
    
        
    def check_bust(self,hand):
        if hand >=5:
            return(0)
        else:
            return(hand)
    def check_bust(self,hand):
        if hand >=5:
            return(0)
        else:
            return(hand)
    def check_split(self,L,R):
        if L==0 and R%2 ==0:
            return((True,'R'))
        elif R==0 and L%2 ==0:
            return((True,'L'))
        else:
            return((False,None))
#The two players playing are "Player 0" and "Player 1" so that 
root = sTree((0,1,1,1,1))
