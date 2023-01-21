

FROM node:16.17.1 as client

WORKDIR /usr/app/react/
COPY SWK_Handyticket_React/package*.json ./
RUN npm install 

WORKDIR /usr/app/
COPY config.json ./

WORKDIR /usr/app/react/
COPY SWK_Handyticket_React/ ./
RUN npm run build

# Setup the server

FROM node:16.17.1


WORKDIR /usr/app/server/
COPY SWK_Handyticket_Server/package*.json ./
RUN npm install

WORKDIR /usr/app/
COPY config.json ./

WORKDIR /usr/app/server/
COPY --from=client /usr/app/react/build/ ./SWK_Handyticket_React/build/
COPY SWK_Handyticket_Server/ ./
EXPOSE 50030
CMD ["npm", "start"]