GDEmu folder organizer
===============================

If you use GDEmu, this project will help you organizer your games so they are listed in alphabetical order.

## How to use it

GDEmu requires your images to be placed under a [sequential folder structure](https://gdemu.wordpress.com/operation/gdemu-operation/), the limitation with that is that you need to rearrange your folder/files manually.

### Naming the folders

For each folder, create a `GAMENAME.txt` containing the name of the title inside it (this file is ignored by GDemu).

### Running the script

You need a Python3 environment.

Install dependencies and run `gdemu_folder_organizer.py` indicating where your SD Card is mounted:

```bash
pip3 install -r requirements.txt
python3 gdemu_folder_organizer.py "/Volumes/GDEMU"
```

Re-run the script every time you add/change your main folder structure.