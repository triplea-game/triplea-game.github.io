---
layout: default
title: How to Host / Firewall Configuration
permalink: /user-guide/how-to-host
---

# How to Host in Lobby

You can use [whatismyip](https://whatismyipaddress.com) to determine your IP address.

Launch TripleA and host a direct network game. Then use [canyouseeme.org](https://canyouseeme.org)
to check that your IP address at port 3300 is reachable. If not, you'll need to be sure you
have both firewall and port forwarding rules in place.

## Configuring Firewall

Your Firewall is what blocks unallowed requests from being processed and/or answered from your Computer.
This is a good thing, but in this case we need to setup a special rule for it in order to allow
TripleA to be accessed by other clients over the web.

TripleA uses port 3300 (TCP) by default.

### Finding your Firewall-Settings

**Windows**

Open the Control Panel, click on "Windows Firewall" > "Allow a program or feature through Windows Firewall"

More detailed instructions can be found at: <https://www.windowscentral.com/how-open-port-windows-firewall>

**Linux**

This will vary by distrubtion. On Ubuntu and Debian based systems using `ufw`, the command is:
```
ufw allow 3300
```

**Mac**

See: <https://support.apple.com/en-us/HT201642>


### Configure Port-Forwarding

If you have a router (if you're not plugged directly into your modem), you'll need to set up
port forwarding rules so requests are forwarded from your router to your computer. Each router
can be slightly different, your best bet is to do an internet search for your brand of router
and "how to set up port forwarding".

Make sure your Router forwards Port 3300 to Port 3300 on your local machine.
If you are asked for the Protocol select TCP.


### Troubleshooting

* Try temporarily disabling your Firewall. If everything is working fine with your Firewall disabled,
 you haven't setup your Firewall correctly. If it's still not working your Router isn't correctly 
 forwarding the traffic to your PC.

If you still have any questions, feel free to ask on the player help forum:
<https://forums.triplea-game.org/category/10/player-help>

