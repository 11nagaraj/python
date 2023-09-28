import matplotlib.pyplot as plt

# Employee details
employees = {
    'Alice': 5,
    'Bob': 8,
    'Charlie': 2,
    'Diana': 6,
    'Ethan': 7
}

# Extract names and task counts
names = list(employees.keys())
task_counts = list(employees.values())

# Create a color list for each slice
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen']

# Create a pie chart
plt.figure(figsize=(8,8))
plt.pie(task_counts, labels=names, autopct='%1.1f%%', startangle=140, colors=colors)

# Add title
plt.title('Tasks Completed by Each Employee')

# Show the pie chart
plt.show()
