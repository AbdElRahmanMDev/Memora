
---

# 🧠 Memora – Alzheimer's Virtual Assistant

## 📝 Project Overview

**Memora** is an intelligent mobile assistant designed to support individuals living with moderate Alzheimer’s disease. This innovative application integrates **face recognition**, **speech recognition**, and **task scheduling** to enhance memory retention and communication for patients, while also empowering caregivers with tools to manage and support daily routines.

This project was developed as part of our graduation thesis, addressing the growing need for accessible, affordable, and user-friendly digital solutions for dementia care.

---

## 🎯 Objectives

- 📱 Build a cross-platform mobile application tailored for Alzheimer’s patients.
- 🧬 Integrate machine learning-based **face recognition** for identifying individuals in the patient’s environment.
- 🗣 Enable **speech recognition** and **natural language processing** to transcribe and summarize conversations.
- 📅 Implement personalized task scheduling and reminder systems.
- 🔐 Ensure secure authentication for patients and caregivers.
- 🔁 Establish scalable backend services using Django REST Framework and MySQL.

---

## 🔧 Technologies Used

| Layer           | Stack / Tool                            |
|----------------|------------------------------------------|
| **Frontend**    | Flutter                                  |
| **Backend**     | Django, Django REST Framework            |
| **Database**    | MySQL                                    |
| **ML Models**   | Face Recognition (OpenCV), BART for NLP |
| **Authentication** | JWT-based Authentication            |
| **Cloud Storage** | Local file system / Firebase (optional) |

---

## 🚀 Core Features

### 👥 Face Recognition  
Patients can recognize and recall people by simply capturing their photos. The app matches the image with known individuals stored in the database.

### 🧏‍♂️ Speech Recognition & Summarization  
Conversations are transcribed into text and automatically summarized using NLP. This allows patients to revisit key points from recent interactions.

### 📅 Daily Scheduling & Task Reminders  
Caregivers can organize daily activities, appointments, and medication schedules to reduce confusion and improve routine adherence.

### 🔒 Role-Based Access  
- **Caregivers** manage patient profiles, conversations, and schedules.  
- **Patients** access their daily tasks, recognized individuals, and summarized conversations.

---

## 🛠️ API Highlights

The backend exposes a suite of RESTful APIs including:

### 🗂️ Face & Speaker Recognition
- `facedect`: Detect and identify known individuals.
- `Encoding`: Encode and store facial data.
- `SpeakerImageView`: Add or retrieve speaker image data.

### 🔊 Audio Processing
- `ConversationAudioUploadView`: Upload, transcribe, and summarize patient conversations.
- `summarize`: Generate conversation summaries using NLP models.
- `check_audio_exists`: Check if patient audio is already uploaded.

### 🧑‍⚕️ Patient & Caregiver Management
- `GetPatientByEmail` / `GetCaregiverByEmail`: Fetch ID using email.
- `Loginpatient` / `Logincaregiver`: Auth endpoints.
- `CaregiverListCreateView`: CRUD operations for caregivers and patients.

### 📓 Conversation History
- `LastConversationView` / `last_conversation_api`: Retrieve recent dialogue and summaries.

Each endpoint adheres to REST conventions, with proper error handling, validation, and JSON responses.



## 📁 Project Structure (Simplified)

```
memora/
├── backend/
│   ├── models/
│   ├── views/
│   ├── serializers/
│   ├── api/ (face & audio recognition)
│   └── urls.py
├── frontend/
│   └── flutter/ (mobile UI)
└── docs/
    └── research_paper.pdf
```

---

## 📚 Research Basis

This project is grounded in real-world research on Alzheimer’s care. The solution aligns with key findings from literature reviews highlighting:

- The importance of routine reinforcement in memory care.
- The role of visual and auditory triggers in memory recall.
- The accessibility gaps in current Alzheimer’s assistive tools.

The app has been tested for usability, with a focus on elderly-friendly UI design and minimal cognitive load.

---



## 🧪 How to Run the Project

### Backend (Django):
```bash
git clone https://github.com/yourusername/memora.git
cd memora/backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


---
