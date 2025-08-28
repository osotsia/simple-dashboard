import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


def prepare_and_export_model_data():
    """
    Loads the wine quality dataset, trains a classifier, and exports the test set
    predictions to a JSON file for the dashboard.
    """
    print("--- Step 1: Loading and Preparing Data ---")

    # Load the Red Wine Quality dataset directly from the UCI repository
    try:
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
        df = pd.read_csv(url, sep=';')
    except Exception as e:
        print(f"Error downloading or reading data: {e}")
        print("Please ensure you have an internet connection or download the file manually.")
        return

    # 'quality' is our target variable. The rest are features.
    X = df.drop('quality', axis=1)
    y = df['quality']

    # The classes are the unique quality scores.
    class_names = sorted(y.unique())
    print(f"Dataset loaded successfully. Found {len(df)} records.")
    print(f"Target classes (wine quality): {class_names}")

    # Split data into training and testing sets.
    # We use 'stratify=y' to ensure the class distribution is similar in train/test sets,
    # which is important for imbalanced datasets.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    print(f"Data split into {len(X_train)} training and {len(X_test)} testing samples.")

    print("\n--- Step 2: Training the Model ---")

    # We'll use a RandomForestClassifier. It's a good general-purpose model.
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Model training complete.")

    # Optional: Display a classification report to see how the model performed.
    print("\n--- Model Performance on Test Set (for reference) ---")
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred, zero_division=0))

    print("\n--- Step 3: Generating Data Payload for Dashboard ---")

    # Get the probability scores for each class on the test set.
    # This is an array where each row is a sample and each column is the probability for a class.
    # The order of columns corresponds to `model.classes_`.
    all_scores = model.predict_proba(X_test)

    # The final payload for our JSON file.
    # It will contain the class names and a list of all test cases.
    payload = {
        # The names of our classes, in the order the model predicts them.
        # e.g., [3, 4, 5, 6, 7, 8]
        "class_names": model.classes_.tolist(),

        # A list of all the individual cases from our test set.
        "test_cases": []
    }

    # Convert y_test to a numpy array for easier indexing.
    y_test_np = y_test.to_numpy()

    for i in range(len(y_test_np)):
        payload["test_cases"].append({
            # The ground truth label for this case.
            "true_class": int(y_test_np[i]),
            # The model's confidence scores for each class.
            # We round to 4 decimal places to keep the file size reasonable.
            "scores": [round(s, 4) for s in all_scores[i]]
        })

    print(f"Generated payload for {len(payload['test_cases'])} test cases.")

    print("\n--- Step 4: Exporting Data to JSON ---")

    # Write the payload to a file.
    output_filename = 'model_data.json'
    with open(output_filename, 'w') as f:
        json.dump(payload, f)

    print(f"Successfully exported data to '{output_filename}'.")
    print("This file is now ready to be used by the HTML dashboard.")


if __name__ == '__main__':
    prepare_and_export_model_data()