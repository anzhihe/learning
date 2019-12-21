在 Windows 上， 你可以创建一个批处理文件，利用 Win-R 运行窗口， 来运行
这个程序（关于批处理文件的更多信息，参见附录 B）。在文件编辑器中输入以下
代码， 保存为 pw.bat， 放在 C:\Windows 目录下：
@py.exe C:\Python34\pw.py %*
@pause
有了这个批处理文件， 在 Windows 上运行口令保存程序，就只要按下 Win-R，
再输入 pw <account name>。
