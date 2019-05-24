

class stree:
    def __init__(self,game_state):
        self.valid_moves = []
        if 'prev_moves' not in globals():
            globals()['prev_moves'] = set()
        else:
            global prev_moves
            prev_moves.add(f'{game_state}')
        self.game_state = game_state
        self.p_turn,self.L1,self.R1,self.L2,self.R2 = game_state
        self.playing = True
        self.split = None
        self.L1 = self.check_bust(self.L1)
        self.R1 = self.check_bust(self.R1)
        self.L2 = self.check_bust(self.L2)
        self.R2 = self.check_bust(self.R2)
        self.LL = None
        self.LR = None
        self.RR = None
        self.RL = None

        if self.L1 == 0 and self.R1 ==0:
            self.playing = False
            self.winner = 2

        elif self.L2 == 0 and self.R2 == 0:
            self.playing = False
            self.winner = 1
        else:
            pass
        
        if self.playing == True:
            if self.p_turn == 1:
                if self.L1 != 0 and self.L2 !=0:
                    self.LL = stree((2, self.L1, self.R1, self.L2 + self.L1, self.R2))
                if self.L1 !=0 and self.R2!=0:
                    self.LR = stree((2,self.L1, self.R1, self.L2, self.R2 + self.L1))
                if self.R1 !=0 and self.L2!=0:
                    self.RL = stree((2,self.L1, self.R1, self.L2 + self.R1, self.R2))
                if self.R1 !=0 and self.R2!=0:
                    self.RR = stree((2,self.L1, self.R1, self.L2, self.R2 + self.R1))
            else:
                if self.L1 !=0 and self.L2!=0:
                    self.LL = stree((1, self.L1 + self.L2, self.R1, self.L2, self.R2))
                if self.L2 !=0 and self.R1!=0:
                    self.LR = stree((1, self.L1, self.R1 + self.L2, self.L2, self.R2))
                if self.R2 !=0 and self.L1!=0:
                    self.RL = stree((1, self.L1 + self.R2, self.R1, self.L2, self.R2))
                if self.R2 !=0 and self.R1!=0:
                    self.RR = stree((1, self.L1, self.R1 + self.R2, self.L2, self.R2))
            
            if self.p_turn == 1:
                self.bsplit,self.wsplit = self.check_split(self.L1,self.R1)
                if self.bsplit:
                    if self.wsplit == 'L':
                        if f'{(2, int(self.L1/2), int(self.L1/2), self.L2, self.R2)}' not in prev_moves:
                            self.split = stree((2, int(self.L1/2), int(self.L1/2), self.L2, self.R2))
                    else:
                        if f'{(2,  int(self.R1/2), int(self.R1/2), self.L2, self.R2)}' not in prev_moves:
                            self.split = stree((2,  int(self.R1/2), int(self.R1/2), self.L2, self.R2))


            if self.p_turn == 2:
                self.bsplit,self.wsplit = self.check_split(self.L2,self.R2)
                if self.bsplit:
                    if self.wsplit == 'L':
                        if f'{(2, self.L1, self.R1, int(self.L2/2), int(self.L2/2))}' not in prev_moves:
                            self.split = stree((2, self.L1, self.R1, int(self.L2/2), int(self.L2/2)))
                    else:
                        if f'{(2,  self.L1, self.R1, int(self.R2/2), int(self.R2/2))}' not in prev_moves:
                            self.split = stree((2,  self.L1, self.R1, int(self.R2/2), int(self.R2/2)))
        if self.LL!=None:
            self.valid_moves.append(self.LL)
        if self.LR!=None:
            self.valid_moves.append(self.LR)
        if self.RL!=None:
            self.valid_moves.append(self.RL)
        if self.RR!=None:
            self.valid_moves.append(self.RR)
        if self.split!=None:
            self.valid_moves.append(self.split)

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

    def __len__(self):
        return(1)

    def __str__(self):
        return(f"{self.game_state}")

