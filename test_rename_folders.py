import os
import pytest
from gdemu_folder_organizer import rename_sub_folders

@pytest.fixture
def setup_test_folders(tmpdir) -> str: 
    # Define the folder names and game names in the wrong order
    folder_names = ['01', '02', '03', '04', '05', '06']
    game_names = ['', 'Quake 3 Arena', 'Xeno Crisis', 'Crazy Taxi', 'Soul Calibur', '18 Wheeler American Pro trucker']
    
    # Create the test folders
    for folder_name, game_name in zip(folder_names, game_names):
        folder_path = tmpdir.join(folder_name)
        folder_path.mkdir()

        # Create the GAMENAME.txt file
        if not folder_name == "01":
            game_file_path = folder_path.join('GAMENAME.txt')
            game_file_path.write_text(game_name, 'UTF-8')

    return tmpdir

def test_rename_sub_folders(setup_test_folders):
    folder_name = str(setup_test_folders)

    # Call the function to rename subfolders
    rename_sub_folders(folder_name)

    # Check the order of the renamed folders and game names
    expected_order = ['01', '02', '03', '04', '05', '06']
    renamed_folders = sorted(os.listdir(folder_name))
    assert renamed_folders == expected_order

    # Check the order of the game names in renamed folders
    expected_game_names = ['', '18 Wheeler American Pro trucker', 'Crazy Taxi', 'Quake 3 Arena', 'Soul Calibur', 'Xeno Crisis']
    for sub_folder_name, expected_game_name in zip(renamed_folders[1:], expected_game_names[1:]):
        folder_path = os.path.join(folder_name, sub_folder_name, 'GAMENAME.txt')
        with open(folder_path, 'r') as game_file:
            game_name = game_file.read().strip()
            assert game_name == expected_game_name
