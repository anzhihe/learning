#!/bin/sh
objectdir="/data/www/OMserverweb"
/usr/bin/inotifywait -mrq --exclude "(static|logs|shell|\.swp|\.swx|\.pyc|\.py\~)" --timefmt '%d/%m/%y %H:%M' --format '%T %w%f' --event modify,delete,move,create,attrib ${objectdir} | while read files
do
    /bin/touch /data/www/OMserverweb/shell/reload.set
    continue
done &