#!/bin/bash

FILE=/usr/src/app/resultsfile
if [-f "$FILE" ]; then
  rm "$FILE"
fi

FOLDER=/usr/src/app/output
if [-d "$FOLDER" ]; then
  rm -rf "$FOLDER"
fi

HEAP="-Xms1g -Xmx1g -XX:MaxMetaspaceSize=256m" CLASSPATH=$(pwd) ./apache-jmeter-5.4.3/bin/jmeter -n -t myconfig.jmx -l ./resultsfile -e -o output