# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Start coding here!
nobel = pd.read_csv('nobel.csv')

print(nobel.columns)
print()

#1
top_gender = nobel['sex'].mode()[0]
top_country = nobel['birth_country'].mode()[0]

print(top_gender)
print()
print(top_country)

#2
second_task = nobel[['birth_country', 'year', 'sex']].copy()
second_task['USA_winner'] = second_task['birth_country'] == 'United States of America'
second_task['decade'] = (second_task['year'] // 10) * 10 

ratio = second_task.groupby('decade').agg(
    total_winners=('year', 'count'),
    usa_winners=('USA_winner', 'sum')
)

ratio['ratio'] = ratio['usa_winners'] / ratio['total_winners']

max_decade_usa = ratio['ratio'].idxmax()

print(max_decade_usa)
print()

#3
nobel['decade'] = (nobel['year'] // 10) * 10
female_winners = nobel[nobel['sex'] == "Female"]
grouped_females = female_winners.groupby(['decade', 'category']).size()
total_winners = nobel.groupby(['decade', 'category']).size()
female_ratio = grouped_females / total_winners
max_decade_category = female_ratio.idxmax()
max_female_dict = {max_decade_category[0]: max_decade_category[1]}
print(max_female_dict)
print()

#4
task_four = nobel[['category', 'full_name', 'sex', 'year']]
task_four = nobel[nobel['sex'] == "Female"]
task_four = task_four.sort_values('year', ascending=True)
first_woman = task_four.iloc[0]
first_woman_name = first_woman['full_name']
first_woman_category = first_woman['category']
print(first_woman_name)
print()
print(first_woman_category)
print()

#5
five_task = nobel[['prize', 'full_name', 'organization_name']]
name_counts = five_task['full_name'].value_counts()
name_counts = name_counts[name_counts >= 2].index
repeat_list = list(name_counts)
print(repeat_list)