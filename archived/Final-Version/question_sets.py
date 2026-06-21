
def generate_ask():

    def read_file_content(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def prepare_question_set():
        question_set = {
            "Summary": {
                "Observations Comparison": [
                    "What were the key metrics before and during the chaos experiment?",
                    "How did response time, latency, error rates, and query time change during the experiment?",
                    "Were there any exceptions or errors encountered during the chaos?"
                ]
            },
            "Recommendations": {
                "Performance Improvements": [
                    "How can we optimize response time and latency given the observed increases during the chaos?",
                    "What strategies can be employed to reduce error rates or handle faulty responses more effectively?",
                    "Are there specific areas, such as query optimization or error handling, that need immediate attention?"
                ]
            },
            "GenAI's Insights": {
                "Pattern Analysis": [
                    "What patterns or trends do the collected metrics exhibit during the chaos experiment?",
                    "Are there correlations between specific chaos types (e.g., latency injection, faulty responses) and the observed changes in metrics?"
                ],
                "Root Cause Analysis": [
                    "Can GenAI identify potential root causes for the observed increase in response time, latency, and exceptions during chaos?",
                    "Are there specific patterns or anomalies in the chaos-induced metrics that highlight underlying issues?"
                ],
                "Chaos Impact Assessment": [
                    "What is the impact of injected chaos on the API's performance and reliability?",
                    "How do the observed exceptions align with the types of chaos injected, and what implications do they have on system behavior?"
                ],
                "Recommendation Prioritization": [
                    "Which recommendations or areas of improvement should be prioritized based on the severity of observed changes and their potential impact on the system?"
                ]
            }
        }

        return question_set

    def main():
        files = [
            "api_info.txt",
            "exceptions_occured_during_chaos.json",
            "metrics_after_chaos.json",
            "metrics_during_chaos.json",
            "metrics_before_chaos.json"
        ]

        file_contents = {file: read_file_content(file) for file in files}

        question_set = prepare_question_set()

        output_text = "I have executed one chaos experiment. Below are the details. Please provide insights on the experiments with the answers for the questions added below. Write your insights professionally in a markdown format." + "\n\n\n" + "CHAOS EXPERIMENT DETAILS" + "\n" + str("="*50) + '\n'
        for file, content in file_contents.items():
            output_text += f"File: {file}\n\n{content}\n\n" + "=" * 50 + "\n\n"

        output_text += "Generated Questions for GenAI:\n\n"
        for category, subcategories in question_set.items():
            output_text += f"{category}:\n"
            for subcategory, questions in subcategories.items():
                output_text += f"{subcategory}:\n"
                for question in questions:
                    output_text += f"- {question}\n"
                output_text += "\n"

        with open('genai_questions.txt', 'w') as output_file:
            output_file.write(output_text)

    main()
