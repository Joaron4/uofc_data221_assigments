# Question 8 (1 Point): Pandas DataFrame with Computed Column
#------------------------------------------------------------------------
"""
Install the pandas package and import it using the alias pd. Then:
• Create a DataFrame using the provided column data.
• Add a new column derived from existing columns.
• Print the final DataFrame.

"""
import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}
df = pd.DataFrame(data)
df['D'] = df['A'] + df['B']
print(df)