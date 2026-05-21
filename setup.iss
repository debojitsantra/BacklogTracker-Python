; Inno Setup Script for Backlog Tracker
[Setup]
AppId={{D37F2F11-D6D2-4E38-92B1-4A53D9E99C6A}
AppName=Backlog Tracker
AppVersion=1.0
AppPublisher=Debojit Santra

; Allows installation without Admin privileges
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog

DefaultDirName={autopf}\Backlog Tracker
DefaultGroupName=Backlog Tracker
AllowNoIcons=yes

SetupIconFile=icon.ico
UninstallDisplayIcon={app}\icon.ico

Compression=lzma
SolidCompression=yes
WizardStyle=modern

OutputDir=installer_output
OutputBaseFilename=BacklogTracker_Setup

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Sources the single portable binary built with PyInstaller --onefile
Source: "dist\BacklogTracker.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Backlog Tracker"; Filename: "{app}\BacklogTracker.exe"; IconFilename: "{app}\icon.ico"
Name: "{group}\{cm:UninstallProgram,Backlog Tracker}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Backlog Tracker"; Filename: "{app}\BacklogTracker.exe"; IconFilename: "{app}\icon.ico"; Tasks: desktopicon

[Run]
; Launches the program under original user privileges to protect database pathing
Filename: "{app}\BacklogTracker.exe"; Description: "{cm:LaunchProgram,Backlog Tracker}"; Flags: nowait postinstall skipifsilent runasoriginaluser