import google.generativeai as genai
import json

def analyze_logs(config, before_logs, during_logs, after_logs):
    api_key = config.get('gemini', {}).get('api_key')
    if api_key == 'YOUR_GEMINI_API_KEY_HERE':
        print("Gemini API key not configured. Skipping analysis.")
        return "<p>Gemini API key not configured. Please update config.yaml</p>"

    genai.configure(api_key=api_key)
    model_name = config.get('gemini', {}).get('model_name', 'gemini-1.5-pro')
    model = genai.GenerativeModel(model_name)

    prompt = f"""
    You are an expert Chaos Engineering Analyst. Analyze the following MongoDB and System metrics collected during a chaos engineering experiment.
    
    The experiment has 3 phases:
    1. Before Chaos (Baseline)
    2. During Chaos (Experiment active)
    3. After Chaos (Recovery)
    
    Metrics Before Chaos:
    {json.dumps(before_logs, indent=2)}
    
    Metrics During Chaos:
    {json.dumps(during_logs, indent=2)}
    
    Metrics After Chaos:
    {json.dumps(after_logs, indent=2)}
    
    Please provide a comprehensive analysis. Identify anomalies, performance degradation, bottlenecks, and recovery behavior. 
    Format the output as a clean and well-structured HTML document (without ```html markdown codeblocks, just the pure HTML code starting with <html> or <div>), which can be directly sent via email. Include styling if necessary.
    """
    
    print("Asking Gemini for insights...")
    try:
        response = model.generate_content(prompt)
        html_content = response.text.replace("```html", "").replace("```", "").strip()
        
        with open("analysis_report.html", "w") as f:
            f.write(html_content)
            
        return html_content
    except Exception as e:
        print(f"Error during Gemini analysis: {e}")
        return f"<p>Error during Gemini analysis: {e}</p>"
