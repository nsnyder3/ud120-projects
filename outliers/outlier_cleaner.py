#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    

    
    combined = [(age[0], actual[0], abs(actual[0] - prediction[0])) for prediction, actual, age in zip(predictions, net_worths, ages)]
    sorted_data = sorted(combined, key=lambda x: x[2], reverse=True)
    split_point = int(len(sorted_data) * .1)
    return sorted_data[split_point:]
