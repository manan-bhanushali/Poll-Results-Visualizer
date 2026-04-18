import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
def plot_bar(percent):
    plt.figure(figsize=(6,4))
    sns.barplot(x=percent.index, y=percent.values)
    plt.title("Overall Preference")
    plt.savefig("images/bar_chart.png")
    plt.close()

def plot_pie(percent):
    plt.figure(figsize=(5,5))
    plt.pie(percent, labels=percent.index, autopct="%1.1f%%")
    plt.title("Vote Share")
    plt.savefig("images/pie_chart.png")
    plt.close()

def plot_region(region_percent):
    region_percent.plot(kind="bar", stacked=True, figsize=(8,5))
    plt.title("Region-wise Preference")
    plt.savefig("images/region_chart.png")
    plt.close()
def plot_age_group(df):
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x="Age_Group", hue="Product")
    plt.title("Age Group Preference")
    plt.savefig("images/age_group_chart.png")
    plt.close()