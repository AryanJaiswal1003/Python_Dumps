import pandas

# Load the squirrel census dataset into a DataFrame
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# Define the fur colors and ages we want to categorize
primary_fur_color = ["Gray", "Black", "Cinnamon"]
ages = ["Juvenile", "Adult"]

squirrel_count = {} # Dictionary to hold counts of squirrels by (age + fur color) combination

# Loop through each color and age to filter and count matching squirrels
for color in primary_fur_color:
    for age in ages:
        census = data[(data["Primary Fur Color"] == color) & (data["Age"] == age)] # Filter the dataset where both fur color and age match
        count = len(census) # Count the number of rows that match
        squirrel_count[f"{age}_{color}"] = count # Store in dictionary with key format: "Age_Color"


# Convert dictionary to DataFrame for easy saving/analysis
df = pandas.DataFrame(list(squirrel_count.items()), columns=['Category', 'Count'])
df.to_csv("squirrel_count.csv", index = False) # Save results into a CSV file (Category vs Count)