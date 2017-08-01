#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import glob
import json
import atexit


def strip_static_lib(lib_file, is_arm):
    ndk_path = os.environ.get('ANDROID_NDK_ROOT')
    print('ndk_path=', ndk_path)
    if ndk_path:
        strip_path = "arm-linux-androideabi-4.8/prebuilt/darwin-x86_64/arm-linux-androideabi/bin/strip"
        if not os.path.exists(strip_path):
            strip_path = "arm-linux-androideabi-4.9/prebuilt/darwin-x86_64/arm-linux-androideabi/bin/strip"

        if 'arm64-v8a' in lib_file:
            strip_path = "aarch64-linux-android-4.9/prebuilt/darwin-x86_64/aarch64-linux-android/bin/strip"
        if not is_arm:
            strip_path = "x86-4.8/prebuilt/darwin-x86_64/i686-linux-android/bin/strip"
            if not os.path.exists(strip_path):
                strip_path = "x86-4.9/prebuilt/darwin-x86_64/i686-linux-android/bin/strip"
        strip_path = ndk_path + "/toolchains/" + strip_path
        print('strip_path=', strip_path, os.path.exists(strip_path))

strip_static_lib('/tmp/bb', True)
