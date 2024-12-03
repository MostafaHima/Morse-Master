# Morse Code Converter

This is a simple Python script that converts any text input into Morse code. The script allows users to input text, checks for valid characters that can be converted into Morse code, and outputs the result.

## Features

- Converts English letters (A-Z) and numbers (0-9) into Morse code.
- Supports common punctuation marks such as `.` `,` `!` `@` `/` and others.
- Handles invalid characters by listing them separately.

## How to Use

1. Run the script in your Python environment.
2. Enter any text when prompted.
3. The script will:
   - Output the equivalent Morse code for valid characters.
   - Notify you of any invalid characters that cannot be converted.

## Example

### Input:
- Write your text here without spaces: Hello, World!
### Output:
- Morse Code Translation: •••• • •-•• •-•• --- --..-- .-- --- •-• •-•• -•• -.-.--

## Supported Characters

- **Letters**: A-Z (case-insensitive)
- **Numbers**: 0-9
- **Punctuation**: `. , ! @ / & ( ) + = " : '`

## Notes

- Characters not found in the Morse code dictionary are treated as invalid and listed in the output.
- The script is fully customizable and can be extended to include more symbols.
