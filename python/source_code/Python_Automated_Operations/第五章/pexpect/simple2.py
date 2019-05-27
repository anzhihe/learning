from __future__ import unicode_literals

import pexpect
import sys

child = pexpect.spawnu('ftp ftp.openbsd.org')
child.expect('(?i)name .*: ')
child.sendline('anonymous')
child.expect('(?i)password')
child.sendline('pexpect@sourceforge.net')
child.expect('ftp> ')
child.sendline('bin')
child.expect('ftp> ')
child.sendline('get robots.txt')
child.expect('ftp> ')
sys.stdout.write (child.before)
print("Escape character is '^]'.\n")
sys.stdout.write (child.after)
sys.stdout.flush()
child.interact() # Escape character defaults to ^]
child.sendline('bye')
child.close()
