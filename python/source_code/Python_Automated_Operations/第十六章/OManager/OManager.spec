# -*- mode: python -*-
a = Analysis(['OManager.py'],
             pathex=['D:\\python\\OManager\\OManager'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='OManager.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='img\\imac.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='OManager')
