#!/usr/bin/csh

echo $cwd
touch diff.txt
touch modified.txt
touch copyright.txt
touch sdl_report.txt
git diff --name-only HEAD~1 > diff.txt
sed '/linux_app/d' diff.txt >  modified.txt
sed -n '/.*\.h$/p;/.*\.c$/p;/.*\.S$/p;/.*\.py$/p;/.*\.mk$/p;' modified.txt > copyright.txt
echo $cwd
ls
foreach line ( `cat copyright.txt`)
    ./copyright_checker.py $cwd/$line >> sdl_report.txt
end
cat sdl_report.txt
