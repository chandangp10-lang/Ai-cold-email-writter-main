# ✉️ AI Cold Email Writer

An AI-powered web app that generates personalized job emails instantly — built with **Python**, **Streamlit**, and **Groq LLaMA API**.


## 🎯 Features
- **3 Email Types** — Job Application, Cold Outreach, Post-Interview Follow-Up
- **3 Tone Options** — Formal, Friendly, Bold
- **Instant Generation** — powered by LLaMA 3.3 70B via Groq API
- **Copy Ready** — copy your email with one click
- **Beautiful UI** — dark green theme built with Streamlit

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ai-cold-email-writer.git
cd ai-cold-email-writer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your free Groq API key
- Go to 👉 [console.groq.com](https://console.groq.com)
- Sign up free → API Keys → Create Key

### 4. Create a `deep.env` file
```
GROQ_API_KEY=your-groq-key-here
```

### 5. Run the app
```bash
streamlit run app.py
```

Opens at `http://localhost:8501` 🎉

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Web UI framework |
| Groq API | AI inference engine |
| LLaMA 3.3 70B | Language model |
| python-dotenv | Environment variables |

---

## 💡 How It Works
1. User fills in their details (name, role, company, resume summary)
2. App builds a structured prompt based on email type and tone
3. Prompt is sent to Groq's LLaMA 3.3 70B model
4. AI returns a JSON response with subject + body
5. App displays the email in a clean, copy-ready format

---

## 🎓 What I Learned Building This
- Calling LLM APIs with structured prompts
- Parsing JSON responses from AI models
- Building interactive web UIs with Streamlit
- Debugging real-world API errors (403, 404, 429, 400!)
- Prompt engineering for consistent structured outputs
- Working with environment variables securely

---

## 🔮 Future Improvements
- [ ] Deploy on Streamlit Cloud (live link)
- [ ] Save email history
- [ ] LinkedIn message generator
- [ ] One-click Gmail integration

---

## 👩‍💻 Built by
**Chandan** — CS fresher exploring Generative AI 🌱

Connect with me on [LinkedIn](https://linkedin.com)
