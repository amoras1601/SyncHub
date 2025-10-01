# SyncHub

O SyncHub é uma plataforma SaaS (Software as a Service) projetada para centralizar e automatizar a gestão de vendas para pequenos e médios comerciantes que atuam em múltiplos marketplaces online, como Mercado Livre, Shopee, Amazon, entre outros.

## Arquitetura do Sistema

O sistema foi projetado como uma **aplicação web monolítica** utilizando o framework **Django**. A arquitetura adota a renderização no lado do servidor (Server-Side Rendering - SSR), o que simplifica o desenvolvimento, unifica o stack tecnológico e otimiza o SEO (Search Engine Optimization) nativamente.

## Stack Tecnológico

- **Backend:** Python com o framework Django.
- **Frontend:** Django Template Engine (DTL) para renderização, com HTMX e Alpine.js para interatividade dinâmica sem a necessidade de um framework JavaScript pesado.
- **Banco de Dados:** PostgreSQL.
- **Tarefas Assíncronas:** Celery com Redis como message broker.
- **Infraestrutura (Cloud):**
    - **Provedor:** AWS (Amazon Web Services).
    - **Hospedagem:** Contêineres Docker orquestrados com AWS Fargate (ECS).
    - **Serviços Gerenciados:** Amazon RDS for PostgreSQL, Amazon ElastiCache for Redis.
- **DevOps:**
    - **Containerização:** Docker.
    - **CI/CD:** GitHub Actions para automação de build, teste e deploy.

## Lista de Tarefas (TODO)

- [ ] **Core:**
    - [ ] Configurar projeto Django e estrutura inicial.
    - [ ] Implementar autenticação de usuário e arquitetura multi-tenant.
    - [ ] Modelar e implementar o schema do banco de dados (`ProdutoCentral`, `Loja`, `Anuncio`).
- [ ] **Integrações:**
    - [ ] Desenvolver módulo de conexão OAuth2 para Mercado Livre e Shopee.
    - [ ] Implementar webhook listeners para receber notificações de pedidos (`orders_v2`).
    - [ ] Criar tarefas assíncronas (Celery) para processar webhooks e buscar detalhes dos pedidos.
    - [ ] Desenvolver lógica para atualizar o estoque nos marketplaces via API.
- [ ] **Funcionalidades:**
    - [ ] Construir o módulo de gerenciamento de catálogo de produtos (CRUD de `ProdutoCentral`).
    - [ ] Desenvolver a lógica de vinculação entre `ProdutoCentral` e anúncios (`Anuncio`).
    - [ ] Implementar o painel de controle (dashboard) com as principais métricas de vendas.
    - [ ] Criar a interface de usuário (UI/UX) para todas as funcionalidades.
- [ ] **DevOps & Infra:**
    - [ ] Escrever `Dockerfile` e `docker-compose.yml` para ambientes de desenvolvimento e produção.
    - [ ] Configurar o pipeline de CI/CD com GitHub Actions para deploy na AWS.
    - [ ] Implementar estratégia de testes unitários e de integração.