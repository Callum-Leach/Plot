#!/bin/bash                                                                     
for d in Processed/ ; do (cd "$d" && for d in ./*/ ; do (cd "$d" &&  chmod +x Allclean && ./Allclean && rm -R "$PWD"/logs && mv "$PWD" ../../Unprocessed); done ); done
