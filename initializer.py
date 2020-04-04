import os
from constants import PROFILE_FILE_PATH


def init():
    if os.path.isfile(PROFILE_FILE_PATH):
        print('You already have file with Cisco AnyConnect profiles.')
        return
    # Create profile file
    with open('AnyConnectProfile.xml', 'r') as inp:
        with open(PROFILE_FILE_PATH, 'w') as out:
            out.write(inp.read())
    print('Cisco AnyConnect profile file was successfully created.')
