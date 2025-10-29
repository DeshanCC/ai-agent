import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    # add gurad to prevent LLM going other directories
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    
    try:
        final_args = ["python3", file_path]
        final_args.extend(args)
        output = subprocess.run(final_args, cwd=abs_working_dir, timeout=30, capture_output=True)
        final_str = f"""
        STDOUT: {output.stdout.decode("utf-8")}
        STDERR: {output.stderr.decode("utf-8")}
        """
        if output.stdout == "" and output.stderr == "":
            final_str = "No output produced. \n"
        if output.returncode != 0:
            final_str += f"Process exited with code: {output.returncode}"
        return final_str
    except Exception as e:
        return f"Error: executing Python file: {e}"
                