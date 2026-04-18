import pandas as pd
import numpy as np

def generate_data(n=300):
    np.random.seed(42)

    data = {
        "Respondent_ID": range(1, n+1),
        "Region": np.random.choice(["North", "South", "East", "West"], n),
        "Age_Group": np.random.choice(["18-25", "26-35", "36-50"], n),
        "Gender": np.random.choice(["Male", "Female"], n),
        "Product": np.random.choice(["Product A", "Product B", "Product C"], n),
    }

    df = pd.DataFrame(data)
    df.to_csv("data/poll_data.csv", index=False)

    return df