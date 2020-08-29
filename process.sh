#!/bin/bash                                                                     
for d in Unprocessed/ ; do (cd "$d" && for d in ./*/ ; do (cd "$d" &&  chmod +x Allrun && ./Allrun && mv "$PWD" ../../Processed); done ); done
