team_name = 'cx'
strategy_name = 'Beat Lucas'
strategy_description = 'Do random things in an attempt to win'

#test
def fbf(my_history, their_history):
    if len(my_history) == 0:
        return 'c'
    elif 'b' in their_history:
        return 'b'
    else:
        return 'c'
    
def rtft(my_history, their_history):
    if len(my_history) == 0:
        return 'b'
    elif their_history[-1] == 'b':
        return 'c'
    else:
        return 'b'
        
def collective(my_history, their_history):
    if len(my_history) == 0:
        return 'c'
    elif len(my_history) == 1:
        return 'b'
    elif their_history[-1] and their_history[-2] == 'b':
            return 'b'
    else:
        if their_history[-1] == 'b':
            return 'c'
        else:
            return 'b'
        
def tft(my_history, their_history):
    if len(my_history) == 0:
        return 'c'
    else:
        return (their_history[-1])
    
def stft(my_history, their_history):
    if len(my_history) == 0:
        return 'b'
    else:
        return tft(my_history, their_history)
 #end
   
def move(my_history, their_history, my_score, their_score):  
   
    if len(their_history) > 6:
   
        i = 0
        for round in their_history[-6:]:
            if round == 'b':
                i+=1
        if i < 3:
            return fbf(my_history, their_history)
        elif i == 3 and len(their_history):
            return collective(my_history[-6:], their_history[-6:])
        else:
            return 'b'
    else:
        return tft(my_history, their_history)
            
        