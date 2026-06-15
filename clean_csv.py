import pandas as pd

df = pd.read_csv("students.csv")

print(df)

# missing
print("Missing Values: ")
print(df.isnull().sum())

#duplicated
print("Duplicates: ")
print(df.duplicated())

print("Duplicated rows: ")
print(df.duplicated().sum())

print("\nDuplicate Rows Without ID:")
print(df.duplicated(subset=["name", "age", "marks", "city"]))

print("\nDuplicate Count Without ID:")
print(df.duplicated(subset=["name", "age", "marks", "city"]).sum())

# remove duplicated
df = df.drop_duplicates(subset=["name", "age", "marks", "city"])
print("\nAfter Removing Duplicates:")
print(df)

# Convert marks to numerics
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")

print("After Converting marks into numerics: ")
print(df)

# fill unknown
df["name"] = df["name"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].mean())
df["marks"] = df['marks'].fillna(df["marks"].mean())
df["city"] = df["city"].fillna("Not Available")

print("\nAfter Filling Missing Values: ")
print(df)

# check and fix d types
print("\nData Types Before Conversion: ")
print(df.dtypes)

df["age"] = df["age"].astype(int)

print("\nData types after Conversion: ")
print(df.dtypes)

#Analysis
print("\nAverage Marks: ")
print(df["marks"].mean())

print("\nHighest Marks: ")
print(df["marks"].max())

print("\nLowest Marks: ")
print(df["marks"].min())

topper = df[df["marks"] == df["marks"].max()]

print("\nTopper: ")
print(topper)

print("\nTotal Students: ")
print(len(df))

# City-wise analysis using group-by
print("\nCity-wise Average Marks: ")
print(df.groupby("city")["marks"].mean())

print("\nCity-wise Student Count: ")
print(df.groupby("city")["id"].count())

# Sort student marks
print("\nStudents sorted by Marks(high-low): ")
print(df.sort_values(by="marks", ascending=False))

print("\nTop 3 Students: ")
print(df.sort_values(by="marks", ascending=False).head(3))

print("\nBottom 3 Students: ")
print(df.sort_values(by="marks", ascending=True).head(3))

# save cleaned data
df.to_csv("cleaned_students.csv", index=False)
print("\nCleaned CSV file created successfully.")