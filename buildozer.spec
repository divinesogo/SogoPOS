[app]
title = Sogo POS
package.name = sogopos
package.domain = com.sogo.pos
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Main entry point
entrypoint = main.py

# Supported Python packages
requirements = python3,kivy==2.3.0,kivymd,requests

# Optional icons
icon.filename = %(source.dir)s/icon.png

# Presplash (optional)
presplash.filename = %(source.dir)s/presplash.png

# Application category
category = Business
description = Simple Point of Sale application built with Python and KivyMD.

# Screen configurations
android.minapi = 21
android.api = 34
android.archs = arm64-v8a,armeabi-v7a
android.ndk = 25b
android.sdk = 34

# Use modern SDK tools
android.sdk_path = ~/.buildozer/android/platform/android-sdk
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b
android.accept_sdk_license = True

# Optional signing configuration
# (leave blank for debug build)
android.debug = True

# Window settings
log_level = 2
