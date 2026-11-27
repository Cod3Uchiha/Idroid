# Launcher foundation: Lawnchair

## Upstream

- Project: https://github.com/LawnchairLauncher/lawnchair
- Selected compatibility baseline: `v12.1.0-alpha.4`
- Upstream commit: `b7ad08c775ceee31c9f0715a9f71acb661b4380f`
- License: verify and preserve upstream license/notices when importing source.

## Why this baseline

The current Lawnchair development branch is based on Android 16 Launcher3. iDroid's first target device is the Galaxy A20s, currently running Android 11. The Android-16-based branch is therefore not the right starting point for the first device build. The selected 12.1 alpha tag is an older code line and must be built and tested against the A20s target before it is treated as supported.

## Integration direction

Lawnchair becomes the launcher engine; iDroid supplies the visual theme and device-specific defaults. Do not maintain a second, competing home-screen engine.

Preserve Lawnchair's launcher capabilities where compatible:
- Home-screen pages, folders, drag-and-drop and widgets.
- App drawer, app search and app organization.
- Dock layout and customization.
- Gestures and launcher preferences.
- Backup and restore where supported by the selected version.

iDroid presentation layer:
- No duplicate clock/date widget by default. The Android status bar remains the source of the system clock.
- iOS-inspired grid spacing, rounded-square icon masks and dock surface.
- Keep every installed app's original icon artwork; do not bundle an icon pack or replace icons with Apple artwork.
- Lightweight blur/translucency with an opaque fallback for the A20s.
- User-selectable layout modes: **iDroid Home** (iOS-inspired pages and dock), **One UI-style** (home + app drawer), and **Lawnchair Classic** (standard Lawnchair layout). These are presets over the same launcher engine, not separate launchers.

## Import and build checklist

1. Import the pinned upstream source while preserving its license and notices.
2. Keep the upstream package/module structure intact as much as practical; isolate iDroid changes in theme resources, overlays and small patches.
3. Replace the upstream application identity with the iDroid package identity without changing unrelated upstream behavior.
4. Port only the required launcher changes; avoid cherry-picking Android-16-only code into the Android-11 device build.
5. Add a reproducible build job for the imported source and verify the debug APK.
6. Test app discovery, widgets, folders, gestures, rotation, backup/restore and default-home behavior on the SM-A207F/DS.
7. Keep this launcher app separate from the eventual Android 14 ROM/SystemUI work. A launcher APK is not a ROM.

## Current implementation status

The repository's existing Kotlin launcher is still a small prototype, not imported Lawnchair source. The duplicate date/time header has been removed from that prototype. The Lawnchair source import and the three layout presets are the next integration milestone; do not describe them as implemented until they are present in a tested build.
