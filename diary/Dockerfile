FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN ls -la /app 

CMD ["npm", "run", "dev"]