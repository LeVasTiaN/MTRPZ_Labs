FROM node:20 AS build

WORKDIR /app

COPY package*.json ./

RUN npm install --omit=dev

COPY . .

FROM gcr.io/distroless/nodejs20-debian12

WORKDIR /app

COPY --from=build /app /app

CMD ["app.js"]
