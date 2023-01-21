

FROM node:16.17.1 as client

WORKDIR /usr/app/react/
COPY SWK_Konrad_React/package*.json ./
RUN npm install 

WORKDIR /usr/app/
COPY config.json ./

WORKDIR /usr/app/react/
COPY SWK_Konrad_React/ ./
RUN npm run build

# Setup the server

FROM node:16.17.1

WORKDIR /usr/app/server/
COPY SWK_Konrad_Server/package*.json ./
RUN npm install

WORKDIR /usr/app/
COPY config.json ./

WORKDIR /usr/app/server/
COPY --from=client /usr/app/react/build/ ./SWK_Konrad_React/build/
COPY SWK_Konrad_Server/ ./
EXPOSE 50020
CMD ["npm", "start"]