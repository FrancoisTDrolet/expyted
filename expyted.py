from scipy.stats import binom

def binomial(success,trials,probability):
    k = success
    n = trials
    p = probability
    
    return binom.pmf(k,n,p)

class Binomial_Data:
    def __init__(self):
        self.data = []
        self.n = 0
    
    def smooth(self):
        newData = []
        for datum in self.data:
            newData.append([self.expected(datum[0]*100,datum[1])/100.0,datum[1]])
        self.data = newData
        
    def add_to_data(self,rate,n):
        self.data.append([float(rate)/100,n])
        self.n += n
        
    def expected(self,observed_rate,trials):
        normal = 0.0
        prop = 0.0
        for datum in self.data:
            x = datum[0]
            p_u_e_x = float(datum[1])/self.n
            p_o_g_x = binomial(int(round(observed_rate/100.0*trials*0.36)),round(trials*0.36),x)
            normal += p_u_e_x*p_o_g_x*datum[1]
            prop += x*p_u_e_x*p_o_g_x*datum[1]
        return prop/normal*100
        
        
        
        
def get_Binomial_Data_For_3Bet():
    file = open("Report.csv")
    out = Binomial_Data()
    for line in file:
        data = line.split(",")
        if data[0] == "\"E_Nelligan\"":
            continue
        elif data[7] == "na":
            continue
        
        out.add_to_data(float(data[6])*100,int(data[2])*0.36)
    file.close()
    return out
 
def get_Binomial_Data_For_FCBet():
    print "need update"
    return
    file = open("PlayerGrid.csv")
    out = Binomial_Data()
    for line in file:
        data = line.split(",")
        if data[0] == "E_Nelligan" or data[0] == "Player Name":
            continue
        elif data[16] == "na":
            continue
        
        out.add_to_data(float(data[16]),int(data[2]))
    file.close()
    return out

def get_Binomial_Data_For_TCBet():
    print "need update"
    return
    file = open("PlayerGrid.csv")
    out = Binomial_Data()
    for line in file:
        data = line.split(",")
        if data[0] == "E_Nelligan" or data[0] == "Player Name":
            continue
        elif data[17] == "na":
            continue
        
        out.add_to_data(float(data[17]),int(data[2]))
    file.close()
    return out
    
def get_Binomial_Data_For_RCBet():
    print "need update"
    return
    file = open("PlayerGrid.csv")
    out = Binomial_Data()
    for line in file:
        data = line.split(",")
        if data[0] == "E_Nelligan" or data[0] == "Player Name":
            continue
        elif data[18] == "na":
            continue
        
        out.add_to_data(float(data[18]),int(data[2]))
    file.close()
    return out

if __name__ == "__main__":
    data3Bet = get_Binomial_Data_For_3Bet()    
    b3 = data3Bet.expected
    