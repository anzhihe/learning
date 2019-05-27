appname: website
flow:
  maxconn: 30000
  maxmem: 6G
 {% if grains['id'] == 'SN2013-08-022' %}
  maxcpu: 8
 {% else %}
  maxcpu: 4
 {% endif %}
