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
dir /a:d /b
ren "D:\Dung\zettelkasten\Bins\Notion-to-Obsidian-Converter\Export\toob\@ puratosgrandplace com, Bánh mì nguyên cám - " "D:\Dung\zettelkasten\Bins\Notion-to-Obsidian-Converter\Export\toob\abcd"
