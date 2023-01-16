

FROM node:16.17.1 as client

WORKDIR /usr/app/react/
COPY config.json ./
COPY SWK_Handyticket_React/package*.json ./
RUN npm install 
COPY SWK_Handyticket_React/ ./
RUN npm run build


# Setup the server

FROM node:16.17.1

WORKDIR /usr/app/server
COPY --from=client /usr/app/react/build/ ./SWK_Handyticket_React/build/

WORKDIR /usr/app/server/
COPY config.json ./
COPY SWK_Handyticket_Server/package*.json ./
RUN npm install
COPY SWK_Handyticket_Server/ ./

ENV PORT 8000

EXPOSE 8000

CMD ["npm", "start"]