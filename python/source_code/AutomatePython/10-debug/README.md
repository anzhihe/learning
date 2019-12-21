# raise
<pre>raise Exception(msg)</pre>

# try...except...as...
<pre>try:
    code block
except Exception as err:
    error handling</pre>

# traceback.format_exc()
* convert traceback stack info to be a string

# assert condition, message
* Python -O option will disable assertions

# logging module
<pre>
import logging
logging.disable（logging.CRITICAL）
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, 
                    format='(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
</pre>
