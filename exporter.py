import json
import csv
import os

class Exporter:
    def __init__(self, objects):
        """
        Initialize the exporter with the list of objects to export.
        :param objects: List of objects to be exported.
        """
        self.objects = objects

    def export_to_json(self, file_path):
        """
        Export the objects to a JSON file.
        :param file_path: Path to the output JSON file.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(self.objects, json_file, ensure_ascii=False, indent=4)
            print(f"Successfully exported {len(self.objects)} objects to {file_path}")
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def export_to_csv(self, file_path):
        """
        Export the objects to a CSV file.
        :param file_path: Path to the output CSV file.
        """
        if not self.objects:
            print("No objects to export.")
            return
        
        # Validate that all objects are dictionaries and collect all keys
        all_keys = set()
        for obj in self.objects:
            if not isinstance(obj, dict):
                print(f"Error: All objects must be dictionaries for CSV export")
                return
            all_keys.update(obj.keys())
        
        keys = sorted(all_keys)
        
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(self.objects)
            print(f"Successfully exported {len(self.objects)} objects to {file_path}")
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# TODO: Add unit tests for the Exporter class
# TODO: Implement support for exporting to other formats (e.g., XML)
# TODO: Consider adding a feature to filter objects before exporting

if __name__ == "__main__":
    # Example usage
    sample_objects = [
        {"name": "Object1", "type": "Furniture", "material": "Wood"},
        {"name": "Object2", "type": "Window", "material": "Glass"}
    ]

    exporter = Exporter(sample_objects)
    exporter.export_to_json("objects.json")
    exporter.export_to_csv("objects.csv")
