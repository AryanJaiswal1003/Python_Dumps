# Squirrel Census Data Analysis

This project analyzes the **2018 Central Park Squirrel Census** dataset to categorize squirrels based on their **Primary Fur Color** and **Age**.

---

## Dataset
    --> The dataset used is:
        * 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
        * It contains various attributes about squirrels observed in Central Park, including their **fur color** and **age**.

---

## How It Works
    1. The script loads the dataset using `pandas`.
    2. It filters the data for each combination of:
          - **Fur Colors:** Gray, Black, Cinnamon  
          - **Ages:** Juvenile, Adult  
    3. Counts are calculated for each **Age + Color** category.
    4. The results are stored in a new CSV file called `squirrel_count.csv`.

---

## This file contains two columns:
    - **Category** → Combination of Age and Fur Color (e.g., "Juvenile_Gray")  
    - **Count** → Number of squirrels matching that category  