# Power BI Measures and Calculated Columns

This file documents the main DAX logic used in the dashboard.

## Measures

### Total Screenings

```DAX
Total Screenings =
SUM(pekab40_screenings_state[screenings])
```

### Avg Daily Screenings

```DAX
Avg Daily Screenings =
DIVIDE(
    [Total Screenings],
    DISTINCTCOUNT(pekab40_screenings_state[date])
)
```

### Active Screening Days

```DAX
Active Screening Days =
COUNTROWS(
    FILTER(
        VALUES(pekab40_screenings_state[date]),
        CALCULATE([Total Screenings]) > 0
    )
)
```

### Population 40 Plus

```DAX
Population 40 Plus =
SUM(population_state[population_40plus_000]) * 1000
```

### Screening Intensity

```DAX
Screening Intensity =
DIVIDE(
    [Total Screenings],
    [Population 40 Plus]
) * 100000
```

## Calculated Columns

### StateYearKey for pekab40_screenings_state

```DAX
StateYearKey for pekab40_screenings_state =
pekab40_screenings_state[state] & "-" & FORMAT(pekab40_screenings_state[Year], "0")
```

### StateYearKey for population_state

```DAX
StateYearKey for population_state =
population_state[state] & "-" & FORMAT(population_state[Year], "0")
```

