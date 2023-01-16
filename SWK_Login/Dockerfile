

FROM node:16.17.1 as client

WORKDIR /usr/app/react/
COPY config.json ./
COPY SWK_Login_React/package*.json ./
RUN npm install 
COPY SWK_Login_React/ ./
RUN npm run build


# Setup the server

FROM node:16.17.1

WORKDIR /usr/app/server
COPY --from=client /usr/app/react/build/ ./SWK_Login_React/build/

WORKDIR /usr/app/server/
COPY config.json ./
COPY SWK_Login_Server/package*.json ./
RUN npm install
COPY SWK_Login_Server/ ./

EXPOSE 50020

CMD ["npm", "start"]