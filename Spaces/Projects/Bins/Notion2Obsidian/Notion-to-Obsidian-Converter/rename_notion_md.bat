rem 
rem read first line of hehe.txt
rem set /p texte=< hehe.txt
rem
rem rename hehe by fistline read above
rem ren hehe.txt "%texte%.txt"
rem
rem support unicode characters
chcp 65001
@echo off 
for %%F in (*.md) do (
  set "name=%%F"
  set /p texte=< %%F
 
  echo %texte%
  echo %%F
  
  ren "%%F" "%texte:~2,512%.md"
)
