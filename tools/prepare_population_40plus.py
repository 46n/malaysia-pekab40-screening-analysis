"""Prepare the population aged 40+ denominator for screening intensity.

This utility documents the data-preparation step used before building the
Power BI dashboard. It expects the raw `population_state.csv` file and writes
the cleaned state-year denominator used by the report.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


AGE_GROUPS_40_PLUS = {
    "40-44",
    "45-49",
    "50-54",
    "55-59",
    "60-64",
    "65-69",
    "70-74",
    "75-79",
    "80-84",
    "85+",
}


def prepare_population_40plus(input_path: Path, output_path: Path) -> pd.DataFrame:
    population = pd.read_csv(input_path)
    filtered = population[population["age"].astype(str).isin(AGE_GROUPS_40_PLUS)]

    grouped = (
        filtered.groupby(["state", "date"], as_index=False)["population"]
        .sum()
        .rename(columns={"date": "year", "population": "population_40plus"})
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    grouped.to_csv(output_path, index=False)
    return grouped


def main() -> None:
    prepare_population_40plus(
        input_path=Path("data/raw/population_state.csv"),
        output_path=Path("data/cleaned/population_40plus_by_state_year.csv"),
    )


if __name__ == "__main__":
    main()
