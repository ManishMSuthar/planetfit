[app]

# (str) Title of your application
title = PlanetFit

# (str) Package name
package.name = planetfit

# (str) Package domain (can be anything, doesn't need to be real)
package.domain = org.manis

# (str) Source file to use as the main entry point for the app
entrypoint = planetfit.py

# (str) Icon of the application
icon.filename = logo.png

# (list) Permissions
android.permissions = INTERNET

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (list) Application requirements
requirements = python3,kivy

# (str) Presplash screen image (optional)
# presplash.filename = presplash.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Supported architectures (armeabi-v7a, arm64-v8a, x86, x86_64)
android.archs = armeabi-v7a, arm64-v8a

# (str) Android API to use
android.api = 31

# (str) Minimum API your APK will support
android.minapi = 21

# (bool) Copy libraries instead of making a libpymodules.so
copy_libs = 1

# (str) Build mode: release or debug
buildozer.build_mode = debug

# (str) Package format: apk, aab or all
android.package_format = apk

# (list) Include source files
source.include_exts = py,png,jpg,kv

# (list) Exclude unwanted files
source.exclude_exts = spec,pyc

# (str) Additional Java jars to add to the libs
# android.add_jars = path/to/some.jar

# (bool) Enable logcat during APK build
log_level = 2
