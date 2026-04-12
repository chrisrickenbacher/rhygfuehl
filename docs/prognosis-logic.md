# Rhine Swimming Prognosis Logic

This document defines the automated estimation logic used to determine if swimming in the Rhine at Basel is currently advisable. The prognosis factors in water quality (bacterial risk from rain) and physical safety (temperature).


## Input Parameters
Data is fetched every 15 minutes from the [Basel-Stadt Open Data Portal](https://data.bs.ch/).

| Parameter | Station | Unit | Metric Used |
| :--- | :--- | :--- | :--- |
| **Precipitation** | Rheinpromenade 2 | mm/24h | Weighted 72h impact ($I$) |
| **Global Radiation** | St. Johann | W/m² | 72h average recovery bonus ($B$) |
| **Water Temperature** | Weil am Rhein | °C | Latest ($T_{now}$) & 48h Average ($T_{avg}$) |


## Calculation Models

### A. Rain Impact Score ($I$)
Rain triggers combined sewer overflows (CSO), increasing bacterial load. This impact decays over time:
- $R_0$: Rain today (100% weight)
- $R_1$: Rain yesterday (50% weight)
- $R_2$: Rain 2 days ago (25% weight)

**Formula:** $I = (R_0 \times 1.0) + (R_1 \times 0.5) + (R_2 \times 0.25)$

### B. UV Recovery Bonus ($B$)
UV radiation acts as a natural disinfectant. High radiation speeds up the "clearing" of the river after rain.
- $UV_{threshold}$: 170 W/m² (Reference for a sunny day)

**Formula:** $B = \frac{\text{Avg}(UV_{0..2})}{UV_{threshold}}$


## Decision Matrix

The prognosis follows a "Safety First" principle. Temperature overrides quality if safety risks are present.

### Level 3: Excellent (Green)
**Condition:** Perfect water quality AND safe temperature.
- **Quality:** $I < 0.5$ (Dry) OR ($R_0 < 1.0$ AND $I < 2.0$ AND $B > 1.2$)
- **Safety:** $T_{now} \ge 18^\circ\text{C}$ AND $T_{avg} \le 22^\circ\text{C}$

### Level 2: Good (Yellow)
**Condition:** Acceptable quality OR "Fresh/Warm" water.
- **Quality:** $I < 3.5$ OR ($R_0 < 2.0$ AND $I < 5.0$ AND $B > 1.0$)
- **Safety:** $T_{now} \ge 14^\circ\text{C}$
- *Note: Status is capped at "Good" if water is $14-18^\circ\text{C}$ (Cold risk) or $> 22^\circ\text{C}$ (Bacterial risk).*

### Level 1: Discouraged (Red)
**Condition:** Poor quality OR dangerous temperature.
- **Quality:** $I \ge 3.5$ (Significant rain/overflow risk)
- **Safety:** $T_{now} < 14^\circ\text{C}$ (High cold-shock risk)


## Scientific Rationale

- **The 3.5mm Threshold:** In Basel, sewer overflows typically begin after 3-5mm of rain. Our threshold of 3.5 reflects this tipping point.
- **The 14°C Rule:** Water below 14°C significantly increases the risk of "Cold Shock Response" (involuntary gasping/hyperventilation), which is a leading cause of drowning.
- **The 22°C Average:** Sustained high temperatures (especially overnight) promote the rapid growth of intestinal bacteria. A 48h average is used to filter out short daytime peaks.


## Disclaimer
This is an **automated estimate** based on environmental proxies. It is **not** a real-time biological measurement. Swimming in the Rhine is always at your own risk. Local pollution events can occur unpredictably.
