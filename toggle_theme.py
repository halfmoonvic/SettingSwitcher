import sublime
import sublime_plugin
import os

class ToggleThemeCommand(sublime_plugin.ApplicationCommand):
    def run(self, theme_type):
        # 获取设置文件
        settings = sublime.load_settings('toggle_theme.sublime-settings')
        preferences = sublime.load_settings('Preferences.sublime-settings')

        if theme_type == 'light':
            color_scheme = settings.get('light')
        else:
            color_scheme = settings.get('dark')

        # 更新 color_scheme
        preferences.set('color_scheme', color_scheme)
        sublime.save_settings('Preferences.sublime-settings')
