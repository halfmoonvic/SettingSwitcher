import sublime
import sublime_plugin
import os

class ToggleThemeCommand(sublime_plugin.ApplicationCommand):
    def run(self, theme_type):
        settings = sublime.load_settings('toggle_theme.sublime-settings')
        theme_settings = settings.get(theme_type)

        # Traverse all configured plug-ins
        for plugin_name, plugin_settings in theme_settings.items():

            # Preferences.sublime-settings
            if plugin_name == 'color_scheme':
                preferences = sublime.load_settings('Preferences.sublime-settings')
                preferences.set('color_scheme', plugin_settings)
                sublime.save_settings('Preferences.sublime-settings')
                continue

            # plugins settings
            settings_filename = plugin_name + '.sublime-settings'
            plugin_settings_obj = sublime.load_settings(settings_filename)

            for key, value in plugin_settings.items():
                plugin_settings_obj.set(key, value)

            # save settings
            sublime.save_settings(settings_filename)
