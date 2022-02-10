#!/bin/bash
#script to install git on attack machine and clone a repository

echo "Select The given Choice"
echo "1) Install git and other dependencies"
echo "2) Just Clone a Repository"
echo "3) Remove the cloned repository"
read m

case $m in
1)
ansible linux1 -m raw -a 'apt-get install git python3 python -y '
;;
2)
ansible linux1 -m raw -a 'git clone https://github.com/Ishan3011/flood_80.git '
;;
3)
ansible linux1 -m raw -a 'rm -rf flood_80/'
;;
*)
exit
;;
esac
