import argparse
import json
import os
try:
    from exporter import export_objects
except ImportError:
    from .exporter import export_objects
try:
    from config import Config
except ImportError:
    from .config import Config

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Export selected ArchiCAD objects to a specified file format.")
    parser.add_argument('-f', '--format', choices=['json', 'csv'], required=True, help="Output file format (json or csv).")
    parser.add_argument('-o', '--output', required=True, help="Output file path.")
    
    # Parse arguments
    args = parser.parse_args()

    # Load configuration settings
    try:
        config = Config()
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return

    # Ensure the output directory exists
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        print(f"Output directory does not exist: {output_dir}")
        return

    # Export the selected objects
    try:
        if not hasattr(config, 'selected_objects'):
            print("Error: Config object has no 'selected_objects' attribute")
            return
        export_objects(config.selected_objects, args.format, args.output)
        print(f"Export successful: {args.output}")
    except Exception as e:
        print(f"Error during export: {e}")

if __name__ == "__main__":
    main()
