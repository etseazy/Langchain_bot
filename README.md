# Counseling Follow-Up Generator (LangChain + Gemini)

A beginner-friendly project that transforms career counseling session transcripts into warm, personalized follow-up emails — powered by **Google Gemini** and **LangChain**.

 Python CLI App | LangChain | Google Gemini API

---

## Project Purpose

Career counseling is most effective when students feel guided even after the session ends. This tool:

- Extracts a student's **career goals** and **recommended action items** from the counseling transcript.
- Crafts a friendly, professional **follow-up email** using those insights.
- Demonstrates practical use of **LLMs for student engagement** and support.

---

## How It Works

1. Paste the transcript of a conversation between a student and counselor.
2. The app uses **Gemini via LangChain** to:
   - Identify career goals.
   - Extract action items/advice.
3. Then, it generates a follow-up email for the student.
4. The email is displayed in the terminal (can be sent via email API later).

---

## Demo

**Input**:  
```

Counselor: What are you interested in?
Student: I want to explore psychology and become a counselor.
Counselor: That's great! You should look into internship programs and pursue a relevant degree.

```

**Output**:  
```

Extracting key takeaways...

Career Goals:

* Become a counselor
* Explore psychology field

Action Items:

* Look into internship programs
* Pursue a relevant degree

Follow-Up Email:
Hi Priya,

It was wonderful speaking with you today! I'm thrilled to hear about your interest in psychology and becoming a counselor...

```

---

## Tech Stack

- **Python** 3.10+
- **LangChain** (prompt chaining)
- **Google Gemini API** (Generative AI)
- **dotenv** (API key management)
- Simple **command-line interface**

---

## Folder Structure

```

counseling-followup-bot
┣ main.py              # Main app script
┣ prompts.py           # LangChain prompt templates
┣ .env                 # Your API key 
┣ README.md            # This file


````

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/counseling-followup-bot.git
cd counseling-followup-bot
````

### 2. Set up Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# OR
source .venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get Google Gemini API Key

1. Visit: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Copy your key and save it in `.env`:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

##  How to Run

```bash
python main.py
```

You'll be asked to:

* Enter the student’s name
* Paste the transcript
* Get the extracted takeaways and email draft

---

## Future Improvements

*  Replace mock email sender with actual email API (e.g., SMTP, SendGrid)
*  Create a web version using Streamlit or Flask
*  Add more context awareness to transcripts (multi-turn dialogues)

---
