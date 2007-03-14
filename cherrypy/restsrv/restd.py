"""The restsrv daemon."""

import getopt
import sys

from cherrypy import restsrv


class _Optionset(object):
    host = '0.0.0.0'
    port = 80
    protocol = 'HTTP/1.1'
    scheme = 'http'
options = _Optionset()

shortopts = []
longopts = [
    # someday: 'cover', 'profile', 'validate', 'conquer',
    'host=', 'port=', '1.0', 'ssl',
    'project=', 'help',
    ]


def help():
    """Print help for restd command-line options."""
    
    print """
restd. Start the restsrv daemon.

Usage:
    restd [options]

Options:
  --host=<name or IP addr>: use a host other than the default (%s).
  --port=<int>: use a port other than the default (%s)
  --1.0: use HTTP/1.0 servers instead of default HTTP/1.1
  --ssl: use HTTPS instead of default HTTP
  --project=<module name>: import a module to set up the project
  --help: print this usage message and exit
""" % (options.host, options.port)


def importer(name)
    # Wrap the given 'name' in a closure.
    def _import():
        __import__(name, {}, {}, [''])
    _import.priority = 20
    return _import


def start(opts):
    if '--project' in opts:
        # delay import until after daemonize has a chance to run
        engine.subscribe('start', importer(opts['--project']))
    
    if 'win' not in sys.platform:
        engine.subscribe('start', restsrv.plugins.daemonize)
    
    engine.start()
    engine.block()


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
    except getopt.GetoptError:
        help()
        sys.exit(2)
    
    if "--help" in opts:
        help()
        sys.exit(0)
    
    start(dict(opts))