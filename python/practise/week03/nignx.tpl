server {{
    listen       {port} {server};
    server_name  {servername};

    access_log  {access_log}  main;

    location / {{
        root   {home};
        index  index.html index.htm;
        proxy_pass   http://127.0.0.1:{proxy_port};
    }}
}}