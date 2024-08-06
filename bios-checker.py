import subprocess

# Set locale to US English so output matches the expected strings
env = {"LC_ALL": "en_US.utf8"}

# Function to run a command with pkexec
def run_with_pkexec(cmd):
    return subprocess.check_output(['pkexec', 'sh', '-c', cmd], env=env)

# Run the commands and store their output in variables
bios_info = run_with_pkexec("dmidecode | grep -A20 'Vendor:'")
cpu_info = subprocess.check_output("lshw -C cpu", shell=True, env=env)
kernel_version = subprocess.check_output("uname -r", shell=True, env=env)

# Print result
print("BIOS Information:\n{}\nCPU Information:\n{}\nKernel Version: {}".format(bios_info.decode(), cpu_info.decode(), kernel_version.decode()))
