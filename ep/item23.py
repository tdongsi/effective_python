import subprocess
import time

# Typical subprocess call to call OS commands
proc = subprocess.Popen(
    ['echo', 'Hello World'],
    stdout=subprocess.PIPE
)
out, err = proc.communicate()
print(out.decode('utf-8'))

# Parallelism with subprocess
proc = subprocess.Popen(['sleep', '0.3'])
while proc.poll() is None:
    print('Working...')
    # Time consuming process
    time.sleep(0.2)

print('Exit status: %d' % proc.poll())

# Another example with parallelism
def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

start = time.time()
procs = []
for _ in range(10):
    proc = run_sleep(0.3)
    procs.append(proc)

for proc in procs:
    proc.communicate()

end = time.time()
print('Takes %f seconds' % (end - start))

# You can pipe data from Python program to subprocess
# In this way, you can call other programs to run in parallel with Python process.
# Run subprocesses on multiple CPUs.


