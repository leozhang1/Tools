import pwd
import os

AUTOMATE_TEXTING_PATH = f'/home/{pwd.getpwuid(os.getuid()).pw_name}/Documents/GitHub/automate_texting/'
LOG_PATH = '/tmp/'
BASE_DIR = f'/home/{pwd.getpwuid(os.getuid()).pw_name}/Documents/GitHub/'
PATH_TO_WALLPAPERS = f'/home/{pwd.getpwuid(os.getuid()).pw_name}/custom_wallpapers/Community-wallpapers/merged/'
CHROME_DATA_PATH = f'/home/{pwd.getpwuid(os.getuid()).pw_name}/.config/google-chrome/'
CHROME_BINARY_LOCATION = "/opt/google/chrome/google-chrome"