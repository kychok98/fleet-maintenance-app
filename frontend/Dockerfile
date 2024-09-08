FROM node:20.12-alpine3.19 AS base

# Install dependencies
FROM base AS deps
WORKDIR /app
COPY package.json yarn.lock* ./
RUN npm install

# Build code
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# Production Build
FROM base AS prod
WORKDIR /app
ENV NODE_ENV production
COPY --from=builder /app/ ./
EXPOSE 3000
CMD ["npm",  "run",  "preview"]
#CMD [ "serve", "-s", "dist" ]
#CMD node index.js
#
#WORKDIR /frontend
#COPY package.json .
#RUN npm install
#RUN npm i -g serve
#COPY . .
#
#RUN npm run build
#
#EXPOSE 3000
#
#CMD [ "serve", "-s", "dist" ]