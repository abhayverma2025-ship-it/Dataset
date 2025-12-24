"""
String Analysis Program

This program analyzes the composition of characters in a string (typically email addresses)
and calculates the percentage of:
- Uppercase letters
- Lowercase letters
- Digits
- Other characters (symbols like @, ., -, etc.)

Author: String Analysis Solution
Date: 2025-12-24
"""


def analyze_string(input_string):
    """
    Analyzes a string and returns the percentage of character types.
    
    Args:
        input_string (str): The string to analyze
        
    Returns:
        tuple: Four float values representing percentages of:
               (uppercase, lowercase, digits, other_chars)
               
    Raises:
        ValueError: If input_string is None or empty
    """
    # Handle edge case: None or empty string
    if input_string is None:
        raise ValueError("Input string cannot be None")
    
    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty")
    
    # Initialize counters for each character type
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    other_count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        if char.isupper():
            # Character is an uppercase letter (A-Z)
            uppercase_count += 1
        elif char.islower():
            # Character is a lowercase letter (a-z)
            lowercase_count += 1
        elif char.isdigit():
            # Character is a digit (0-9)
            digit_count += 1
        else:
            # Character is something else (symbol, space, punctuation, etc.)
            other_count += 1
    
    # Calculate total length of the string
    total_length = len(input_string)
    
    # Calculate percentages for each category
    # Using (count / total) * 100 to get percentage
    uppercase_percentage = (uppercase_count / total_length) * 100
    lowercase_percentage = (lowercase_count / total_length) * 100
    digit_percentage = (digit_count / total_length) * 100
    other_percentage = (other_count / total_length) * 100
    
    # Return all four percentages as a tuple
    return (uppercase_percentage, lowercase_percentage, digit_percentage, other_percentage)


def format_output(percentages):
    """
    Formats the percentage output with 3 decimal places.
    
    Args:
        percentages (tuple): Tuple of four percentage values
        
    Returns:
        str: Formatted string with each percentage on a new line
    """
    # Format each percentage with exactly 3 decimal places
    output_lines = []
    for percentage in percentages:
        # Round to 3 decimal places and format with % symbol
        output_lines.append(f"{percentage:.3f}%")
    
    # Join all lines with newline character
    return "\n".join(output_lines)


def main():
    """
    Main function to run the string analysis program.
    Prompts user for input and displays the analysis results.
    """
    print("String Analysis Program")
    print("=" * 50)
    print("This program analyzes character composition in strings.")
    print("=" * 50)
    
    try:
        # Get input from user
        input_string = input("\nInput:\n")
        
        # Analyze the string
        percentages = analyze_string(input_string)
        
        # Format and display output
        output = format_output(percentages)
        print("\nOutput:")
        print(output)
        
        # Display detailed breakdown (optional, for debugging)
        print("\n" + "=" * 50)
        print("Breakdown:")
        print(f"Uppercase letters: {percentages[0]:.3f}%")
        print(f"Lowercase letters: {percentages[1]:.3f}%")
        print(f"Digits: {percentages[2]:.3f}%")
        print(f"Other characters (symbols): {percentages[3]:.3f}%")
        print("=" * 50)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Test cases to verify the solution
def run_tests():
    """
    Runs test cases to verify the correctness of the solution.
    """
    print("Running Test Cases...")
    print("=" * 50)
    
    # Test case from problem statement
    test1 = "My e-mail: eMail Address321@anymail.com"
    print(f"\nTest 1: '{test1}'")
    result1 = analyze_string(test1)
    print(format_output(result1))
    print(f"Expected: 7.5%, 65%, 7.5%, 20%")
    print(f"Actual: {result1[0]:.1f}%, {result1[1]:.0f}%, {result1[2]:.1f}%, {result1[3]:.0f}%")
    
    # Exercise 1
    test2 = "Supportl@litwork.in"
    print(f"\nTest 2 (Exercise-1): '{test2}'")
    result2 = analyze_string(test2)
    print(format_output(result2))
    print(f"Expected: 5.263%, 78.947%, 5.263%, 10.526%")
    
    # Exercise 2
    test3 = "Client.1234@litwork.in"
    print(f"\nTest 3 (Exercise-2): '{test3}'")
    result3 = analyze_string(test3)
    print(format_output(result3))
    print(f"Expected: 4.545%, 63.636%, 18.182%, 13.636%")
    
    # Edge case: String with only one type of character
    print("\n" + "=" * 50)
    print("Edge Cases:")
    print("=" * 50)
    
    test4 = "ABCDEFG"
    print(f"\nEdge Case 1: Only uppercase - '{test4}'")
    result4 = analyze_string(test4)
    print(format_output(result4))
    
    test5 = "abcdefg"
    print(f"\nEdge Case 2: Only lowercase - '{test5}'")
    result5 = analyze_string(test5)
    print(format_output(result5))
    
    test6 = "1234567"
    print(f"\nEdge Case 3: Only digits - '{test6}'")
    result6 = analyze_string(test6)
    print(format_output(result6))
    
    test7 = "@#$%^&*"
    print(f"\nEdge Case 4: Only symbols - '{test7}'")
    result7 = analyze_string(test7)
    print(format_output(result7))
    
    test8 = "A"
    print(f"\nEdge Case 5: Single character - '{test8}'")
    result8 = analyze_string(test8)
    print(format_output(result8))
    
    # Test error handling
    print("\n" + "=" * 50)
    print("Error Handling Tests:")
    print("=" * 50)
    
    try:
        print("\nTesting empty string:")
        analyze_string("")
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    try:
        print("\nTesting None value:")
        analyze_string(None)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    print("\n" + "=" * 50)
    print("All tests completed!")
    print("=" * 50)


if __name__ == "__main__":
    # Uncomment the line below to run tests
    # run_tests()
    
    # Run the main interactive program
    main()
