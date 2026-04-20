# 🎯 VisionMeet – AI Smart Meeting Assistant

VisionMeet is a real-time AI-powered meeting assistant that combines **video conferencing, live transcription, and intelligent Q&A** using **Stream Video SDK** and **Gemini AI**.

It enables users to conduct meetings while automatically generating transcripts and interacting with an AI assistant during the session.

---

# 🚀 Features

## 🎥 Real-time Video Meetings

* Powered by Stream Video SDK
* Users can join and interact in live meetings
* Camera and microphone support

## 📝 Live Transcription

* Automatic speech-to-text conversion
* Displays real-time transcripts in the UI
* Speaker-wise transcript tracking

## 🤖 AI Assistant (Gemini)

* Triggered using **"Hey Assistant"**
* Answers questions based on meeting context
* Provides intelligent responses using transcript data

## 💬 Chat Integration

* Real-time messaging using Stream Chat
* Used for backend communication and event handling

## 🔄 Seamless Frontend-Backend Integration

* Next.js frontend
* Node.js API routes
* Python backend using Vision Agents

---

# 🏗️ Project Structure

```
VisionMeet/
│
├── backend/                # Python backend (Vision Agents + Gemini)
│   ├── main.py            # Core AI agent logic
│   ├── pyproject.toml     # Dependencies (uv/pip)
│   ├── uv.lock            # Dependency lock file
│   ├── .env               # Backend environment variables
│
├── visionmeet/            # Next.js frontend
│   ├── app/
│   │   ├── api/token/
│   │   │   └── route.js   # Generates Stream user token
│   │   │
│   │   ├── components/
│   │   │   ├── meeting-room.jsx   # Main video UI
│   │   │   ├── stream-provider.jsx # Stream client setup
│   │   │   └── transcript.jsx     # Live transcript panel
│   │   │
│   │   ├── hooks/
│   │   │   └── use-stream-clients.js # Handles Stream clients
│   │   │
│   │   ├── meeting/       # Meeting routes/pages
│   │   ├── layout.js
│   │   └── page.js
│
├── public/                # Static assets
├── .env                   # Frontend environment variables
├── package.json           # Frontend dependencies
└── README.md
```

---

# ⚙️ Tech Stack

### Frontend

* Next.js (React)
* Tailwind CSS
* Stream Video React SDK
* Stream Chat React

### Backend

* Python
* Vision Agents SDK
* Gemini AI (Google)
* Stream Video API

---

# 🔑 Environment Variables

## 📌 Frontend (.env)

```
NEXT_PUBLIC_STREAM_API_KEY=your_stream_api_key
```

---

## 📌 Backend (.env)

```
STREAM_API_KEY=your_stream_api_key
STREAM_API_SECRET=your_stream_secret
GEMINI_API_KEY=your_gemini_api_key
```

---

# 🧠 How It Works

1. User opens the web app
2. Connects via Stream Video
3. Backend AI agent joins the meeting
4. Speech is converted to text in real-time
5. Transcript is displayed in UI
6. When user says:

   ```
   "Hey Assistant"
   ```

   → AI processes the transcript
   → Generates a contextual response

---

# ▶️ Setup Instructions

## 🔥 1. Clone the Repository

```
git clone https://github.com/your-username/VisionMeet.git
cd VisionMeet
```

---

## 🔥 2. Setup Frontend

```
cd visionmeet
npm install
npm run dev
```

---

## 🔥 3. Setup Backend

```
cd backend
python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

---

# 🧪 Usage

1. Start frontend and backend
2. Open the app in browser
3. Join a meeting
4. Speak → see live transcript
5. Say:

   ```
   Hey Assistant, summarize the meeting
   ```
6. AI responds based on transcript

---

# ⚠️ Important Notes

* Do NOT commit `.env` files (security risk)
* Ensure Stream and Gemini APIs are properly configured
* Backend must be running for AI features to work

---

# 🚀 Future Enhancements

* AI meeting summary panel
* Action item extraction
* Meeting recording & playback
* User authentication
* Multi-language transcription

---

# 👨‍💻 Author

**Atharva Phanse**

---

# ⭐ Conclusion

VisionMeet demonstrates the integration of **real-time communication + AI intelligence**, making meetings smarter, interactive, and more productive.

---
