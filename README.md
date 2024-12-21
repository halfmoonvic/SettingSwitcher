# SettingSwitcher

A Sublime Text plugin that enables quick switching between different setting configurations.

## Features

-   Switch multiple plugin settings with a single command
-   Dynamically generated command palette entries
-   Easy configuration through a single settings file

## Installation

1. Clone this repository to your Sublime Text Packages directory
2. Restart Sublime Text

## Configuration

Create a `SettingSwitcher.sublime-settings` file in your User package directory with your desired configurations:

```json
{
    "command1": {
        "Preferences.sublime-settings": {
            "font_size": 14,
            "word_wrap": true
        },
        "Package1.sublime-settings": {
            "setting1": "value1"
        }
    },
    "command2": {
        "Preferences.sublime-settings": {
            "font_size": 18,
            "word_wrap": false
        }
    }
}
```

## Usage

1. Open the command palette (Ctrl+Shift+P / Cmd+Shift+P)
2. Type "SettingSwitcher: Switch to" and select your desired configuration, "command1" or "command2"
3. The plugin will automatically update all settings defined in that configuration

## How It Works

The plugin loads configurations from `SettingSwitcher.sublime-settings` on startup and creates command palette entries for each configuration. When a switch command is executed, it updates the settings of all specified packages according to the selected configuration.

## License

MIT License
