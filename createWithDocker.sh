#!/usr/bin/env bash
cd "$(dirname "$0")" || exit

#map to $PWD to make sure the created mapping file has the corrects paths
docker run -i --rm --net=host  \
--volume $PWD:/$PWD \
meyermeyer/esw_build:latest \
bash \
-c "cd /$PWD && ./build.sh" \

#docker run -it --entrypoint /bin/bash meyermeyer/esw-daemon:latest
