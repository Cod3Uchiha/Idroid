# Roadmap

## Phase 0 — Repository foundation
- [x] Define project scope and target device.
- [x] Establish modular repository layout.
- [x] Document architecture and safety constraints.
- [ ] Add CI checks for formatting and repository structure.

## Phase 1 — Device bring-up
- [ ] Record exact firmware build, bootloader revision and CSC.
- [ ] Identify partition layout and verified recovery/restore route.
- [ ] Select Android 14 base and pin exact source/GSI build.
- [ ] Gather device tree, kernel source and vendor dependency references.
- [ ] Boot the unmodified base and record logs.
- [ ] Test display, touch, audio, Wi-Fi, Bluetooth, camera, sensors, GPS, telephony and fingerprint.

**Exit criteria:** repeatable boot and documented hardware status on SM-A207F/DS.

## Phase 2 — Visual foundation
- [ ] Define light/dark design tokens.
- [ ] Create original wallpaper and icon assets.
- [ ] Implement typography, shape, spacing and motion guidelines.
- [ ] Add translucent surfaces with low-cost fallbacks.
- [ ] Validate contrast and accessibility.

## Phase 3 — User-facing components
- [ ] iDroid Launcher.
- [ ] Notification styling.
- [ ] Control Centre / Quick Settings integration.
- [ ] Lock screen / Keyguard styling.
- [ ] Dynamic Island-inspired notification surface.
- [ ] Settings integration and companion app.
- [ ] Volume and brightness surfaces.

## Phase 4 — System integration
- [ ] Apply framework resource overlays.
- [ ] Integrate SystemUI changes against pinned source revision.
- [ ] Resolve signature, privileged permission and SELinux requirements.
- [ ] Add build-time validation and reproducible packaging.

## Phase 5 — Release qualification
- [ ] Clean build from documented environment.
- [ ] Verify package signatures and checksums.
- [ ] Test upgrade, clean install and recovery paths.
- [ ] Publish known issues and device compatibility matrix.
- [ ] Release only after successful device testing.

## Current status

Only the documentation and repository scaffold are being established. No bootable image or flashable package exists yet.
