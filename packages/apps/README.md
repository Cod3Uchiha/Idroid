# iDroid applications

Planned Android applications:

| App | Responsibility | Integration level |
| --- | --- | --- |
| iLauncher | Home screen, dock, folders and app library | Regular app |
| iControlCenter | Optional control surface and shortcuts | Regular app plus supported system APIs |
| iLockScreen | Companion customization UI; actual keyguard requires SystemUI integration | Mixed |
| iSettings | iDroid-specific preferences | Regular app |
| iDynamicIsland | Notification/activity presentation | Regular app with user-granted permissions or privileged integration |

Applications should be separate Gradle modules with clear minimum/target SDK settings, tests, accessibility labels and no hidden collection of user data.

Important: a normal third-party app cannot silently replace secure keyguard, grant itself privileged permissions, or fully control system Quick Settings. Those functions require framework/SystemUI integration in the ROM build.
