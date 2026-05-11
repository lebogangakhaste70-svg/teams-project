import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Year":[2020,2021,2022,2023],
    "Sales":[100,150,200,250]
})

print(data)

data.plot(x="Year", y="Sales", kind="line")

plt.show()