# Fleet Maintenance Application

This application is designed to handle fleet maintenance management for Company A. 
The project is built within a Dockerized environment.
- Django Rest Framework (backend)
- Vue 3 Typescript with Vite (frontend)
- SQLite (database)

### Prerequisites
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Node](https://nodejs.org/en/download/package-manager) or [NVM](https://www.freecodecamp.org/news/node-version-manager-nvm-install-guide/) (for frontend development)
- [Yarn](https://classic.yarnpkg.com/lang/en/docs/install/#mac-stable) (for frontend development)
- [Python 3](https://www.python.org/downloads/) (for backend development)

---
### Overview

The Docker Compose configuration defines the following **services**:
- **db-sqlite**: SQLite lightweight db to persist database data

- **backend-dj**: Django backend, on port `8000`

- **frontend-vite**: TypeScript Vue 3 TypeScript with Vite frontend, on port `3000`.

- **nginx**: Nginx server to act as a reverse proxy, routing requests to the backend and frontend.
---

### Project Setup
#### 1. Clone the repository

```bash
git clone https://github.com/kychok98/courier-maintenance-app.git
cd courier-maintenance-app
```

#### 2. Build and Run the Application
   Use Docker Compose to build and run the entire stack (backend, frontend, database, and Nginx).
```bash
docker-compose up --build
```
This will:
- Launch the SQLite database in a container.
- Build the Django backend and Vite frontend.
- Expose the backend at port `8000` and frontend at port `3000`, both accessible through Nginx on port `80`.

#### 3. Apply Database Migrations
Once the containers are up, run the following command to apply migrations in the backend:
```bash
docker exec fma-backend make migration-apply
```
> Note: `fma-backend` is the container-name in `docker-compose.yml` for backend

#### 4. Access the Application
Once everything is set up, you can access the application by visiting:
> http://localhost:80


---
### Common Commands
Django apply migrations
```bash
docker exec fma-backend make migration-apply
```

Start the application:
```bash 
docker-compose up
```

Start in detached mode (run in the background):
```bash 
docker-compose up -d
```

Build and start the application:
```bash 
docker-compose up --build
```

Stop all services:
```bash 
docker-compose down
```
For more information, refer to the [Docker Compose Documentation](https://docs.docker.com/reference/cli/docker/compose/up/)

---
### Frontend Setup locally
If you prefer to run the frontend and backend locally (without Docker), follow these steps:
1. Navigate to the frontend directory:
```bash
cd frontend
```
2. Install dependencies using Yarn:
```bash
yarn install
```
3. To run the frontend locally:
```bash
yarn dev
```
4. (Optional) Set Proxy in `vite-config.ts`: 

If you need to set up a proxy to redirect API requests during local development, update the following:

`vite-config.ts`
```javascript
server: {
  proxy: {
    "/api": {
      target: "http://127.0.0.1:8000",  // Point to your local Django backend
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, "")
    }
  }
}
```
>This ensures that API calls to `/api` on the frontend will be correctly proxied to your local Django backend.

---
### Backend Setup Locally
1. Navigate to the `backend` directory:
```bash
cd backend
```
2. Set up a Python virtual environment:
```bash
python3 -m venv env
source env/bin/activate
```
3. Install required dependencies:
```bash
pip3 install -r requirements.txt
```
4. To run the Django development server locally:
```bash
make run-server 
```

This will start the backend on `http://127.0.0.1:8000`.

---

