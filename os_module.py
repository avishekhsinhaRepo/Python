import os

# Get the current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Change the current working directory
os.chdir('/path/to/new/directory')

# List files and directories in the current directory
files = os.listdir('.')
print(f"Files and directories in the current directory: {files}")

# Create a new directory
os.mkdir('new_directory')

# Check if a file exists
file_path = 'path/to/file.txt'
if os.path.exists(file_path):
    print(f"File '{file_path}' exists.")
else:
    print(f"File '{file_path}' does not exist.")

# Get the value of an environment variable
home_dir = os.getenv('HOME')
print(f"Home directory: {home_dir}")

# Execute a command in the system shell
os.system('ls -l')