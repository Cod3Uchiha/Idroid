plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.cod3uchiha.idroid.launcher"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.cod3uchiha.idroid.launcher"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "0.1.0"
    }
}
