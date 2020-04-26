#!/usr/bin/python3

from xml.dom import minidom
import argparse
import os
import initializer
import host
import sys


class Amp:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Simple utility which helps to manage Cisco AnyConnect profiles', usage='''amp <command> [<args>]
Available commands:
   init     Initialize AnyConnect profile if does not exist
   host     List available hosts
        ''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def init(self):
        parser = argparse.ArgumentParser(
            description='Initialize AnyConnect profile if does not exist'
        )

        parser.add_argument('init')
        parser.add_argument('-r', '--rewrite', action='store_true')

        args = parser.parse_args(sys.argv[1:])
        initializer.init(args.rewrite)

    def host(self):
        parser = argparse.ArgumentParser(
            description='Manage hosts in your profile'
        )

        parser.add_argument('host')
        parser.add_argument('host_cmd', nargs='?')

        args = parser.parse_args()
        if args.host_cmd:
            if args.host_cmd == 'ls':
                host.list()
        else:
            # by default we just list available servers
            host.list()

    def schema(self):
        with open('AnyConnectProfile.xsd', 'r') as inp:
            print(inp.read())


def main():
    Amp()


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
