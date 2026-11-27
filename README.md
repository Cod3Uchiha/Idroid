# iDroid

An Android 14-based, iOS 18 + iOS 26-inspired custom ROM project, initially targeting the Samsung Galaxy A20s (SM-A207F/DS).

> **Status: early project scaffold.** This repository does not yet contain a bootable ROM, device tree, kernel, vendor blobs, recovery image, or flashable package.

## Project goals

- Build on a compatible Android 14 source/GSI foundation.
- Deliver a cohesive iOS-inspired experience while retaining Android app compatibility.
- Blend the familiar iOS 18 layout and interaction patterns with selected iOS 26 Liquid Glass visual treatments.
- Target the Galaxy A20s (codename: `a20s`, model family SM-A207F/DS).
- Keep device-specific code, system UI changes, overlays, and apps modular.

## Planned components

| Component | Planned implementation |
| --- | --- |
| Launcher | Kotlin app: home screen, folders, dock, app library |
| Control Centre | Android system component/privileged app, depending on base ROM |
| Notifications | SystemUI integration and notification styling |
| Lock screen | SystemUI/keyguard integration |
| Dynamic Island-style surface | Android overlay/service with lifecycle-aware notification integration |
| Settings | Settings overlays and optional iDroid settings app |
| Theme | Resource overlays, icons, typography, wallpapers, sounds |
| Device support | A20s device configuration, kernel and proprietary vendor dependencies |

## Repository layout

- `device/samsung/a20s/` — device bring-up notes and eventual device configuration.
- `vendor/samsung/a20s/` — proprietary dependency documentation; blobs are not checked in.
- `frameworks/overlays/` — resource overlays.
- `packages/apps/` — iDroid applications.
- `systemui/` — SystemUI integration notes and patches.
- `themes/` — visual assets and design tokens.
- `build/` — reproducible build scripts and documentation.
- `docs/` — architecture, milestones, compatibility and contribution notes.

## Important constraints

- This is **not Apple iOS** and does not include Apple's proprietary operating system or assets.
- The iOS-inspired interface will be implemented using Android components and original assets.
- A20s compatibility must be verified against the exact firmware, partition layout, bootloader revision, kernel and vendor implementation before flashing.
- A generic Android 14 GSI is not automatically a complete device-specific ROM.
- No installable ZIP or image is provided at this stage. Do not flash this repository.

## Development status

See [docs/ROADMAP.md](docs/ROADMAP.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), and [device/samsung/a20s/README.md](device/samsung/a20s/README.md).
