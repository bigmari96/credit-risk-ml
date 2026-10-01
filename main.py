import csv
from pathlib import Path

# Trova il CSV partendo dalla cartella di questo script.
csv_path = Path(__file__).parent / "data" / "applicants.csv"

with csv_path.open(encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    required_columns = {
        "applicant_id",
        "age",
        "annual_income",
        "loan_amount",
        "default",
    }

    actual_columns = set(reader.fieldnames or [])
    missing_columns = required_columns - actual_columns

    if missing_columns:
        missing_names = ", ".join(sorted(missing_columns))
        raise ValueError(f"Colonne mancanti nel CSV: {missing_names}")
    applicants = list(reader)

total = len(applicants)
defaults = sum(int(row["default"]) for row in applicants)
default_rate = defaults / total if total > 0 else 0

print(f"Richiedenti: {total}")
print(f"Mancati rimborsi: {defaults}")
print(f"Percentuale di mancati rimborsi: {default_rate:.0%}")