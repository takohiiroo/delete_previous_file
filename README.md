# Delete_Previous_File
***
I usualy rec my video game playing with [Bandicam](https://www.bandicam.jp/). It is very useful because I can start and stop recording just only by pressing F12. However, because I rec a lot and make files too much, I usualy forget which files I should delete.  
 Therefore, I made this repository which delete the latest created file of a folder. And I made bat file. We can delete immediately failed movie **during playing video games** if we set it to keyboard shortcut.
<br>
<br>
私はゲームをしているとき、[Bandicam](https://www.bandicam.jp/)を使ってよく画面キャプチャをしています。
F12を押すだけで撮影を開始、停止できるのでとても便利なのですが、撮りすぎてファイルが増えすぎてしまい、どの動画がボツかがわからなくなることがよくあります。  
そこで対象フォルダ内のファイルの中で作成時間が最新のものを消すプログラムを作りました。一緒にbatファイルも作ったので、これをキーボードショートカットに登録すれば**ゲーム中すぐに**ボツ動画を消すことができます。
<br>
<br>
<br>
<br>
Procram flow
1.Set the path of movie files location<br>
2.Use *"glep"* and regex to extract all files in the folder <br>
3.Use *"max"* and set the key *"getctime"* to find the most recent file as of the creation date.<br>
4.Delete<br>
5.Use *"plyer"* module to output toast notification and finish
<br>
<br>
プログラムの流れ  
1.動画が保存されるフォルダのパスを設定<br>
2.*glep*で正規表現を使いフォルダ内の全ファイルを取り出す<br>
3.max関数の*key*を*getctime*にして作成日時における最新のファイルを見つけ出す<br>
4.削除<br>
5.*plyer*モジュールを使い、トースト通知を出して終了