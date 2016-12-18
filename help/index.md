---
layout: page
title: Help &amp; Rules
permalink: /docs/
---

## Help
* [Submit Bug Report]({{ "/bug_report" | prepend: site.baseurl }})
* [Set up port forwarding to host lobby games](http://tripleadev.1671093.n2.nabble.com/Download-Maps-Links-Hosting-Games-General-Information-tp4074312p4085700.html)
* [How to Host in Lobby](http://tripleadev.1671093.n2.nabble.com/Download-Maps-Links-Hosting-Games-General-Information-td4074312.html#a4085700)

## Rules

* [Lobby Conduct Rules](http://www.tripleawarclub.org/modules/newbb/viewtopic.php?topic_id=100&forum=1)
* [Game Rules Manual]({{ "/files/TripleA_RuleBook.pdf" | prepend: site.baseurl }})
* [TripleA Wiki Rulebook](http://en.wikibooks.org/wiki/TripleA)


## Older Documentation
* [Readme]({{ "/playing_the_game_engine_readme" | prepend: site.baseurl }})


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

## User Interface help notes:

### Selecting Units
* Left click on a unit stack to select 1 unit.
* ALT-Left click on a unit stack to select 10 units of that type in the stack.
* CTRL-Left click on a unit stack to select all units of that type in the stack.
* Shift-Left click on a unit to select all units in the territory.
* Left click on a territory but not on a unit to bring up a selection window for inputing the desired selection.

### Deselecting Units
* Right click somewhere not on a unit stack to unselect the last selected unit.
* Right click on a unit stack to unselect one unit in the stack.
* ALT-Right click on a unit stack to unselect 10 units of that type in the stack.
* CTRL-Right click on a unit stack to unselect all units of that type in the stack.
* CTRL-Right click somewhere not on a unit stack to unselect all units selected.

### Moving Units to a new Territories
* After selecting units Left click on a territory to move units there (do not Left click and Drag, instead select units, then move the mouse, then select the territory).
* CTRL-Left click on a territory to select the territory as a way point (this will force the units to move through this territory on their way to the destination).

### Moving the Map Screen
* Right click and Drag the mouse to move your screen over the map.
Left click on the map (anywhere), then use the Arrow Keys to move your map around.
* Left click in the Minimap at the top right of the screen, and Drag the mouse.
* Move the mouse to the edge of the map window, and the screen will scroll in that direction.
scrolling the mouse wheel will move the map up and down.

### Zooming Out
* Holding ALT while Scrolling the Mouse Wheel will zoom the map in and out.
* Select 'Zoom' from the 'View' menu, and change to the desired level.

### Turn off Art
* Deselect 'Map Details' in the 'View' menu, to show a map without the artwork.
* Select a new 'Map Skin' from the 'View' menu to show a different kind of artwork (not all maps have skins).
