import json
import os

def update_settings(font, font_size, theme, zoom):
    data = {font, font_size, theme, zoom}
    create_saved()
    try:
        # Check if the file exists
        if not os.path.exists('saved_settings.json'):
            return
        print('File exists')
        # Open and load the existing JSON file
        with open(f'saved_settings.json', 'r') as file:
            data = json.load(file)
        print('file loaded')
        # Save the updated data back to the JSON file
        with open('saved_settings.json', 'w') as file:
            json.dump(data, file, indent=4)
        print('file updated')
    except json.JSONDecodeError:
        return
    except Exception as e:
        return

def read_settings():
    saved_settings = 'saved_settings.json'
    default_settings = 'default_settings.json'
    try:
        # Check if the file already exists
        if not os.path.exists(saved_settings):
            with open(default_settings, 'r') as file:
                settings = json.load(file)
                print(settings)
            return
    except Exception as e:
        return
    
def create_saved():
    saved_settings = 'saved_settings.json'
    default_settings = 'default_settings.json'
    try:
        # Check if the file already exists
        if not os.path.exists(saved_settings):
            with open(default_settings, 'r') as file:
                settings = json.load(file)
            with open(saved_settings, 'w') as file:
                json.dump(settings, file)
            return
    except Exception as e:
        return

# Example usage
if __name__ == '__main__':
    update_settings('Ariel', '24', 'light', '1')