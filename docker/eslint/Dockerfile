FROM node:8.10.0-alpine


WORKDIR /usr/src/myapp
RUN  yarn init -y \
     && yarn add --dev eslint eslint-config-airbnb-base eslint-plugin-import
ENTRYPOINT ["./node_modules/eslint/bin/eslint.js"]
