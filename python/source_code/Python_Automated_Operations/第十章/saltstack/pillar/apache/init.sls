pkgs:
{% if grains['os_family'] == 'Debian' %}
  apache: apache2
  {% elif grains['os_family'] == 'RedHat' %}
  apache: httpd
  {% elif grains['os'] == 'Arch' %}
  apache: apache
{% endif %}
