import subprocess
import time
import os

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
# Run sub-processes on multiple CPUs.


def run_openssl(data):
    """A computing-intensive method, best for running separately on separate CPUs."""
    env = os.environ.copy()
    env['password'] = b'asdf'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc


def run_md5(input_stdin):
    proc = subprocess.Popen(
        ['md5'],
        stdin=input_stdin,
        stdout=subprocess.PIPE
    )
    return proc

input_procs = []
for _ in range(5):
    data = os.urandom(100)
    proc = run_openssl(data)
    input_procs.append(proc)

hash_procs = []
for proc in input_procs:
    # input of hash subprocess is output of openssl subprocess
    hash_proc = run_md5(proc.stdout)
    hash_procs.append(hash_proc)

for proc in input_procs:
    proc.communicate()

for proc in hash_procs:
    out, _ = proc.communicate()
    print(out)


