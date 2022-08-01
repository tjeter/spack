from __future__ import print_function

import inspect
import textwrap

from six.moves import zip_longest
from six import string_types
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

description = "get common vulnerabilities/exposures (CVEs) for a package and its dependencies; and stores this info in a json file"
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
        ('--update', cve_refresh.__doc__),
        ('--dep', cve_deps.__doc__),
        ('-d', cve_deps.__doc__),
        ('-u', cve_refresh.__doc__)
    ]
    for opt, help_comment in options:
        subparser.add_argument(opt, action='store_true', help=help_comment)

    arguments.add_common_arguments(subparser, ['package'])

def section_title(s):
    return header_color + s + plain_format


def packagize(pkg):
    if isinstance(pkg, string_types):
        return spack.repo.path.get_pkg_class(pkg)
    else:
        return pkg

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
                json_list.append(cve_dict)
        # and eachCVE.score[2] == "CRITICAL":

    with open(cve_json_path, 'w') as json_file:
        json.dump(json_list, json_file)
    '''if eachCVE.score[0] == 'V3': #and len(eachCVE.id) == len(set(eachCVE.id)):
            print(eachCVE.id, str(eachCVE.score[1]), eachCVE.url)
        else:
            pass
    '''
def cve_deps(pkg):
    color.cprint('')
    deps = sorted(pkg.dependencies_of_type('build'))
    for d in deps:
        #pkgconfig does not exist (???) and is called pkgconf again (???)
        if d == "pkgconfig":
            d = 'pkgconf'
        
        dep = packagize(d)
        repo = spack.repo.path
        path_to_pkg = repo.filename_for_package_name(dep.name)
        path_parent = os.path.dirname(path_to_pkg)
        cve_json_path = path_parent+"/cve.json"
        file_exists = exists(path_parent+"/cve.json")
        json_list = []

        for i in dep.cpe:
            r = (nvdlib.searchCVE(cpeName=dep.cpe[i], key=api_key))
        # by default includes V2 scores that don't apply to specified version
            for eachCVE in r:
                if eachCVE.score[0] == 'V3':
                    cve_dict = {str(i):{"cve":None, "score":None, "url":None}}
                    cve_dict[i]["cve"] = eachCVE.id
                    cve_dict[i]["score"] = eachCVE.score[1]
                    cve_dict[i]["url"] = eachCVE.url
                    json_list.append(cve_dict)
            # and eachCVE.score[2] == "CRITICAL":
        with open(cve_json_path, 'w') as json_file:
            json.dump(json_list, json_file)

def read_json(pkg):
    repo = spack.repo.path
    path_to_pkg = repo.filename_for_package_name(pkg.name)
    path_parent = os.path.dirname(path_to_pkg)
    file_exists = exists(path_parent+"/cve.json")
    cve_json_path = path_parent+"/cve.json"
    deps = sorted(pkg.dependencies_of_type('build'))
    title_bool = False

    if file_exists:
        title_pkg_bool = False
        if title_pkg_bool == False:
            color.cprint('')
            color.cprint(section_title('Package '))
            title_pkg_bool = True
        with open(cve_json_path, 'r') as json_file:
            cve_loader = json.load(json_file)
            for cves in cve_loader:
                for version, data in cves.items():
                   print(pkg.name, "|", version, "|", data["cve"], "|",  data["score"], "|",  data["url"])
                   print("-"*90)
    else:
        print("file could not be found check permissions and if", cve_json_path, "exists for ", pkg.name)

    if title_bool == False:
        color.cprint('')
        color.cprint(section_title('Dependencies '))
        title_bool = True
    for d in deps:
        #pkgconfig does not exist (???) and is called pkgconf again (???)
        if d == "pkgconfig":
            d = 'pkgconf'
    
        dep = packagize(d)
        dep_repo = spack.repo.path
        dep_path_to_pkg = repo.filename_for_package_name(dep.name)
        dep_path_parent = os.path.dirname(dep_path_to_pkg)
        dep_cve_json_path = dep_path_parent+"/cve.json"
        dep_file_exists = exists(dep_path_parent+"/cve.json")
        
        if dep_file_exists:
            with open(dep_cve_json_path, 'r') as json_file:
                cve_loader = json.load(json_file)
                for cves in cve_loader:
                    for version, data in cves.items():
                       print(dep.name, "|", version, "|", data["cve"], "|",  data["score"], "|",  data["url"])
                       print("-"*90)
        else:
            print("file could not be found check permissions and if", dep_cve_json_path, "exists for ", dep.name)



def cve(parser, args):
    pkg = spack.repo.get(args.package)
    repo = spack.repo.path
    path_to_pkg = repo.filename_for_package_name(pkg.name)
    path_parent = os.path.dirname(path_to_pkg)
    file_exists = exists(path_parent+"/cve.json")
    cve_json_path = path_parent+"/cve.json"

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
        (args.all or args.update, cve_refresh),
        (args.all or args.dep, cve_deps)

    ]
    for print_it, func in sections:
        if print_it:
            func(pkg)

    if file_exists:
        read_json(pkg)
    else:
        cve_refresh(pkg)
        cve_deps(pkg)
        read_json(pkg)
