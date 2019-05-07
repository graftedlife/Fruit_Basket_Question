#!/usr/bin/env python
# coding: utf-8



import numpy as np

fruit_basket = {'apple': 7, 'banana': 3, 'orange': 5}

def pick_fruit(fruit_basket:dict):
    '''
    This function takes a dictionary of fruit basket as input 
    and rutrns a fruit picked from the basket 
    according to the likelihood of picking each fruit.
    
    Note: The maximal capacity of this function is 
    to handle quanties within the precision range of float128, 
    which should be reasonably large enough to meet the requirement 
    of this task.
    
    Input: A dictionary whose keys are fruit names (str) 
           and values are their corresponding quantities.
    Output: The label of the picked fruit (str).
    '''  
    #First calculate the probabilities of picking each fruit
    total = sum([np.float128(v) for v in fruit_basket.values()])
    if total == float('inf'):
        return('Quantities of fruit exceed the maximal precision of float128.')
    probs = {key:np.float128(value)/total for (key,value) in fruit_basket.items()}
    
    #Then pick a fruit according to the probabilities of picking each type of fruit
    picked_fruit_label = np.random.choice(list(probs.keys()), 1, p = list(probs.values()))[0]
    return(picked_fruit_label)

pick_fruit(fruit_basket)