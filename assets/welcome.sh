
#!/bin/bash

clear

echo -e '🎉 WELCOME TO THE BEST HELLO WORLD! 🎉'
echo -e '   '
echo -e 'The server is already running, \033[0;34mCtrl + C\033[0m to stop the server if you like.
Debugging support is fully enabled in GitPod.'
echo -e '   '
echo -e 'The following commands are available to you:'
echo -e '   '
echo -e '- \033[0;34m$ poetry install \033[0m to reinstall all dependencies'
echo -e '- \033[0;34m$ poetry run pytest\033[0m to run the tests'
echo -e '- \033[0;34m$ poetry run gunicorn -b0.0.0.0:5002 app:app\033[0m start flask web server (if not already running) \n\n'
