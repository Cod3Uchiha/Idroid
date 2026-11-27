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


def edit_once(relative, marker, old, new, label):
    path = UPSTREAM / relative
    if marker in path.read_text(encoding="utf-8"):
        print(f"already applied: {label}")
        return
    edit(relative, old, new, label)


preference_manager_path = UPSTREAM / "lawnchair/src/app/lawnchair/preferences2/PreferenceManager2.kt"
if 'val idroidMode = preference(' not in preference_manager_path.read_text(encoding="utf-8"):
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
else:
    print("already applied: two-mode preference and mode preset behavior")

# Extend older applied overlays as well as clean upstream checkouts. The mode
# preset keeps Lawnchair's shared workspace and only changes appearance prefs.
edit(
    "lawnchair/src/app/lawnchair/preferences2/PreferenceManager2.kt",
    '''            enableSmartspace.setBlocking(mode == "one_ui")
            reloadHelper.restart()
''',
    '''            enableSmartspace.setBlocking(mode == "one_ui")
            hotseatMode.setBlocking(
                HotseatMode.fromString(if (mode == "one_ui") "lawnchair" else "disabled"),
            )
            folderBackgroundOpacity.setBlocking(if (mode == "one_ui") 1.0f else 0.82f)
            folderPreviewBackgroundOpacity.setBlocking(if (mode == "one_ui") 1.0f else 0.58f)
            reloadHelper.restart()
''',
    "mode-specific search bar and folder material presets",
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
    '<string name="config_default_hotseat_mode" translatable="false">lawnchair</string>',
    '<string name="config_default_hotseat_mode" translatable="false">disabled</string>',
    "use an icon-only dock in iDroid Home",
)
edit(
    "lawnchair/res/values/config.xml",
    '<item name="config_default_folder_preview_background_opacity" type="dimen" format="float">1.0</item>',
    '<item name="config_default_folder_preview_background_opacity" type="dimen" format="float">0.58</item>',
    "translucent iDroid folder icon previews",
)
edit(
    "lawnchair/res/values/config.xml",
    '<item name="config_default_folder_background_opacity" type="dimen" format="float">1.0</item>',
    '<item name="config_default_folder_background_opacity" type="dimen" format="float">0.82</item>',
    "translucent iDroid folder surfaces",
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

# Draw a lightweight, wallpaper-visible capsule behind the existing hotseat
# icons in iDroid Home. No blur or continuous animation is used.
edit(
    "src/com/android/launcher3/Hotseat.java",
    "import android.graphics.Rect;\n",
    """import android.content.res.Configuration;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Rect;
import android.graphics.RectF;
""",
    "hotseat drawing imports",
)
edit(
    "src/com/android/launcher3/Hotseat.java",
    "    PreferenceManager2 preferenceManager2;\n",
    """    PreferenceManager2 preferenceManager2;
    private final Paint mIdroidDockPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final RectF mIdroidDockBounds = new RectF();
""",
    "lightweight iDroid dock drawing state",
)
edit(
    "src/com/android/launcher3/Hotseat.java",
    "        super(context, attrs, defStyle);\n\n        preferenceManager2 = PreferenceManager2.getInstance(context);",
    "        super(context, attrs, defStyle);\n        setWillNotDraw(false);\n\n        preferenceManager2 = PreferenceManager2.getInstance(context);",
    "enable hotseat background drawing",
)
edit_once(
    "src/com/android/launcher3/Hotseat.java",
    "private void drawIdroidDock(Canvas canvas)",
    "    public void setWorkspace(Workspace<?> w) {\n",
    """    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        drawIdroidDock(canvas);
    }

    private void drawIdroidDock(Canvas canvas) {
        if (!"idroid_home".equals(
                PreferenceExtensionsKt.firstBlocking(preferenceManager2.getIdroidMode()))) {
            return;
        }
        if (mHasVerticalHotseat) {
            return;
        }

        ViewGroup icons = getShortcutsAndWidgets();
        if (icons == null || icons.getVisibility() != View.VISIBLE) {
            return;
        }

        float density = getResources().getDisplayMetrics().density;
        float horizontalInset = 10f * density;
        float verticalInset = 3f * density;
        mIdroidDockBounds.set(
                icons.getLeft() + horizontalInset,
                icons.getTop() + verticalInset,
                icons.getRight() - horizontalInset,
                icons.getBottom() - verticalInset);
        if (mIdroidDockBounds.width() <= 0 || mIdroidDockBounds.height() <= 0) {
            return;
        }

        boolean nightMode = (getResources().getConfiguration().uiMode
                & Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES;
        float radius = mIdroidDockBounds.height() / 2f;

        mIdroidDockPaint.setStyle(Paint.Style.FILL);
        mIdroidDockPaint.setColor(nightMode
                ? Color.argb(168, 24, 26, 32)
                : Color.argb(198, 250, 251, 255));
        canvas.drawRoundRect(mIdroidDockBounds, radius, radius, mIdroidDockPaint);

        mIdroidDockPaint.setStyle(Paint.Style.STROKE);
        mIdroidDockPaint.setStrokeWidth(Math.max(1f, density));
        mIdroidDockPaint.setColor(nightMode
                ? Color.argb(48, 255, 255, 255)
                : Color.argb(115, 255, 255, 255));
        canvas.drawRoundRect(mIdroidDockBounds, radius, radius, mIdroidDockPaint);
    }

    public void setWorkspace(Workspace<?> w) {
""",
    "translucent iDroid Home dock capsule",
)

edit(
    "src/com/android/launcher3/Hotseat.java",
    '''        if (!"idroid_home".equals(
                PreferenceExtensionsKt.firstBlocking(preferenceManager2.getIdroidMode()))) {
            return;
        }

        ViewGroup icons = getShortcutsAndWidgets();
''',
    '''        if (!"idroid_home".equals(
                PreferenceExtensionsKt.firstBlocking(preferenceManager2.getIdroidMode()))) {
            return;
        }
        if (mHasVerticalHotseat) {
            return;
        }

        ViewGroup icons = getShortcutsAndWidgets();
''',
    "skip floating dock in vertical layouts",
)

edit(
    "lawnchair/res/values/strings.xml",
    '<string name="idroid_interface_mode_description">Choose iDroid Home or One UI Mode. The preset changes the icon mask and home information panel.</string>',
    '<string name="idroid_interface_mode_description">Choose iDroid Home or One UI Mode. The preset changes the icon mask, dock, folder surfaces and home information panel while keeping your workspace.</string>',
    "describe complete launcher mode presets",
)

# Guard against silently producing an upstream-only APK.
checks = {
    "lawnchair/src/app/lawnchair/preferences2/PreferenceManager2.kt": 'val idroidMode = preference(',
    "lawnchair/src/app/lawnchair/ui/preferences/destinations/GeneralPreferences.kt": 'R.string.idroid_mode_heading',
    "lawnchair/res/values/config.xml": '<string name="config_default_icon_shape" translatable="false">squircle</string>',
    "build.gradle": "applicationId 'com.cod3uchiha.idroid'",
    "src/com/android/launcher3/Hotseat.java": "private void drawIdroidDock(Canvas canvas)",
}
for relative, marker in checks.items():
    if marker not in (UPSTREAM / relative).read_text(encoding="utf-8"):
        raise SystemExit(f"Overlay verification failed: {relative} is missing {marker!r}")

print("iDroid overlay applied and verified.")
