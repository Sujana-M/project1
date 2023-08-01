#!/usr/bin/sh

lsb_release -a
python --version
python2 --version
python3 --version
echo $PWD
touch diff.txt
touch modified.txt
touch copyright.txt
touch sdl_report.txt
#git diff --name-only HEAD~1 > diff.txt
find $PWD > diff.txt
sed '/linux_app/d' diff.txt >  modified.txt
sed -n '/.*\.h$/p;/.*\.c$/p;/.*\.S$/p;/.*\.py$/p;/.*\.mk$/p;' modified.txt > copyright.txt
echo $PWD
ls
for i in $(cat copyright.txt)
do
    python copyright_checker.py $cwd/$line >> sdl_report.txt
done
cat sdl_report.txt
