# 🌤️ Weather Agent Tool

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python)
![Agentic AI](https://img.shields.io/badge/Agentic-AI-green?style=for-the-badge)
![Function Calling](https://img.shields.io/badge/Function-Calling-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Learning-success?style=for-the-badge)

**A beginner-friendly Agentic AI project demonstrating Tool Calling using the Schema → Function → Executor pattern.**

</div>

---

## 📌 Overview

Large Language Models (LLMs) cannot directly interact with APIs, databases, or external services.

This project demonstrates how an AI Agent can use tools through a simple three-step architecture:

```text
User Question
      │
      ▼
Schema (What the LLM Sees)
      │
      ▼
Function (Python Implementation)
      │
      ▼
Executor (Runs the Tool)
      │
      ▼
Tool Response
      │
      ▼
Final Answer
```

---

## ✨ Features

* ✅ Weather Tool Schema
* ✅ Simulated Weather Database
* ✅ OpenWeatherMap API Integration
* ✅ Tool Registry
* ✅ Function Executor
* ✅ LLM Tool Call Simulation
* ✅ JSON Formatted Responses
* ✅ Beginner Friendly Code
* ✅ Easy to Extend with More Tools

---

## 📂 Project Structure

```text
weather-agent-tool/
│
├── main.py
├── weather_schema.py
├── weather_tool.py
├── executor.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠 Technologies Used

* Python
* Requests
* JSON
* OpenWeatherMap API
* Agentic AI Concepts
* Function Calling
* Tool Execution Pattern

---

## 🧠 Understanding the Architecture

### 1️⃣ Schema

The schema describes the tool.

It tells the language model:

* When to use the tool
* What arguments to provide

Example:

```python
weather_tool_schema = {
    "name": "get_current_weather",
    ...
}
```

---

### 2️⃣ Function

The actual Python code.

Example:

```python
get_current_weather(
    city="Mumbai",
    unit="celsius"
)
```

---

### 3️⃣ Executor

Acts as a bridge between the model's decision and Python execution.

Example:

```python
execute_tool_call(
    tool_name,
    tool_args,
    tool_registry
)
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Ronit049/weather-agent-tool.git

cd weather-agent-tool
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## 📸 Sample Output

```text
SCHEMA (what LLM sees):

Name        : get_current_weather

Description : Get the current weather for a given city...

Parameters  : ['city', 'unit']


FUNCTION

Direct call:

{
    "city": "Jaipur",
    "temperature": 41,
    "unit": "celsius",
    "condition": "Sunny",
    "humidity": 22
}


EXECUTOR

LLM decided:

call get_current_weather(city='Mumbai')


Executor ran it →

{
  "city": "Mumbai",
  "temperature": 31,
  "unit": "celsius",
  "condition": "Humid and Cloudy",
  "humidity": 85
}
```

---

## 🎯 Future Improvements

* [ ] Gemini Function Calling
* [ ] Forecast Support
* [ ] Command Line Interface
* [ ] Multi Tool Agent
* [ ] Calculator Tool
* [ ] Currency Converter Tool
* [ ] Web Search Tool
* [ ] Memory Support

---

## 🌟 Inspirational Quote

> "The people who are crazy enough to think they can change the world are the ones who do."
>
> — Steve Jobs

---

## 👨‍💻 Author

### Ronit Raj

Computer Science Student (CSE'28)

Arya College of Engineering, Jaipur

GitHub: https://github.com/Ronit049

LinkedIn: https://www.linkedin.com/in/your-linkedin-profile/

Email: [ronitraj049@gmail.com](mailto:ronitraj049@gmail.com)

---

## 🙌 Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

### ⭐ Thanks Button

```text
⭐ Star this repository
🍴 Fork it
🛠 Contribute
📢 Share it with others
```

---

## 📜 License

This project is created for educational and learning purposes.

Feel free to use, modify, and improve it.

---

<div align="center">

### Thanks for visiting ❤️

**Happy Coding and Keep Building Amazing Things! 🚀**

</div>
