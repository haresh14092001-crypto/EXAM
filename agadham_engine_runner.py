import subprocess
import sys
import time

python_path = r"C:\Users\hares\.copilot\EXAM\.venv\Scripts\python.exe"
runner_script = "run_generation.py"

print("Starting Agadham Autonomous Generation Engine...")
start_time = time.time()
iterations = 0

while True:
    iterations += 1
    # Run run_generation.py
    res = subprocess.run([python_path, runner_script], capture_output=True, text=True)
    
    # Print its stdout
    print(res.stdout.strip())
    
    if res.returncode == 0:
        print(f"Generation Complete! Ran {iterations} batches in {time.time() - start_time:.2f} seconds.")
        break
    elif res.returncode == 2:
        # Continue to next batch
        pass
    else:
        print("ERROR occurred in generator script:")
        print(res.stderr)
        sys.exit(1)
