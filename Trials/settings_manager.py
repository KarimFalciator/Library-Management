import json
import os


class SettingsManager:
    def __init__(self, settings_file="settings.json"):
        self.settings_file = settings_file
        self.default_settings = {
            "font_size": 12,
            "font_type": "Arial",
            "font_color": "Black",
            "color_mode": "System"
        }
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as file:
                return json.load(file)
        else:
            return self.default_settings

    def save_settings(self):
        with open(self.settings_file, "w") as file:
            json.dump(self.settings, file, indent=4)

    def update_settings(self, font_size=None, font_type=None, font_color=None, color_mode=None):
        if font_size is not None:
            self.settings["font_size"] = font_size
        if font_type is not None:
            self.settings["font_type"] = font_type
        if font_color is not None:
            self.settings["font_color"] = font_color
        if color_mode is not None:
            self.settings["color_mode"] = color_mode
        self.save_settings()


# Create a global instance of SettingsManager
settings_manager = SettingsManager()