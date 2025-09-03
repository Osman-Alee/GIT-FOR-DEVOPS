def describe_number(number: int) -> str:
    """
    Returns a description of the input number as positive, negative, or zero.

    Args:
        number (int): The number to describe.

    Returns:
        str: A description of the number.
    """
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."


# Example usage
if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    result = describe_number(user_input)
    print(result)
