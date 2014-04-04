#! /bin/bash

for pythonFile in p*.py ; do
    problemNumber=${pythonFile:1:3} ;
    [ "${problemNumber}" -eq 0 ] && continue ;
    ###
    printf "${problemNumber}:\t" ; ./${pythonFile} ;
done
