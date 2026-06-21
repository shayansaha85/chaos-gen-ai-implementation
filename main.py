import time
import threading
import json
from config_loader import load_config
from collector import Collector
from chaos_runner import run_chaos_experiment
from ai_analyzer import analyze_logs
from notifier import send_email_report

def main():
    print("Loading configuration from config.yaml...")
    try:
        config = load_config()
    except Exception as e:
        print(f"Failed to load config: {e}")
        return

    print("Initializing metric collector...")
    collector = Collector(config)
    collector_thread = threading.Thread(target=collector.start, daemon=True)
    collector_thread.start()

    before_duration = config.get('experiment_run', {}).get('before_collection_duration_seconds', 10)
    print(f"\n[Phase 1] Collecting baseline metrics (Before Chaos) for {before_duration} seconds...")
    time.sleep(before_duration)
    before_logs = list(collector.get_logs())
    collector.metrics_log.clear()

    print("\n[Phase 2] Starting Chaos Experiment...")
    run_chaos_experiment(config)
    during_logs = list(collector.get_logs())
    collector.metrics_log.clear()

    after_duration = config.get('experiment_run', {}).get('after_collection_duration_seconds', 10)
    print(f"\n[Phase 3] Collecting recovery metrics (After Chaos) for {after_duration} seconds...")
    time.sleep(after_duration)
    after_logs = list(collector.get_logs())
    
    print("\nStopping metric collector...")
    collector.stop()
    collector_thread.join()

    all_logs = {
        "before": before_logs,
        "during": during_logs,
        "after": after_logs
    }
    with open("collected_metrics.json", "w") as f:
        json.dump(all_logs, f, indent=4)
    print("Metrics saved to collected_metrics.json.")

    print("\nAnalyzing logs with Gemini AI...")
    html_report = analyze_logs(config, before_logs, during_logs, after_logs)

    print("\nSending analysis report via Email...")
    send_email_report(config, html_report)

    print("\nPipeline execution finished successfully! Check analysis_report.html for details.")

if __name__ == "__main__":
    main()
