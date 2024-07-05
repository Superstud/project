## Chest-Cancer-Detection-MLFLOW-DVC


## WorkFlows

Update config.yaml
Update params.yaml
Update the entity
Update the configuration manager in src config
Update the components
Update the pipeline
Update the main.py
Update the dvc.yaml
app.py


### dagshub 
import dagshub
dagshub.init(repo_owner='abdullahsheikh0945', repo_name='Cancer_project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


MLFLOW TRACKING URI = https://dagshub.com/abdullahsheikh0945/Cancer_project.mlflow

---bash commands to export as env variables
  
export MLFLOW_TRACKING_URI=  https://dagshub.com/abdullahsheikh0945/Cancer_project.mlflow

export MLFLOW_TRACKING_USERNAME=abdullahsheikh0945 

export MLFLOW_TRACKING_PASSWORD=28ce57c27917c5d26e494f1779e2dd44bad1ea7a 