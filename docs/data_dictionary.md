# Data Dictionary

## `pekab40_screenings_state.csv`

| Column | Description |
| --- | --- |
| `date` | Date of the screening record. |
| `state` | Malaysian state or federal territory where screenings were recorded. |
| `screenings` | Number of PeKaB40 screening records for the date and state. |

## `population_state.csv`

| Column | Description |
| --- | --- |
| `date` | Date or reference period for the population estimate. |
| `state` | Malaysian state or federal territory. |
| `sex` | Population category by sex. |
| `age` | Population age group. |
| `ethnicity` | Population category by ethnicity. |
| `population` | Population estimate for the selected state, sex, age, and ethnicity group. |

## `population_40plus_by_state_year.csv`

| Column | Description |
| --- | --- |
| `state` | Malaysian state or federal territory. |
| `date` | Date or reference period carried from the population dataset. |
| `Year` | Year extracted for joining and annual comparison. |
| `population_40plus_000` | Population aged 40+ by state and year, stored in thousands. |

