ARG BUILD_FROM="ghcr.io/home-assistant/base:latest"
FROM $BUILD_FROM

ARG BUILD_VERSION
ARG BUILD_ARCH

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    python3 \
    py3-pip \
    sqlite \
    bash \
    curl \
    unzip

WORKDIR /app

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt --break-system-packages

COPY . /app/

RUN mkdir -p /app/core/static && \
    mkdir -p /app/core/control && \
    mkdir -p /app/core/assist && \
    mkdir -p /app/core/assistant && \
    mkdir -p /app/core/coaching && \
    mkdir -p /app/core/dashboard && \
    mkdir -p /app/core/relax && \
    mkdir -p /app/core/mood && \
    mkdir -p /app/core/domotica && \
    mkdir -p /app/core/control/migrations && \
    mkdir -p /app/core/assist/migrations && \
    mkdir -p /app/core/assistant/migrations && \
    mkdir -p /app/core/coaching/migrations && \
    mkdir -p /app/core/dashboard/migrations && \
    mkdir -p /app/core/relax/migrations && \
    mkdir -p /app/core/mood/migrations && \
    mkdir -p /app/core/domotica/migrations && \
    touch /app/core/assist/__init__.py \
          /app/core/assistant/__init__.py \
          /app/core/coaching/__init__.py \
          /app/core/control/__init__.py \
          /app/core/mood/__init__.py \
          /app/core/domotica/__init__.py \
          /app/core/dashboard/__init__.py \
          /app/core/relax/__init__.py \
          /app/core/assist/migrations/__init__.py \
          /app/core/mood/migrations/__init__.py \
          /app/core/domotica/migrations/__init__.py \
          /app/core/assistant/migrations/__init__.py \
          /app/core/coaching/migrations/__init__.py \
          /app/core/control/migrations/__init__.py \
          /app/core/dashboard/migrations/__init__.py \
          /app/core/relax/migrations/__init__.py

# Downloads the actual compiled release zip file, extracts it, and cleans up
RUN mkdir -p /app/core/static && \
    curl -sL https://github.com/twbs/bootstrap/releases/download/v5.3.3/bootstrap-5.3.3-dist.zip -o /tmp/bootstrap.zip && \
    unzip -q /tmp/bootstrap.zip -d /tmp/bootstrap-dist && \
    cp /tmp/bootstrap-dist/bootstrap-5.3.3-dist/css/bootstrap.min.css /app/core/static/ && \
    rm -rf /tmp/bootstrap.zip /tmp/bootstrap-dist

# Pre-build migrations and static files once during image build for fast startup
RUN python3 /app/manage.py makemigrations core domotica assist mood --noinput && \
    python3 /app/manage.py collectstatic --noinput

LABEL \
    io.hass.version="${BUILD_VERSION}" \
    io.hass.type="app" \
    io.hass.arch="${BUILD_ARCH}"

RUN mkdir -p /etc/services.d/automautist-rest
COPY s6-run-service /etc/services.d/automautist-rest/run
RUN chmod +x /etc/services.d/automautist-rest/run
RUN chmod +x /app/run.sh
