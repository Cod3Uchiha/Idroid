package com.cod3uchiha.idroid.launcher

import android.app.Activity
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Color
import android.graphics.Typeface
import android.graphics.drawable.GradientDrawable
import android.os.Bundle
import android.view.Gravity
import android.view.View
import android.widget.GridLayout
import android.widget.ImageView
import android.widget.LinearLayout
import android.widget.ScrollView
import android.widget.TextView
import java.util.Locale

class MainActivity : Activity() {
    private val blue = Color.rgb(55, 120, 246)
    private val ink = Color.rgb(28, 37, 55)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        window.statusBarColor = Color.rgb(234, 240, 250)
        window.navigationBarColor = Color.rgb(234, 240, 250)
        @Suppress("DEPRECATION")
        window.decorView.systemUiVisibility =
            View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR or View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR
        setContentView(createHome())
    }

    private fun createHome(): View {
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(dp(20), dp(18), dp(20), dp(14))
            background = GradientDrawable(
                GradientDrawable.Orientation.TL_BR,
                intArrayOf(Color.rgb(238, 244, 255), Color.rgb(220, 232, 250), Color.rgb(244, 239, 255))
            )
        }

        val heading = TextView(this).apply {
            text = "Your apps"
            setTextColor(ink)
            textSize = 19f
            setTypeface(null, Typeface.BOLD)
            setPadding(0, 0, 0, dp(14))
        }
        root.addView(heading)

        val apps = loadApps()
        val scroll = ScrollView(this).apply {
            isFillViewport = false
            clipToPadding = false
        }
        val content = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
        }
        val grid = GridLayout(this).apply {
            columnCount = 4
            useDefaultMargins = false
        }

        apps.forEach { app ->
            grid.addView(appTile(app), GridLayout.LayoutParams().apply {
                width = 0
                height = dp(104)
                columnSpec = GridLayout.spec(GridLayout.UNDEFINED, 1f)
                setMargins(dp(2), dp(2), dp(2), dp(8))
            })
        }

        if (apps.isEmpty()) {
            content.addView(TextView(this).apply {
                text = "No launchable apps found"
                setTextColor(ink)
                textSize = 14f
                setPadding(0, dp(20), 0, dp(20))
            })
        } else {
            content.addView(grid)
        }
        scroll.addView(content)
        root.addView(scroll, LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, 0, 1f
        ))

        val dockApps = apps.take(4)
        val dock = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            gravity = Gravity.CENTER
            setPadding(dp(8), dp(9), dp(8), dp(5))
            background = rounded(Color.argb(150, 255, 255, 255), dp(28))
            elevation = dp(8).toFloat()
        }
        dockApps.forEach { app ->
            dock.addView(appTile(app, compact = true), LinearLayout.LayoutParams(0, dp(68), 1f))
        }
        root.addView(dock, LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, dp(78)
        ).apply { topMargin = dp(10) })

        return root
    }

    private data class LaunchableApp(val label: String, val packageName: String, val icon: android.graphics.drawable.Drawable)

    private fun loadApps(): List<LaunchableApp> {
        val intent = Intent(Intent.ACTION_MAIN).addCategory(Intent.CATEGORY_LAUNCHER)
        return packageManager.queryIntentActivities(intent, PackageManager.MATCH_ALL)
            .mapNotNull { info ->
                val packageName = info.activityInfo?.packageName ?: return@mapNotNull null
                if (packageName == packageNameForThisApp()) return@mapNotNull null
                LaunchableApp(
                    info.loadLabel(packageManager).toString(),
                    packageName,
                    info.loadIcon(packageManager)
                )
            }
            .distinctBy { it.packageName }
            .sortedBy { it.label.lowercase(Locale.getDefault()) }
    }

    private fun packageNameForThisApp() = applicationContext.packageName

    private fun appTile(app: LaunchableApp, compact: Boolean = false): View {
        val tile = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            gravity = Gravity.CENTER
            isClickable = true
            isFocusable = true
            setOnClickListener {
                val launch = packageManager.getLaunchIntentForPackage(app.packageName)
                if (launch != null) runCatching { startActivity(launch) }
            }
            contentDescription = app.label
        }
        // Keep the installed application's own icon; only add a consistent rounded-square tile.
        val iconFrame = android.widget.FrameLayout(this).apply {
            background = rounded(Color.argb(110, 255, 255, 255), dp(16))
            elevation = dp(2).toFloat()
            layoutParams = LinearLayout.LayoutParams(dp(58), dp(58))
        }
        val icon = ImageView(this).apply {
            setImageDrawable(app.icon)
            scaleType = ImageView.ScaleType.FIT_CENTER
            layoutParams = android.widget.FrameLayout.LayoutParams(dp(48), dp(48), Gravity.CENTER)
        }
        iconFrame.addView(icon)
        tile.addView(iconFrame)
        if (!compact) {
            tile.addView(TextView(this).apply {
                text = app.label
                setTextColor(ink)
                textSize = 11f
                gravity = Gravity.CENTER
                maxLines = 1
                ellipsize = android.text.TextUtils.TruncateAt.END
                setPadding(dp(1), dp(5), dp(1), 0)
            })
        }
        return tile
    }

    private fun rounded(color: Int, radius: Int) = GradientDrawable().apply {
        setColor(color)
        cornerRadius = radius.toFloat()
        setStroke(dp(1), Color.argb(90, 255, 255, 255))
    }

    private fun dp(value: Int): Int = (value * resources.displayMetrics.density).toInt()
}
