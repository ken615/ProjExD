# 第3回
## 迷路ゲーム : 迷えるこうかとん(ex03/maze.py)
### ゲーム概要
- ex03/maze.pyを実行すると、1500x900のcanvasに迷路が描画され、迷路に沿ってこうかとんを移動させるゲーム
- 実行するたびに迷路の構造は変化する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する。
### 追加機能
- スタート地点とゴール地点の追加 : スタート地点赤色で表示し、ゴール地点は青色で表示した。
- 制限時間を20秒とした。残り10秒になると、「あと10秒!」と表示される。残り時間が0秒になると、「残念！ タイムアップ!」と表示される。
### ToDo(実装しようと思ったけど時間がなかった。)
- [ ] 残り時間を常に表示する機能。
- [ ] 向いている向きによってこうかとんの画像が変わる機能。