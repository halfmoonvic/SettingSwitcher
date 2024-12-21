# SettingSwitcher

A Sublime Text plugin that enables quick switching between different setting configurations.

## Features

-   Switch multiple plugin settings with a single command
-   Dynamically generated command palette entries
-   Easy configuration through a single settings file

## Installation

1. Clone or download git repo into your packages folder
2. Using Package Control:
   Run "Package Control: Install Package" command, and find SettingSwitcher package

## Configuration

Create a `SettingSwitcher.sublime-settings` file in your User package directory with your desired configurations:

```json
{
    "light": {
        "Preferences": {
            "color_scheme": "Packages/Color Scheme - Default/Breakers.sublime-color-scheme",
            "font_size": 14
        }
    },
    "dark": {
        "Preferences": {
            "color_scheme": "Packages/Color Scheme - Default/Mariana.sublime-color-scheme",
            "font_size": 14
        }
    }
}
```

## Usage

1. Open the command palette (Ctrl+Shift+P / Cmd+Shift+P)
2. Type "setting_switcher: switch to" and select your desired configuration, like "switch to light" or "switch to dark"
3. The plugin will automatically update all settings defined in that configuration

## How It Works

The plugin loads configurations from `SettingSwitcher.sublime-settings` on startup and creates command palette entries for each configuration. When a switch command is executed, it updates the settings of all specified packages according to the selected configuration.

## License

MIT License
