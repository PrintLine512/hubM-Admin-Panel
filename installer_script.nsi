!include "MUI2.nsh"
!include LogicLib.nsh

; !define SOURCE_DIR "dist\hubM Admin Panel"
!define SOURCE_DIR "${__FILEDIR__}\dist\hubM Admin Panel"
!define APP_NAME "hubM Admin Panel"


; The name of the installer
Name "${APP_NAME}"

; The file to write
; OutFile "dist/hubM Admin Panel Installer.exe"
OutFile "${__FILEDIR__}\dist\hubM Admin Panel Installer.exe"

; Request application privileges for Windows Vista
RequestExecutionLevel user

; Build Unicode installer
Unicode True

; The default installation directory
InstallDir "$APPDATA\hubM Admin Panel"

;--------------------------------
#!define MUI_FINISHPAGE_TITLE "Title"
#!define MUI_FINISHPAGE_TEXT "Text"
!define MUI_FINISHPAGE_RUN "$INSTDIR\hubM Admin Panel.exe"



; Pages

!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "Russian"

;--------------------------------


; The stuff to install
Section "" ;No components page, name is not important

  # Убедимся, что процесс dkcl64.exe завершен
  #nsExec::ExecToStack 'taskkill /F /IM dkcl64.exe /T'
  
  # Убедимся, что процесс Auto-Find.exe завершен
  #nsExec::ExecToStack 'taskkill /F /IM Auto-Find.exe /T'

  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  File /r "${SOURCE_DIR}\*.*"

  #ExecShell "" "$INSTDIR\Auto-Find.exe"
  
  CreateShortCut "$DESKTOP\hubM Admin Panel.lnk" "$INSTDIR\hubM Admin Panel.exe"
  WriteUninstaller $INSTDIR\Uninstall.exe
  
SectionEnd

Section "Uninstall"

# Убедимся, что процесс dkcl64.exe завершен перед деинсталляцией
  nsExec::ExecToStack 'taskkill /F /IM hubM Admin Panel.exe /T'

# Удаление файлов программы
  Delete $INSTDIR\*
  Delete "$INSTDIR\*.*"
 
# Удаление ярлыков с рабочего стола
  Delete "$DESKTOP\hubM Admin Panel.lnk"

# Удаление папки установки
  RMDir /r $INSTDIR

SectionEnd