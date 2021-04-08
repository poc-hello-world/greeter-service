FROM gitpod/workspace-full:latest

USER gitpod

RUN pyenv install 3.9.2 && pyenv global 3.9.2
