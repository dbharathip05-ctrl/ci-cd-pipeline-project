# CI/CD Pipeline Project

This project is an end-to-end **CI/CD demo** using Python, Docker, and GitHub Actions.

## Structure

- `app.py` → Python Flask app  
- `requirements.txt` → Python dependencies  
- `tests/` → Contains unit tests  
- `Dockerfile` → Builds Docker image  
- `.gitignore` → Ignores unnecessary files  
- `README.md` → Project information  

## How to run locally

1. Install Python 3.11  
2. Install dependencies: `pip install -r requirements.txt`  
3. Run the app: `python app.py`  
4. Open browser: [http://localhost:5000](http://localhost:5000)

## How CI/CD works

- GitHub Actions runs tests automatically on every push  
- Builds Docker image if tests pass