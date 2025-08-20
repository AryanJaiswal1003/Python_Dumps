with open("Input/Names/invited_names.txt") as name_file: # Open the file containing the list of invited names

    with open("Input/Letters/starting_letter.txt") as letter_file:  # Open the file containing the letter template
        letter_template = letter_file.read() # Read the contents of the letter template into a variable

        # Loop through each name in the invited names file
        for name in name_file:
            stripped_name = name.strip() # Remove any whitespace (like newline characters) from the name
            personalized_letter = letter_template.replace("[name]", stripped_name) # Replace the placeholder [name] in the template with the actual name

            # Creating new personalized letter file for each name in the "ReadyToSend" folder
            with open(f"Output/ReadyToSend/{stripped_name}.txt", mode="w") as output_files:
                output_files.write(personalized_letter) # Write the personalized letter content

"""
[HINTS]
1. https://www.w3schools.com/python/ref_string_replace.asp
2. https://www.w3schools.com/python/ref_string_strip.asp
"""