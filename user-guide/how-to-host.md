---
layout: default
title: How to Host / Firewall Configuration
permalink: /user-guide/how-to-host
---


In order to allow requests to reach your computer we need to configure 2 Components:

## Configuring your Local Firewall

Your Firewall is what blocks unallowed requests from being processed and/or answered from your Computer.
This is a good thing, but in this case we need to setup a special rule for it in order to allow
 TripleA to be accessed by other clients over the web.


On Windows it's often sufficient to just allow a single Application to communicate through the
Firewall. You can add TripleA to the "Allowed Applications" in your Control Panel.


On all operating systems you have the possibility to open single ports manually. 
TripleA uses  port 3300 by default.

DO NOT TURN OFF YOUR FIREWALL FOR A LONGER PERIOD OF TIME UNDER ANY CIRCUMSTANCES

### Finding your Firewall-Settings

**Windows**

Open your Control Panel,  click on "Windows Firewall" > "Allow a program or feature through Windows Firewall"

More detailed instructions can be found at: <https://www.windowscentral.com/how-open-port-windows-firewall>

**Linux**

This will very by distrubtion. On Ubuntu and Debian based systems using `ufw`, the command is:
```
ufw allow 3300
```

**Mac**

See: <https://support.apple.com/en-us/HT201642>


### Configure Port-Forwarding

Assuming yor Computer is not connected directly to the internet, but connected to a router instead 
which is most likely the case, we need to tell your Route it's supposed to route all TripleA-related 
traffic to your computer.
This is called "Port-Forwarding". You can find tons of guides for every router model out there in
the Internet. It would be impossible to list all of those here!
Make sure your Router forwards Port 3300 to Port 3300 on your local machine.
If you are asked for the Protocol select TCP.


### Troubleshooting

* Try temporarily disabling your Firewall. If everything is working fine with your Firewall disabled,
 you haven't setup your Firewall correctly. If it's still not working your Router isn't correctly 
 forwarding the traffic to your PC.

[canyouseeme.org](https://canyouseeme.org) is a website that helps you checking if your configuration is 
working. Just enter the port you want to check (in our case 3300).

[whatismyip](https://whatismyipaddress.com) can be used to double check your public facing IP address,
it must be accessible from other computes.


If you still have any questions, feel free to ask on the player help forum:
<https://forums.triplea-game.org/category/10/player-help>

