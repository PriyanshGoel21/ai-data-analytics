import csv
import sqlite3

filename = "traffic.csv"
conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

with open(filename, "r") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row[0] == "date_of_metrics":
            continue
        date_of_visit = row[0]
        partner_region = row[1]
        partner_country = row[2]
        partner = row[3]
        if row[4].startswith("Samsung"):
            brand_name = "Samsung"
            phone_model = row[4].replace("Samsung", "").strip()
        elif row[4].startswith("Apple"):
            brand_name = "Apple"
            phone_model = row[4].replace("Apple", "").strip()
        elif row[4].startswith("Oppo"):
            brand_name = "Oppo"
            phone_model = row[4].replace("Oppo", "").strip()
        elif row[4].startswith("Google"):
            brand_name = "Google"
            phone_model = row[4].replace("Google", "").strip()
        elif row[4].startswith("Website"):
            brand_name = None
            phone_model = None
        if phone_model == "":
            phone_model = None
        total_visits = int(row[5].split(".")[0])
        # cursor.execute(
        #     "INSERT INTO traffic (date_of_metrics, total_visits, brand_name, phone_model, partner, partner_country, "
        #     "partner_region) VALUES (?, ?, ?, ?, ?, ?, ?)",
        #     (
        #         date_of_visit,
        #         total_visits,
        #         brand_name,
        #         phone_model,
        #         partner,
        #         partner_country,
        #         partner_region,
        #     ),
        # )
        with open("rag.txt", "a+") as F:
            F.write(
                f"The date of metrics is {date_of_visit}. The partner region is {partner_region}. The partner country "
                f"is {partner_country}. The partner is {partner}. The brand name is {brand_name}. The total visits is "
                f"{total_visits}. The phone model is {phone_model}\n"
            )
conn.commit()
conn.close()
