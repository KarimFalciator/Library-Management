import json
import os

def edit_json(file_path, key, value):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"File '{file_path}' does not exist.")
            return

        print(f"Opening file: {file_path}")
        # Open and load the existing JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"Current data: {data}")

        # Update the key if it exists, or inform the user otherwise
        if key in data:
            print(f"Updating key '{key}' to '{value}'")
            data[key] = value
        else:
            print(f"Key '{key}' not found in the JSON file. Available keys: {list(data.keys())}")
            return

        # Save the updated data back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"New data: {data}")

        print(f"Successfully updated {key} to {value} in {file_path}")

    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
edit_json('Trials/default_settings2.json', 'Font', 'Courier')
