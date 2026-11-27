# Build and packaging

A reproducible ROM build requires a Linux build host, a pinned Android source manifest, device configuration, kernel source, matching vendor dependencies and sufficient disk space/RAM.

## Current state

There is no build script yet because the repository does not contain a validated Android source tree or A20s device configuration. A script that merely downloads an arbitrary GSI and renames it would not produce a genuine iDroid ROM.

## Planned build pipeline

1. Sync the pinned Android 14 manifest.
2. Apply iDroid framework and SystemUI patches.
3. Build iDroid applications and overlays.
4. Build or integrate the exact A20s kernel and device target.
5. Assemble images using the selected base's supported packaging method.
6. Run static checks and verify image metadata.
7. Generate SHA-256 checksums and release notes.

Never publish a flashable artifact until it has been tested on the exact target and a verified stock restore path is available.
