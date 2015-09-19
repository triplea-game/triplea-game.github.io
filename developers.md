---
layout: page
title: Developers
permalink: /developers/
---

## Contributing
Do you know Java, like to write games, and have a lot of free time? If you answered yes to all three then we would like to hear from you.

To get started simply download the latest development version from Github. You can also browse the repository from here. If you have ant installed, you simply need to type `ant` in the main directory, after you unzip.

Submit changes as pull requests on Github.

### What needs to be done

- Online game net traffic relay server (so no need for port forwarding)

- NAT Traversal (STUN/TURN/ICE for punching through router firewall, so no need for port forwarding)

- Better map editor, specifically for the xml part

- Better AI (can you write something to beat the current AI, or improve existing AIs)

- Optional Rules (WW1 1914, etc...)

- Other games (Risk, etc...)

- Ability to hide information from user, fully encrypted with per-player/per-nation passwords

## Github

The easiest way to get the latest TripleA development version is through this command, if you have git installed:

`git clone https://github.com/triplea-game/triplea.git`

### How to Submit a Pull Request

If you would like to propose a change you have made to the source code, push to a fork of the main repo and submit a pull request. More info in the official Github help page.

## Build system

[Gradle](www.gradle.org) is used. The gradlew (on Windows gradlew.bat) file is a proxy to execute build commands.
On first call these files will install the correct version of Gradle on your system. Most commonly used commands:

* Creates a jar file from the project, dependencies are not added:
`./gradlew jar` (creates into build/libs/triplea-<version>.jar)

* Creates a self contained jar file from the project, all JAR dependencies are included: `./gradlew shadowJar` (creates into build/libs/triplea-<version>-all.jar)
* Run the application right from the source (no jar is created); this may be used from inside an IDE to debug `./gradlew run` (creates into build/libs/triplea-<version>-all.jar)

Tooling and IDE setup
=====================

With the help of the Gradle system any modern IDE support is provided out of box, such as:

* Eclipse - use the [Buildship plugin](https://github.com/eclipse/buildship/blob/master/docs/user/Installation.md)
* Intellij IDEA - out of box integration support (just import project, and specify the settings.gradle file)
* Netbeans - use the [Gradle plugin](http://plugins.netbeans.org/plugin/44510/gradle-support)
