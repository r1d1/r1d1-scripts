#/usr/bin/sh

#date >> time_nex.txt; { /usr/bin/time -p sleep $(( ($RANDOM % 5) +1 )) ; } 2>> time_nex.txt
date >> time_nex.txt; { /usr/bin/time -p nexuiz ; } 2>> time_nex.txt
python nexuizproc.py
echo '-------------'
python nexuiz_plot.py

