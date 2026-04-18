from src.data_generator import generate_data
from src.analysis import load_data, clean_data, overall_analysis, region_analysis, save_summary
from src.visualization import plot_bar, plot_pie, plot_region
from src.visualization import plot_age_group

# Step 1: Generate Data
generate_data()

# Step 2: Load
df = load_data()

# Step 3: Clean
df = clean_data(df)

# Step 4: Analysis
overall = overall_analysis(df)
region = region_analysis(df)

# Step 5: Save Summary
save_summary(overall)
plot_age_group(df)

# Step 6: Visualize
plot_bar(overall)
plot_pie(overall)
plot_region(region)

print("Project executed successfully!")