FROM python:3.12-slim
WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --no-cache
COPY . .
ENV PATH="/app/.venv/bin:$PATH"
