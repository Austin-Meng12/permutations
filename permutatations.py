def permutations(LIST):
    NUMBER = []

    if len(LIST) <= 1:    # Base Case
        return LIST
    else:
        for i in range(len(LIST)):
            FIXED = LIST[i]
            left = LIST[:i] + LIST[i+1:] # What is remaining
            VAL = permutations(left)
            print(len(VAL))
            for i in range(len(VAL)):
                if type(VAL[i]) == list:
                    VAL[i].insert(0,FIXED)
                else:
                    VAL[i] =  [FIXED,VAL[i]]
                    
                NUMBER.append(VAL[i])
        
        
      
        return NUMBER







n = 3
NUM = []
TOTAL = []
for i in range(1,n+1):
    NUM.append(i)
VALUE = permutations(NUM)
#print(len(VALUE))
