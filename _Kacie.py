####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'cx'
strategy_name = 'Win'
strategy_description = 'Always Win'
    
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
    
def move(my_history, their_history, my_score, their_score):    
   
    i = 0
    for round in their_history[0:6]:
        if round == 'b':
            i+=1
    if i < 3:
        return tft(my_history, their_history)
    elif i == 3 and len(their_history):
        return stft(my_history[6:], their_history[6:])
    else:
        return 'b'
        
        