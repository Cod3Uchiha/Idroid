# Launcher foundation: Lawnchair

## Upstream source

iDroid now tracks the official Lawnchair repository as a Git submodule:

- Repository: https://github.com/LawnchairLauncher/lawnchair
- Submodule path: `upstream/lawnchair`
- Selected branch: `14-beta`
- Branch purpose: Lawnchair 14, based on Android 14 Launcher3.
- Upstream README: https://github.com/LawnchairLauncher/lawnchair/tree/14-beta

The current upstream default branch is `16-dev`, based on Android 16 Launcher3. It is not the selected base for this device target. iDroid's intended ROM base is Android 14, so Lawnchair's `14-beta` branch is the closer match and avoids starting from an Android 16 launcher tree.

## Complete iDroid visual redesign

The full launcher visual target is specified in [IOS26_DESIGN_SPEC.md](IOS26_DESIGN_SPEC.md). It covers the home screen, icons, dock, app drawer, folders, widgets, search, settings, gestures, context menus, wallpaper behavior, animation, accessibility and light/dark theming. This is a complete-surface redesign, not an icon-only theme.

## iDroid modifications on top of Lawnchair

Lawnchair is the launcher engine; iDroid will be a branded and customized derivative, not a separate launcher implementation. Keep upstream history and license notices. Preserve the Apache 2.0 license and all applicable attribution/NOTICE files when redistributing modified source or APKs.

iDroid presentation requirements:
- Remove the default date/clock header from the home layout; don't add a second clock when Android's status bar already shows time.
- iOS-inspired home-screen grid, spacing, dock and translucent surfaces.
- Force original installed app artwork into a consistent iOS-style rounded-square mask, with no white backing tile, border, or inset. Do not bundle an icon pack or replace app artwork.
- Use subtle blur/translucency with an opaque fallback for the Galaxy A20s.
- Provide selectable layout presets:
  - **iDroid Home** — iOS-inspired pages and dock.
  - **One UI-style** — home screen plus app drawer.
  - **Lawnchair Classic** — standard Lawnchair layout.
- Keep these presets in the same Lawnchair engine and settings model, not separate launcher activities.

## Device and compatibility target

- Device: Samsung Galaxy A20s, SM-A207F/DS.
- ROM target: Android 14.
- Hardware: Snapdragon 450 / Adreno 506; avoid expensive blur, overdraw and animation effects.
- Validate Android 14 behavior on the target device. Do not infer device compatibility merely because the source branch is based on Android 14.

## Integration sequence

1. Initialize the `upstream/lawnchair` submodule at the pinned `14-beta` branch commit.
2. Build the unmodified upstream branch first and record all dependencies, required submodules and build instructions.
3. Create an iDroid application identity and branding while retaining upstream notices and attribution.
4. Apply iDroid changes as a small, reviewable patch series over Lawnchair.
5. Replace the old standalone prototype module; do not ship two competing launchers.
6. Add CI that checks out submodules recursively and builds the Lawnchair-derived iDroid APK.
7. Test home pages, app drawer, search, folders, widgets, dock, gestures, icon masks, backup/restore and default-home behavior on SM-A207F/DS.

## Current status

- A `.gitmodules` declaration now identifies the official Lawnchair repository, intended submodule path `upstream/lawnchair`, and `14-beta` branch.
- The actual Git submodule gitlink/source checkout has not yet been committed; the source is not present in the repository tree yet.
- The earlier hand-written Kotlin launcher remains in the repository temporarily while migration is prepared.
- The old prototype APK is not the Lawnchair-based iDroid build.
- The submodule pointer alone does not mean the upstream source has already been compiled or that iDroid modifications have been integrated. Those are the next build milestones.
