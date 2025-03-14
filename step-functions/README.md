# Step Functions paramaters
Inside each step function json file, there are three variables that you need to change, according to your environment

# increase-db-size-step-function

* DbInstanceIdentifier: Change the database instance identifier, e.g.: dbtst
* DbInstanceClass: Change the database instance class, e.g.: db.t3.xlarge
* DbParameterGroupName: Change the database parameter group (PG) corresponding to your DbInstanceClass

# decrease-db-size-step-function

* DbInstanceIdentifier: Change database instance identifier, e.g.: dbtst
* DbInstanceClass: Change database instance class, e.g.: db.t3.medium
* DbParameterGroupName: Change database parameter group (PG) corresponding to your DbInstanceClass

