import pandas as pd

data = {
    "Category": ["Regions", "Functions", "Lines", "Branches"],
    "Missed / Total": ["13,865 / 15,955", "1,959 / 2,650", "24,586 / 27,692", "7,263 / 7,884"],
    "Cover %": [13.10, 26.08, 11.22, 7.88]
}

df = pd.DataFrame(data)
print(df.to_string(index=False))
