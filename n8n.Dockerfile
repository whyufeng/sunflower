FROM n8nio/n8n:latest
USER root
RUN npm install -g lunar-javascript && \
    mkdir -p /usr/local/lib/node_modules && \
    ln -s $(npm root -g)/lunar-javascript /usr/local/lib/node_modules/lunar-javascript
USER node
