from xml.dom import minidom
from host_entry import HostEntry
from colorama import Fore, Style
import cisco_path
import os


def list():
    def create_host_entry(entry_elm):
        return HostEntry(host_entry_elm.getElementsByTagName('HostName')[0].firstChild.nodeValue, host_entry_elm.getElementsByTagName('HostAddress')[0].firstChild.nodeValue)

    def splitter(count=None):
        return "=" * count if count else "=" * 77

    profile_path = os.path.join(
        cisco_path.profiles_dir(), 'AnyConnectProfile.xml')
    with open(profile_path, 'r') as inp:
        dom = minidom.parse(inp)
        elms = dom.getElementsByTagName('ServerList')[0]

        entry_elms = elms.getElementsByTagName('HostEntry')
        msg = f'You have {Fore.GREEN}{ len(entry_elms) } available servers{Style.RESET_ALL} in your AnyConnectProfile.xml config:'
        print(msg)

        print(splitter())
        for idx, host_entry_elm in enumerate(entry_elms):
            host_entry = create_host_entry(host_entry_elm)

            print(f'Id: {idx}')
            print(
                f'Server name: {Fore.GREEN}{host_entry.name}{Style.RESET_ALL}')
            print(
                f'Server host: {Fore.GREEN}{host_entry.address}{Style.RESET_ALL}')
            print(splitter())
