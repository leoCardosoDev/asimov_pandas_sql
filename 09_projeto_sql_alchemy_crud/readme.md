Para garantir a persistência dos dados do PostgreSQL e configurar o pgAdmin 4, você pode criar um arquivo `docker-compose.yml` que monta volumes no diretório onde o `docker-compose.yml` está localizado. Aqui está um exemplo de como fazer isso:

### Estrutura do Diretório

```
/seu-diretorio
  ├── docker-compose.yml
  └── pgdata/
```

### Conteúdo do `docker-compose.yml`

```yaml
services:
  postgres:
    image: postgres:latest
    container_name: postgres
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: 12345
      POSTGRES_DB: aula_db
    ports:
      - "5432:5432"
    volumes:
      - ./pgdata:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "8080:80"
    depends_on:
      - postgres

volumes:
  pgdata:
```

### Passos para Configuração

1. **Crie o diretório para os dados do PostgreSQL:**
   ```bash
   mkdir -p /seu-diretorio/pgdata
   ```

2. **Navegue até o diretório que contém o `docker-compose.yml`:**
   ```bash
   cd /seu-diretorio
   ```

3. **Inicie os contêineres com `docker-compose`:**
   ```bash
   docker-compose up -d
   ```

### Verificar a Persistência

Para verificar se os dados persistem após parar e reiniciar os contêineres:

1. **Pare os contêineres:**
   ```bash
   docker-compose down
   ```

2. **Reinicie os contêineres:**
   ```bash
   docker-compose up -d
   ```

Os dados do PostgreSQL devem permanecer salvos no diretório `pgdata` e estarão disponíveis quando você reiniciar os contêineres.
