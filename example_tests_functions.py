def area_of_rectangle(width: float | int, height: float | int) -> float:
    """This function calculates the area of a rectangle.
    
    The function takes in height and width of a rectangle, the area is then computed using width x height.

    Args:
        width (float): numerical value for width of rectangle.
        height (float): numerical value for height of rectangle.
    
    Returns:
        float: Area of the rectangle based on height and width inputs.
    """
    area = width * height
    return area


def perimeter_of_rectangle(width: float | int, height: float | int) -> float:
    """This function calculates the perimeter of a rectangle.
    
    The function takes in height and width of a rectangle, the perimeter is then computed using 2(width) + 2(height).

    Args:
        width (float): numerical value for width of rectangle.
        height (float): numerical value for height of rectangle.
    
    Returns:
        float: Perimeter of the rectangle based on height and width inputs.
    """
    perimeter = (2 * width) + (2 * height)
    return perimeter
