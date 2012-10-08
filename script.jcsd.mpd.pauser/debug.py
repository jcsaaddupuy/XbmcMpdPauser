import sys, os
import xbmcaddon, xbmc

__scriptid__ = 'script.jcsd.mpd.pauser'
__addon__ = xbmcaddon.Addon(id=__scriptid__)
__logfname__ = "addon.log"

class Debug:
    _addon = None
    def __init__(self):        
        self.isLogTofile = __addon__.getSetting('log_to_file')
        self.logfolder = __addon__.getSetting('log_folder')
        
        if self.isLogTofile and not os.path.exists(self.logfolder):
            os.makedirs(self.logfolder)
            
    def Log(self, data):
        if self.isLogTofile :
            try:
                xbmc.log(data)
                l = open(os.path.join(self.logfolder, __logfname__), 'a+')
                l.write(data+"\n")
                l.close()
            except Exception as e:
                xbmc.log(e)
            
    @staticmethod
    def launch_remote_debug():
        d=Debug()
        isRemoteDebug = __addon__.getSetting('remote_debug')
        debug_port = int( __addon__.getSetting('debug_port'))
        debug_host = __addon__.getSetting('debug_host')
        # append pydev remote debugger
        if isRemoteDebug == True:
            # Make pydev debugger works for auto reload.
            # Note pydevd module need to be copied in XBMC\system\python\Lib\pysrc
            try:
                import pysrc.pydevd as pydevd
                # stdoutToServer and stderrToServer redirect stdout and stderr to eclipse console
                pydevd.settrace(debug_host, port=debug_port, stdoutToServer=True, stderrToServer=True)
                d.Log("Remote debugger connected")
            except ImportError:
                d.Log("Error: You must add org.python.pydev.debug.pysrc to your PYTHONPATH.")
                sys.exit(1)
