import sys, os
import xbmcaddon, xbmc


__scriptid__ = 'script.jcsd.mpd.pauser'
__addon__ = xbmcaddon.Addon(id=__scriptid__)


class Debug(object):                  

    @staticmethod
    def launch_remote_debug():
        d = Debug()
        isRemoteDebug = __addon__.getSetting('remote_debug')
        debug_port = int(__addon__.getSetting('debug_port'))
        debug_host = __addon__.getSetting('debug_host')
        xbmc.log("[MPD PAUSER] isRemoteDebug '%s'" % (isRemoteDebug))
        xbmc.log("[MPD PAUSER] debug_host '%s'" % (debug_host))
        xbmc.log("[MPD PAUSER] debug_port '%s'" % (debug_port))
        # append pydev remote debugger
        if isRemoteDebug == 'true':
            xbmc.log("[MPD PAUSER] Remote debug enabled")
            # Make pydev debugger works for auto reload.
            # Note pydevd module need to be copied in XBMC\system\python\Lib\pysrc
            try:
                xbmc.log("[MPD PAUSER] Trying to import pydevd")
                import pysrc.pydevd as pydevd
                xbmc.log("[MPD PAUSER] Import ok")
                # stdoutToServer and stderrToServer redirect stdout and stderr to eclipse console
                pydevd.settrace(debug_host, port=debug_port, stdoutToServer=True, stderrToServer=True, trace_only_current_thread=False, suspend=False)
                xbmc.log("[MPD PAUSER] Remote debugger connected")
            except ImportError:
                xbmc.log("[MPD PAUSER] Error: You must add org.python.pydev.debug.pysrc to your PYTHONPATH.",0)
                sys.exit(1)
        else:
            xbmc.log("[MPD PAUSER] Remote debug disabled",0)
