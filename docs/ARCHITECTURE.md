# iDroid architecture

## Product direction

iDroid is a custom Android distribution with an interface inspired by two generations of Apple's design language:

- **iOS 18 influence:** clear hierarchy, familiar home-screen grid, compact controls, readable notifications and restrained translucency.
- **iOS 26 influence:** selective Liquid Glass-inspired surfaces, layered blur, specular highlights and depth.

The design must remain legible, performant and accessible on the Galaxy A20s hardware. Glass effects are progressive enhancements, not a requirement for every surface.

## System architecture

```text
Android 14 base (AOSP-compatible foundation)
  |
  +-- Device adaptation
  |     +-- Samsung A20s device configuration
  |     +-- matching kernel / boot image
  |     +-- vendor blobs and HAL compatibility
  |
  +-- Framework resource overlays
  |     +-- colors, dimensions, typography
  |     +-- navigation and system resource styling
  |
  +-- SystemUI integration
  |     +-- status bar and quick settings
  |     +-- notification shade
  |     +-- keyguard / lock screen
  |     +-- volume and brightness surfaces
  |
  +-- iDroid applications
  |     +-- launcher
  |     +-- control centre extensions where supported
  |     +-- settings companion
  |     +-- Dynamic Island-style notification surface
  |
  +-- Theme assets
        +-- icons, wallpapers, sounds and design tokens
```

## Integration strategy

1. Start from a known Android 14 source or a verified Android 14 GSI configuration.
2. Establish an unmodified booting baseline on the exact A20s variant.
3. Record hardware functionality before changing SystemUI.
4. Add visual overlays in small, reversible groups.
5. Build and test privileged applications separately.
6. Integrate framework/SystemUI patches only against the exact selected Android source revision.
7. Produce signed, reproducible artifacts only after device bring-up and recovery procedures are verified.

A launcher or ordinary APK cannot replace Android SystemUI, Keyguard, framework resources or the boot process. Full integration requires source-level changes and a compatible build environment.

## Design system

Use shared design tokens rather than hard-coded values in individual apps:

- Semantic surfaces: base, elevated, translucent and emphasized.
- Semantic text: primary, secondary and disabled.
- Accent and status colors with light/dark variants.
- Corner radii and spacing scale.
- Motion durations with reduced-motion alternatives.
- Blur fallback for devices or contexts where real-time blur is too expensive.

Do not use Apple trademarks, copied proprietary assets, or claims that this is genuine iOS.

## Performance principles

The A20s is an entry-level device. Avoid always-on expensive blur, large background services, excessive animation layers and unnecessary accessibility overlays. Prefer hardware-accelerated rendering where available, with opaque fallbacks and user-adjustable effects.
