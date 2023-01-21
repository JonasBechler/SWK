

FROM node:16.17.1 as client

WORKDIR /usr/app/react/
COPY SWK_Login_React/package*.json ./
RUN npm install 

WORKDIR /usr/app/
COPY config.json ./

WORKDIR /usr/app/react/
COPY SWK_Login_React/ ./
RUN npm run build

# Setup the server

FROM node:16.17.1

WORKDIR /usr/app/server/
COPY SWK_Login_Server/package*.json ./
RUN npm install

WORKDIR /usr/app/
COPY config.json ./

WORKDIR /usr/app/server/
COPY --from=client /usr/app/react/build/ ./SWK_Login_React/build/
COPY SWK_Login_Server/ ./
EXPOSE 50010
CMD ["npm", "start"]