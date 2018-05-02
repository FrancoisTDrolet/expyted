from scipy.stats import binom

FACING_A_RAISE_RATE = 0.4044

class Universe:
    def __init__(self):
        self.excluded_players = []
        self.three_bets = []
        
    def build_from_file(self,file_name):
        file = open(file_name,"r")
        lines_count = 0
        for line in file.readlines():
            if lines_count<20:
                lines_count += 1
                continue
            
            line_data = line.split(",")
            player_name = line_data[0]
                
            if player_name in self.excluded_players:
                continue
                
            name_fuck_corrector = 0
            
            if line_data[1] != "2":
                for i in range(50):
                    if line_data[i]== "2":
                        name_fuck_corrector = i-1
                        break
                
            player_number_of_hands = int(line_data[2+name_fuck_corrector])
            player_three_bet_rate = float(line_data[6+name_fuck_corrector])
            
            if player_number_of_hands > 5:
                rate = player_three_bet_rate
                trials = player_number_of_hands*FACING_A_RAISE_RATE
                self.three_bets.append([rate, trials])
            
            
        file.close()
        
    def refine_three_bets(self):
        n = 0
        new_three_bets = []
        for event in self.three_bets:
            new_rate = expected_three_bet(event[0],
                                          event[1]/FACING_A_RAISE_RATE, self)
            new_three_bets.append([new_rate,event[1]])
        self.three_bets = new_three_bets

def binomial(success,trials,probability):
    k = success
    n = trials
    p = probability
    
    return binom.pmf(k,n,p)
    
def expected_three_bet(observed_three_bet_rate, hands, universe):
    crazy_sum = 0
    normalizer = 0
    trials = int(hands*FACING_A_RAISE_RATE)
    three_bets_count = int(observed_three_bet_rate*trials)
    for event in universe.three_bets:
        bayes = binomial(three_bets_count,trials,event[0])*event[1]
        normalizer += bayes
        crazy_sum += bayes*event[0]
        
    return crazy_sum/normalizer

    
if __name__=="__main__":
    u = Universe()
    u.build_from_file("Report.csv")
    #u.refine_three_bets()
    print expected_three_bet(0.05,60,u)
        