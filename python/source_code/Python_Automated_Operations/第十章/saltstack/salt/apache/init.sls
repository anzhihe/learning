apache:
   pkg:
     - installed
     - name: {{ pillar['pkgs']['apache'] }}
   service.running:
     - name: {{ pillar['pkgs']['apache'] }}
     - require:
       - pkg: {{ pillar['pkgs']['apache'] }}
