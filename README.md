# SyncHub

O SyncHub é uma plataforma SaaS (Software as a Service) projetada para centralizar e automatizar a gestão de vendas para pequenos e médios comerciantes que atuam em múltiplos marketplaces online, como Mercado Livre, Shopee, Amazon, entre outros..

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

## Instalação

Siga os passos abaixo para executar o projeto localmente em um ambiente de desenvolvimento com o banco SQLite (sem Docker):

1. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Aplique migrações e crie um superusuário:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Rode o servidor de desenvolvimento:

```bash
python manage.py runserver
```

5. Acesse no navegador: `http://127.0.0.1:8000/`

## Lista de Tarefas (TODO)

Abaixo está o estado atual das principais tarefas do projeto, organizado por prioridade. Marquei o que já foi implementado, o que está em progresso e o que ainda falta.

- [x] **UX / Design & Frontend**
    - [x] Extrair tokens e styles do design React (`SyncHub UI_UX Design`) e gerar `static/css/ui.css`.
    - [x] Criar `base.html` com topbar, sidebar e layout principal.
    - [x] Implementar dashboard inicial (cards, estatísticas básicas).
    - [x] Implementar lista de produtos (tabela + grid) com modal de criação via HTMX.
    - [x] Adicionar variação de card para produtos e polir estilos (botões, inputs, tabelas).
    - [x] Avatar no cabeçalho com dropdown; FAB acessível com SVG.
    - [ ] Polir dashboard para ficar fiel ao layout de referência (stat cards, ações rápidas, notificações).

- [x] **Core & Models**
    - [x] Scaffold do app `core` e modelos iniciais (`ProdutoCentral`, `Loja`, `Anuncio`).
    - [ ] Ajustes finos e decisão sobre campo opcional de imagem (`image`) para `ProdutoCentral` (migração necessária).

- [~] **Views & Interatividade**
    - [x] CRUD básico para produtos/lojas/anúncios com templates.
    - [~] Suporte HTMX nas operações de criação (modal) — em uso; melhorar validação inline.
    - [ ] Finalizar página de detalhe de anúncio (`anuncio_detail`).
    - [in-progress] Portar/terminar `produto_detail` com layout final (visual polishing em andamento).

- [ ] **Autenticação & Permissões**
    - [x] Integração básica com `django.contrib.auth` (login/logout/profile).
    - [ ] Implementar permissões owner-only para edição/exclusão de `Loja` e `Anuncio`.

- [ ] **Integrações & Automação**
    - [ ] Implementar OAuth para marketplaces (Mercado Livre, Shopee) — skeleton `mercadolivre` criado, integração pendente.
    - [ ] Criar listeners/webhooks para receber eventos de pedidos e atualizações.
    - [ ] Implementar tarefas assíncronas (Celery + Redis) para processar webhooks e sincronizações.

- [ ] **Qualidade & Infra**
    - [ ] Adicionar testes unitários e de integração para models e views.
    - [ ] Escrever `Dockerfile` e `docker-compose.yml` para ambiente de desenvolvimento.
    - [ ] Configurar pipeline de CI/CD (GitHub Actions) para build e deploy.
    - [ ] Revisar requisitos e `requirements.txt` (atualizar versões se necessário).
    - [ ] Melhorar acessibilidade (focus-trap no modal, keyboard navigation, roles/labels).