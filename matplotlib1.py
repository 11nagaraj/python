import matplotlib.pyplot as plt

# Student details
students = {
    'John': 85,
    'Marta': 90,
    'Mike': 80,
    'Emma': 95,
    'Chris': 78
}

# Extract names and marks
names = list(students.keys())
marks = list(students.values())

# Create bar chart
plt.figure(figsize=(10,6))
plt.bar(names, marks, color='blue')

# Add title and labels
plt.title('Marks of Students')
plt.xlabel('Students')
plt.ylabel('Marks')

# Show the bar chart
plt.show()
