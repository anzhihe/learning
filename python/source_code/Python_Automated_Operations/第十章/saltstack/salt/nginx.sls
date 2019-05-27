nginx:
  pkg:
   - installed
  file.managed:
   - source: salt://nginx/nginx.conf
   - name: /etc/nginx/nginx.conf
   - user: root
   - group: root
   - mode: 644
   - template: jinja

  service.running:
   - enable: True
#   - reload: True
   - watch:
     - file: /etc/nginx/nginx.conf
     - pkg: nginx

#restart_service:
#   cmd.run:
#      - name: 'service nginx restart'
#      - user: root
#      - group: root
#      - require:
#        - file: /etc/nginx/nginx.conf
