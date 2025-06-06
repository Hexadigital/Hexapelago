# Lunacid Setup Guide
## Requirements

You will need:
- [BepInEx 5.4.22](https://github.com/BepInEx/BepInEx/releases/tag/v5.4.22)
- [Archipelago Client](https://github.com/ArchipelagoMW/Archipelago/releases)
- The [Lunacid Randomizer Mod and the APworld](https://github.com/Witchybun/LunacidAPClient/releases/).

## Installation

- Download and unpack the BepInEx version for x64 into your Lunacid installation folder.  If you don't know where it is, in Steam you can right-click and Manage -> Browse Local Files will get you there.
- **LINUX ONLY**: Right click Lunacid in Steam, go to Properties, and in Launch Options put `WINEDLLOVERRIDES="winhttp.dll=n,b" %command%`.
- Launch the game at least once, close.
- In BepInEx/plugins, take the folder in the mod zip named "LunacidAP" and place it here.
- Install Archipelago Client.  Documentation is [here](https://archipelago.gg/tutorial/Archipelago/setup/en).
- Once installed, go to where your client is installed, go to lib/worlds, drop the attached .apworld here.
- Run ArchipelagoLauncher, hit Generate Template Settings, in order for the Lunacid.yaml to be generated.

Hosting a game locally is simply taking the Lunacid.yaml file, editing it to suit the settings you want, putting the file in the Players folder, and hitting Generate in ArchipelagoLauncher.  For yaml formatting help, look [here](https://archipelago.gg/tutorial/Archipelago/advanced_settings/en).

## In-game setup

- Create a new save.  The first part of character creation is to log in.  After a successful connect, you'll be allowed to make a new character. 
- If successful, all data is saved to a file, found in the base game's folder under ArchSaves.
- Enjoy playing!

## Troubleshooting

*Q: My server's port changed and I can't connect.  How do I fix this?*

**A: Open the .json file for your related save, and change the port in the save directly.**

*Q: I was sent a key to open a door, but it won't open.*

**A: This is now bug report worthy, but short-term, walk to where the item exists, then leave the same area, or reload the area.  If it's the talismans, you may have to reopen the chests.**

If more stuff comes up I'll add it here.  Probably will, you know how it is.
