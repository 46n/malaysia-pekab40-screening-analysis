# PeKaB40 Preventive Healthcare Screening Analysis

## Project Overview

PeKaB40, or Skim Peduli Kesihatan untuk Kumpulan B40, is a Malaysian Ministry of Health initiative designed to support the healthcare needs of low-income Malaysians, especially in relation to non-communicable diseases (NCDs). The programme provides free health screening and related healthcare support to eligible Sumbangan Tunai Rahmah (STR) recipients and their registered spouses aged 40 and above. :contentReference[oaicite:0]{index=0}

Preventive screening is important because NCDs such as diabetes, hypertension, and cardiovascular-related risks can remain undetected until they become more serious. Analyzing PeKaB40 screening activity helps identify how screening participation changes over time and whether some states may require closer outreach review.

This project analyzes PeKaB40 health screening records across all Malaysian states and federal territories from 2019 to 2025. It compares yearly trends, state-level screening activity, and population-adjusted screening intensity using the population aged 40 and above as an approximation. The goal is to highlight states with lower screening intensity and support more evidence-based outreach planning.

## Business / Public Health Question

Which Malaysian states recorded lower PeKaB40 screening intensity, and where should outreach campaigns be reviewed or prioritized?

## Tools Used

- Power BI
- Power Query
- DAX
- CSV datasets
- GitHub


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

The dashboard preview is grouped into two sections:

- **Overview**: overall screening activity, time trends, state totals, and geographic distribution.
- **Outreach Priority**: population-adjusted screening intensity and evidence for reviewing lower-intensity states.

### Overview

#### PeKaB40 Screenings Trend Over Time

<p align="center">
  <img src="screenshots/screenings-trend-over-time.png" alt="PeKaB40 screenings trend over time" width="850">
</p>

This chart shows annual PeKaB40 screening records from 2019 to 2025. Screening activity dropped sharply in 2021, then recovered strongly from 2022 onward.

**Concluded insight:** 2021 was the weakest year in the period, while 2023 marked the strongest recovery point before a mild decline in 2024 and 2025.

#### Top and Bottom 5 States by Total Screenings

<p align="center">
  <img src="screenshots/top-and-bottom-5-states-by-total-screenings.png" alt="Top and bottom 5 states by total screenings" width="850">
</p>

This view compares the highest and lowest states by total PeKaB40 screening records. Perak, Kedah, Sarawak, Selangor, and Johor appear among the strongest states by total volume, while W.P. Putrajaya and W.P. Labuan record the lowest totals.

**Concluded insight:** Total screening volume is useful for understanding operational scale, but it should be read together with population-adjusted screening intensity before judging outreach performance.

#### Total Screenings by State

<p align="center">
  <img src="screenshots/total-screenings-by-state.png" alt="Total screenings by state" width="850">
</p>

This dashboard view combines KPI cards with a ranked state bar chart. It shows total screening records, active screening days, average daily screenings, and how screening volume is distributed across states.

**Concluded insight:** Larger states generally contribute more screening records, so raw totals alone do not fully explain relative outreach strength.

#### Monthly PeKaB40 Screenings Trend and State Screening Intensity

<p align="center">
  <img src="screenshots/monthly-screenings-trend-and-screenings-rate-by-state.png" alt="Monthly screenings trend and screening intensity by state" width="850">
</p>

The monthly trend shows seasonal movement in screening records, with weaker activity around April and May and stronger activity later in the year. The state comparison below highlights clear variation in screening intensity between states.

**Concluded insight:** Screening activity is not evenly distributed across the year or across states, which supports the need for targeted outreach monitoring.

#### PeKaB40 Screening Intensity by State Map

<p align="center">
  <img src="screenshots/screenings-rate-by-state-map.png" alt="PeKaB40 screening intensity by state map" width="850">
</p>

The map provides a geographic view of state-level screening intensity. It helps identify where screening activity is concentrated and where intensity appears lower across Malaysia.

**Concluded insight:** Geographic variation is visible, so outreach planning should consider both state ranking and location-based access patterns.

### Outreach Priority

This section focuses on population-adjusted screening intensity and evidence for reviewing lower-intensity states. Screening intensity is used because the denominator is population aged 40+, not the exact eligible PeKaB40 population.

#### Screening Intensity by State Per 100,000 Population Aged 40+

<p align="center">
  <img src="screenshots/screenings-intensity-by-state-per-100000-population-aged-40%2B.png" alt="Screening intensity by state per 100,000 population aged 40+" width="850">
</p>

This chart ranks states by screening intensity per 100,000 population aged 40+. Kelantan records the highest screening intensity, while W.P. Putrajaya, W.P. Kuala Lumpur, and W.P. Labuan appear at the lower end.

**Concluded insight:** W.P. Putrajaya, W.P. Kuala Lumpur, and W.P. Labuan should be reviewed as priority areas because their screening intensity is noticeably lower than most other states.

#### Outreach Priority Evidence

<p align="center">
  <img src="screenshots/outreach-priority-evidence.png" alt="Outreach priority evidence" width="850">
</p>

This evidence table compares screening intensity, average daily screenings, population aged 40+, and total screening records by state. It supports the outreach-priority view by showing both raw activity and population-adjusted intensity in one place.

**Concluded insight:** Low screening intensity in W.P. Putrajaya, W.P. Kuala Lumpur, and W.P. Labuan may reflect awareness gaps, access patterns, eligible-population differences, or cross-state healthcare usage, so these states need further investigation rather than a simple raw-count comparison.

More screenshot notes are available in [screenshots/README.md](screenshots/README.md).

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
|   |-- README.md
|   |-- monthly-screenings-trend-and-screenings-rate-by-state.png
|   |-- outreach-priority-evidence.png
|   |-- screenings-intensity-by-state-per-100000-population-aged-40+.png
|   |-- screenings-rate-by-state-map.png
|   |-- screenings-trend-over-time.png
|   |-- top-and-bottom-5-states-by-total-screenings.png
|   `-- total-screenings-by-state.png
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

