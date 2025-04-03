
daemon = True
workers = 5
threads = 5

# default localhost:8000
bind = '127.0.0.1:8000'

# Pid
pidfile = '/opt/seatable/pids/dtable-web.pid'

# for file upload, we need a longer timeout value (default is only 30s, too short)
timeout = 1200

limit_request_line = 8190

# Log
#accesslog = '/opt/seatable/logs/gunicorn-access.log'
#errorlog = '/opt/seatable/logs/gunicorn-error.log'

