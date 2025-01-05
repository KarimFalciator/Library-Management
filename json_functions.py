import json
import os

def update_settings(font, font_size, theme, zoom):
    create_saved()
    try:
        if not os.path.exists('saved_settings.json'):
            print('File does not exist')
            return

        # Open and load the existing JSON file
        with open('saved_settings.json', 'r') as file:
            data = json.load(file)

        # Update the data dictionary with new values
        data['Font'] = font
        data['Font_size'] = font_size
        data['Theme'] = theme
        data['Zoom'] = zoom

        # Save the updated data back to the JSON file
        with open('saved_settings.json', 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")


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
# if __name__ == '__main__':
#     update_settings('Ariel', '12', 'System', '1')\