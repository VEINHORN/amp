import os
import cisco_path


def init(rewrite=False):
    profile_path = os.path.join(
        cisco_path.profiles_dir(), 'AnyConnectProfile.xml')

    if not rewrite and os.path.isfile(profile_path):
        print('You already have file with Cisco AnyConnect profiles.')
        return
    # Create profile file
    with open('AnyConnectProfile.xml', 'r') as inp:
        with open(profile_path, 'w') as out:
            out.write(inp.read())
    print('Cisco AnyConnect profile file was successfully created.')
