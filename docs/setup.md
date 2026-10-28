# Setup

## 1. UV

### Create uv enviroment

```
uv init --no-package --python 3.13
```

- no package för att de nya uv skapar paket automatiskt

### Install packages

```
uv add pandas pydantic-ai ipykernel
```

## 2. Nvida build

https://build.nvidia.com/

### Generate an api - key in nvida

https://build.nvidia.com/settings/api-keys

### Save it in .env-file and gitignore
