
# Answer Evaluation Engine (v1)
See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

## Overview

The Answer Evaluation Engine is an AI-powered backend service designed to automatically evaluate candidate answers for technical interview and assessment questions.

The system uses a hybrid evaluation approach that combines rule-based validation and Large Language Models (LLMs) to assess answer relevance, correctness, and completeness. It generates a score, feedback, and confidence value for each response.

The engine currently supports three technical domains:

* Data Structures and Algorithms (DSA)
* Database Management Systems (DBMS)
* Operating Systems (OS)

---

## Features

* Automated answer evaluation
* Relevance detection
* Correctness assessment
* Score generation (0–10)
* Confidence estimation
* Constructive feedback generation
* Domain detection (DSA, DBMS, OS)
* FastAPI REST API
* Rule-based fallback mechanism
* Unit and integration testing

---

## Project Architecture

Question + Answer

↓
Input Validation

↓
Domain Detection

↓
Rule-Based Relevance Check

↓
LLM Evaluation (Gemini/OpenAI)

↓
Score Calculation

↓
Feedback Generation

↓
JSON Response

---

## Tech Stack

### Backend

* Python 3.13
* FastAPI
* Pydantic
* Uvicorn

### AI & NLP

* Google Gemini API
* OpenAI API
* google-generativeai
* sentence-transformers

### Testing

* pytest
* FastAPI TestClient
* unittest.mock

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd answer-evaluation-engine
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key

PRIMARY_PROVIDER=gemini
GEMINI_MODEL=gemini-2.5-flash
OPENAI_MODEL=gpt-4o-mini
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

**GET**

```http
/health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Evaluate Answer

**POST**

```http
/evaluate
```

Request Body:

```json
{
  "question": "What is a Primary Key?",
  "answer": "A primary key uniquely identifies each row in a table."
}
```

Response:

```json
{
  "score": 8.5,
  "feedback": "The answer correctly defines a primary key and explains its purpose.",
  "confidence": 0.90
}
```

---

## Testing

Run all tests:

```bash
pytest
```

Expected Result:

```text
11 passed in 0.69s
```

---

## Edge Cases Handled

### Empty Answer

Input:

```json
{
  "question": "What is DBMS?",
  "answer": ""
}
```

Output:

```json
{
  "score": 0,
  "feedback": "No answer provided.",
  "confidence": 1.0
}
```

### Irrelevant Answer

Input:

```json
{
  "question": "What is DBMS?",
  "answer": "I like playing cricket."
}
```

Output:

```json
{
  "score": 0,
  "feedback": "Answer is irrelevant.",
  "confidence": 1.0
}
```

---

## Supported Domains

### DSA

Topics include:

* Arrays
* Linked Lists
* Stacks
* Queues
* Trees
* Graphs
* Searching
* Sorting

### DBMS

Topics include:

* SQL
* Normalization
* Joins
* Indexing
* ACID Properties
* Transactions

 Operating Systems

Topics include:

* Processes
* Threads
* Scheduling
* Memory Management
* Deadlocks
* Virtual Memory

---

 Project Structure

```text
answer-evaluation-engine/
│
├── app/
│   ├── main.py
│   ├── evaluator.py
│   ├── schemas.py
│   ├── config.py
│   └── llm.py
│
├── tests/
│   ├── test_evaluator.py
│   └── test_api.py
│
├── requirements.txt
├── .env.example
├── README.md
└── LICENSE
```

---

 Future Improvements

* Support additional technical domains
* Multi-language answer evaluation
* Advanced semantic similarity scoring
* Answer plagiarism detection
* Detailed strengths and weaknesses analysis
* Dashboard for evaluation analytics

---

 Author

Jaya Singh Rajput

Intern Project – Answer Evaluation Engine (v1)

Phase 3 – Core Engine Development



See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.
