import psutil

# Function to close a specific software/process
def create_process_name(order):
    length=len(order)
    process_name=""
    for string in order:
        process_name=process_name+string.lower()
        length=length-1
        if length==0:
            process_name=process_name+".exe"
        else :
            process_name=process_name+" "
    return process_name


def close(order):
    # Iterate over all running processes
    process_name=create_process_name(order)
    for proc in psutil.process_iter():
        try:
            # Check if the process name matches
           
            if proc.name().lower() == process_name:
                # Terminate the process

                proc.terminate()
                print(f"{process_name} has been terminated.")
        except psutil.AccessDenied:
            print(f"No permission to terminate {process_name}.")
        except psutil.NoSuchProcess:
            print(f"{process_name} is not running.")


