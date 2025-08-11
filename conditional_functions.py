def match_condition(conditions):
    """
    A function that mimics if-else-elif behavior using a list of conditions and actions.
    
    Args:
        conditions: A list of tuples where each tuple contains:
                    - A condition function that returns True/False
                    - An action function to execute if condition is True
    
    Returns:
        The result of the first matching action, or None if no conditions match
    """
    for condition_func, action_func in conditions:
        if condition_func():
            return action_func()
    return None

def switch_case(value, cases, default=None):
    """
    A function that mimics switch-case behavior.
    
    Args:
        value: The value to match against
        cases: A dictionary where keys are values to match and values are functions to execute
        default: A function to execute if no cases match (optional)
    
    Returns:
        The result of the matching case or default function
    """
    if value in cases:
        return cases[value]()
    elif default:
        return default()
    else:
        return None

# Example usage:
if __name__ == "__main__":
    # Example 1: Using match_condition
    x = 10
    
    result = match_condition([
        (lambda: x < 0, lambda: "Negative number"),
        (lambda: x == 0, lambda: "Zero"),
        (lambda: x > 0 and x < 10, lambda: "Positive single digit"),
        (lambda: x >= 10, lambda: "Positive double digit or larger")
    ])
    
    print(f"Result 1: {result}")
    
    # Example 2: Using switch_case
    day = "Monday"
    
    result2 = switch_case(
        day,
        {
            "Monday": lambda: "Start of work week",
            "Friday": lambda: "End of work week",
            "Saturday": lambda: "Weekend!",
            "Sunday": lambda: "Weekend!"
        },
        default=lambda: "Regular day"
    )
    
    print(f"Result 2: {result2}")