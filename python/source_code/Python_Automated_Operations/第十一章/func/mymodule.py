#
# Copyright 2014
# liutiansi <liutiansi@gmail.com>
#
# This software may be freely redistributed under the terms of the GNU
# general public license.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import func_module


class Mymodule(func_module.FuncModule):

    # Update these if need be.
    version = "0.0.1"
    api_version = "0.0.1"
    description = "My module for func."

    def echo(self,vcount):
        """
        TODO: Document me ...
        """
        command="/usr/bin/tail -n "+str(vcount)+" /var/log/messages"
        cmdref = sub_process.Popen(command, stdout=sub_process.PIPE,
                                   stderr=sub_process.PIPE, shell=True,
                                   close_fds=True)
        data = cmdref.communicate()
        return (cmdref.returncode, data[0], data[1])
