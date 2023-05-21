#!/usr/local/bin/python3

import argparse
import os
import coloredlogs
import logging

coloredlogs.install(level='DEBUG')

def get_game_names(folder_name):
    game_names = []
    sub_folders = [f for f in os.listdir(folder_name) if os.path.isdir(os.path.join(folder_name, f))]
    
    for sub_folder in sub_folders:
        sub_folder_path = os.path.join(folder_name, sub_folder)
        game_file_path = os.path.join(sub_folder_path, "GAMENAME.txt")
        
        if os.path.exists(game_file_path):
            with open(game_file_path, 'r') as game_file:
                game_name = game_file.read().strip()
                game_names.append( (game_name, sub_folder_path) )
    
    return sorted(game_names)

def rename_sub_folders(folder_name):
    game_names = get_game_names(folder_name)
    logging.info(f'Number of games found: {len(game_names)}')
    
    replacements = dict()

    new_folder_index = 2
    for game_name, existing_game_path in game_names:
        
        new_folder_name = f"0{new_folder_index}" if new_folder_index < 10 else str(new_folder_index)
        
        logging.info(f'Processing {game_name} in {existing_game_path} with a target to: {new_folder_name}')
        
        # potential replacement
        existing_game_path = replacements[existing_game_path] if existing_game_path in replacements else existing_game_path

        target_game_path = os.path.join(folder_name, new_folder_name)

        if str(existing_game_path) == str(target_game_path):
            logging.debug(f'Already in the right place')
        else:    
            logging.debug(f'Moving from {existing_game_path} to {target_game_path} ')

            if os.path.exists(target_game_path):
                logging.debug(f'{target_game_path} already exists, renaming it temporarily')
                renamed = target_game_path + "_tmp"
                os.rename(target_game_path, renamed)
                replacements[target_game_path] = renamed
            
            os.rename(existing_game_path, target_game_path)
            
            logging.debug(f"Renamed folder '{existing_game_path}' to '{target_game_path}'")
        
        new_folder_index += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GDEMU Folder organizer")

    parser.add_argument("folder_name", help="Path to the SDCard root")

    args = parser.parse_args()

    folder_name = args.folder_name

    rename_sub_folders(folder_name)

    logging.info('Job done')
