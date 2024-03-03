import subprocess

# Define the paths to your Python scripts
script1_path = "main.py"
script2_path = "the_face.py"

# Run the scripts concurrently
process1 = subprocess.Popen(["python", script1_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process2 = subprocess.Popen(["python", script2_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for either process to finish
while True:
    if process1.poll() is not None:
        print("Script 1 finished first")
        process2.terminate()
        break
    elif process2.poll() is not None:
        print("Script 2 finished first")
        process1.terminate()
        break
