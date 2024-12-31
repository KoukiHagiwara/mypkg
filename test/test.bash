#!/bin/bash -xv
# SPDX-FileCopyrightText: 2024 Kouki Hagiwara
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py | tee -  /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen: 10'	


# 10秒間実行して、ログを取得
timeout 15 ros2 run mypkg transmitter | tee /tmp/transmitter.log

cat /tmp/transmitter.log
