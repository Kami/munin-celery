#!/bin/sh
for out in `ls src/body_*.py`
do
	x=${out#src/body_}
	x=${x%.py}
	out=celery_$x
	
	echo "Generating: $out"
	
	echo "#!/usr/bin/env python" > $out
	cat src/readme_$x.py >> $out
	cat src/common.py >> $out
	cat src/body_$x.py >> $out
	chmod 755 $out
done