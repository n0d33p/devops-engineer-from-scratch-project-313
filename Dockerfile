FROM python:3.12-slim

RUN apt-get update && apt-get install -y nginx curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock package.json ./
RUN uv sync --frozen --no-cache --no-install-project
RUN npm install

RUN mkdir -p /app/public
RUN cp -r ./node_modules/@hexlet/project-devops-deploy-crud-frontend/dist/. /app/public/

COPY nginx.conf /etc/nginx/sites-available/default
COPY . .

RUN echo "#!/bin/bash\nnginx -g 'daemon off;' & uv run gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8080 main:app" > /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]