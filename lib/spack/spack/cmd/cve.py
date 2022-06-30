from __future__ import print_function

import inspect
import textwrap

from six.moves import zip_longest

import llnl.util.tty as tty
import llnl.util.tty.color as color
from llnl.util.tty.colify import colify

import spack.cmd.common.arguments as arguments
import spack.fetch_strategy as fs
import spack.paths
import spack.repo
import spack.spec
from spack.package_base import has_test_method, preferred_version
import os
from os.path import exists
import json

import nvdlib
api_key = "92e8afaf-85fd-4a65-a862-3bedf09dcd87"

description = 'get common vulnerabilities/exposures (CVEs)'
section = 'basic'
level = 'short'

header_color = '@*b'
plain_format = '@.'

def setup_parser(subparser):
    subparser.add_argument(
        '-a', '--all', action='store_true', default=False,
        help="output all package information"
    )

    options = [
        ('--refresh'),
    ]
    for opt, help_comment in options:
        subparser.add_argument(opt, action='store_true', help=help_comment)

    arguments.add_common_arguments(subparser, ['package'])


def cve_refresh(pkg):
    color.cprint('')
    color.cprint(section_title('Known CVEs: '))
    
    repo = spack.repo.path
    path_to_pkg = repo.filename_for_package_name(pkg.name)
    path_parent = os.path.dirname(path_to_pkg)
    file_exists = exists(path_parent+"/cve.json")
    cve_json_path = path_parent+"/cve.json"
    
    cve_dict = {}
    json_list = []

    for i in pkg.cpe:
        r = (nvdlib.searchCVE(cpeName=pkg.cpe[i], key=api_key))
    # by default includes V2 scores that don't apply to specified version
        for eachCVE in r:
            if eachCVE.score[0] == 'V3':
                cve_dict = {str(i):{"cve":None, "score":None, "url":None}}
                cve_dict[i]["cve"] = eachCVE.id
                cve_dict[i]["score"] = eachCVE.score[1]
                cve_dict[i]["url"] = eachCVE.url
                print(i,"|", eachCVE.id, "|",  str(eachCVE.score[0]), "|", str(eachCVE.score[1]), "|", eachCVE.url)
                print("-"*80)
                json_list.append(cve_dict)
        # and eachCVE.score[2] == "CRITICAL":

    with open(cve_json_path, 'w') as json_file:
        json.dump(json_list, json_file)
    '''if eachCVE.score[0] == 'V3': #and len(eachCVE.id) == len(set(eachCVE.id)):
            print(eachCVE.id, str(eachCVE.score[1]), eachCVE.url)
        else:
            pass
    '''

def cve_to_json(pkg):
    repo = spack.repo.path
    path_to_pkg = repo.filename_for_package_name(pkg.name)
    path_parent = os.path.dirname(path_to_pkg)
    color.cprint('')
    color.cprint(section_title('JSON Data: '))
    file_exists = exists(path_parent+"/cve.json")
    cve_json_path = path_parent+"/cve.json"

    with open(cve_json_path, 'r') as json_file:
        cve_loader = json.load(json_file)
        for cves in cve_loader:
            for version, data in cves.items():
               print(version, "|", data["cve"], "|",  data["score"], "|",  data["url"])
               print("-"*80)

def cve(parser, args):
    pkg = spack.repo.get(args.package)
    repo = spack.repo.path
    path_to_pkg = repo.filename_for_package_name(pkg.name)
    path_parent = os.path.dirname(path_to_pkg)
    file_exists = exists(path_parent+"/cve.json")
    cve_json_path = path_parent+"/cve.json"

    if(args == '--refresh' or file_exists = False):
        cve_refresh(pkg)
    # Output core package information
    header = section_title(
        '{0}:   '
    ).format(pkg.build_system_class) + pkg.name
    color.cprint(header)

    color.cprint('')
    color.cprint(section_title('Description:'))
    if pkg.__doc__:
        color.cprint(color.cescape(pkg.format_doc(indent=4)))
    else:
        color.cprint("    None")

    color.cprint(section_title('Homepage: ') + pkg.homepage)

    # Now output optional information in expected order
    sections = [
        (args.all or args.refresh),
    ]
    for print_it, func in sections:
        if print_it:
            func(pkg)
    color.cprint('')
