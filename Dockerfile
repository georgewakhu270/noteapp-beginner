########## Vue.js build/development image ##########
FROM node:22-alpine AS frontend

WORKDIR /app/note-frontend

# Copy package metadata first so dependency installation can be cached.
COPY note-frontend/package*.json ./
RUN npm install

COPY note-frontend/ ./

EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]


########## Vue.js production build ##########
FROM frontend AS frontend-build
RUN npm run build


########## Django image ##########
FROM python:3.12-slim AS django

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir -r requirements.txt

COPY . ./

# Keep the compiled Vue application in the Django image for deployments that
# serve frontend assets through a reverse proxy or a static-file server.
COPY --from=frontend-build /app/note-frontend/dist ./note-frontend/dist

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
