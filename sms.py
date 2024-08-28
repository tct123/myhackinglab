import subprocess
from tabulate import tabulate

# ADB-Befehl ausführen, um SMS-Nachrichten abzurufen
result = subprocess.run(
    ["adb", "shell", "content query --uri content://sms/inbox"],
    capture_output=True,
    text=True,
)

# Überprüfen, ob der Befehl erfolgreich war
if result.returncode != 0:
    print("Fehler beim Ausführen des ADB-Befehls.")
    exit(1)

# Verarbeiten der ADB-Ausgabe
output = result.stdout.splitlines()

# Liste zur Speicherung der SMS-Daten
sms_data = []

# Verarbeitung der Ausgabezeilen
for line in output:
    # Extrahiere die Adresse und den Nachrichtentext aus jeder Zeile
    try:
        address = line.split("address=", 1)[1].split(",")[0].strip()
        body = line.split("body=", 1)[1].split(",")[0].strip()
        sms_data.append({"address": address, "message": body})
    except IndexError:
        continue  # Ignoriere fehlerhafte oder unvollständige Zeilen

# Wenn keine SMS-Daten vorhanden sind, eine Meldung anzeigen
sms_dict = {}
if not sms_data:
    print("Keine SMS-Daten gefunden oder Fehler beim Abrufen.")
else:
    # Ausgabe der SMS-Daten in Tabellenform
    table = [[[sms["address"]], [sms["message"]]] for sms in sms_data]
    for row in table:
        print(row[0][0],row[1][0])
        sms_dict["address"] = row[0][0]
        sms_dict["message"] = row[1][0]
        print(sms_dict)
