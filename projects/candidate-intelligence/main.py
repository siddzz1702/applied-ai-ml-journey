
import pandas as pd
import numpy as np


# ============================================================
# CONFIGURATION
# ============================================================

DATA_FILE = "projects/candidate-intelligence/candidate.csv"

SKILL_COLUMNS = [
    "python",
    "sql",
    "excel",
    "machine_learning"
]

SKILL_WEIGHTS = np.array([
    0.4,  # Python
    0.3,  # SQL
    0.2,  # Excel
    0.1   # Machine Learning
])


# ============================================================
# 1. DATA LOADING
# ============================================================

def load_data(file_path):

    """Load candidate data from a CSV file."""

    df = pd.read_csv(file_path)

    print("\nData loaded successfully.")

    return df


# ============================================================
# 2. DATA VALIDATION
# ============================================================

def validate_data(df):

    """Check whether the candidate dataset is valid."""

    required_columns = ["name"] + SKILL_COLUMNS

    # Check required columns
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check candidate names
    if df["name"].isna().any():
        raise ValueError("Candidate names cannot be empty.")

    if df["name"].astype(str).str.strip().eq("").any():
        raise ValueError("Candidate names cannot be blank.")

    # Check duplicate candidate names
    if df["name"].astype(str).str.strip().str.lower().duplicated().any():
        raise ValueError("Duplicate candidate names found.")

    # Check skill values
    for skill in SKILL_COLUMNS:

        values = pd.to_numeric(
            df[skill],
            errors="coerce"
        )

        if values.isna().any():
            raise ValueError(
                f"Invalid or missing values found in {skill}."
            )

        if not values.isin([0, 1]).all():
            raise ValueError(
                f"{skill} must contain only 0 or 1."
            )

    print("Data validation successful.")

    return True


# ============================================================
# 3. DATA CLEANING
# ============================================================

def clean_data(df):

    """Clean candidate names and skill columns."""

    df = df.copy()

    # Remove unnecessary spaces from names
    df["name"] = df["name"].str.strip()

    # Convert skill columns into integers
    for skill in SKILL_COLUMNS:

        df[skill] = pd.to_numeric(
            df[skill],
            errors="raise"
        ).astype(int)

    print("Data cleaning successful.")

    return df


# ============================================================
# 4. SKILL ANALYSIS
# ============================================================

def analyse_skills(df):

    """Calculate the number and percentage of candidates
    possessing each skill."""

    print("\n===== SKILL ANALYSIS =====")

    total_candidates = len(df)

    for skill in SKILL_COLUMNS:

        count = df[skill].sum()

        percentage = (
            count / total_candidates
        ) * 100 if total_candidates else 0

        print(
            f"{skill.title()}: "
            f"{count} candidates "
            f"({percentage:.1f}%)"
        )


# ============================================================
# 5. CANDIDATE SKILL COUNT
# ============================================================

def calculate_candidate_skills(df):

    """Calculate the total number of skills possessed
    by each candidate."""

    df = df.copy()

    df["total_skills"] = df[SKILL_COLUMNS].sum(axis=1)

    return df


# ============================================================
# 6. RANK CANDIDATES BY SKILL COUNT
# ============================================================

def rank_candidates(df):

    """Rank candidates based on their total skill count."""

    ranked_df = df.sort_values(
        by=["total_skills", "name"],
        ascending=[False, True]
    )

    return ranked_df


# ============================================================
# 7. FILTER CANDIDATES BY INDIVIDUAL SKILL
# ============================================================

def get_candidates_by_skill(df, skill):

    """Return candidates possessing a particular skill."""

    if skill not in SKILL_COLUMNS:
        raise ValueError(f"Unknown skill: {skill}")

    result = df[df[skill] == 1]

    return result


# ============================================================
# 8. SEARCH FOR A CANDIDATE
# ============================================================

def search_candidate(df, candidate_name):

    """Search for a candidate by name."""

    result = df[
        df["name"].str.contains(
            candidate_name,
            case=False,
            na=False,
            regex=False
        )
    ]

    return result


# ============================================================
# 9. FILTER BY MULTIPLE SKILLS
# ============================================================

def filter_by_multiple_skills(df, required_skills):

    """Find candidates possessing all requested skills."""

    invalid_skills = [
        skill for skill in required_skills
        if skill not in SKILL_COLUMNS
    ]

    if invalid_skills:
        raise ValueError(
            f"Unknown skills: {invalid_skills}"
        )

    result = df[
        (df[required_skills] == 1).all(axis=1)
    ]

    return result


# ============================================================
# 10. WEIGHT VALIDATION
# ============================================================



def validate_data(df):

    """Check whether the candidate dataset is valid."""

    if df.empty:
        raise ValueError("Dataset cannot be empty.")

    required_columns = ["name"] + SKILL_COLUMNS

    # Check required columns
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check candidate names
    if df["name"].isna().any():
        raise ValueError("Candidate names cannot be empty.")

    if df["name"].astype(str).str.strip().eq("").any():
        raise ValueError("Candidate names cannot be blank.")

    # Check duplicate names
    if df["name"].astype(str).str.strip().str.lower().duplicated().any():
        raise ValueError("Duplicate candidate names found.")

    # Check skill values
    for skill in SKILL_COLUMNS:

        values = pd.to_numeric(
            df[skill],
            errors="coerce"
        )

        if values.isna().any():
            raise ValueError(
                f"Invalid or missing values found in {skill}."
            )

        if not values.isin([0, 1]).all():
            raise ValueError(
                f"{skill} must contain only 0 or 1."
            )

    print("Data validation successful.")

    return True



def validate_weights():

    """Ensure scoring weights are valid."""

    # Check number of weights
    if len(SKILL_WEIGHTS) != len(SKILL_COLUMNS):
        raise ValueError(
            "Number of weights must match number of skills."
        )

    # Check for negative weights
    if np.any(SKILL_WEIGHTS < 0):
        raise ValueError(
            "Skill weights cannot be negative."
        )

    # Check whether weights add up to 1
    if not np.isclose(SKILL_WEIGHTS.sum(), 1.0):
        raise ValueError(
            "Skill weights must add up to 1."
        )

    print("Weight validation successful.")


# ============================================================
# 11. WEIGHTED CANDIDATE SCORING
# ============================================================


def calculate_weighted_score(df):

    """Calculate weighted scores and individual skill
    contributions for every candidate."""

    df = df.copy()

    # Validate candidate data
    validate_data(df)

    # Validate scoring weights
    validate_weights()

    # Calculate individual skill contributions
    for index, skill in enumerate(SKILL_COLUMNS):

        df[f"{skill}_contribution"] = (
            df[skill] * SKILL_WEIGHTS[index] * 100
        )

    # Calculate total weighted score
    contribution_columns = [
        f"{skill}_contribution"
        for skill in SKILL_COLUMNS
    ]

    df["weighted_score"] = df[
        contribution_columns
    ].sum(axis=1)

    # Rank candidates
    df = df.sort_values(
        by=["weighted_score", "total_skills", "name"],
        ascending=[False, False, True]
    )

    return df

    # Calculate total weighted score
    contribution_columns = [
        f"{skill}_contribution"
        for skill in SKILL_COLUMNS
    ]

    df["weighted_score"] = df[
        contribution_columns
    ].sum(axis=1)

    # Rank candidates by weighted score
    df = df.sort_values(
        by=["weighted_score", "total_skills", "name"],
        ascending=[False, False, True]
    )

    return df


# ============================================================
# 12. WEIGHTED SCORE STATISTICS
# ============================================================

def analyse_weighted_scores(df):

    """Calculate statistical information about
    candidate weighted scores."""

    scores = df["weighted_score"].to_numpy()

    print("\n===== WEIGHTED SCORE STATISTICS =====")

    print(f"Average score: {np.mean(scores):.2f}")
    print(f"Highest score: {np.max(scores):.2f}")
    print(f"Lowest score: {np.min(scores):.2f}")
    print(f"Standard deviation: {np.std(scores):.2f}")


# ============================================================
# 13. MAIN APPLICATION
# ============================================================

def main():

    # Load data
    df = load_data(DATA_FILE)

    # Validate data
    validate_data(df)

    # Clean data
    df = clean_data(df)

    # Analyse skills
    analyse_skills(df)

    # Calculate total skills
    df = calculate_candidate_skills(df)

    # Rank candidates by skill count
    ranked = rank_candidates(df)

    print("\n===== CANDIDATE RANKING BY SKILL COUNT =====")

    print(
        ranked[["name", "total_skills"]]
        .to_string(index=False)
    )

    # Individual skill filtering
    print("\n===== PYTHON CANDIDATES =====")

    print(
        get_candidates_by_skill(df, "python")[["name"]]
        .to_string(index=False)
    )

    # Candidate search
    print("\n===== CANDIDATE SEARCH =====")

    print(
        search_candidate(df, "candidate a")[["name"]]
        .to_string(index=False)
    )

    # Multiple skill filtering
    print("\n===== PYTHON + SQL CANDIDATES =====")

    print(
        filter_by_multiple_skills(
            df, ["python", "sql"]
        )[["name"]]
        .to_string(index=False)
    )

    # Calculate weighted scores
    weighted_df = calculate_weighted_score(df)

    # Display explainable candidate scores
    print("\n===== EXPLAINABLE CANDIDATE SCORES =====")

    display_columns = (
        ["name"]
        + [
            f"{skill}_contribution"
            for skill in SKILL_COLUMNS
        ]
        + ["weighted_score"]
    )

    print(
        weighted_df[display_columns]
        .round(2)
        .to_string(index=False)
    )

    # Analyse weighted score statistics
    analyse_weighted_scores(weighted_df)


# ============================================================
# 14. RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    main()
