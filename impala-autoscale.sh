#!/bin/bash

/bin/rm -rf output
/bin/rm resultsfile

HEAP="-Xms1g -Xmx1g -XX:MaxMetaspaceSize=256m" CLASSPATH=$(pwd) ./apache-jmeter-5.4.3/bin/jmeter -n -t myconfig.jmx -l ./resultsfile -e -o output