02
Set Up Tracking Backend
Recommended: SQLite
Choose where MLflow will store experiment data.

Option A: Local SQLite DB → mlflow.set_tracking_uri("sqlite:///mlflow.db")

Option B: Local file system (default) → creates mlruns/ folder

Option C: Remote server → mlflow.set_tracking_uri("http://localhost:5000")

03
Create or Select Experiment
Organize runs under a named experiment.

mlflow.set_experiment("my-first-experiment")

Use descriptive names for clarity

04
Log Parameters, Metrics, and Models
Track your ML workflow during training.

Wrap code with with mlflow.start_run():

Log parameters: mlflow.log_param("alpha", 0.1)

Log metrics: mlflow.log_metric("rmse", 0.89)

Log models: mlflow.sklearn.log_model(model, "model")

05
Launch MLflow UI
Visualize experiments and compare runs.

Run in terminal:

mlflow ui

Open browser at http://localhost:5000

Inspect parameters, metrics, and artifacts