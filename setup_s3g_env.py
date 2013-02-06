import os
import sys
import subprocess

python_exe = sys.executable
try:
  dist_eggs = sys.argv[2]
  mb_eggs = sys.argv[3]
  env_dir = sys.argv[4]
except IndexError as ie:
  print 'Expected location of dist_eggs, makerbot_eggs, and the virtualenv_dir'
  print ie
  sys.exit(1)
  
virtualenv_command = [
  python_exe,
  'virtualenv.py',
  '--extra-search-dir=' + dist_eggs,
  '--never-download',
  env_dir
]
try:
  subprocess.Popen(virtualenv_command, stdout=subprocess.PIPE)
except:
  print 'something went wrong calling virtualenv'
  sys.exit(2)


if 'win32' == sys.platform:
  virtualenv_easy_install = os.path.join(env_dir, 'Scripts', 'easy_install.exe')
else:
  print "I didn't expect this to be used on anything but windows, sorry."
  sys.exit(3)
  
e_install = [virtualenv_easy_install, '-q']
eggs = [
  os.path.join(dist_eggs, 'mock-1.0.1-py2.7.egg'),
  os.path.join(dist_eggs, 'lockfile-0.9.1-py2.7.egg'),
  os.path.join(dist_eggs, 'argparse-1.2.1-py2.7.egg'),
  os.path.join(dist_eggs, 'unittest2-0.5.1-py2.7.egg'),
  os.path.join(mb_eggs, 'pyserial-2.7_mb2.1-py2.7.egg')
]
s3g_egg = os.path.join(mb_eggs, 'makerbot_driver-0.1.1-py2.7.egg')
if os.path.exists(s3g_egg):
  eggs.append(s3g_egg)
  
try:
  for egg in eggs:
    subprocess.Popen(e_install + [egg], stdout=subprocess.PIPE)
except:
  print 'something went wrong installing the eggs'
  sys.exit(4)
  

  