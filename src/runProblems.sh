#! /bin/bash

# Constants

SOLUTIONFILE='../dat/solutions.md5' ;
OK='\033[1;32mOK\033[0m' ;
FAIL='\033[1;31mFAIL\033[0m' ;

# Arguments

[ "${#}" -gt 0 ] && pythonFiles="${@}" || pythonFiles=p*.py ;

# Check solutions

for pythonFile in ${pythonFiles} ; do

    problemNumber=${pythonFile:1:3} ;
    [ "${problemNumber}" -eq 0 ] && continue ;

    RESULT="$(./${pythonFile} | md5 -r)" ;
    EXPECTED=$(sed -n "${problemNumber}p" "${SOLUTIONFILE}")

    if [ "${RESULT}" == "${EXPECTED}" ] ; then
        echo -e "${problemNumber}:\t${OK}" ;
    else
        echo -e "${problemNumber}:\t${FAIL}" ;
    fi ;

done
