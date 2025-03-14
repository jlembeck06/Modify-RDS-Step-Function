# Modify-RDS
Modify RDS using step function workflow

# Step Functions paramaters
Inside each step function json file, there are three variables that you need to change, according to your environment

# increase-db-size-step-function

The purpose of this step function is to increase the size of the database to perform some activity that requires more resources.
* DbInstanceIdentifier: Change the database instance identifier, e.g.: dbtst
* DbInstanceClass: Change the database instance class, e.g.: db.t3.xlarge
* DbParameterGroupName: Change the database parameter group (PG) corresponding to your DbInstanceClass

![stepfunctions_graph_increase](https://github.com/user-attachments/assets/4a29d79d-2995-436b-95cc-6ee9fc810026)


# decrease-db-size-step-function

The purpose of this step function is to return the database size to the same setting as before, after you have completed your task that required more computing power.
* DbInstanceIdentifier: Change database instance identifier, e.g.: dbtst
* DbInstanceClass: Change database instance class, e.g.: db.t3.medium
* DbParameterGroupName: Change database parameter group (PG) corresponding to your DbInstanceClass

![stepfunctions_graph_decrease](https://github.com/user-attachments/assets/a7b3c814-a1ba-43d9-95f2-e667b0790523)
