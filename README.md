# String Analysis Program

A Python program that analyzes the composition of characters in a string and calculates the percentage of uppercase letters, lowercase letters, digits, and other characters (symbols).

## Features

- **Character Type Analysis**: Categorizes each character as:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Other characters (symbols, spaces, punctuation)

- **Percentage Calculation**: Computes accurate percentages for each category

- **Edge Case Handling**: Properly handles:
  - Empty strings
  - None values
  - Single character strings
  - Strings with only one type of character

- **Comprehensive Comments**: Well-documented code with detailed explanations

## Usage

### Running the Interactive Program

```bash
python3 string_analysis.py
```

The program will prompt you to enter a string and will display the analysis results.

### Running Tests

To run the comprehensive test suite, edit the `string_analysis.py` file and uncomment the line:

```python
# run_tests()  # Uncomment this line
```

Then run:

```bash
python3 string_analysis.py
```

### Using as a Module

```python
from string_analysis import analyze_string, format_output

# Analyze a string
input_string = "Client.1234@litwork.in"
percentages = analyze_string(input_string)

# Format and print the output
output = format_output(percentages)
print(output)
```

## Examples

### Example 1: Email Address Analysis

**Input:** `My e-mail: eMail Address321@anymail.com`

**Output:**
```
7.692%
66.667%
7.692%
17.949%
```

**Breakdown:**
- Uppercase letters: 7.692%
- Lowercase letters: 66.667%
- Digits: 7.692%
- Other characters: 17.949%

### Example 2 (Exercise-1)

**Input:** `Support1@litwork.in`

**Output:**
```
5.263%
78.947%
5.263%
10.526%
```

### Example 3 (Exercise-2)

**Input:** `Client.1234@litwork.in`

**Output:**
```
4.545%
63.636%
18.182%
13.636%
```

## Output Format

The program outputs four lines, each representing a percentage with 3 decimal places:

1. Percentage of uppercase letters
2. Percentage of lowercase letters
3. Percentage of digits
4. Percentage of other characters (symbols)

## Error Handling

The program handles the following error cases:

- **Empty String**: Raises `ValueError` with message "Input string cannot be empty"
- **None Value**: Raises `ValueError` with message "Input string cannot be None"

## Requirements

- Python 3.x (no external dependencies required)

## File Structure

```
Dataset/
├── string_analysis.py    # Main program file
├── README.md            # This file
└── Toyota.csv           # Dataset file
```

## Author

String Analysis Solution - December 2025
