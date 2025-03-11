# 📊 Metrics Observability App

Plataforma para medir, visualizar e melhorar o desempenho de equipes ágeis de desenvolvimento de software. Este projeto une princípios de engenharia de software, métricas ágeis e práticas de produto em uma única ferramenta interativa.

---

## 🚀 Objetivo

Desenvolver uma aplicação que permita capturar métricas-chave do processo de desenvolvimento, tanto de forma automática (via APIs do GitHub, Jira e SonarQube), quanto manual (inseridas pela própria equipe). Em seguida, visualizar e analisar essas métricas para identificar gargalos, otimizar entregas e melhorar a qualidade do software.

---

## 🧩 Componentes do Projeto

- **ETL e orquestração de dados**: com Apache Airflow  
- **Extração de métricas**: a partir do GitHub, Jira e SonarQube  
- **Banco de dados**: PostgreSQL (Neon.tech)  
- **Backend**: Flask ou Django (API REST)  
- **Frontend**: React ou Vue (visualização e entrada manual de métricas)  
- **Dashboard**: KPIs e gráficos em tempo real com Grafana ou Looker Studio  

---

## 📌 Métricas Analisadas

- 🕐 **Lead Time**  
- 🔄 **Cycle Time**  
- 🧪 **Cobertura de código**  
- ✅ **Velocidade por sprint**  
- 🛠️ **Pull Requests por desenvolvedor**  
- ⛔ **Erros por sprint**

---

## ⚙️ Como Executar o Projeto (quando estiver pronto)

### Clonar o repositório
```bash
git clone https://github.com/seu-usuario/metrics-observability-app.git
