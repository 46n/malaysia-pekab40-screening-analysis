# PeKaB40 Preventive Healthcare Screening Analysis

## Project Overview

This project analyzes Malaysia's PeKaB40 preventive healthcare screening activity by state from 2019 to 2025. The goal is to identify screening trends, compare state-level activity, and highlight outreach-priority areas using population-adjusted screening intensity.

## Business / Public Health Question

Which Malaysian states recorded lower PeKaB40 screening intensity, and where should outreach campaigns be reviewed or prioritized?

## Tools Used

- Power BI
- Power Query
- DAX
- CSV datasets
- GitHub


## Dataset Sources

- [Daily PeKaB40 Health Screenings by State](https://data.gov.my/data-catalogue/pekab40_screenings_state)
- [Population Table by State](https://data.gov.my/data-catalogue/population_state)
- [Cleaned population aged 40+ by state and year](data/cleaned/population_40plus_by_state_year.csv), created from the population dataset

## Methodology

The PeKaB40 screening dataset was combined with Malaysia state-level population data. Since PeKaB40 targets eligible individuals aged 40 and above, the population dataset was filtered to include age groups from 40-44 up to the oldest available age group. The filtered population data was grouped by state and year, then used to calculate screening intensity.

Formula:

```text
Screening Intensity = Total Screenings / Population Aged 40+ * 100,000
```

## Dashboard Preview

Dashboard screenshots should be added before publishing this repository.

Expected screenshot files:

- `screenshots/overview_page.png`
- `screenshots/outreach_priority_page.png`

See [screenshots/README.md](screenshots/README.md) for screenshot instructions.

## Key Insights

1. PeKaB40 screenings dropped sharply in 2021, making it the weakest year in the 2019-2025 trend.
2. Screenings recovered strongly after 2021 and reached their highest point in 2023, before slightly declining in 2024 and 2025.
3. Kelantan recorded the highest screening intensity per 100,000 population aged 40+ in the selected year.
4. W.P. Putrajaya recorded the lowest screening intensity per 100,000 population aged 40+.
5. W.P. Putrajaya, W.P. Kuala Lumpur, and W.P. Labuan showed noticeably lower screening intensity compared with other states, making them priority areas for further outreach review.

## Recommendations

- Review W.P. Putrajaya, W.P. Kuala Lumpur, and W.P. Labuan as priority areas for further outreach investigation.
- Investigate whether low screening intensity is linked to awareness gaps, clinic accessibility, eligible-population differences, or cross-state healthcare usage.
- Use Kelantan as a reference case to understand what may be supporting stronger screening intensity.
- Monitor the slight decline after the 2023 peak to determine whether additional outreach campaigns are needed.

## Limitations

- Screening intensity uses population aged 40+ as an approximation.
- The metric does not represent exact PeKaB40 eligibility or exact coverage because the dataset does not include the eligible B40/STR population by state.
- The screening dataset represents screening records, not necessarily unique individuals.
- Urban areas such as Kuala Lumpur may have cross-state healthcare usage, especially with nearby Selangor.

## Repository Structure

```text
daily PekaB40 Health Screaning By State
|-- dashboard
|   `-- PeKaB40_Healthcare_Screening_Dashboard.pbix
|-- data
|   |-- raw
|   |   |-- pekab40_screenings_state.csv
|   |   `-- population_state.csv
|   `-- cleaned
|       `-- population_40plus_by_state_year.csv
|-- screenshots
|   `-- README.md
|-- docs
|   |-- methodology.md
|   |-- data_dictionary.md
|   `-- limitations.md
|-- measures.md
|-- README.md
`-- .gitignore
```

## How to Open the Dashboard

1. Install Power BI Desktop.
2. Open `dashboard/PeKaB40_Healthcare_Screening_Dashboard.pbix`.
3. If Power BI asks about file paths or data refresh, confirm that the CSV files are available in the `data` folder.

