# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

def my_adder(a: int, b: int, c: int) -> int:
    """Takes the sum of 3 numbers.
    
    Calculates the sum of 3 integers using simple addition.
    
    Args:
        a (int): First interger to be sumed.
        b (int): Second integer to be sumed.
        c (int): Third integer to be sumed.

    Returns:
        int: the sum of the 3 integers.
    """
    
    # this is the summation
    out = a + b + c
    
    return out


def my_thermo_stat(temp: int, desired_temp: int) -> str:
    """Changes the status of the thermostat.

    Changes the status of the thermostat based on temperature and desired temperature.

    Args:
        temp (int): current temperature of the thermostat.
        desired_temp (int): desired temperature that indicates whether to change thermostat status.

    Returns:
        str: description of the current thermostat status.

    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status
    
 
def have_digits(s: str) -> int:
    """Checks if a string has digits.

    Loops over a string to check characters for numerical digits.

    Args:
        s: string that is to be checked for digits, of type str.

    Returns:
        out: 0 if no digits are present and 1 if digits are detected, of type int.
    """
    
    out = 0
    
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out
    
 
