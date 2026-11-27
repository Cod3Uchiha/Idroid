# Samsung Galaxy A20s device target

- Target model: **SM-A207F/DS**
- Device family/codename: **a20s**
- SoC: Qualcomm Snapdragon 450 (verify against the device's reported hardware)
- Target Android base: Android 14

## Required device-specific evidence

Before creating or importing a device tree, collect and verify:

1. Full firmware build number and CSC from Settings → About phone → Software information.
2. Bootloader revision and OEM unlock state from Download Mode.
3. Partition map and dynamic-partition status.
4. Current boot, recovery, vbmeta and vendor image provenance.
5. Kernel source/revision and defconfig for the exact model.
6. Vendor blobs and HAL versions from matching stock firmware.
7. Existing community device tree and recovery status, with commit hashes.

## Bring-up rules

- Do not assume all SM-A207 regional variants share identical partition layouts or firmware.
- Do not flash a generic GSI or modified boot image until the exact install method and rollback path are confirmed.
- Preserve a complete matching stock-firmware recovery package.
- Validate verified-boot and vbmeta requirements for the chosen base.
- Keep proprietary vendor binaries out of this repository unless their redistribution terms explicitly permit it; document extraction instead.
- Capture boot logs and hardware test results for every baseline.

## Planned configuration files

The following should only be added when backed by a real, tested source tree:

- Android product makefiles.
- Board configuration.
- Device manifest.
- Kernel configuration and source reference.
- Proprietary-files manifest.
- SELinux policy.
- Init and fstab configuration.

This directory is currently documentation only; it is not a usable device tree.
