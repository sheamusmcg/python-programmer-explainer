# Python Programmer Explainer

An interactive Streamlit app that teaches beginner Python programming through guided explanation, runnable examples, short practice prompts, validation checks, and Google Colab deep-dive notebooks.

The app follows the same explainer pattern as the other projects in this folder: plain-English concepts first, hands-on interaction second, and deeper notebook work when the learner is ready.

## Lessons

1. Introduction: variables, printing, and types
2. Operators: arithmetic, comparisons, and logic
3. Control Structures: if statements and loops
4. Data Structures: lists, dictionaries, tuples, and sets
5. Functions: parameters, return values, and reuse
6. Modules and Libraries: imports and standard-library tools
7. Objects and Classes: attributes and methods
8. Try / Except: handling errors gracefully
9. Pythonic Code: comprehensions and readable idioms
10. JSON, APIs, and Environments: structured data and configuration

## Learning Flow

Each lesson includes:

- A beginner-friendly concept explanation
- A mental model
- A runnable example
- A line-by-line walkthrough
- A code editor practice challenge
- Hints
- A sample solution
- A Google Colab deep-dive notebook link
- Progress tracking after the challenge passes

## Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the local Streamlit URL and advance through the ten lessons.

## Notes

The in-app code runner is designed for beginner exercises. It uses a restricted execution environment with a small allowlist of built-ins and standard modules. The Colab notebooks are the right place for longer experiments and open-ended coding.
