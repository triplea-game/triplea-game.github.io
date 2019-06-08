---
layout: default
title: How to Host / Firewall Configuration
permalink: /user-guide/how-to-host
---

*Disclaimer*: Because this Guide heavily depends on the software AND hardware you are using, 
I won't go into the details. Google or any other Search-Engine is your best friend!

In order to allow requests to reach your computer we need to configure 2 Components:
Configuring your Local Firewall

Your Firewall is what blocks unallowed requests from being processed and/or answered from your Computer.
This is a good thing, but in this case we need to setup a special rule for it in order to allow
 TripleA to be accessed by other clients over the web.
On Windows it's often sufficient to just allow a single Application to communicate through the
 Firewall. You can add TripleA to the "Allowed Applications" in your Control Panel, if you are 
 not using the installer, you need to add java instead.
On all operating systems you have the possibility to open single ports manually. TripleA uses 
port 3300 by default.
DO NOT TURN OFF YOUR FIREWALL FOR A LONGER PERIOD OF TIME UNDER ANY CIRCUMSTANCES
Finding your Firewall-Settings
Windows

Open your Control Panel, change the View By setting to "Small/Large Icons" and click on "Windows 
Firewall">Allow a program or feature through Windows Firewall
Linux

Based on the distribution you are using this will differ. On Debian based systems (including Ubuntu)
 you can use ufw (uncomplicated firewall) instead of manually messing with iptables. With ufw you just enter sudo ufw allow 3300 in a terminal. Done.
If you are using Linux you probably know how to figure out how to do this on other distributions. 
There are just too many to list them all.
Mac

I have no idea... (If you are a mac user, please tell me so I can edit this in here later)
Configuring your Router

Assuming yor Computer is not connected directly to the internet, but connected to a router instead 
which is most likely the case, we need to tell your Route it's supposed to route all TripleA-related 
traffic to your computer.
This is called "Port-Forwarding". You can find tons of guides for every router model out there in
the Internet. It would be impossible to list all of those here!
Make sure your Router forwards Port 3300 to Port 3300 on your local machine.
If you are asked for the Protocol select TCP.


### Troubleshooting

Computers often don't work like you want them to, here are some tricks that might come in handy 
if something is not working for you:
Try temporarily disabling your Firewall. If everything is working fine with your Firewall disabled,
 you haven't setup your Firewall correctly. If it's still not working your Router isn't correctly 
 forwarding the traffic to your PC.

[canyouseeme.org](https://canyouseeme.org) is a website that helps you checking if your configuration is 
working. Just enter the port you want to check (in our case 3300).

If you still have any questions, feel free to ask!


### Bot Hosting
Anyone that can host can host bots.

Now you will need to place a bot folder or multiple ones, in the same TripleA program folder. 
The below is an example of one of my bots. Using windows. Other operating systems are slightly 
different.

```
@echo off
SET PORT=3363
SET BOT_NUMBER=25

SET LOBBY_HOST=45.79.144.53
SET LOBBY_PORT=3304

java -server -Xmx320m -Djava.awt.headless=true -classpath bin/triplea.jar games.strategy.engine.framework.headlessGameServer.HeadlessGameServer -Ptriplea.game.host.console=false -Ptriplea.game= -Ptriplea.server=true -Ptriplea.port=%PORT% -Ptriplea.lobby.host=%LOBBY_HOST% -Ptriplea.lobby.port=%LOBBY_PORT% -Ptriplea.name=Bot%BOT_NUMBER%_Pras1 -Ptriplea.lobby.game.hostedBy=Bot%BOT_NUMBER%_Pras1 -Ptriplea.lobby.game.supportEmail=prastle7@hotmail.com -Ptriplea.lobby.game.comments="automated_host" -Ptriplea.lobby.game.reconnection=172800
pause
```

Save the above to a notepad file and rename it with the name and number that you wish for your bot.
Make sure it is using one of the correct port numbers you have opened on your router. Now 
resave the notepad file as a .bat file and place it in your Triple program folder. Test to see if 
your bot launches in the lobby. 
