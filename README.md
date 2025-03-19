# OLS
1.- Ordinary Least Squares Do It Yourself (50 points)

Create a program with the following characteristics:

Name: ols_diy.py
Accepts 2 csv files (2 paths pointing to 2 csv files)
The first csv file has 2 columns with titles feature and target
The second file as one column named values_to_predict
Using the information in the first file and the OLS formulas for univariate linear regression the program needs to calculate the values of b0 and b1 of a linear regression of the form y = b0 + b1 * x


Once the b0 and b1 have been calculated the program needs to calculate the predictions for the values in the second file and store them in a csv predictions.csv with just two columns (values_to_predict and predictions)
b0 and b1 have to be calculated in the program, no libraries can be used to obtain them. ie you can use numpy, pandas, etc but not scikit learn, statsmodel or similar.
No loops are allowed in the code