# Chaos Engineering with GenAI Analysis on MongoDB

A comprehensive automated pipeline for running Chaos Engineering experiments on MongoDB, collecting system and database metrics, analyzing the impact using Google Gemini AI, and sending an HTML report via email.

## 🚀 Features

- **Automated Metric Collection:** Uses `psutil` and `pymongo` to gather CPU, RAM, connection stats, and query latency before, during, and after chaos.
- **Dynamic Chaos Injection:** Dynamically loads and executes single or multiple chaos experiments from the `chaos-experiments-source-codes` folder sequentially or in parallel.
- **GenAI Analysis:** Replaces manual log analysis by leveraging Google Gemini (`google-generativeai`) to pinpoint anomalies, performance degradation, and recovery patterns.
- **Email Notification:** Generates a visually structured HTML report and sends it via SMTP.
- **Centralized YAML Configuration:** A single `config.yaml` file manages all database connections, secrets, email credentials, and detailed experiment parameters. 
- **Dynamic Database Targeting:** Chaos experiment scripts dynamically read their target `uri`, `database`, and `collection` from the YAML configuration, meaning you no longer have to hardcode MongoDB target parameters.
- **Cross-Platform Compatibility:** The pipeline uses `sys.executable` and `psutil` to remain universally cross-platform. Linux-specific OS-level networking chaos tools (like `iptables` and `tc`) are wrapped in `platform.system() == 'Linux'` checks, automatically falling back gracefully (by skipping) on Windows to prevent execution errors, while application-level chaos works seamlessly on both.

## 📋 Prerequisites

- **Python 3.8+**
- **MongoDB Instance:** Local or remote MongoDB up and running.
- **Gemini API Key:** Get it from [Google AI Studio](https://aistudio.google.com/).
- **Email Credentials:** An SMTP capable email account (e.g. Outlook/Gmail with an app password).

## 🛠️ Installation & Setup

1. **Clone the repository** (if not already done).
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure the application:**
   Edit the `config.yaml` file in the root directory.

   ```yaml
   mongodb:
     uri: "mongodb://localhost:27017/"
     database: "admin"
     collection: "TEST"

   gemini:
     api_key: "YOUR_GEMINI_API_KEY_HERE"
     model_name: "gemini-1.5-pro"

   email:
     smtp_server: "smtp.outlook.com"
     smtp_port: 587
     sender_email: "YOUR_EMAIL@outlook.com"
     sender_password: "YOUR_APP_PASSWORD"
     receiver_email: "RECEIVER_EMAIL@example.com"

   collector:
     interval_seconds: 2

   experiment_run:
     before_collection_duration_seconds: 15
     after_collection_duration_seconds: 15
     chaos_duration_seconds: 30
     execution_mode: "parallel" # or "sequential"
     experiments:
       - "connection-overload.py"
       - "query-complexity.py"
   ```

## 🧪 Running the Pipeline

To execute the entire pipeline (data collection -> chaos injection -> AI analysis -> email reporting), simply run:

```bash
python main.py
```

### What happens under the hood?
1. The collector starts in the background and gathers baseline metrics for the configured `before_collection_duration_seconds`.
2. The orchestrator triggers the specified chaos script(s) either sequentially or in parallel for the `chaos_duration_seconds`.
3. Metrics are continuously logged during the chaos phase.
4. After chaos stops, the collector gathers recovery metrics for `after_collection_duration_seconds`.
5. All metrics (`before`, `during`, `after`) are passed to Google Gemini.
6. Gemini generates an HTML analysis report highlighting vulnerabilities and system behavior.
7. The HTML report is saved as `analysis_report.html` and emailed via SMTP.

## 📁 Project Structure

- `main.py`: The main orchestrator script.
- `config.yaml`: Central configuration file.
- `config_loader.py`: Module to parse configuration.
- `collector.py`: Background thread script for metric collection.
- `chaos_runner.py`: Trigger mechanism for chaos experiments (parallel/sequential).
- `ai_analyzer.py`: Integration with Google Gemini for log analysis.
- `notifier.py`: Email dispatcher.
- `chaos-experiments-source-codes/`: Directory containing all MongoDB chaos scripts.
- `archived/`: Older deprecated versions, modules, and unused legacy files.

## 📊 Chaos Experiments Available

Navigate to `chaos-experiments-source-codes/` to see available experiments such as:
- `connection-overload.py`
- `disk-full-scenario.py`
- `packet-loss-chaos.py`
- `random-node-shutdown.py`
...and more. You can add your own custom python scripts here!
