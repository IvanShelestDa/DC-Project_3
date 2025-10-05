# DC-Project_3 — Analyzing Nobel Prize Data

**Author:** Completed independently by Ivan Shelest
**Based on DataCamp project:** [Visualizing the History of Nobel Prize Winners](https://app.datacamp.com/learn/projects/1888)

---

## Project Description

The Nobel Prize is awarded annually to exceptional individuals and organizations across six categories: **Chemistry, Literature, Physics, Medicine, Economics, and Peace.** Since its inception in 1901, it has been one of the most prestigious honors in the world.

This project explores more than a century of Nobel Prize data to uncover **patterns and potential biases** in the way these awards have been distributed.
Through data manipulation and analysis in **Python (pandas, seaborn, numpy)**, the goal is to identify:

* Which gender and country dominate among laureates,
* How the representation of the United States has changed over time,
* The rise of female winners in different decades and disciplines,
* The first female laureate in Nobel history,
* And who received the Nobel Prize more than once.

---

## Objectives

1. **Identify general trends** among laureates (e.g., most common gender and birth country).
2. **Measure the share of U.S. winners by decade** to see when the U.S. dominance peaked.
3. **Analyze the proportion of female laureates** in each decade and category.
4. **Find the first woman to win a Nobel Prize** and determine her field.
5. **List individuals and organizations** that received multiple Nobel Prizes.

---

## Dataset

The dataset `nobel.csv` contains detailed records of all Nobel Prize winners from **1901 to 2020**.
Key columns include:

| Column              | Description                                              |
| ------------------- | -------------------------------------------------------- |
| `year`              | Year of the award                                        |
| `category`          | Award category (Physics, Chemistry, etc.)                |
| `full_name`         | Laureate’s full name                                     |
| `sex`               | Gender of the laureate                                   |
| `birth_country`     | Country of birth                                         |
| `organization_name` | Institution or organization associated with the laureate |
| `motivation`        | Reason for the award                                     |
| `prize_share`       | Fraction of the award shared                             |
| `death_date`        | Date of death (if applicable)                            |

---

## Methodology

### 1. Load and preprocess data

* Import and inspect dataset using `pandas`.
* Handle relevant columns for gender, birth country, year, and category.

### 2. Calculate metrics

* Use `mode()`, `groupby()`, and `agg()` to identify dominant patterns.
* Compute U.S. share of laureates by decade.
* Measure the ratio of female laureates across categories and decades.

### 3. Identify milestones

* Determine the **first female laureate** chronologically.
* Find all laureates who have **won multiple prizes**.

---

## Code Example

```python
nobel = pd.read_csv('nobel.csv')

# 1. Most common gender and country
top_gender = nobel['sex'].mode()[0]
top_country = nobel['birth_country'].mode()[0]

# 2. U.S. dominance by decade
nobel['decade'] = (nobel['year'] // 10) * 10
nobel['USA_winner'] = nobel['birth_country'] == 'United States of America'
usa_ratio = nobel.groupby('decade')['USA_winner'].mean()
max_decade_usa = usa_ratio.idxmax()

# 3. Female laureates by category
female_ratio = (
    nobel[nobel['sex'] == 'Female']
    .groupby(['decade', 'category'])
    .size() / nobel.groupby(['decade', 'category']).size()
)
max_decade_category = female_ratio.idxmax()

# 4. First female laureate
first_female = nobel[nobel['sex'] == 'Female'].sort_values('year').iloc[0]

# 5. Multiple winners
repeat_winners = nobel['full_name'].value_counts()[lambda x: x > 1].index.tolist()
```

---

## Results

| Analysis                                                   | Finding                                                                                    |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Most common gender                                         | Male                                                                                       |
| Most common birth country                                  | United States of America                                                                   |
| Decade with highest share of U.S. laureates                | 2000s                                                                                      |
| Decade and category with highest share of female laureates | 2020s, Literature                                                                          |
| First female laureate                                      | Marie Curie (Physics, 1903)                                                                |
| Laureates with multiple awards                             | Marie Curie, John Bardeen, Frederick Sanger, Linus Pauling, International Red Cross, UNHCR |

---

## Interpretation

The analysis confirms strong historical patterns:

* Nobel Prizes have predominantly gone to **men** and **U.S.-born scientists**, especially after 1950.
* Female representation has increased notably since the 2000s, reaching its highest levels in **Literature and Peace** categories in recent decades.
* Several institutions and scientists have achieved **multiple Nobel honors**, highlighting their long-term global impact on science and humanitarian work.

---

## Technologies Used

* Python 3.12
* pandas — data manipulation
* numpy — numerical calculations
* seaborn / matplotlib — data visualization
* VS Code

---

## Repository Structure

```
DC-Project_3/
│
├── main.py        # Analysis script
├── nobel.csv      # Dataset of Nobel Prize laureates
└── README.md      # Documentation
```

---

## Conclusion

Through exploratory analysis of more than a century of Nobel Prize data, this project reveals both **progress and bias** in the history of global recognition.
While the representation of women and non-Western countries is still limited, the past two decades show a **gradual move toward greater diversity** in Nobel recognition.