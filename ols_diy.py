import pandas as pd
import numpy as np
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='OLS DIY')
    parser.add_argument('training_file', type=str, help='Path to the CSV file with feature and target columns')
    parser.add_argument('predict_file', type=str, help='Path to the CSV file with values to predict')
    return parser.parse_args()

def calculate_coefficients(X, y):
    # Calculate means
    X_mean = np.mean(X)
    y_mean = np.mean(y)

    # Calculate slope (b₁)
    numerator = np.sum((X - X_mean) * (y - y_mean))
    denominator = np.sum((X - X_mean) ** 2)
    beta_1 = numerator / denominator

    # Calculate intercept (b₀)
    beta_0 = y_mean - beta_1 * X_mean

    return beta_0, beta_1

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Read data
    training_data = pd.read_csv(args.training_file)
    prediction_data = pd.read_csv(args.predict_file)

    # Extract features and target
    X = training_data['feature'].values
    y = training_data['target'].values

    # Calculate coefficients
    beta_0, beta_1 = calculate_coefficients(X, y)

    # Make predictions
    values_to_predict = prediction_data['values_to_predict'].values
    predictions = beta_0 + beta_1 * values_to_predict

    # Store results
    results = pd.DataFrame({
        'values_to_predict': values_to_predict,
        'predictions': predictions
    })
    results.to_csv('predictions.csv', index=False)
    
    # Print coefficients for verification
    print(f"\nCalculated coefficients:")
    print(f"b0 (intercept): {beta_0:.4f}")
    print(f"b1 (slope): {beta_1:.4f}")

if __name__ == '__main__':
    main()

  


    
