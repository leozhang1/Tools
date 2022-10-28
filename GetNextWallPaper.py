import os
import sys
import re

os.chdir(os.path.dirname(__file__))

# write to bash script the next item in the absolute path
BASH_SCRIPT_PATH = os.getcwd() + '/' + 'bash_scripts/set_i3_wallpaper.sh'
PATH_TO_WALLPAPERS = '/home/leo_zhang/custom_wallpapers/Community-wallpapers/merged/'
if not os.path.exists(BASH_SCRIPT_PATH):
    open(BASH_SCRIPT_PATH,'w').close()

# TODO: don't assume wallpapers is not empty
wallpapers = os.listdir(PATH_TO_WALLPAPERS)
for wallpaper in wallpapers:
    print(wallpaper)

print(len(wallpapers))

def main():
    # get the file name (without the path to it) of the wallpaper from the bash script
    filename = None
    
    if os.stat(BASH_SCRIPT_PATH).st_size == 0:
        with open(BASH_SCRIPT_PATH, 'w') as f:
            f.write(f'feh --bg-fill {PATH_TO_WALLPAPERS}{wallpapers[0]}')
        return
    
    
    with open(BASH_SCRIPT_PATH, 'r') as f:
        # parse out the previous filename
        cmd = f.readline()
        print(cmd)
        get_match = re.search('\/([A-Za-z_0-9-\s.]+\.[A-Za-z]{3,4})', cmd)
        filename = get_match.group(1) if get_match else None
            
    with open(BASH_SCRIPT_PATH, 'w') as w:
        if filename: 
            # find the position of the current filename
            # TODO: dont assume filename is in the directory
            pos = wallpapers.index(filename)
            print(f'position: {pos}')
            # write the next wallpaper at the (p + 1)th position to the bash script
            w.write(f'feh --bg-fill {PATH_TO_WALLPAPERS}{wallpapers[(pos+1)%len(wallpapers)]}')

if __name__ == "__main__":
    main()





