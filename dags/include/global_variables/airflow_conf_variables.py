"""Python file that contains configuration variables."""

# --------------- #
# Package imports #
# --------------- #

import logging
from pendulum import duration

# ----------------------- #
# Configuration variables #
# ----------------------- #


# Get Airflow task logger
task_log = logging.getLogger('airflow.task')


# DAG default arguments (specify to fit your requirements)
default_args = {
    'owner': 'airflow user',
    'retries': 1,
    'retry_delay': duration(minutes = 5),
    'email': ['info@ubuntu.local'],
    'email_on_failure': True,
    'depends_on_past': False
}