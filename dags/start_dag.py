"""DAG that kicks off the pipeline by setting up a new Airflow pool."""

# --------------- #
# Package imports #
# --------------- #

from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from pendulum import datetime

# -------------------- #
# Local module imports #
# -------------------- #

from include.global_variables import airflow_conf_variables as gv


# --- #
# DAG #
# --- #


@dag(
    dag_id = 'start_dag',
    start_date = datetime(2024, 1, 1),
    # After being unpaused, this DAG will run once, afterwards it can be run manually with the play button in the Airflow UI
    schedule = '@once',
    catchup = False,
    default_args = gv.default_args,
    description = 'Run this DAG to create a pool and start the pipeline.',
    tags = ['start', 'setup'],
)
def start():

    # This task uses the BashOperator to run a bash command creating an Airflow pool called 'custom_pool_1' which contains one worker slot. All tasks that arerunning will be assigned to this pool, preventing parallelism
    create_pool = BashOperator(
        task_id = 'bash_task',
        bash_command = "airflow pools list | grep -q 'custom_pool_1' || airflow pools set custom_pool_1 1 'First custom pool'",
    )


# When using the @dag decorator, the decorated function needs to be called after the function definition
start_dag = start()

