def count_apples_and_oranges(s: int, t: int, a: int, b: int, apples: list, oranges: list) -> None:
    """
    Counts and prints the number of apples and oranges that land on the house.

    Args:
        s (int): Starting point of the house.
        t (int): Ending point of the house.
        a (int): Location of the apple tree.
        b (int): Location of the orange tree.
        apples (list): List of distances at which apples fall from the tree.
        oranges (list): List of distances at which oranges fall from the tree.
    """
    
    # Calculate landing positions
    apples_landing = [a + apple for apple in apples]
    oranges_landing = [b + orange for orange in oranges]

    # Count apples and oranges landing on the house
    count_apples = sum(s <= apple <= t for apple in apples_landing)
    count_oranges = sum(s <= orange <= t for orange in oranges_landing)

    # Print the results
    print(count_apples)
    print(count_oranges)
