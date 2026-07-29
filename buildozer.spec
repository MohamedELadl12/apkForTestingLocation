[app]

# (str) Title of your application
title = Location Tracker

# (str) Package name
package.name = locationtracker

# (str) Package domain (needed for android packaging)
package.domain = org.eladl

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of exclusions using pattern matching
#source.exclude_exts = spec

# (list) List of directory to exclude
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using carriage return
#source.exclude_patterns = license, images//*jpg

# (str) Application version (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3, kivy, plyer, android

# (str) Custom source folders for requirements
# Defers to recipe, see https://github.com/kivy/python-for-android/blob/master/doc/source/recipes.rst
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientations
# Valid values are: landscape, portrait, all
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT_TO_PY

#
# OSX Specific
#

# author = © Copyright Info

#
# Android specific
#

# (bool) Indicate if the XML export should be authorised
#android.xml_export = False

# (list) Android permissions to request
android.permissions = ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION

# (list) features required by the app
#android.features = android.hardware.location.gps

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 33

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess bandwidth usage or offline builds
#android.skip_update = False

# (bool) If True, then automatically accept SDK licenses
# This is required for cleaner automatic builds
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the image (will match all if empty)
#android.image_whitelist =

# (str) Bootstrap to use for android builds
# android.bootstrap = sdl2

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jar file that already exist in the tree.
#android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project (for custom java code)
#android.add_src =

# (list) Android AAR archives to add (uses android.add_aar)
#android.add_aars =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Required for modern SDKs and dependencies.
android.enable_androidx = True

# (list) Packaging options to add (uses packagingOptions in build.gradle)
#android.packaging_options =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
#android.ouya.category = APP

# (str) Filename of OUYA Console icon. Must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android directories to be added to the project
#android.add_assets =

# (list) Android XML files to add to the project (will be copied to res/values)
#android.add_resources =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D Kivy:D

# (str) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android-v7/libgnustl_shared.so

# (bool) Copy library instead of linking (for OS X)
#android.copy_libs = 1

# (list) The Android architectures to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a, arm64-v8a

# (int) overrides automatic versioning (must be numeric)
#android.numeric_version = 1

# (bool) grant_all_permissions parameter passed to adb install
#android.adb_install_self_grant = True

# (str) Path to a custom whitelist file
#android.whitelist =

# (str) Path to a custom blacklist file
#android.blacklist =

# (list) List of extra java classes to add to the compile classpath
#android.add_compile_classpath =

#
# Python for android (p4a) specific
#

# (str) python-for-android branch to use, default is master
#p4a.branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned)
#p4a.source_dir =

# (str) The directory where buildozer will store downloaded packages and builds
#build_dir = ./.buildozer

# (str) The directory where buildozer will store the outputs (.apk, .aab, etc.)
#bin_dir = ./bin

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
