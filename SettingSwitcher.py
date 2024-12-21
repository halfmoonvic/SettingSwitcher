import sublime
import sublime_plugin
import os

SETTING_FILE = "SettingSwitcher.sublime-settings"


def generate_commands():
    # setting_switcher preferences commands
    resources = sublime.find_resources("commands.json")
    commands_content = sublime.load_resource(resources[0])
    commands = sublime.decode_value(commands_content)

    # setting switcher settings
    setting_resources = sublime.find_resources(SETTING_FILE)
    if not setting_resources:
        return

    content = sublime.load_resource(
        setting_resources[-1] if len(setting_resources) > 1 else setting_resources[0]
    )
    settings_dict = sublime.decode_value(content)
    command_types = settings_dict.keys()

    # add dynamic commands
    for command_type in command_types:
        commands.append(
            {
                "caption": "setting_switcher: switch to " + command_type,
                "command": "setting_switcher",
                "args": {"command_type": command_type},
            }
        )

    package_path = os.path.join(sublime.packages_path(), "SettingSwitcher")

    if not os.path.exists(package_path):
        os.makedirs(package_path)

    commands_path = os.path.join(package_path, "Default.sublime-commands")

    try:
        with open(commands_path, "w", encoding="utf-8") as f:
            json_content = sublime.encode_value(commands, pretty=True)
            f.write(json_content)
    except Exception as e:
        print("Error writing file:", str(e))


def plugin_loaded():
    generate_commands()
    sublime.load_settings(SETTING_FILE).add_on_change(
        "generate_commands", generate_commands
    )


class SettingSwitcherCommand(sublime_plugin.ApplicationCommand):
    def run(self, command_type):
        switcher_settings = sublime.load_settings(SETTING_FILE)
        settings = switcher_settings.get(command_type)

        # traverse all configured plug-ins
        for plugin_name, setting_map in settings.items():
            # plugins settings
            settings_filename = plugin_name + ".sublime-settings"
            settings_file = sublime.load_settings(settings_filename)

            for key, value in setting_map.items():
                settings_file.set(key, value)

            # save settings
            sublime.save_settings(settings_filename)
