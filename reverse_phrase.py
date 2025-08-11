def reverse_phrase(phrase):
    """
    Reverses the letters in a given phrase.
    
    Args:
        phrase (str): The input phrase to reverse
        
    Returns:
        str: The phrase with letters reversed
    """
    return phrase[::-1]

def main():
    # Get input from user
    user_phrase = input("Enter a phrase to reverse: ")
    
    # Reverse the phrase
    reversed_phrase = reverse_phrase(user_phrase)
    
    # Display the result
    print(f"Original phrase: {user_phrase}")
    print(f"Reversed phrase: {reversed_phrase}")

if __name__ == "__main__":
    main()