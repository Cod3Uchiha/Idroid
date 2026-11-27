# Launcher foundation: Lawnchair

## Pinned upstream source

iDroid uses the official Lawnchair 14 source as a Git submodule:

- Upstream: https://github.com/LawnchairLauncher/lawnchair
- Submodule: `upstream/lawnchair`
- Upstream branch: `14-beta`
- Pinned commit: `6f4a81266c8d86361496a035d3080c2ebcb4886a`
- Build variant: `LawnWithQuickstepGithubDebug`

The upstream source is a real Git submodule (gitlink), not a copied prototype or a documentation-only declaration. The unmodified upstream variant has passed GitHub Actions once. The iDroid overlay build is a separate verification milestone and must pass before an iDroid APK is called ready.

## Visual target

The reference images and [IOS26_DESIGN_SPEC.md](IOS26_DESIGN_SPEC.md) define the visual acceptance target. The redesign covers the home pages, app icons, dock, folders, widgets, app library/search, settings, gestures, context menus, wallpaper treatment, light/dark appearance and restrained animations.

iDroid is an Android launcher inspired by iOS design; it is not Apple iOS and does not include Apple's proprietary system services or assets.

## Exactly two launcher modes

Both modes use the same Lawnchair engine, workspace database, widget host and launcher settings. Switching modes must not create a second launcher activity or discard workspace placements.

1. **iDroid Home** — default mode. iOS 26-inspired home layout, wallpaper-led pages, floating dock and original app artwork clipped to a consistent squircle. No duplicate clock/date header.
2. **One UI Mode** — Samsung One UI-inspired home layout with an app drawer and rounded-square icon treatment.

There is no Lawnchair Classic option in the iDroid mode selector.

## Implementation rules

- Preserve original installed app artwork. Apply a mask only; do not add a white backing tile, border, external icon pack or artificial inset.
- Use lightweight/translucent surfaces with opaque fallbacks; avoid expensive blur and animation on the Galaxy A20s.
- Keep Android's status bar as the only clock. Do not add a second clock.
- Preserve upstream licensing and notices. Lawnchair source is GPL-3.0; retain its license and attribution when redistributing a modified source build.
- System lockscreen, notification shade, Quick Settings, system recents and status-bar behavior require SystemUI/framework integration. They are not delivered by a launcher APK alone.

## Device target

- Samsung Galaxy A20s, SM-A207F/DS.
- Planned ROM base: Android 14.
- Snapdragon 450 / Adreno 506.
- Test Android 14 compatibility on the target device; selecting Lawnchair 14 does not by itself prove ROM or device compatibility.

## Build and overlay workflow

1. Actions checks out the pinned Lawnchair submodule recursively.
2. `scripts/apply-idroid-overlay.py` applies a deterministic, fail-closed overlay to the upstream source.
3. The overlay adds the two-mode selector and reversible presets, iDroid branding/application ID, squircle masking of the original app artwork, removes the duplicate home information panel, uses an icon-only dock with a lightweight translucent capsule in iDroid Home, and softens folder surfaces. One UI Mode keeps the standard Lawnchair search bar and opaque folder treatment.
4. Actions builds `assembleLawnWithQuickstepGithubDebug` and uploads the resulting APK.

The overlay script is deterministic, safe to re-run and checks its expected source anchors. Dock material uses a static alpha surface with an opaque fallback; it does not add a continuously blurred layer. If upstream changes those anchors, the build fails rather than silently producing an unmodified APK.

## Status

- [x] Official Lawnchair 14 submodule pinned in the iDroid repository.
- [x] Unmodified Lawnchair 14 Quickstep debug build passed in CI.
- [x] First iDroid overlay implementation added to the repository branch.
- [ ] iDroid overlay build and APK artifact verification.
- [ ] Verify the two visual presets and workspace preservation on-device.
- [ ] Complete reference-image visual redesign across all launcher surfaces.
- [ ] Device testing on SM-A207F/DS, including contrast, gestures, widgets and dock layout.
- [ ] Android 14 ROM integration and system UI work.

The old standalone Kotlin prototype is not the intended product launcher. It must not be shipped alongside the Lawnchair-derived launcher.
