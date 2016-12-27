---
layout: page
title: FAQ
permalink: /help/faq
---


## FAQ

> Q. How do you set way points when moving.

A. Ctrl-click on the territory you want to use as a way point.


> Q. If the game is open source, how do you prevent people from hacking the dice.

A. In PBEM games, all dice are rolled by a third party dice server, and mailed to the players. This allows you to verify that your opponent is not cheating.

In online games, the dice are rolled on two computers, and are encrypted (for more details see OnlineDice ). If you are playing as a client (NOTE: if there are multiple clients, then only 1 client will have the verified random number), you can check the dice by using the menu games->show verified dice. If the dice in this window don't match the dice in the game, then the server has been hacked.


> Q. When I try to host a game, people cannot connect to me.

A. You are probably behind a router and/or a firewall. Read these for more details,

* [How to Host a TripleA game](http://tripleadev.1671093.n2.nabble.com/Download-Maps-Links-Hosting-Games-General-Information-tp4074312p4085700.html)

* <http://portforward.com/>


> Q. How do I open a port under Linux?

A. Using the root account (or sudo), at a command prompt type the following exactly, including capitalisation, spacing, and dashes. Note that in some places there is 1 dash and in other places there are 2 dashes:

`iptables -A INPUT -m state --state NEW -p tcp --dport 3300 -j ACCEPT`

(If you want to open a different port, just replace the 3300 with the port number you want to open.)


> Q. How do I Download more maps and games?

Please read one of the two following links:

* Downloading Maps Link Listing
* A picture tutorial step by step of how to download new maps.


> Q. Where can I play in tournaments and ladders?

A. The TripleA War Club


> Q. How do I move units, and use TripleA to play?

Choose the game you want to play, then click "Start Local Game" to begin a game on your machine.
After the game has started, click on the "Help" menu option near the top of the screen. From there, click "Game Notes" to see specific notes about the map you are currently playing, or click "Movement Help" to see general notes about how to move units and use Triplea.

> Q. Can I change game settings after starting a game?

Yes, save the game, load it again and change the setting before starting.
