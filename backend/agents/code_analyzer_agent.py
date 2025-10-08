import os
import openai

def analyze_code_diff(pr_data):
    # Extract code diff from PR data
    code_diff = pr_data.get("diff", "")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Analyze the following code diff for quality and flag any redundant or low-quality code. Provide explanations for flagged lines.\n\n{code_diff}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    analysis_text = response.choices[0].message["content"]
    # Simple parsing: if 'flagged' keyword appears, set flagged True
    flagged = "flagged" in analysis_text.lower()
    return {"flagged": flagged, "details": analysis_text}

def get_pr_data(pr_url):
    # Placeholder: Fetch PR data from GitHub API
    return {}

def main():
    pr_url = os.getenv("PR_URL")
    pr_data = get_pr_data(pr_url)
    analysis_result = analyze_code_diff(pr_data)
    print(analysis_result)

if __name__ == "__main__":
    main()