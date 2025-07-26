#Team Hustler_23BCE7380

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = r"C:\Users\mehal\Downloads\fact_transport.csv"
df = pd.read_csv(file_path,encoding='latin-1')

# Convert 'month' column to datetime format
df['month'] = pd.to_datetime(df['month'])

# 1. Fuel Efficiency Insights
# Aggregate fuel consumption by vehicle class
vehicle_fuel_usage = df[[
    "vehicleClass_MotorCycle", "vehicleClass_MotorCar", "vehicleClass_AutoRickshaw", 
    "vehicleClass_Agriculture", "vehicleClass_others", 
    "fuel_type_petrol", "fuel_type_diesel", "fuel_type_electric"
]].sum()

# Extract vehicle class and fuel data separately
vehicle_classes = vehicle_fuel_usage[:5]
fuel_types = vehicle_fuel_usage[5:]

# Plot vehicle class distribution
plt.figure(figsize=(10, 5))
sns.barplot(x=vehicle_classes.index, y=vehicle_classes.values, hue=vehicle_classes.index, dodge=False, palette="viridis")
plt.title("Total Vehicle Registrations by Class")
plt.xlabel("Vehicle Class")
plt.ylabel("Total Count")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Plot fuel consumption distribution
plt.figure(figsize=(8, 5))
sns.barplot(x=fuel_types.index, y=fuel_types.values, palette="coolwarm")
plt.title("Total Fuel Consumption by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Total Count")
plt.grid(axis='y')
plt.show()

# 2. Fuel Consumption Trends Over Time
fuel_trends = df.groupby('month')[['fuel_type_petrol', 'fuel_type_diesel', 'fuel_type_electric']].sum()

plt.figure(figsize=(12, 6))
sns.lineplot(data=fuel_trends, marker="o")
plt.title("Fuel Consumption Trends Over Time")
plt.xlabel("Month")
plt.ylabel("Total Vehicles Registered")
plt.legend(["Petrol", "Diesel", "Electric"])
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 3. Electric Vehicle (EV) Growth Projection
# Extract EV registrations over time
ev_growth = fuel_trends['fuel_type_electric']

# Plot EV growth trend
plt.figure(figsize=(10, 5))
sns.lineplot(x=ev_growth.index, y=ev_growth.values, marker="o", color='green')
plt.title("Electric Vehicle Growth Over Time")
plt.xlabel("Month")
plt.ylabel("EV Registrations")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 4. Fuel vs. Seating Capacity
# Aggregating seating capacity data by fuel type
seating_capacity_fuel = df[['fuel_type_petrol', 'fuel_type_diesel', 'fuel_type_electric',
                            'seatCapacity_1_to_3', 'seatCapacity_4_to_6', 'seatCapacity_above_6']].sum()

# Reshaping data for visualization
seating_capacity_fuel = seating_capacity_fuel.iloc[3:].reset_index()
seating_capacity_fuel.columns = ['Seating Capacity', 'Total Vehicles']

# Plotting the seating capacity distribution
plt.figure(figsize=(8, 5))
sns.barplot(x=seating_capacity_fuel['Seating Capacity'], y=seating_capacity_fuel['Total Vehicles'], palette="magma")
plt.title("Total Vehicles by Seating Capacity")
plt.xlabel("Seating Capacity Category")
plt.ylabel("Total Vehicles")
plt.grid(axis='y')
plt.show()

# Aggregating fuel type distribution within each seating capacity category
fuel_vs_seating = df[['seatCapacity_1_to_3', 'seatCapacity_4_to_6', 'seatCapacity_above_6',
                      'fuel_type_petrol', 'fuel_type_diesel', 'fuel_type_electric']].sum()

# Extracting seating capacity and fuel type separately
seating_categories = fuel_vs_seating[:3]
fuel_types = fuel_vs_seating[3:]

# Plotting fuel type distribution within seating capacity categories
plt.figure(figsize=(8, 5))
sns.barplot(x=fuel_types.index, y=fuel_types.values, palette="coolwarm")
plt.title("Total Fuel Consumption by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Total Vehicles")
plt.grid(axis='y')
plt.show()

# 5. Correlation Analysis: Fuel Type vs. Seating Capacity
correlation_matrix = df[['fuel_type_petrol', 'fuel_type_diesel', 'fuel_type_electric',
                         'seatCapacity_1_to_3', 'seatCapacity_4_to_6', 'seatCapacity_above_6']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Between Fuel Type and Seating Capacity")
plt.show()
