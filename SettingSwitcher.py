import sublime
import sublime_plugin
import os
import json

def plugin_loaded():
    settings = sublime.load_settings('SettingSwitcher.sublime-settings')
    resources = sublime.find_resources('SettingSwitcher.sublime-settings')

    if not resources:
        return

    content = sublime.load_resource(resources[-1] if len(resources) > 1 else resources[0])
    settings_dict = sublime.decode_value(content)
    command_types = settings_dict.keys()

    commands = [
        {
            "caption": "Preferences: SettingSwitcher Settings",
            "command": "edit_settings",
            "args": {
                "base_file": "${packages}/SettingSwitcher/SettingSwitcher.sublime-settings",
                "default": "// SettingSwitcher Settings - User\n{\n\t$0\n}\n"
            }
        }
    ]

    for command_type in command_types:
        commands.append({
            "caption": "setting_switcher: Switch to " + command_type.title(),
            "command": "setting_switcher",
            "args": {"command_type": command_type}
        })

    package_path = os.path.join(sublime.packages_path(), "SettingSwitcher")

    if not os.path.exists(package_path):
        os.makedirs(package_path)

    commands_path = os.path.join(package_path, "Default.sublime-commands")

    try:
        with open(commands_path, 'w', encoding='utf-8') as f:
            json_content = sublime.encode_value(commands, pretty=True)
            f.write(json_content)
    except Exception as e:
        print("Error writing file:", str(e))

class SettingSwitcherCommand(sublime_plugin.ApplicationCommand):
    def run(self, command_type):
        switcher_settings = sublime.load_settings('SettingSwitcher.sublime-settings')
        settings = switcher_settings.get(command_type)

        # Traverse all configured plug-ins
        for plugin_name, setting_map in settings.items():
            # plugins settings
            settings_filename = plugin_name + '.sublime-settings'
            settings_file = sublime.load_settings(settings_filename)

            for key, value in setting_map.items():
                settings_file.set(key, value)

            # save settings
            sublime.save_settings(settings_filename)
