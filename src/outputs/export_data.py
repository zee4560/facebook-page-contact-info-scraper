thonimport json
import csv

def export_json(data, filename='output.json'):
    """Export data to JSON."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def export_csv(data, filename='output.csv'):
    """Export data to CSV."""
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)