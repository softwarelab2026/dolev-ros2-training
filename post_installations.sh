#!/bin/bash
apt update
apt install -y ros-humble-turtlesim

chmod 600 /root/.ssh/id_ed25519
eval \"$(ssh-agent -s)\"
ssh-add /root/.ssh/id_ed25519
git config --global core.sshCommand 'ssh -i /root/.ssh/id_ed25519 -o StrictHostKeyChecking=yes'
