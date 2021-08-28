# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:34:37 2020

@author: books
"""

from os import makedirs, path
from re import compile
from shutil import copyfileobj, make_archive
from zipfile import ZipFile
from pathlib import Path
import notion_sync_module
from tempfile import TemporaryDirectory
from easygui import fileopenbox
import module.fontmatter 

NotionZip = Path(fileopenbox(filetypes = ['*.zip']))


# Load zip file
notionsData = ZipFile(NotionZip, 'r')

NotionPathRaw = []
ObsidianPathRaw = []
NotionPaths = []
ObsidianPaths = []



# Generate a list of file paths for all zip content
[NotionPathRaw.append(line.rstrip()) for line in notionsData.namelist()]

verbose = False
def debug_print(msg):
    if verbose:
        print(msg)

# Clean paths for Obsidian destination
regexUID = compile("\s+\w{32}")
regexForbitCharacter = compile("[<>?:/\|*\"]")

for line in NotionPathRaw:
    ObsidianPathRaw.append(regexUID.sub("", line))


### PATHS IN PROPER OS FORM BY PATHLIB ###
[NotionPaths.append(Path(line)) for line in NotionPathRaw]
[ObsidianPaths.append(Path(line)) for line in ObsidianPathRaw]



# Get all the relevant indices (folders, .md, .csv, others)
mdIndex, folderIndex, folderTree = notion_sync_module.ObsIndex(ObsidianPaths)
 

## Create a temporary directory to work with
unzipt = TemporaryDirectory()
tempPath = Path(unzipt.name)


## Create temp directory paths that match zip directory tree
tempDirectories = []

# Construct complete directory paths (<tempDirecory>/<zipDirectories>)
for d in folderTree:
    tempDirectories.append(tempPath / d)

## Create the temporary directory structure for future archive
for d in tempDirectories:
    makedirs(d, exist_ok=True)


num_link = [0, 0, 0, 0]
# Process all MD files
for n in mdIndex:
    
    # Access the original MD file
    with notionsData.open(NotionPathRaw[n], "r") as mdFile:
        print(module.fontmatter.fontmatter_get(mdFile))
        # Find and convert Internal Links to Obsidian style
        mdContent, cnt = notion_sync_module.N2Omd(mdFile)
        num_link = [cnt[i]+num_link[i] for i in range(len(num_link))]
        
        # Exported md file include header in first line
        # '# title of file'
        # Get full file name by first line of exported md file instead file name ObsidianPaths[n]
        ## Make temp destination file path
        new_file_name = mdContent[0].replace('# ', '') + '.md'
        new_file_name = regexForbitCharacter.sub("", new_file_name)
        newfilepath = tempPath / path.dirname(ObsidianPaths[n]) / new_file_name
        
        # Check if file exists, append if true
        if path.exists(newfilepath):
            append_write = 'a' # append if already exists
        else:
            append_write = 'w' # make a new file if not
        
        # Save modified content as new .md file
        with open(newfilepath, append_write, encoding='utf-8') as tempFile:
            [print(line.rstrip(), file=tempFile) for line in mdContent]



# Save temporary file collection to new zip
make_archive( NotionZip.parent / (NotionZip.name[:-4]+'-ObsidianReady'), 'zip', tempPath)




# Close out!
notionsData.close()