---
layout: page
title: 1.8.0.9 Upgrade Notes
permalink: /upgrade_notes/
---

## Upgrading from 1.8.0.9 to 1.9


### Game Engine
The new game engine will install in a new folder, and you can play 1.8.0.9 games with that engine. With some luck the transition to the new engine should be easy.


### Maps
Assuming windows, and tripleA is installed to: "C:\Program Files\triplea", and your user home folder is "C:\Users\Jane"

Copy any maps from "C:\Program Files\triplea\maps" to "C:\Users\Jane\triplea\maps". From there you can safely remove the old game engine at: "C:\Program Files\triplea\".

1.9 maps are loaded from "C:\Users\Jane\triplea\downloadedMaps". This is to allow for the 1.8 maps to live side by side with 1.9. TripleA requires map versions be the same. When starting 1.9 games, the maps used will be the new ones in "C:\Users\Jane\triplea\downloadedMaps". 1.8 compatibility games (games started with the 1.9 engine playinig a 1.8 save) will use maps from "C:\Users\Jane\triplea\maps".

 
