import psutil
from text_to_sound import text_to_speech
from color import write_color

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
    stoped=False
    process_name=create_process_name(order)
    for proc in psutil.process_iter():
        try:
            # Check if the process name matches
           
            if proc.name().lower() == process_name:
                # Terminate the process

                proc.terminate()
                stoped=True

        except psutil.AccessDenied:
            text_to_speech(f"No permission to terminate {process_name}.")
        except psutil.NoSuchProcess:
            write_color("0,255,0")
            text_to_speech(f"{process_name} is not running.")
            write_color("200,0,0")
    if stoped:
        write_color("0,255,0")
        text_to_speech(f"{process_name} has been terminated.")
        write_color("200,0,0")
    else:
        write_color("0,255,0")
        text_to_speech(f"i couldn't find {process_name} .")
        write_color("200,0,0")



