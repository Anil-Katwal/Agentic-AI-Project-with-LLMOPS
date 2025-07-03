import subprocess
import time

def run_backend():
    return subprocess.Popen(["uvicorn", "main:app", "--reload", "--port", "8000"])

def run_frontend():
    return subprocess.Popen(["streamlit", "run", "streamlit_app.py"])

if __name__ == "__main__":
    backend_process = run_backend()
    print("Started FastAPI backend... waiting 3 seconds for it to be ready.")
    time.sleep(3)  # wait for backend startup

    frontend_process = run_frontend()
    print("Started Streamlit frontend.")

    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("Shutting down both apps...")
        backend_process.terminate()
        frontend_process.terminate()
