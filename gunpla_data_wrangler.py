import os
import csv
import re

# File source is from https://www.kaggle.com/datasets/marzho/gunpla-dataset

gunpla_file = os.chdir(os.getcwd() + "gunpla_files")

high_grade = [
    "hg00.csv",
    "hgage.csv",
    "hgibo.csv",
    "hgreconguista.csv",
    "hgseed.csv",
    "hgtheorigin.csv",
    "hgthunderbolt.csv",
    "hgwfm.csv",
    "highgrade.csv",
]
other_files_apperance = ["1_100seed.csv", "1_100_00.csv", "re100.csv"]
master_grade = ["mastergrade.csv"]
real_grade = ["realgrade.csv"]
perfect_grade = ["perfectgrade.csv"]
sd_grade = ["sdbb.csv", "sdcs.csv", "sdexs.csv", "sdgg.csv"]

row_data = []

for file in high_grade:
    with open(file, "r", encoding="utf-8") as csv_reads:
        reader = csv.DictReader(csv_reads)
        for row in reader:
            row_data.append(
                {
                    "Product Name": row["Product Name"],
                    "Release Date": row["Release Date"],
                    "First appearance": row["First appearance"],
                    "MSRP": row["MSRP"],
                    "Grade": "High Grade",
                }
            )

for file in other_files_apperance:
    with open(file, "r", encoding="utf-8") as csv_reads:
        reader = csv.DictReader(csv_reads)
        for row in reader:
            row_data.append(
                {
                    "Product Name": row["Product Name"],
                    "Release Date": row["Release Date"],
                    "First appearance": row["First appearance"],
                    "MSRP": row["MSRP"],
                    "Grade": "Other",
                }
            )

with open(master_grade[0], "r", encoding="utf-8") as csv_reads:
    reader = csv.DictReader(csv_reads)
    for row in reader:
        row_data.append(
            {
                "Product Name": row["Product Name"],
                "Release Date": row["Release Date"],
                "First appearance": row["First appearance"],
                "MSRP": row["MSRP"],
                "Grade": "Master Grade",
            }
        )
#
with open(real_grade[0], "r", encoding="utf-8") as csv_reads:
    reader = csv.DictReader(csv_reads)
    for row in reader:
        row_data.append(
            {
                "Product Name": row["Product Name"],
                "Release Date": row["Release Date"],
                "First appearance": row["First appearance"],
                "MSRP": row["MSRP"],
                "Grade": "Real Grade",
            }
        )
#
with open(perfect_grade[0], "r", encoding="utf-8") as csv_reads:
    reader = csv.DictReader(csv_reads)
    for row in reader:
        row_data.append(
            {
                "Product Name": row["Product Name"],
                "Release Date": row["Release Date"],
                "First appearance": row["First appearance"],
                "MSRP": row["MSRP"],
                "Grade": "Perfect Grade",
            }
        )

with open("advancedgrade.csv", "r", encoding="utf-8") as csv_reads:
    reader = csv.DictReader(csv_reads)
    for row in reader:
        row_data.append(
            {
                "Product Name": row["Product Name"],
                "Release Date": row["Release Date"],
                "First appearance": "Mobile Suit Gundam AGE",
                "MSRP": row["MSRP"],
                "Grade": "Advanced Grade",
            }
        )

with open("ibofullmechanics.csv", "r", encoding="utf-8") as csv_reads:
    reader = csv.DictReader(csv_reads)
    for row in reader:
        row_data.append(
            {
                "Product Name": row["Product Name"],
                "Release Date": row["Release Date"],
                "First appearance": "Mobile Suit Gundam: Iron Blooded Orphans",
                "MSRP": row["MSRP"],
                "Grade": "Full Mechanics",
            }
        )

for file in sd_grade:
    with open(file, "r", encoding="utf-8") as csv_reads:
        reader = csv.DictReader(csv_reads)
        for row in reader:
            row_data.append(
                {
                    "Product Name": row["Product Name"],
                    "Release Date": row["Release Date"],
                    "First appearance": row["First appearance"],
                    "MSRP": row["MSRP"],
                    "Grade": "SD",
                }
            )

#
with open("gundam_data.csv", "w", encoding="utf-8") as write:
    csv_writer = csv.DictWriter(
        write,
        fieldnames=[
            "Product Name",
            "Release Date",
            "First appearance",
            "MSRP",
            "Grade",
        ],
        lineterminator="\n",
    )
    csv_writer.writeheader()
    for row in row_data:
        csv_writer.writerow(row)
