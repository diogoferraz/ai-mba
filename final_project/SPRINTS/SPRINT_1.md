### **4.1 Sprint 1: Planejamento**  

#### **Objetivo da Sprint**  
Definir e estruturar as ferramentas, recursos e processos necessários para o desenvolvimento do agente de investimentos autônomo, garantindo alinhamento com os requisitos do projeto e mitigação de riscos iniciais.  

---  

### **Evidências (Entregáveis)**  

| **Atividade**                          | **Ferramentas/Recursos**          | **Resultado Esperado**                                                                 |  
|----------------------------------------|----------------------------------|---------------------------------------------------------------------------------------|  
| Levantamento de requisitos das APIs    | Documentação das APIs (Neologica Profit, Yahoo Finance, Fundamentus), Postman (para testes) | Lista de endpoints necessários, limites de requisições e custos associados.           |  
| Configuração do ambiente Python        | VS Code, Jupyter Notebook, pip   | Ambiente configurado com bibliotecas (Pandas, NumPy, Requests) e virtualenv.           |  
| Protótipo de coleta de dados           | Yahoo Finance API (`yfinance`), Fundamentus (web scraping com BeautifulSoup) | Script funcional que extrai dados históricos de 1 ação (ex.: VALE3).                   |  
| Quadro de gestão (Trello/Jira)         | Trello (gratuito) ou Jira (versão free para estudantes)   | Backlog priorizado com tarefas da Sprint 1 e divisão de responsabilidades.             |  

---  

### **Lições Aprendidas (Retrospectiva)**  

#### **Ajustes Necessários:**  
1. **Dependência de APIs:**  
   - *Problema:* A API da Neologica Profit exige assinatura paga para acesso completo aos gregos em tempo real.  
   - *Solução:* Iniciar com dados estáticos ou limitados via Yahoo Finance e validar viabilidade antes do investimento.  

2. **Web Scraping no Fundamentus:**  
   - *Problema:* O site pode bloquear requisições frequentes sem headers adequados.  
   - *Solução:* Usar `requests.Session()` com delay entre requisições e rotacionar User-Agents.  

3. **Ambiente Python:**  
   - *Problema:* Conflito entre versões de bibliotecas (ex.: Pandas 2.x vs. 1.x).  
   - *Solução:* Criar um `requirements.txt` com versões fixas para replicabilidade (`pip freeze > requirements.txt`).  

---  

### **Ferramentas Definidas**  
- **Desenvolvimento:** Python 3.9+, Jupyter Notebook (para prototipagem rápida), NextJs para aplicativo web.  
- **APIs:** `yfinance` (Yahoo Finance), `requests` (Fundamentus), Neologica Profit (via token de acesso).  
- **Gestão:** Trello (para equipe pequena) com colunas: *To Do*, *Doing*, *Testing*, *Done*.  

---  

### ***Checklist* Final da Sprint 1**  
- [ ] Documentação das APIs revisada e endpoints mapeados.  
- [ ] Ambiente Python configurado com bibliotecas essenciais. 
- [ ] Ambiente NextJs configurado com bibliotecas essenciais.  
- [ ] Protótipo de coleta de dados funcional para pelo menos 1 ação.  
- [ ] Quadro de gestão atualizado com tarefas da Sprint 2 (*ex.: integração da Neologica*).  
