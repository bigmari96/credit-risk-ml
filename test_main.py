import shutil
import subprocess
import sys
from pathlib import Path


def test_missing_default_column(tmp_path):
    # Copia lo script nella cartella temporanea del test.
    original_script = Path(__file__).parent / "main.py"
    test_script = tmp_path / "main.py"
    shutil.copy(original_script, test_script)

    # Prepara un CSV a cui manca la colonna "default".
    data_folder = tmp_path / "data"
    data_folder.mkdir()

    csv_path = data_folder / "applicants.csv"
    csv_path.write_text(
        "applicant_id,age,annual_income,loan_amount\n"
        "1,25,28000,8000\n",
        encoding="utf-8",
    )

    # Esegue lo script e raccoglie il risultato.
    result = subprocess.run(
        [sys.executable, str(test_script)],
        capture_output=True,
        text=True,
    )

    # Verifica che si fermi con l'errore previsto.
    assert result.returncode != 0
    assert "Colonne mancanti nel CSV: default" in result.stderr