import salt.minion
import salt.client

def get_file(path, dest, env='base'):
    '''
    Used to get a single file from the Salt master

    CLI Example:
    salt '*' cp.get_file salt://vimrc /etc/vimrc
    '''
    # Create the FileClient object
    opts = salt.client.LocalClient().opts
    client = salt.minion.FileClient(opts)
    # Call get_file
    return client.get_file(path, dest, False, env)

get_file('salt://nginx/nginx.conf','/tmp/nginx.conf')
