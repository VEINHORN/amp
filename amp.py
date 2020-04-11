#!/usr/bin/python3

from xml.dom import minidom
import argparse
import os
import initializer
import host


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('command')
    parser.add_argument('second_command', nargs='?')

    parser.add_argument('-r', '--rewrite', action='store_true')

    args = parser.parse_args()

    if args.command:
        if args.command == 'init':
            initializer.init(args.rewrite)
        elif args.command == 'host':
            if args.second_command:
                if args.second_command == 'ls':
                    host.list()
            else:
                # by default we just list available servers
                host.list()


def parse_profiles():
    with open('/opt/cisco/anyconnect/profile/AnyConnectProfile.xml', 'r') as f:
        DOMTree = minidom.parse(f)
        profile = DOMTree.documentElement

        server_list = profile.getElementsByTagName('ServerList')

        get_hosts(server_list[0])
        # print(f"hosts in profile = {len(server_list)}")

        # print(server_list[0].tagName)
        # print(server_list[0].tagName)
        # print(len(host_entries))


def get_hosts(server_list_elm):
    for host_entry in server_list_elm.getElementsByTagName('HostEntry'):
        print(host_entry.toxml() + "\n")

        host_name = host_entry.getElementsByTagName(
            'HostName')[0].firstChild.nodeValue
        host_address = host_entry.getElementsByTagName(
            'HostAddress')[0].firstChild.nodeValue
        print(f"name, address = {host_name}, {host_address}")


if __name__ == '__main__':
    main()
