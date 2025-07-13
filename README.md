# GitHub Webhook Listener with UI

This project implements a simple **Flask-based webhook listener** that receives GitHub webhook events like `push`, `pull_request`, and `merge_group`, stores them in **MongoDB**, and displays them through a minimal HTML UI.


##  Technologies Used

- Python
- Flask
- MongoDB 
- GitHub Webhooks
- HTML/CSS (UI)

##  Project Structure
webhook-repo/
├── app.py           # Flask app with webhook endpoint and UI
├── requirements.txt # Dependencies
├── templates/
│ └── index.html     # Web interface to display event logs
└── README.md

##  How to Run

1. Clone the repo:

git clone https://github.com/ishitagupta26/webhook-repo.git
cd webhook-repo

2. Create virtual environment and install dependencies:
   python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

3. Start MongoDB server (must be running on localhost:27017)

4.Run the Flask server:
python app.py

5. Visit http://127.0.0.1:5000 in your browser to view logs

## Demo Links
Action(trigger) Repo: [action-repo](https://github.com/ishitagupta26/action-repo)

Webhook Repo: [webhook-repo](https://github.com/ishitagupta26/webhook-repo)

Demo Video: [Watch here](https://drive.google.com/file/d/1pCkZo2WvHzBMWraYbpM1MXnrO4WscLZk/view?usp=sharing)

## Features
--Receives GitHub webhook events
--Captures push, PR, and merge_group activity
--Logs are saved to MongoDB
--Events displayed via web interface
