# Simple Phishing Detection using LLM

This is a Streamlit app for simple phishing detection using LLM and Ollama.

## Setup Instructions

Follow these steps to run the project:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/simple-phishing-detection-using-llm.git
    cd simple-phishing-detection-using-llm
    ```

2. **Ensure Ollama is installed:**
    Install Ollama and run the model you want to use! This repo is using `llama3.1`
    ```sh
    ollama run llama3.1
    ```

3. **Install dependencies using `uv`:**
    ```sh
    uv sync
    ```

4. **Run the Streamlit app:**
    ```sh
    streamlit run main.py
    ```

## Usage

1. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
2. Type a message in the input box to evaluate if it is a phishing attempt.
3. The app will display the evaluation result including whether it is phishing, the confidence level, and an explanation.

Enjoy using the app for phishing detection!

