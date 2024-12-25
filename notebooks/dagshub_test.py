import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/nikhilkumarbharti/water-potability-test.mlflow')

dagshub.init(repo_owner='nikhilkumarbharti', repo_name='water-potability-test', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)