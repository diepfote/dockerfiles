#!/usr/bin/env python3

import os
import sys
import subprocess
from jinja2 import Environment, FileSystemLoader


image_name=sys.argv[1]
image_is_cached=True if sys.argv[2] == 'cached' else False


# Load jinja template file
TEMPLATE_FILE = 'Dockerfile.template'
template_loader = FileSystemLoader(searchpath='.')
template_env = Environment(loader=template_loader)
template = template_env.get_template(TEMPLATE_FILE)


arch_pkgs = []
filename_pkg_explicit_internal = os.environ['HOME'] \
    + '/Documents/misc/arch/packages_explicit_internal'
with open(filename_pkg_explicit_internal) as f:
    content = f.read()
    arch_pkgs.extend(content.split('\n'))
    del content

filename_pkg_explicit_external = os.environ['HOME'] \
    + '/Documents/misc/arch/packages_explicit_external'
with open(filename_pkg_explicit_external) as f:
    content = f.read()
    arch_pkgs.extend(content.split('\n'))
    del content

filename_exclusions = os.environ['HOME'] \
    + f'/Documents/misc/arch/{image_name}-docker-image-package-exclusions.txt'
with open(filename_exclusions) as f:
    content = f.read()
    exclusions = content.split('\n')[:-1]
    del content
# print(f'{exclusions=}')


def item_included(item, exclusions):
    for exclusion in exclusions:
        if item.startswith(exclusion):
            return False
    return True


tmp_split = []
# print(f'{arch_pkgs=}')
for item in arch_pkgs:
    if item_included(item, exclusions) and item:
        tmp_split.append(item)
        # print(f'DEBUG included: {item}')
    # else:
        # print(f'DEBUG excluded: {item}')
# print(f'{tmp_split=}')
arch_pkgs = tmp_split
del tmp_split

image = 'docker.io/archlinux:base'
yay_install="""
# ----------
# yay cannot be run as root!
#
# taken from: https://github.com/justin8/docker-makepkg/blob/master/Dockerfile
#
ADD sudoers /etc/sudoers
RUN useradd -m -d /build build-user || true
WORKDIR /build

RUN sudo -u build-user git clone https://aur.archlinux.org/yay.git && cd yay && sudo -u build-user makepkg -sri --noconfirm && cd - && rm -rf yay
# ----------
#
"""

if image_is_cached:
    yay_install = ''
    image = f'localhost/{image_name}'

with open('Dockerfile', 'w') as f:
    f.write(template.render(image=image,
                            arch_pkgs=' '.join(arch_pkgs),
                            yay_install=yay_install ))

