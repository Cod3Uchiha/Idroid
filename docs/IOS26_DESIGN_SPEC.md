# iDroid visual system — iOS 26-inspired launcher

This document defines the visual and interaction target for the Lawnchair-derived iDroid launcher. It is an original Android implementation inspired by the broad visual language of iOS 26; it must not copy Apple's proprietary assets or imply that Apple services are present.

## Design direction

Apply one coherent design system across every launcher surface, not just the home screen. Prioritize recognizable iOS-like proportions, typography, spacing, icon geometry, layered translucent materials, soft depth, and restrained motion. Keep the UI responsive and lightweight enough for the Galaxy A20s (Snapdragon 450 / Adreno 506).

## Surfaces in scope

| Surface | iDroid treatment |
| --- | --- |
| Home pages | Clean grid, generous spacing, wallpaper-led layout, no duplicate clock/date header |
| App icons | Mask each app's original artwork to a consistent squircle; no white backing, border, external icon pack, or added inset |
| Dock | Floating translucent rounded container, consistent icon sizing and spacing |
| App drawer | Searchable, categorized/app-list presentation with matching typography and surfaces |
| Folders | Rounded translucent folder panel, compact icon previews, consistent open/close motion |
| Search | Full-screen or overlay search with matching field, results, keyboard and empty states |
| Widgets | Rounded widget frames and consistent spacing; do not distort app-provided widget content |
| Launcher settings | iDroid-branded settings with live previews and clear controls |
| Gestures | Home, swipe-up/app drawer, folder, and supported Lawnchair gestures with clear feedback |
| Context menus | Rounded floating menus, readable hierarchy, accessible touch targets |
| Wallpaper and layout | Edge-to-edge composition, adaptive contrast, safe-area/inset handling |
| Animations | Short, smooth, interruptible transitions; reduced-motion option |
| Theming | Light/dark modes, wallpaper-aware accent colors, translucent and opaque material variants |

## Design tokens

- Icon mask: one consistent rounded-square/squircle mask, applied at render time to the original app drawable.
- Icon treatment: preserve original colors and artwork; never add a white tile, outline, glow, or artificial padding.
- Surfaces: layered translucent material where supported, with a solid-color fallback.
- Corners: use a small, consistent radius scale for cards, search fields, folders, and dock.
- Typography: use Android/system sans-serif with iOS-inspired hierarchy and restrained weights; do not bundle Apple's proprietary font.
- Motion: prioritize spring-like but restrained transitions; avoid expensive continuous blur or parallax on low-end hardware.
- Accessibility: preserve labels, content descriptions, contrast, font scaling, keyboard navigation and large touch targets.

## Launcher modes

All modes must use the same Lawnchair engine and shared preferences; switching modes must not create separate launcher activities or lose home-screen data.

1. **iDroid Home** — iOS-inspired pages, floating dock, no mandatory app drawer button.
2. **One UI-style** — home screen plus app drawer, with configurable swipe direction and grid.
3. **Lawnchair Classic** — familiar Lawnchair layout and controls.

Mode changes must be reversible and must preserve app placements where possible.

## Implementation rules

- Keep upstream Lawnchair history, license, NOTICE and attribution intact.
- Implement appearance through focused resource, drawable, layout and Kotlin patches; avoid a wholesale rewrite of Launcher3.
- Prefer platform APIs and existing Lawnchair extension points.
- Do not fake system-wide iOS features in a launcher. Lock screen, notification shade, Control Centre, recents and status bar require separate SystemUI/framework integration.
- Do not claim a feature is complete until it exists in source, builds, and is tested.
- Build the unmodified upstream source before applying large patches; record the exact source commit and build variant.
- Validate Android 11 launcher compatibility separately from the intended Android 14 ROM target.
