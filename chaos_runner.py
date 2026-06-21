import os
import subprocess
import concurrent.futures
import sys

def run_chaos_experiment(config):
    chaos_dir = os.path.join(os.path.dirname(__file__), 'chaos-experiments-source-codes')
    
    experiment_config = config.get('experiment_run', {})
    experiments = experiment_config.get('experiments', [])
    execution_mode = experiment_config.get('execution_mode', 'sequential')
    duration = experiment_config.get('chaos_duration_seconds', 30)

    if not os.path.exists(chaos_dir):
        print(f"Chaos directory {chaos_dir} not found.")
        return

    if not experiments:
        print("No chaos scripts configured to run.")
        return

    print(f"Running chaos experiments: {experiments} in {execution_mode} mode for {duration} seconds.")

    def run_single_experiment(experiment):
        script_path = os.path.join(chaos_dir, experiment)
        if not os.path.exists(script_path):
            print(f"Experiment script {experiment} not found. Skipping.")
            return

        print(f"Starting {experiment}...")
        process = subprocess.Popen([sys.executable, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            process.wait(timeout=duration)
        except subprocess.TimeoutExpired:
            process.kill()
            print(f"Experiment {experiment} terminated after {duration} seconds.")
        else:
            print(f"Experiment {experiment} finished execution.")

    if execution_mode.lower() == 'parallel':
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, len(experiments))) as executor:
            list(executor.map(run_single_experiment, experiments))
    else:
        for experiment in experiments:
            run_single_experiment(experiment)

    print("All chaos experiments completed.")
