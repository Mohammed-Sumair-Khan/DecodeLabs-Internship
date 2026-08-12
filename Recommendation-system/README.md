Recommendation System Using User Preferences

 Project Title 

Simple Recommendation System

Description 

This project is a basic recommendation system built using Python. It takes user preferences such as preferred category and favorite genres, compares them with available items, calculates a matching score, and recommends the items that best match the user's interests.

The project demonstrates the basic concept of a recommendation system using logic and pattern matching.

Features Takes user preferences as input Supports movie and series categories Accepts multiple favorite genres Matches user preferences with available items Calculates a recommendation score Sorts recommendations based on the highest score Displays matching recommendations Technologies Used Python 3 Lists Dictionaries Functions Conditional statements Loops Sorting String processing How It Works 

The system assigns scores based on matching preferences:

Matching category → +2 points 
Each matching genre → +1 point 

Items with higher scores are considered better recommendations and are displayed first.

Project Structure 
recommendation-system/ 
│ 
├── recommendation.py 
└── README.md 

How to Run 

1. Install Python 

Make sure Python 3 is installed on your computer.

Check the installation:

python --version 

2. Run the program 

Open the project folder in a terminal and run:

python recommendation.py 

3. Enter Preferences 

Example:

What do you prefer? (movie/series): movie Enter your favorite genres separated by commas (e.g. action, thriller): action, thriller Example Output ===== Recommended Items ===== The Dark Knight - Match Score: 4 Inception - Match Score: 4 Interstellar - Match Score: 1 Learning Outcomes 

Through this project, you will learn:

How to collect user input How to store data using lists and dictionaries How to compare user preferences How to implement matching logic How to calculate recommendation scores How to sort results Basic concepts of recommendation systems Future Improvements 

The system can be improved by adding:

More movies and series User ratings Multiple users Machine learning-based recommendations Cosine similarity A graphical user interface A database for storing user preferences Personalized recommendations based on previous choices Conclusion 

This project provides a simple introduction to recommendation systems by using user preferences, logical matching, and scoring. It is suitable for understanding the basic concepts before moving to more advanced machine-learning recommendation systems.

