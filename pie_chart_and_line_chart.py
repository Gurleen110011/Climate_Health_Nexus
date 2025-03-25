import matplotlib.pyplot as plt

disease_summary = data['Disease'].value_counts()

plt.figure(figsize=(8, 8))
disease_summary.head(5).plot.pie(autopct='%1.1f%%', startangle=140, cmap='tab20')
plt.title('Top 5 Diseases by Occurrence')
plt.ylabel('')  
plt.savefig("dataset_pie.png", dpi=300, bbox_inches='tight') 
plt.show()

yearly_deaths = data.groupby('year')['Deaths'].sum()

plt.figure(figsize=(10, 6))
plt.plot(yearly_deaths.index, yearly_deaths.values, marker='o', linestyle='-', color='b')
plt.title('Yearly Deaths Across All Diseases')
plt.xlabel('Year')
plt.ylabel('Total Deaths')
plt.grid(True)
plt.savefig("dataset_line.png", dpi=300, bbox_inches='tight')  
plt.show()

state_cases = data.groupby('state_ut')['Cases'].sum().sort_values(ascending=False)

data['Cases'] = pd.to_numeric(data['Cases'], errors='coerce').fillna(0)

state_cases = data.groupby('state_ut')['Cases'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
state_cases.head(10).plot(kind='bar', color='coral')
plt.title('Top 10 States by Total Cases')
plt.xlabel('State/UT')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.savefig("top_10_states.png", dpi=300, bbox_inches='tight') 
plt.show()

