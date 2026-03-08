FROM python:3.12-slim
WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --no-cache
RUN uv pip install --system -r pyproject.toml
COPY . .
ENV PATH="/app/.venv/bin:$PATH"
