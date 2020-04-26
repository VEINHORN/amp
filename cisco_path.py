import os

# got from the gist https://gist.github.com/JosefJezek/dc251a71cab6336f55bd


def profiles_dir():
    if os.name == 'posix':
        return '/opt/cisco/anyconnect/profile/'
    elif os.name == 'nt':
        return '%ProgramData%\\Cisco\\Cisco AnyConnect Secure Mobility Client\\Profile'
    else:
        raise ValueError('Unsupported operating system')
