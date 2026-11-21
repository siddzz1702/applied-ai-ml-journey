
import pandas as pd
import pytest

from main import validate_data


@pytest.fixture
def valid_data():
    """Create reusable valid candidate data."""

    return pd.DataFrame({
        "name": ["Candidate A"],
        "python": [1],
        "sql": [1],
        "excel": [0],
        "machine_learning": [1]
    })


def test_valid_dataset(valid_data):
    """Test that valid data passes validation."""

    assert validate_data(valid_data) is True


def test_invalid_skill_value(valid_data):
    """Test that invalid skill values raise an error."""

    invalid_data = valid_data.copy()
    invalid_data.loc[0, "python"] = 5

    with pytest.raises(ValueError):
        validate_data(invalid_data)


def test_missing_candidate_name(valid_data):
    """Test that missing candidate names raise an error."""

    invalid_data = valid_data.copy()
    invalid_data.loc[0, "name"] = None

    with pytest.raises(ValueError):
        validate_data(invalid_data)


def test_duplicate_candidate_names(valid_data):
    """Test that duplicate candidate names raise an error."""

    invalid_data = pd.concat(
        [valid_data, valid_data],
        ignore_index=True
    )

    with pytest.raises(ValueError):
        validate_data(invalid_data)


def test_missing_required_column(valid_data):
    """Test that missing columns raise an error."""

    invalid_data = valid_data.drop(columns=["python"])

    with pytest.raises(ValueError):
        validate_data(invalid_data)

from main import calculate_weighted_score


def test_weighted_score_calculation(valid_data):
    """Test whether weighted scores are calculated correctly."""

    from main import calculate_candidate_skills

    df = calculate_candidate_skills(valid_data)
    result = calculate_weighted_score(df)

    candidate_score = result.loc[
        result["name"] == "Candidate A",
        "weighted_score"
    ].iloc[0]

    assert candidate_score == pytest.approx(80.0)


def test_skill_contributions(valid_data):
    """Test individual skill contributions."""

    from main import calculate_candidate_skills

    df = calculate_candidate_skills(valid_data)
    result = calculate_weighted_score(df)

    candidate = result.iloc[0]

    assert candidate["python_contribution"] == pytest.approx(40.0)
    assert candidate["sql_contribution"] == pytest.approx(30.0)
    assert candidate["excel_contribution"] == pytest.approx(0.0)
    assert candidate["machine_learning_contribution"] == pytest.approx(10.0)


def test_weighted_score_range(valid_data):
    """Test that scores remain between 0 and 100."""

    from main import calculate_candidate_skills

    df = calculate_candidate_skills(valid_data)
    result = calculate_weighted_score(df)

    assert result["weighted_score"].between(0, 100).all()

def test_empty_dataset():
    """Test that an empty dataset is rejected."""

    empty_data = pd.DataFrame(columns=[
        "name",
        "python",
        "sql",
        "excel",
        "machine_learning"
    ])

    with pytest.raises(ValueError):
        validate_data(empty_data)


def test_candidate_search_no_match(valid_data):
    """Test searching for a candidate who does not exist."""

    from main import search_candidate

    result = search_candidate(valid_data, "Candidate Z")

    assert result.empty
