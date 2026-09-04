
""" Function returns the time in minutes for the drone
    return type float
    argument is a float value for the weight of payload in grams"""

def calculate_flight_time(weight_grams):
    if (weight_grams < 0):
        raise ValueError("Weight cannot be negative")

    t = (180 - 0.1 * weight_grams)
    
    result = t if t > 0 else 0
    return result

""" Function prints time table for the fligth times up
     to 1st argument max_weight_grams. Each print increments
       by the step_gram argument"""

def flight_time_table(max_weight_grams,step_grams):
    current_grams = 0
    while(current_grams <= max_weight_grams):
        print(calculate_flight_time(current_grams))
        current_grams += step_grams


    
