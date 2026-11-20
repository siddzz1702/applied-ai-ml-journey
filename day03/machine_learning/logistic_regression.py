
# ============================================================
# PROJECT: LOGISTIC REGRESSION CLASSIFICATION
# DAY 03 - MACHINE LEARNING
# ============================================================

# 1. IMPORT LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    roc_auc_score
)


# ============================================================
# 2. GENERATE DATASET
# ============================================================

def generate_dataset():

    X, y = make_classification(
        n_samples=1000,
        n_features=5,
        n_informative=3,
        n_redundant=1,
        n_classes=2,
        random_state=42
    )

    columns = [
        "feature_1",
        "feature_2",
        "feature_3",
        "feature_4",
        "feature_5"
    ]

    df = pd.DataFrame(X, columns=columns)

    df["target"] = y

    print("\n1. Dataset generated successfully!")

    return X, y, df


# ============================================================
# 3. INSPECT DATASET
# ============================================================

def inspect_dataset(df):

    print("\n========== DATASET INSPECTION ==========")

    print("\nDataset preview:")
    print(df.head())

    print("\nDataset shape:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nTarget distribution:")
    print(df["target"].value_counts())

    print("\n========== INSPECTION COMPLETED ==========")


# ============================================================
# 4. SPLIT DATASET
# ============================================================

def split_dataset(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("\n2. Train-test split completed!")

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    return X_train, X_test, y_train, y_test


# ============================================================
# 5. BUILD MACHINE LEARNING PIPELINE
# ============================================================

def build_model():

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression())
    ])

    print("\n3. Machine learning pipeline created!")

    return model


# ============================================================
# 6. TRAIN MODEL
# ============================================================

def train_model(model, X_train, y_train):

    model.fit(X_train, y_train)

    print("\n4. Model training completed!")

    return model


# ============================================================
# 7. EVALUATE MODEL
# ============================================================

def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("\n========== MODEL EVALUATION ==========")

    print("\nAccuracy:", round(accuracy * 100, 2), "%")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("========== EVALUATION COMPLETED ==========")

    return y_pred


# ============================================================
# 8. EXPERIMENT WITH CLASSIFICATION THRESHOLDS
# ============================================================

def experiment_thresholds(model, X_test, y_test):

    print("\n========== THRESHOLD EXPERIMENT ==========")

    # Probability of class 1
    y_prob = model.predict_proba(X_test)[:, 1]

    thresholds = [0.3, 0.5, 0.7]

    results = []

    for threshold in thresholds:

        y_threshold_pred = (
            y_prob >= threshold
        ).astype(int)

        precision = precision_score(
            y_test,
            y_threshold_pred
        )

        recall = recall_score(
            y_test,
            y_threshold_pred
        )

        matrix = confusion_matrix(
            y_test,
            y_threshold_pred
        )

        print(f"\nThreshold: {threshold}")
        print(f"Precision: {precision:.3f}")
        print(f"Recall: {recall:.3f}")

        print("Confusion Matrix:")
        print(matrix)

        results.append({
            "threshold": threshold,
            "precision": precision,
            "recall": recall
        })

    print("\n========== EXPERIMENT COMPLETED ==========")

    return pd.DataFrame(results)


# ============================================================
# 9. VISUALISE MODEL PERFORMANCE
# ============================================================

def visualize_results(model, X_test, y_test, y_pred):

    print("\n========== MODEL VISUALISATION ==========")

    # Confusion Matrix
    ConfusionMatrixDisplay.from_predictions(
        y_test,
        y_pred,
        cmap="Blues"
    )

    plt.title("Logistic Regression - Confusion Matrix")

    plt.tight_layout()

    plt.savefig(
        "day03/machine_learning/confusion_matrix.png",
        dpi=300
    )

    plt.show()

    plt.close()

    print("Confusion matrix saved!")

    # ROC Curve
    RocCurveDisplay.from_estimator(
        model,
        X_test,
        y_test
    )

    plt.title("Logistic Regression - ROC Curve")

    plt.tight_layout()

    plt.savefig(
        "day03/machine_learning/roc_curve.png",
        dpi=300
    )

    plt.show()

    plt.close()

    print("ROC curve saved!")

    # ROC-AUC score
    y_prob = model.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, y_prob)

    print("\nROC-AUC Score:", round(auc, 4))

    print("\n========== VISUALISATION COMPLETED ==========")

    return auc


# ============================================================
# 10. MAIN FUNCTION - EXECUTE COMPLETE WORKFLOW
# ============================================================

def main():

    print("\n========================================")
    print("LOGISTIC REGRESSION CLASSIFICATION")
    print("========================================")

    # Generate dataset
    X, y, df = generate_dataset()

    # Inspect dataset
    inspect_dataset(df)

    # Split dataset
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    # Build model
    model = build_model()

    # Train model
    model = train_model(model, X_train, y_train)

    # Evaluate model
    y_pred = evaluate_model(model, X_test, y_test)

    # Experiment with thresholds
    threshold_results = experiment_thresholds(
        model,
        X_test,
        y_test
    )

    print("\nThreshold comparison:")
    print(threshold_results.to_string(index=False))

    # Visualise results
    auc = visualize_results(
        model,
        X_test,
        y_test,
        y_pred
    )

    print("\n========================================")
    print("PROJECT EXECUTION COMPLETED")
    print("Final ROC-AUC:", round(auc, 4))
    print("========================================")


# ============================================================
# 11. EXECUTION ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()
