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

timeout 15 ros2 launch mypkg obstacle_alert.launch.py | tee - /tmp/obstacle_alert.log 

# サブスクライバーノードのアラートメッセージを監視
ALERT_COUNT=0
while [ "$ALERT_COUNT" -lt 10 ]; do
    ALERT_COUNT=$((ALERT_COUNT + 1))
done


cat /tmp/obstacle_alert.log 
	


