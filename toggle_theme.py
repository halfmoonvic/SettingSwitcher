import sublime
import sublime_plugin
import os

class ToggleThemeCommand(sublime_plugin.ApplicationCommand):
    def run(self, theme_type):
        # 获取设置文件
        settings = sublime.load_settings('toggle_theme.sublime-settings')

        # 获取主题配置
        theme_settings = settings.get(theme_type)

        # {'color_scheme': 'Packages/Color Scheme - Default/Mariana.sublime-color-scheme', 'file_browser': {'file_browser_theme': 'dark'}}

        # 更新 Sublime Text 主题
        if 'color_scheme' in theme_settings:
            preferences = sublime.load_settings('Preferences.sublime-settings')
            preferences.set('color_scheme', theme_settings['color_scheme'])
            sublime.save_settings('Preferences.sublime-settings')

        # 更新 FileBrowser 主题
        if 'dired' in theme_settings:
            file_browser_settings = sublime.load_settings('dired.sublime-settings')
            for key, value in theme_settings['dired'].items():
                print(key, value)
                file_browser_settings.set(key, value)
            sublime.save_settings('dired.sublime-settings')
