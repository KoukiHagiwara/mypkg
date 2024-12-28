# mypkg
ロボットシステム学のROS2パッケージ

# 障害物検知アラートノード
[![test](https://github.com/KoukiHagiwara/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/KoukiHagiwara/mypkg/actions/workflows/test.yml)

ROS2を使用してロボットの障害物検知を行うことを想定して作成したものです。
ロボットの前方にある障害物を検出し、指定した距離内に障害物が存在する場合、警告メッセージを出します。
- Transmitter(パブリッシャノード)

ランダムな距離データを生成して送信します。

- Detection(サブスクライバノード)

パブリッシャから受信した距離データを解析し、障害物が一定距離の範囲内に入った場合に警告メッセージを出します。

## 実行方法
launchファイルを実行してパブリッシャノードとサブスクライバノードが正しく動いているのかを確認します。
```
$ cd ~/ros2_ws/
```
```
$ colcon build
```
```
$ source ~/.bashrc
```
```
$ ros2 launch mypkg obstacle_alert.launch.py
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
    - [ryuichiueda/my_slides robosys_2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- © 2024 Kouki Hagiwara
