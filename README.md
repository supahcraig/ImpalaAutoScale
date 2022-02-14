# Impala Autoscale with JMeter

This is based on an article by Ryan Jendoubi for load testing Impala with JMeter
https://cloudera.atlassian.net/wiki/spaces/person/pages/2211938365/How+to+set+up+for+load+testing+with+JMeter

It requires installing JMeter and OpenJDK8 which you may or may not want to do on your local machine.   This will build a docker container with all the fixins to run the load test routine as explained in the above link.  It also allows for multiple Impala configurations so you can load test different Impala instances (with different users) and switch between them easily.  The SQL to be executed is also parameterized via command line arguments or supplying a file with the query to be run.


## Installation

### Clone the repository
Clone the repo to your local machine:
`git clone XXXX`


### Download the Impala JDBC jar
* From your Impala virtual warehouse, download the ODBC JDBC driver, which will be named `impala_driver_jdbc_odbc.zip`
* unzip it, which will unzip into two folders: `ClouderaImpalaODBC-2.6.13.1015` and `ClouderaImpala_JDBC-2.6.23.1028` _version numbers subject to change_
* Inside the `JDBC` folder is `ImpalaJDBC42.jar`; this needs to be in the repository folder


### Run the container
Run this command to build the container that will host the JMeter execution.  Once complete it will drop you into the shell for the container.

```
chmod +x ./quickstart.sh
./quickstart.sh
```

