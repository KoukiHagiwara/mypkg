# mypkg
ロボットシステム学のROS2パッケージ

# 障害物検知アラートノード
[![test](https://github.com/KoukiHagiwara/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/KoukiHagiwara/mypkg/actions/workflows/test.yml)

ROS2を使用してロボットの障害物検知を行うことを想定して作成したものです。
ロボットの前方にある障害物を検出し、指定した距離内に障害物が存在する場合、警告メッセージを出します。
- obstacle_alert(パブリッシャノード)

ランダムな距離データを生成します。その後、この距離データが一定距離の範囲内にあった場合に警告メッセージを出します。

## 実行方法
実行は以下のコマンドを用いて行います。

```
$ ros2 run mypkg obstacle_alert
```
そして、以下のような警告メッセージが時間の経過とともに表示されていきます。今回は約0.10mを検出した場合に警告メッセージを出すようにしています。

```
[WARN] [1736300866.947282742] [obstacle_alert]: Warning: Obstacle detected at 0.10m
```
# 動作環境
- Python 3.10
- Ubuntu 22.04 LTS
- ROS2 humble
 
テストに使用したコンテナ
- Docker  ryuichiueda/ubuntu22.04-ros2:latest
# ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024
- © 2024 Kouki Hagiwara
