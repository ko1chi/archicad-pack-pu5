import os
import json

class Config:
    def __init__(self):
        # Default settings for the exporter
        self.output_format = 'json'  # Options: 'json' or 'csv'
        self.output_directory = os.path.expanduser('~')  # Default to user's home directory
        self.include_metadata = True  # Whether to include additional metadata in the export
        self.file_name = 'exported_objects'  # Default file name

    def load_config(self, config_file):
        """Load configuration from a JSON file."""
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"Config file '{config_file}' not found.")

        with open(config_file, 'r') as f:
            config_data = json.load(f)
            self.output_format = config_data.get('output_format', self.output_format)
            self.output_directory = config_data.get('output_directory', self.output_directory)
            self.include_metadata = config_data.get('include_metadata', self.include_metadata)
            self.file_name = config_data.get('file_name', self.file_name)

    def save_config(self, config_file):
        """Save current configuration to a JSON file."""
        config_data = {
            'output_format': self.output_format,
            'output_directory': self.output_directory,
            'include_metadata': self.include_metadata,
            'file_name': self.file_name
        }
        
        with open(config_file, 'w') as f:
            json.dump(config_data, f, indent=4)

    def validate_config(self):
        """Validate current configuration settings."""
        if self.output_format not in ['json', 'csv']:
            raise ValueError("Invalid output format. Choose 'json' or 'csv'.")
        
        if not os.path.isdir(self.output_directory):
            raise ValueError(f"Output directory '{self.output_directory}' does not exist.")

# TODO: Add more configuration options as needed
# TODO: Consider implementing support for more output formats in the future.
