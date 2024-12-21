import sublime
import sublime_plugin
import os
import json

def plugin_loaded():
    settings = sublime.load_settings('toggle_theme.sublime-settings')
    resources = sublime.find_resources('toggle_theme.sublime-settings')

    if not resources:
        return

    content = sublime.load_resource(resources[0])
    settings_dict = sublime.decode_value(content)
    theme_types = settings_dict.keys()

    commands = []
    for theme_type in theme_types:
        commands.append({
            "caption": "Theme: Switch to " + theme_type.title(),
            "command": "toggle_theme",
            "args": {"theme_type": theme_type}
        })

    package_path = os.path.join(sublime.packages_path(), "ToggleTheme")

    if not os.path.exists(package_path):
        os.makedirs(package_path)

    commands_path = os.path.join(package_path, "Default.sublime-commands")

    try:
        with open(commands_path, 'w', encoding='utf-8') as f:
            json_content = sublime.encode_value(commands, pretty=True)
            f.write(json_content)
    except Exception as e:
        print("Error writing file:", str(e))

class ToggleThemeCommand(sublime_plugin.ApplicationCommand):
    def run(self, theme_type):
        settings = sublime.load_settings('toggle_theme.sublime-settings')
        theme_settings = settings.get(theme_type)

        # Traverse all configured plug-ins
        for plugin_name, plugin_settings in theme_settings.items():
            # plugins settings
            settings_filename = plugin_name + '.sublime-settings'
            plugin_settings_obj = sublime.load_settings(settings_filename)

            for key, value in plugin_settings.items():
                plugin_settings_obj.set(key, value)

            # save settings
            sublime.save_settings(settings_filename)
