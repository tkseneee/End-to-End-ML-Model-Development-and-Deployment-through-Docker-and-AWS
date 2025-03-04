🚀 Loan Rejection Probability Prediction - End-to-End-ML-Model-Development-and-Deployment-through-Docker-and-AWS

This project demonstrates the end-to-end development and deployment of a Loan Rejection Probability Prediction Model using Flask, Docker, and AWS EC2. The application includes a web-based frontend, a Flask API backend, and a machine learning model pipeline for making predictions.

--------------------------------------------------------------------------------
Project Overview
--------------------------------------------------------------------------------
✅ Developed a full ML pipeline (data preprocessing + model training)
✅ Built a lightweight Flask app to serve predictions
✅ Created a simple HTML frontend for user input
✅ Containerized the app using Docker (optimized image ~500MB)
✅ Deployed on AWS EC2 (Ubuntu 22.04, Dockerized)
✅ Ensured scalability for future improvements

--------------------------------------------------------------------------------
Tech Stack
--------------------------------------------------------------------------------
- Machine Learning: Scikit-learn (model saved as a .pkl file)
- Backend: Flask API
- Frontend: HTML
- Containerization: Docker
- Cloud Deployment: AWS EC2

--------------------------------------------------------------------------------
Project Structure
--------------------------------------------------------------------------------
loan-rejection-prediction/
├── static/              # CSS & images for frontend
├── templates/           # HTML templates for frontend
├── model/               # Trained ML model (Pickle file)
├── app.py               # Flask API for predictions
├── Dockerfile           # Docker configuration
├── requirements.txt     # Dependencies
└── README.txt           # Project documentation (this file)

--------------------------------------------------------------------------------
How to Run Locally
--------------------------------------------------------------------------------
1. Clone the repository:
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Create a virtual environment (optional, but recommended):
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate    # For Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Run the Flask application:
   python app.py

Now, open http://127.0.0.1:5000/ in your browser.

--------------------------------------------------------------------------------
Running with Docker
--------------------------------------------------------------------------------
1. Build the Docker image:
   docker build -t loan-app .

2. Run the container:
   docker run -p 5000:5000 loan-app

Access the app at http://127.0.0.1:5000/

--------------------------------------------------------------------------------
Deployment on AWS EC2
--------------------------------------------------------------------------------
1. Launch an EC2 instance (Ubuntu 22.04, t2.micro, Free Tier).
2. Install Docker on EC2:
   sudo apt update && sudo apt install -y docker.io
3. Transfer the Docker image to EC2:
   scp -i your-key.pem loan-app.tar ubuntu@your-ec2-ip:~
4. On EC2, load the image and run the container:
   sudo docker load -i loan-app.tar
   sudo docker run -d -p 5000:5000 loan-app

Now, visit http://your-ec2-public-ip:5000/ in your browser.

--------------------------------------------------------------------------------
Screenshots
--------------------------------------------------------------------------------
- Web Frontend: A user-friendly interface for entering loan details.
- Flask API: Backend processes user inputs and returns predictions.
- AWS EC2 Deployment: Hosted securely on the cloud.

(Insert screenshots here if available)

--------------------------------------------------------------------------------
Future Enhancements
--------------------------------------------------------------------------------
- Enhance the ML model using more advanced techniques.
- Add authentication for secure access.
- Integrate a database to store user predictions.

--------------------------------------------------------------------------------
Author
--------------------------------------------------------------------------------
Dr T.K.Senthil Kumar
Email: tkseneee@gmail.com
LinkedIn: www.linkedin.com/in/drtksenthil

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
If you found this project useful, please ⭐ the repo!
