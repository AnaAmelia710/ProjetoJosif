# ♻️ ProjetoJosif – Sistema de Gerenciamento de Lixo Eletrônico

Este projeto tem como objetivo **promover o descarte consciente de resíduos eletrônicos**, facilitando o acesso a pontos de coleta, campanhas de conscientização e o registro das ações dos moradores de uma comunidade.

---

## 🌱 Objetivos do Projeto

- Incentivar o descarte correto de lixo eletrônico.
- Mapear e exibir pontos de coleta em um mapa interativo.
- Cadastrar e gerenciar campanhas de conscientização.
- Registrar a participação dos moradores e seus descartes.
- Fornecer histórico e relatórios de descarte.

---

## 💻 Tecnologias Utilizadas

- **Python 3.11+**
- **Django 4+**
- **SQLite** (banco de dados padrão)
- **Bootstrap 4** (estilização)
- **Leaflet.js** (mapa interativo)
- **HTML5 + CSS3**
- **Git + GitHub** (versionamento)

---

## 📌 Funcionalidades

| Funcionalidade              | Descrição |
|----------------------------|-----------|
| 👥 Cadastro/Login/Logout   | Usuários podem se cadastrar e acessar o sistema. |
| 🗺️ Mapa de Pontos de Coleta | Visualização de pontos com localização via mapa. |
| 🔌 Tipos de Resíduos        | Cadastro e consulta dos tipos de lixo eletrônico. |
| 📍 Pontos de Coleta         | Cadastro dos locais com endereço e coordenadas. |
| 📦 Descarte de Resíduos     | Registro de quantidade, local e data de descarte. |
| 📢 Campanhas de Coleta      | Criação de campanhas em datas específicas. |
| 🧾 Histórico de Descartes   | Consulta dos registros por usuário. |

---

## 🧪 Como rodar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/AnaAmelia710/ProjetoJosif.git
cd ProjetoJosif

# Crie o ambiente virtual (se ainda não tiver)
python -m venv .venv
source .venv/Scripts/activate  # Windows
# ou
source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Rode o servidor local
python manage.py runserver
