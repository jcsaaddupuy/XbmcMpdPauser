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
        xbmc.log(msg="[MPD PAUSER] isRemoteDebug '%s'" % (isRemoteDebug), level=xbmc.LOGDEBUG)
        xbmc.log(msg="[MPD PAUSER] debug_host '%s'" % (debug_host), level=xbmc.LOGDEBUG)
        xbmc.log(msg="[MPD PAUSER] debug_port '%s'" % (debug_port), level=xbmc.LOGDEBUG)
        # append pydev remote debugger
        if isRemoteDebug == 'true':
            xbmc.log(msg="[MPD PAUSER] Remote debug enabled")
            # Make pydev debugger works for auto reload.
            # Note pydevd module need to be copied in XBMC\system\python\Lib\pysrc
            try:
                xbmc.log(msg="[MPD PAUSER] Trying to import pydevd")
                import pysrc.pydevd as pydevd
                xbmc.log(msg="[MPD PAUSER] Import ok")
                # stdoutToServer and stderrToServer redirect stdout and stderr to eclipse console
                pydevd.settrace(debug_host, port=debug_port, stdoutToServer=True, stderrToServer=True, trace_only_current_thread=False, suspend=False)
                xbmc.log(msg="[MPD PAUSER] Remote debugger connected", level = xbmc.LOGDEBUG)
            except ImportError:
                xbmc.log(msg="[MPD PAUSER] Error: You must add org.python.pydev.debug.pysrc to your PYTHONPATH.", level = xbmc.LOGERROR)
                sys.exit(1)
        else:
            xbmc.log(msg="[MPD PAUSER] Remote debug disabled", level = xbmc.LOGSEVERE)
