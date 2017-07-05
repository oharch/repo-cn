#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['gcc63']

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'MOZ_REQUIRE_SIGNING' in line:
      continue
    print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
