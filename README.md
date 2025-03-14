# Modify-RDS
Modify RDS using step function workflow

# Step Functions paramaters
Inside each step function json file, there are three variables that you need to change, according to your environment

# increase-db-size-step-function.json

The purpose of this step function is to increase the size of the database to perform some activity that requires more resources.
* DbInstanceIdentifier: Change the database instance identifier, e.g.: dbtst
* DbInstanceClass: Change the database instance class, e.g.: db.t3.xlarge
* DbParameterGroupName: Change the database parameter group (PG) corresponding to your DbInstanceClass

# decrease-db-size-step-function.json

The purpose of this step function is to return the database size to the same setting as before, after you have completed your task that required more computing power.
* DbInstanceIdentifier: Change database instance identifier, e.g.: dbtst
* DbInstanceClass: Change database instance class, e.g.: db.t3.medium
* DbParameterGroupName: Change database parameter group (PG) corresponding to your DbInstanceClass

# 