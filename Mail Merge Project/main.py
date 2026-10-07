from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
NAMES_FILE = PROJECT_DIR / "Input" / "Names" / "invited_names.txt"
LETTER_FILE = PROJECT_DIR / "Input" / "Letters" / "starting_letter.txt"
OUTPUT_DIR = PROJECT_DIR / "Output" / "ReadyToSend"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

with NAMES_FILE.open(encoding="utf-8") as name_file: # Open the file containing the list of invited names

    with LETTER_FILE.open(encoding="utf-8") as letter_file:  # Open the file containing the letter template
        letter_template = letter_file.read() # Read the contents of the letter template into a variable

        # Loop through each name in the invited names file
        for name in name_file:
            stripped_name = name.strip() # Remove any whitespace (like newline characters) from the name
            personalized_letter = letter_template.replace("[name]", stripped_name) # Replace the placeholder [name] in the template with the actual name

            # Creating new personalized letter file for each name in the "ReadyToSend" folder
            with (OUTPUT_DIR / f"{stripped_name}.txt").open(mode="w", encoding="utf-8") as output_files:
                output_files.write(personalized_letter) # Write the personalized letter content

"""
[HINTS]
1. https://www.w3schools.com/python/ref_string_replace.asp
2. https://www.w3schools.com/python/ref_string_strip.asp
"""