
import pandas as pd
import numpy as np
from pathlib import Path


# ==================================================
# 1. PROJECT CONFIGURATION
# ==================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "candidates.csv"

SKILL_COLUMNS = [
    "python",
    "sql",
    "excel",
    "machine_learning"
]

# Relative importance of each skill
SKILL_WEIGHTS = np.array([0.4, 0.3, 0.2, 0.1])


# ==================================================
# 2. LOAD DATA
# ==================================================

def load_data(file_path):

    df = pd.read_csv(file_path)

    return df


# ==================================================
# 3. VALIDATE DATA
# ==================================================

def validate_data(df):

    required_columns = ["name"] + SKILL_COLUMNS

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    print("\n===== DATA VALIDATION =====")
    print("Missing values:")
    print(df.isnull().sum())

    return df


# ==================================================
# 4. CLEAN DATA
# ==================================================

def clean_data(df):

    df = df.copy()

    df["name"] = df["name"].fillna("Unknown")

    for column in SKILL_COLUMNS:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        df[column] = df[column].fillna(0)

    return df


# ==================================================
# 5. ANALYSE SKILLS
# ==================================================

def analyse_skills(df):

    print("\n===== SKILL ANALYSIS =====")

    for skill in SKILL_COLUMNS:

        count = df[skill].sum()

        percentage = df[skill].mean() * 100

        print(
            f"{skill}: {count} candidates "
            f"({percentage:.1f}%)"
        )


# ==================================================
# 6. CALCULATE TOTAL SKILLS
# ==================================================

def calculate_candidate_skills(df):

    df = df.copy()

    df["total_skills"] = df[SKILL_COLUMNS].sum(axis=1)

    return df


# ==================================================
# 7. RANK CANDIDATES
# ==================================================

def rank_candidates(df):

    return df.sort_values(
        by="total_skills",
        ascending=False
    )


# ==================================================
# 8. FILTER BY INDIVIDUAL SKILL
# ==================================================

def get_candidates_by_skill(df, skill):

    if skill not in SKILL_COLUMNS:

        raise ValueError(
            f"Unknown skill: {skill}"
        )

    return df[df[skill] == 1]


# ==================================================
# 9. SEARCH CANDIDATES BY NAME
# ==================================================

def search_candidate(df, name):

    result = df[
        df["name"].str.contains(
            name,
            case=False,
            na=False
        )
    ]

    return result


# ==================================================
# 10. FILTER BY MULTIPLE SKILLS
# ==================================================

def filter_by_multiple_skills(df, skills):

    if not skills:
        raise ValueError("Select at least one skill.")

    for skill in skills:

        if skill not in SKILL_COLUMNS:

            raise ValueError(
                f"Unknown skill: {skill}"
            )

    result = df[
        df[skills].eq(1).all(axis=1)
    ]

    return result


# ==================================================
# 11. NUMPY: CALCULATE WEIGHTED SCORES
# ==================================================

def calculate_weighted_score(df):

    df = df.copy()

    # Convert Pandas skill columns into a NumPy matrix
    skill_matrix = df[SKILL_COLUMNS].to_numpy(dtype=float)

    # Multiply matrix by skill weights
    weighted_scores = skill_matrix @ SKILL_WEIGHTS

    # Convert scores into a 0-100 scale
    df["weighted_score"] = weighted_scores * 100

    return df


# ==================================================
# 12. NUMPY: CALCULATE SCORE STATISTICS
# ==================================================

def analyse_weighted_scores(df):

    scores = df["weighted_score"].to_numpy()

    print("\n===== WEIGHTED SCORE STATISTICS =====")

    print("Average score:", np.mean(scores))

    print("Highest score:", np.max(scores))

    print("Lowest score:", np.min(scores))

    print("Standard deviation:", np.std(scores))


# ==================================================
# 13. MAIN PROGRAM
# ==================================================

def main():

    # Load data
    df = load_data(DATA_FILE)

    # Validate data
    df = validate_data(df)

    # Clean data
    df = clean_data(df)

    # Analyse skills
    analyse_skills(df)

    # Calculate total skills
    df = calculate_candidate_skills(df)

    # Rank candidates by number of skills
    ranked = rank_candidates(df)

    print("\n===== CANDIDATE RANKING BY SKILL COUNT =====")

    print(
        ranked[["name", "total_skills"]]
    )

    # Individual skill filtering
    print("\n===== PYTHON CANDIDATES =====")

    print(
        get_candidates_by_skill(df, "python")[["name"]]
    )

    # Candidate search
    print("\n===== CANDIDATE SEARCH =====")

    print(
        search_candidate(df, "candidate a")[["name"]]
    )

    # Multiple skill filtering
    print("\n===== PYTHON + SQL CANDIDATES =====")

    print(
        filter_by_multiple_skills(
            df, ["python", "sql"]
        )[["name"]]
    )

    # NumPy weighted scoring
    df = calculate_weighted_score(df)

    print("\n===== WEIGHTED CANDIDATE SCORES =====")

    weighted_ranking = df.sort_values(
        by="weighted_score",
        ascending=False
    )

    print(
        weighted_ranking[
            ["name", "weighted_score"]
        ]
    )

    # NumPy statistics
    analyse_weighted_scores(df)


# ==================================================
# 14. PROGRAM ENTRY POINT
# ==================================================

if __name__ == "__main__":
    main()
