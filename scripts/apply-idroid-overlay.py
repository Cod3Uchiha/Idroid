#!/usr/bin/env python3
"""Apply the maintained iDroid overlay to the pinned Lawnchair 14 checkout.

This is intentionally deterministic and fails closed if upstream moves the
expected integration points. Re-running it is safe.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = ROOT / "upstream" / "lawnchair"

def edit(relative, old, new, label):
    path = UPSTREAM / relative
    text = path.read_text(encoding="utf-8")
    if new in text:
        print(f"already applied: {label}")
        return
    if old not in text:
        raise SystemExit(f"Cannot apply {label}: upstream anchor changed in {relative}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print(f"applied: {label}")

edit(
    "lawnchair/src/app/lawnchair/preferences2/PreferenceManager2.kt",
    '    val enableDotPagination = preference(\n',
    '''    // iDroid exposes exactly two presets. The same Lawnchair engine, database,
    // workspace and widget model are retained when switching between them.
    val idroidMode = preference(
        key = stringPreferencesKey("idroid_mode"),
        defaultValue = "idroid_home",
        parse = { if (it == "one_ui") "one_ui" else "idroid_home" },
        save = { it },
        onSet = { mode ->
            iconShape.setBlocking(
                if (mode == "one_ui") IconShape.RoundedSquare else IconShape.Squircle,
            )
            enableSmartspace.setBlocking(mode == "one_ui")
            reloadHelper.restart()
        },
    )

    val enableDotPagination = preference(
''',
    "two-mode preference and mode preset behavior",
)

edit(
    "lawnchair/src/app/lawnchair/ui/preferences/destinations/GeneralPreferences.kt",
    '    val iconShapeAdapter = prefs2.iconShape.getAdapter()\n',
    '    val iconShapeAdapter = prefs2.iconShape.getAdapter()\n    val idroidModeAdapter = prefs2.idroidMode.getAdapter()\n',
    "mode preference adapter",
)

edit(
    "lawnchair/src/app/lawnchair/ui/preferences/destinations/GeneralPreferences.kt",
    '''    ) {
        PreferenceGroup {
            SwitchPreference(
                adapter = prefs.allowRotation.getAdapter(),
''',
    '''    ) {
        PreferenceGroup(heading = stringResource(R.string.idroid_mode_heading)) {
            val modeEntries = remember {
                listOf(
                    ListPreferenceEntry(
                        value = "idroid_home",
                        label = { stringResource(R.string.idroid_home_mode) },
                    ),
                    ListPreferenceEntry(
                        value = "one_ui",
                        label = { stringResource(R.string.one_ui_mode) },
                    ),
                ).toPersistentList()
            }
            ListPreference(
                adapter = idroidModeAdapter,
                entries = modeEntries,
                label = stringResource(R.string.idroid_interface_mode),
                description = stringResource(R.string.idroid_interface_mode_description),
            )
        }
        PreferenceGroup {
            SwitchPreference(
                adapter = prefs.allowRotation.getAdapter(),
''',
    "two-mode selector in launcher settings",
)

edit(
    "lawnchair/res/values/strings.xml",
    "</resources>",
    '''    <string name="idroid_mode_heading">iDroid interface</string>
    <string name="idroid_interface_mode">Launcher mode</string>
    <string name="idroid_interface_mode_description">Choose iDroid Home or One UI Mode. The preset changes the icon mask and home information panel.</string>
    <string name="idroid_home_mode">iDroid Home</string>
    <string name="one_ui_mode">One UI Mode</string>
</resources>''',
    "iDroid mode labels",
)

edit(
    "lawnchair/res/values/config.xml",
    '<string name="config_default_icon_shape" translatable="false">system</string>',
    '<string name="config_default_icon_shape" translatable="false">squircle</string>',
    "iDroid Home default squircle icon mask",
)
edit(
    "lawnchair/res/values/config.xml",
    '<bool name="config_default_enable_smartspace">true</bool>',
    '<bool name="config_default_enable_smartspace">false</bool>',
    "remove duplicate top information panel by default",
)
edit(
    "lawnchair/res/values/config.xml",
    '<bool name="config_default_smartspace_show_date">true</bool>',
    '<bool name="config_default_smartspace_show_date">false</bool>',
    "hide duplicate date by default",
)

edit(
    "build.gradle",
    'outputFileName = "Lawnchair.${variant.versionName}.$channel.${variant.buildType.name}.apk"',
    'outputFileName = "iDroid.${variant.versionName}.$channel.${variant.buildType.name}.apk"',
    "iDroid APK filename",
)
edit(
    "build.gradle",
    'resValue("string", "derived_app_name", "Lawnchair (Debug)")',
    'resValue("string", "derived_app_name", "iDroid (Debug)")',
    "debug launcher branding",
)
edit(
    "build.gradle",
    'resValue("string", "derived_app_name", "Lawnchair")',
    'resValue("string", "derived_app_name", "iDroid")',
    "release launcher branding",
)
edit(
    "build.gradle",
    "applicationId 'app.lawnchair'",
    "applicationId 'com.cod3uchiha.idroid'",
    "iDroid application ID",
)

# Guard against silently producing an upstream-only APK.
checks = {
    "lawnchair/src/app/lawnchair/preferences2/PreferenceManager2.kt": 'val idroidMode = preference(',
    "lawnchair/src/app/lawnchair/ui/preferences/destinations/GeneralPreferences.kt": 'R.string.idroid_mode_heading',
    "lawnchair/res/values/config.xml": '<string name="config_default_icon_shape" translatable="false">squircle</string>',
    "build.gradle": "applicationId 'com.cod3uchiha.idroid'",
}
for relative, marker in checks.items():
    if marker not in (UPSTREAM / relative).read_text(encoding="utf-8"):
        raise SystemExit(f"Overlay verification failed: {relative} is missing {marker!r}")

print("iDroid overlay applied and verified.")
