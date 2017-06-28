---
layout: page
title: "Set maximum RAM"
permalink: /help/set-ram/
---
(Valid for TripleA v1.9.0.0.5401+)<br>
It may happen that your TripleA client exits with an `OutOfMemoryError`, even if your PC has more RAM to offer.<br>
In this case you might want to increase the usable amount of RAM for your installation of TripleA.<br>
There are multiple ways to achieve this, and they all depend on the way your version of TripleA has been installed on your computer.

<br>
`<amount>` is the amount of memory you want to assign to TripleA.<br>
`1` means 1 byte, `1K` 1024 bytes, `1M` 1024 kilobytes, `1G` 1024 megabytes and so on.<br>
The default value TripleA uses is `1G`.<br><br>

 - Installer
   - Temporary:
     1. Open the commandline/terminal
     2. Enter `/path/to/triplea -J-Xmx<amount>`
   - Permanent:
     1. Go to your TripleA installation directory.
     2. Open the `TripleA.vmoptions` file.
     3. Change the `-Xmx<amount>` to an appropriate value
     4. Start TripleA
 - Jar file
   - Temporary:
     1. Open the commandline/terminal
     2. Enter `java -Xmx<amount> -jar /path/to/the/triplea.jar`
   - Permanent:
     - On Windows
       1. Create a text file called `something.bat`
       2. Insert `java -Xmx<amount> -jar /path/to/the/triplea.jar` and save the file.
       3. Start this batch file instead of the triplea jar in the future.
    - On Unix (macOS/Linux)
      1. Create a text file called `something`
      2. Insert `java -Xmx<amount> -jar /path/to/the/triplea.jar` and save the file.
      3. Mark the file as executable using `chmod +x /path/to/your/file`
      4. Start this script file instead of the triplea jar in the future.
