# iDroid Launcher — 0.1.0

First native Android launcher prototype for the iDroid ROM.

## Included

- HOME/DEFAULT launcher activity.
- Installed-app discovery using launcher intents.
- Four-column app grid with system-provided app icons.
- Bottom dock containing up to four launchable apps.
- Hybrid visual direction: iOS-like spacing and dock with restrained translucent material.
- Native Android Views; no third-party dependencies.

## Build

Open the repository in Android Studio with Android Gradle Plugin 8.7.3 and Android SDK Platform 35 installed, then run the `:launcher:assembleDebug` task.

This module has not yet been built or tested on a physical SM-A207F/DS. The app is an early launcher prototype, not a replacement for Android SystemUI or Keyguard.


## Current limitations

- This is a first UI prototype, not a polished release.
- App discovery currently displays one launchable entry per package.
- The dock currently uses the first four apps alphabetically; configurable pinned apps and drag-and-drop are future work.
- The clock is rendered at activity creation and does not yet update every minute.
- Build and runtime validation are still pending.


## Icon presentation rule

The launcher does not bundle or download an icon pack. It loads each installed app's own icon from Android PackageManager and places it in a consistent rounded-square translucent tile. This changes the container shape, not the app's logo artwork.
