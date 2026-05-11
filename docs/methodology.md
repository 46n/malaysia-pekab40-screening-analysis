# Methodology

## Screening Dataset

The PeKaB40 screening dataset contains daily screening records by Malaysian state. It was used to measure screening activity over time and compare activity between states.

The main fields used from this dataset were:

- `date`
- `state`
- `screenings`

Screening records were aggregated by year and state for trend and state-level comparison.

## Population Dataset

The population dataset contains Malaysia state-level population estimates by date, state, sex, age, and ethnicity. Since PeKaB40 preventive healthcare screening is focused on eligible individuals aged 40 and above, the population dataset was filtered to include age groups from `40-44` up to the oldest available age group.

After filtering, the population values were grouped by state and year to create the cleaned file:

```text
data/cleaned/population_40plus_by_state_year.csv
```

The cleaned population table is used as the denominator for population-adjusted comparison.

## Why Population Adjustment Is Needed

Raw screening counts can make larger states appear to have stronger activity simply because they have more residents. Population adjustment makes state comparisons more balanced by relating screening activity to the size of the population aged 40 and above.

This helps identify states with lower screening intensity, not just states with lower total screening volume.

## Why "Screening Intensity" Is Used Instead of "Coverage"

The term "screening intensity" is used because the denominator is population aged 40+, not the exact eligible PeKaB40 population. The dataset does not include the eligible B40/STR population by state, so the metric should not be interpreted as exact eligibility coverage.

Screening intensity is a safer wording because it describes relative screening activity per 100,000 population aged 40+.

## Formula

```text
Screening Intensity = Total Screenings / Population Aged 40+ * 100,000
```

