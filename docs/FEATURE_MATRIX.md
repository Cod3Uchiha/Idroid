# iDroid feature matrix

This is the intended feature scope, not a claim that every feature is already implemented. Features are delivered in stages and depend on Android 14 platform integration and hardware support.

## Home and navigation
- [x] Basic home launcher and installed-app discovery (prototype).
- [x] Uniform rounded-square icon containers while preserving each installed app's original icon.
- [ ] Pinned, user-configurable dock.
- [ ] Drag-and-drop placement, folders and page management.
- [ ] App library, search and widget host.
- [ ] Home-screen editing mode and icon badge support.

## Lock screen and always-on display
- [ ] iOS-inspired clock/date layouts and wallpaper depth effects.
- [ ] Notification presentation and privacy controls.
- [ ] Shortcut customization.
- [ ] Always-on display only if supported by the panel, kernel and power-management stack.

## Control Centre and quick settings
- [ ] Custom panel layout and brightness/volume controls.
- [ ] Wi-Fi, mobile data, Bluetooth, airplane mode, flashlight, rotation and battery saver.
- [ ] Tile availability and behavior must use Android-supported APIs or privileged SystemUI integration.
- [ ] Secure settings and radio toggles must not be simulated by UI-only switches.

## Notifications and live activities
- [ ] Grouped notification cards, badges and quick actions.
- [ ] Media playback surface and lock-screen media controls.
- [ ] Dynamic Island-inspired visual for calls, timers, media and charging.
- [ ] Respect Android notification permission, listener and foreground-service rules.

## System experience
- [ ] Status bar and navigation styling.
- [ ] Volume and brightness overlays.
- [ ] Recent-apps styling and gesture navigation where supported.
- [ ] Light/dark appearance, wallpapers, sounds and original motion design.
- [ ] Liquid-glass-inspired translucent panels with a low-cost opaque fallback.

## Apps and utilities
- [ ] iDroid Settings companion.
- [ ] Calculator and gallery-style app surfaces.
- [ ] Device search and app search.
- [ ] Weather and calendar widgets using user-selected data sources.

## Platform-dependent / not genuine Apple services
AirDrop, iMessage, FaceTime, Apple Pay, iCloud, Apple Watch pairing, Apple's proprietary Continuity services and Apple's secure enclave integrations are not provided by this ROM. Where appropriate, Android-native or open interoperability alternatives may be explored; they must be described accurately and must not impersonate Apple's services.

## Device support
Every platform feature must be tested on the exact SM-A207F/DS hardware and Android 14 base. Features that require unsupported hardware, Samsung proprietary services or unavailable kernel interfaces will be marked unsupported rather than faked.
