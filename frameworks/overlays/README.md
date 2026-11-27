# Framework overlays

This directory will contain Android Runtime Resource Overlay (RRO) packages for the iDroid visual system.

Planned overlay groups:

- `base/`: semantic colors, dimensions and typography.
- `systemui/`: status bar, quick settings, notification and keyguard resources.
- `settings/`: Settings application resources.
- `navigation/`: navigation bar and gesture-related resources where supported.

Overlay resources must match the exact Android 14 base revision. Avoid overlays that change unrelated framework behavior. Every overlay should document its target package, resource names, activation mechanism and fallback behavior.

No overlay package is implemented yet.
