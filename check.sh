#!/usr/bin/sh

echo $pwd
touch diff.txt
touch modified.txt
touch copyright.txt
touch sdl_report.txt
#git diff --name-only HEAD~1 > diff.txt
find . > diff.txt
sed '/linux_app/d' diff.txt >  modified.txt
sed -n '/.*\.h$/p;/.*\.c$/p;/.*\.S$/p;/.*\.py$/p;/.*\.mk$/p;' modified.txt > copyright.txt
echo $pwd
ls
for i in $(cat copyright.txt)
do
    ./copyright_checker.py $cwd/$line >> sdl_report.txt
done
cat sdl_report.txt
