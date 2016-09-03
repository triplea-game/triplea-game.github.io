---
layout: page
title: 1.8.0.9 Upgrade Notes
---

## Upgrading from 1.8.0.9 to 1.9


### Game Engine
The new game engine will install in a new folder, and you can play 1.8.0.9 games with that engine. With some luck the transition to the new engine should be easy.


### Maps
There are two key folders to be aware of. In the 1.8.0.9 game engine folder, likely in "c:\Program Files\triplea", there is a maps folder. The second key folder is the "triplea/maps" folder that will be in your user accounts home folder. For example: "C:\Documents and Settings\Joe\triplea\maps".

Copy any maps from "c:\Program Files\triplea\maps" to "C:\Documents and Settings\Joe\triplea\maps". From there you can safely remove the old game engine at: "c:\Program Files\triplea\maps".

1.9 maps are loaded from "C:\Documents and Settings\Joe\triplea\downoadedMaps". This is to allow for the 1.8 maps to live side by side with 1.9. TripleA requires map versions be the same, so for starting 1.9 games, the maps used will be the new ones in "C:\Documents and Settings\Joe\triplea\downloadedMaps", 1.8 compatibility games (games started with the 1.9 engine playinig a 1.8 save), will use maps from "C:\Documents and Settings\Joe\triplea\maps""

 
