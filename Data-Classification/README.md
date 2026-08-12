Data Classification Using AI Project Description 

This project demonstrates a basic machine learning classification model using the Iris dataset.

The goal is to load and understand a dataset, split the data into training and testing sets, train a classification algorithm, and evaluate its performance.

The project uses Logistic Regression to classify iris flowers into one of three species based on their measurements.

Technologies Used 
Python 
Scikit-learn 
Machine Learning Logistic 
Regression Dataset 

The project uses the built-in Iris dataset provided by Scikit-learn.

The dataset contains:

150 samples 
4 input features 
3 flower classes 
Features Sepal length Sepal width Petal length Petal width Classes Setosa Versicolor Virginica Project Workflow 
Load Dataset 
      ↓ 
Understand Dataset
      ↓ 
  Split Data 
      ↓ 
Feature Scaling
      ↓
 Train Classification Model 
      ↓ 
Make Predictions
      ↓ 
Evaluate Model Requirements 

Make sure Python is installed on your computer.

Install the required dependency:

pip install -r requirements.txt How to Run 

Clone or download the project.

Open the project folder in a terminal:

cd data-classification 

Install dependencies:

pip install -r requirements.txt 

Run the program:

python classification.py Model Used Logistic Regression 

Logistic Regression is a supervised machine learning classification algorithm.

In this project, it learns the relationship between flower measurements and their species.

The model is trained using 80% of the dataset and tested using the remaining 20%.

Expected Output 

The program displays information such as:

Dataset loaded successfully! Number of samples: 150 Number of features: 4 Classes: ['setosa' 'versicolor' 'virginica'] Training samples: 120 Testing samples: 30 Model trained successfully! Model Accuracy: XX.XX % Classification Report: ... Predicted flower: setosa 

The exact accuracy may vary slightly depending on the model configuration.

Key Skills Demonstrated Dataset loading Data preprocessing Train-test splitting Supervised learning Classification Model training Model prediction Model evaluation Project Structure data-classification/
 │
 ├── classification.py
 ├── requirements.txt
 └── README.md 

Conclusion 

This project provides a simple introduction to supervised machine learning and demonstrates how a classification model can learn from existing data and predict the category of new data.

