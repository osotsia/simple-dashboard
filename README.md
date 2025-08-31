# simple-dashboard

A static HTML dashboard for visualizing the performance of a machine learning-based automation process. 

## Usage

1.  Clone the repository to your local machine:
2.  Navigate to the cloned directory:
3.  Open the `index.html` file in a web browser.

## Dataset and Model

The model fetches data from the "Wine Quality - Red" dataset from the UCI Machine Learning Repository.

*   **Source URL:** `https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv`
*   **Description:** The dataset contains 1599 instances of red Vinho Verde wine samples from Portugal. Each instance has 11 physicochemical input variables (e.g., `fixed acidity`, `volatile acidity`, `alcohol`, etc).
*   **Target Variable:** The `quality` attribute is a sensory-based score from 0 to 10. Most instances are clustered around the median scores (5 and 6), with significantly fewer instances at the low (3, 4) and high (7, 8) ends of the scale.

The trained model accepts input variables and predicts the target variable along with a confidence score. 

For automation, the user decides on a confidence threshold, accepting the model's recommendations only if the model's confidence score is above the threshold. 

This dashboard helps analyze the trade-offs involved in setting various thresholds.


