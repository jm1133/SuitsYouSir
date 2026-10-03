import os, random, sys, threading, time, psutil, pygame, ctypes, pystray; from PIL import Image, ImageDraw

mutex = ctypes.windll.kernel32.CreateMutexW(None, False, "SuitsYouSir_SingleInstance")

if ctypes.windll.kernel32.GetLastError() == 183:
    sys.exit(0)

if getattr(sys, "frozen", False):
    APP_DIR = os.path.dirname(sys.executable)
    RESOURCE_DIR = sys._MEIPASS
else:
    APP_DIR = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_DIR = APP_DIR


SOUNDS_FOLDER = os.path.join(RESOURCE_DIR, "Sounds")
LOG_FILE = os.path.join(APP_DIR, "SuitsYouSir.log")

CHECK_INTERVAL = 0.5


IGNORED_PROCESSES = {
    "Aac3572DramHal_x86.exe",
    "AacAmbientKeyScanner.exe",
    "AacAmbientLighting.exe",
    "AacKingstonDramHal_x86.exe",
    "AcPowerNotification.exe",
    "AgentHelper.exe",
    "AgentService.exe",
    "AggregatorHost.exe",
    "alg.exe",
    "AMDRyzenMasterCLI.exe",
    "OAWrapper.exe",
    "netsh.exe",
    "AppHelperCap.exe",
    "wsl.exe",
    "rg.exe",
    "AppleMobileDeviceService.exe",
    "ApplicationFrameHost.exe",
    "AppVClient.exe",
    "ArmouryCrate.Service.exe",
    "ArmouryCrate.UserSessionHelper.exe",
    "ArmourySocketServer.exe",
    "asus_framework.exe",
    "AsusCertService.exe",
    "AsusROGLSLService.exe",
    "AsusUpdate.exe",
    "atkexComSvc.exe",
    "audiodg.exe",
    "AUEPDU.exe",
    "AUEPMaster.exe",
    "backgroundTaskHost.exe",
    "CC_Engine_x64.exe",
    "Client.exe",
    "cmd.exe",
    "conhost.exe",
    "Connect.exe",
    "copilot-runtime.exe",
    "crashpad_handler.exe",
    "CredentialEnrollmentManager.exe",
    "CrossDeviceResume.exe",
    "CrossDeviceService.exe",
    "csrss.exe",
    "SuitsYouSir.exe",
    "ctfmon.exe",
    "dasHost.exe",
    "DCv2.exe",
    "DDSHelper.exe",
    "DefenderSessionHelper.exe",
    "DiagsCap.exe",
    "dllhost.exe",
    "dotnet.exe",
    "dwm.exe",
    "elevation_service.exe",
    "EvtEng.exe",
    "extensionCardHal_x86.exe",
    "fontdrvhost.exe",
    "fxssvc.exe",
    "GameInputRedistService.exe",
    "GameInputSvc.exe",
    "GameSDK.exe",
    "gamingservices.exe",
    "GamingServices.exe",
    "gamingservicesnet.exe",
    "GamingServicesNet.exe",
    "GooglePlayGamesServices.exe",
    "helperservice.exe",
    "iTunesHelper.exe",
    "jucheck.exe",
    "jusched.exe",
    "KinectMonitor.exe",
    "KinectService.exe",
    "LEDKeeper2.exe",
    "lghub_agent.exe",
    "lghub_system_tray.exe",
    "lghub_updater.exe",
    "LightingService.exe",
    "LightKeeperService.exe",
    "locator.exe",
    "logi_crashpad_handler.exe",
    "logi_lamparray_service.AMD64.exe",
    "LsaIso.exe",
    "lsass.exe",
    "Malwarebytes.exe",
    "MBAMService.exe",
    "MBVpnTunnelService.exe",
    "Microsoft.CodeAnalysis.LanguageServer.exe",
    "Microsoft.VisualStudio.Code.Server.exe",
    "Microsoft.VisualStudio.Code.ServiceController.exe",
    "Microsoft.VisualStudio.Code.ServiceHost.exe",
    "MicrosoftEdgeUpdate.exe",
    "midisrv.exe",
    "millennium.crashhandler64.exe",
    "millennium.luavm64.exe",
    "MoNotificationUx.exe",
    "MoUsoCoreWorker.exe",
    "MpDefenderCoreService.exe",
    "msdtc.exe",
    "msedgewebview2.exe",
    "MSI.CentralServer.exe",
    "MSI.TerminalServer.exe",
    "MSI_Case_Service.exe",
    "MSI_Central_Service.exe",
    "msiexec.exe",
    "MsMpEng.exe",
    "MsSense.exe",
    "Mystic_Light_Service.exe",
    "NahimicMonitorX64.exe",
    "NahimicService.exe",
    "NetworkCap.exe",
    "NgcIso.exe",
    "NhNotifSys.exe",
    "NisSrv.exe",
    "nordsec-threatprotection-service.exe",
    "NordUpdateService.exe",
    "nordvpn-service.exe",
    "nvcontainer.exe",
    "NVDisplay.Container.exe",
    "nvfvsdksvc_x64.exe",
    "nvsphelper64.exe",
    "OpenConsole.exe",
    "Overlay.exe",
    "PanDhcpDns.exe",
    "parfait_crash_handler.exe",
    "PenTablet.exe",
    "PerceptionSimulationService.exe",
    "perfhost.exe",
    "PhoneExperienceHost.exe",
    "powershell.exe",
    "PowerToys.AdvancedPaste.exe",
    "PowerToys.AlwaysOnTop.exe",
    "PowerToys.Awake.exe",
    "PowerToys.FancyZones.exe",
    "PresentationFontCache.exe",
    "ps_server.exe",
    "ps_service_launcher.exe",
    "python.exe",
    "python3.exe",
    "pythonw.exe",
    "ReadyForService.exe",
    "ReFsDedupSvc.exe",
    "RegSrvc.exe",
    "ROGLiveService.exe",
    "RuntimeBroker.exe",
    "rust-analyzer.exe",
    "RvControlSvc.exe",
    "RvRvpnGui.exe",
    "SearchFilterHost.exe",
    "SearchHost.exe",
    "SearchIndexer.exe",
    "SearchProtocolHost.exe",
    "SecurityHealthService.exe",
    "SecurityHealthSystray.exe",
    "SensorDataService.exe",
    "services.exe",
    "ShellExperienceHost.exe",
    "ShellHost.exe",
    "sideloadlydaemon.exe",
    "sihost.exe",
    "smartscreen.exe",
    "smss.exe",
    "SMSvcHost.exe",
    "snmptrap.exe",
    "spoolsv.exe",
    "sppsvc.exe",
    "sqlwriter.exe",
    "ssh-agent.exe",
    "StandardCollector.Service.exe",
    "StartMenuExperienceHost.exe",
    "steamservice.exe",
    "steamwebhelper.exe",
    "svchost.exe",
    "SysInfoCap.exe",
    "taskhostw.exe",
    "Taskmgr.exe",
    "TextInputHost.exe",
    "TieringEngineService.exe",
    "TrustedInstaller.exe",
    "TwitchService.exe",
    "UniGetUI.exe",
    "unsecapp.exe",
    "update.exe",
    "Update.exe",
    "update_service.exe",
    "updater.exe",
    "usbipd.exe",
    "UserOOBEBroker.exe",
    "VBoxSDS.exe",
    "vds.exe",
    "vesktop.exe",
    "vmcompute.exe",
    "VSInstallerElevationService.exe",
    "vssvc.exe",
    "wbengine.exe",
    "wenativehost.exe",
    "Widgets.exe",
    "WidgetService.exe",
    "windhawk.exe",
    "WindowsTerminal.exe",
    "wininit.exe",
    "winlogon.exe",
    "WmiApSrv.exe",
    "WmiPrvSE.exe",
    "wmpnetwk.exe",
    "WpcMon.exe",
    "WsaService.exe",
    "wslservice.exe",
    "WUDFHost.exe",
    "XboxPcAppFT.exe",
    "xgamehelper.exe",
    "ZeroConfigService.exe",
    "ms-teamsupdate.exe",
    "WpcTok.exe",
    "git.exe",
    "git-remote-https.exe",
    "FileCoAuth.exe",
    "icacls.exe",
    "BackgroundDownload.exe",
    "Bloxstrap.exe",
    "chrome.exe",
    "Code.exe",
    "CodeSetup-stable-07f806f999227108933c2e30515b26eecc1fda74.exe",
    "CodeSetup-stable-07f806f999227108933c2e30515b26eecc1fda74.tmp",
    "EOSOverlayRenderer-Win64-Shipping.exe",
    "EpicOnlineServicesInstallHelper.exe",
    "EpicWebHelper.exe",
    "GameBarPresenceWriter.exe",
    "gk.exe",
    "gk_3_1_76.exe",
    "LogonUI.exe",
    "MSI.True Color.exe",
    "NVIDIA Overlay.exe",
    "pet.exe",
    "pnputil.exe",
    "RobloxCrashHandler.exe",
    "RobloxPlayerBeta.exe",
    "RobloxStudioModManager.exe",
    "SoftLandingTask.exe",
    "StoreDesktopExtension.exe",
    "Steam Achievement Notifier (V1.9).exe",
    "SystemSettings.exe",
    "update_notifier.exe",
    "vivaldi.exe",
    "WMIADAP.exe",
    "wermgr.exe",
    "sc.exe",
    "8GadgetPack.exe",
    "sidebar.exe",
    "PowerToys.CropAndLock.exe",
    "PowerToys.Peek.UI.exe",
    "PowerToys.PowerLauncher.exe",
    "PowerToys.ColorPickerUI.exe",
    "SCEWIN_64.exe",
    "dxgiadaptercache.exe",
    "dbInstaller.exe",
    "whoami.exe",
    "CompPkgSrv.exe",
    "code-tunnel.exe",
    "WerFault.exe",
    "tasklist.exe",
    "taskhost.exe",
    "mscopilot_proxy.exe",
    "DataExchangeHost.exe",
    "sdbinst.exe",
    "prevhost.exe",
    "gameoverlayui64.exe",
    "MpCmdRun.exe",
    "CHXSmartScreen.exe",
    "nvrla.exe",
    "PresentMon_x64.exe",
    "OneDriveLauncher.exe",
    "FvContainer.exe",
    "FvContainer.System.exe",
    "FileOperator.exe",
    "dxgiadaptercache.exe",
    "OAWrapper.exe",
    "jp2launcher.exe",
    "StoreDesktopExtension.exe",
    "BackgroundDownload.exe",
    "SoftLandingTask.exe",
    "GameBarPresenceWriter.exe",
    "WMIADAP.exe",
}


IGNORED_PROCESSES = {name.lower() for name in IGNORED_PROCESSES}

pygame.mixer.init()

sound_lock = threading.Lock()
log_lock = threading.Lock()


def log_app(name):
    timestamp = time.strftime("%d/%m/%Y %H:%M:%S")

    with log_lock:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {name}\n")
            file.flush()


def get_sounds():
    os.makedirs(SOUNDS_FOLDER, exist_ok=True)

    return [
        os.path.join(SOUNDS_FOLDER, file)
        for file in os.listdir(SOUNDS_FOLDER)
        if file.lower().endswith((".wav", ".mp3", ".ogg"))
    ]


def play_random_sound():
    with sound_lock:
        if pygame.mixer.music.get_busy():
            return

        sounds = get_sounds()

        if not sounds:
            return

        sound = random.choice(sounds)

        try:
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
        except Exception:
            pass


def get_processes():
    processes = {}

    for process in psutil.process_iter(["pid", "name"]):
        try:
            pid = process.info["pid"]
            name = process.info["name"]

            if name:
                processes[pid] = name

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return processes


def monitor_processes():
    known_processes = get_processes()

    while True:
        time.sleep(CHECK_INTERVAL)

        current_processes = get_processes()

        old_pids = set(known_processes)
        new_pids = set(current_processes)

        started = new_pids - old_pids

        for pid in started:
            name = current_processes[pid]

            if name.lower() not in IGNORED_PROCESSES:
                log_app(name)
                play_random_sound()

        known_processes = current_processes


def quit_app(icon, item):
    pygame.mixer.music.stop()
    icon.stop()


def start_tray():
    icon = pystray.Icon(
        "SuitsYouSir",
        Image.open(os.path.join(RESOURCE_DIR, "Icon.ico")),
        "Suits You Sir",
        menu=pystray.Menu(pystray.MenuItem("Quit", quit_app)),
    )

    icon.run()


threading.Thread(target=monitor_processes, daemon=True).start()

start_tray()
