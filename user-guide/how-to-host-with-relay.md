---
layout: default
title: Hosting with Relay Service
permalink: /user-guide/how-to-host-with-relay
---


Disclaimer: This post uses [ngrok](https://ngrok.io) as its relay service,
simply because I have used it in the past and it's free for personal use. 
If you know how to use the service of your choice you should be able to use
it, as long as it supports raw tcp sockets.


### Downloading and installing ngrok

This step is simple. Go to https://ngrok.com/download and follow Steps
1 to 3. This assumes you know how to open a command prompt on your OS.

You can now come up with a port number you'd like to use. The default port
is 3300, which I will use from now on.

In the command prompt run
```bash
./ngrok tcp 3300
```
where 3300 is your port number.

You'll get to a screen that looks like this:
![e9c19651-391d-4f53-8119-35340257a5f2-grafik.png](/assets/uploads/files/1589396698766-e9c19651-391d-4f53-8119-35340257a5f2-grafik.png)

We only care for the public hostname and port. In my case those are:
Hostname: `0.tcp.ngrok.io` and Port `19404` (they may change whenever
restarting, so you'll have to check every time).


### Setting up your bot
I assume you'll be using @prastle's script from here. You can find it
[here](https://forums.triplea-game.org/topic/593/how-to-host-a-bot). We
have to add modify the last part a bit:

We replace
```bash
-Ptriplea.server.password=%BOT_PASSWORD%
```
with
```bash
-Ptriplea.server.password=%BOT_PASSWORD%^
-PcustomHost=0.tcp.ngrok.io^
-PcustomPort=19404
```
at the end of the file.

Now you should be able to host.

**Note: You need to keep your ngrok window open as long as you want to host.**
