# Delete_Previous_File
***
I usualy rec my video game playing with [Bandicam](https://www.bandicam.jp/). It is very useful because I can start and stop recording just only by pressing F12. However, because I rec a lot and make files too much, I usualy forget which files I should delete.  
 Therefore, I made this repository which delete the latest created file of a folder. And I made bat file. We can delete immediately failed movie **during playing video games** if we set it to keyboard shortcut.
<br>
<br>
## Program flow
1.Set the path of movie files location<br>
2.Use *"glep"* and regex to extract all files in the folder <br>
3.Use *"max"* and set the key *"getctime"* to find the most recent file as of the creation date.<br>
4.Delete<br>
5.Use *"plyer"* module to output toast notification and finish
<br>
<br>
# P.S.
I don't want to delete important file when the video game is not running, so I add a sentence of conditional branching on the bat file. It works only when the game is running.<br>
It passes *tasklist* to *find* to find execute file of the video game, and uses *ERRORLEVEL* to confirm that the prosess succeeded or not.
