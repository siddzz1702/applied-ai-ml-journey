
# Candidate Intelligence — Data Analysis & Scoring Engine

## Overview

Candidate Intelligence is a Python-based data analysis project
developed as part of my Applied AI/ML engineering learning journey.

The project analyses candidate skill data using Pandas and NumPy.
It demonstrates data ingestion, validation, cleaning, filtering,
statistical analysis, candidate ranking and weighted scoring.

## Technologies Used

- Python 3
- Pandas
- NumPy
- Git and GitHub

## Features

1. CSV data ingestion
2. Data validation and missing-value analysis
3. Data cleaning and type conversion
4. Skill-wise statistical analysis
5. Candidate skill-count calculation
6. Candidate ranking
7. Search by candidate name
8. Filtering by individual skills
9. Filtering by multiple skills
10. NumPy-based weighted scoring
11. Statistical analysis of weighted scores

## Weighted Scoring Methodology

The project uses an illustrative weighted scoring model:

| Skill | Weight |
|---|---:|
| Python | 40% |
| SQL | 30% |
| Excel | 20% |
| Machine Learning | 10% |

The weighted score is calculated using NumPy matrix
multiplication.

Weighted Score = Skill Matrix × Weight Vector

The result is converted into a score out of 100.

## Project Structure

candidate-intelligence/
│
├── candidates.csv
├── main.py
└── README.md

## How to Run

1. Clone the repository.
2. Navigate to the candidate-intelligence folder.
3. Install the dependencies.
4. Run the application.

```bash
pip install pandas numpy
python main.py
```

## Learning Outcomes

Through this project, I practised:

- Python functions and modular programming
- Pandas DataFrame operations
- NumPy arrays and matrix multiplication
- Data validation and cleaning
- Numerical statistics
- Git version control and GitHub workflows

## Future Improvements

- Add a graphical user interface
- Introduce actual candidate assessment scores
- Add data visualisations
- Implement more advanced statistical analysis
- Explore machine learning-based analytical features

## Important Note

This is an educational data analysis project.
Its weighted scoring methodology is illustrative and
is not a validated hiring or candidate suitability model.
