### **Desenvolvimento do Projeto**  

### **4.2 Sprint 2: Planejamento**  

#### **Objetivo da Sprint**  
Implementar a integração com a API da Neologica Profit para coleta de dados em tempo real, calcular os gregos (delta, gama, theta) e iniciar a análise fundamentalista das ações selecionadas (VALE3, CMIG4, BBDC4, ABEV3, PETR4).  

---  

### **Evidências (Entregáveis)**  

| **Atividade**                          | **Ferramentas/Recursos**          | **Resultado Esperado**                                                                 |  
|----------------------------------------|----------------------------------|---------------------------------------------------------------------------------------|  
| Integração com API da Neologica Profit | Token de acesso à API, biblioteca `requests` (Python), documentação da API | Conexão estabelecida com a API e extração de dados de gregos e preços de opções.       |  
| Cálculo dos gregos (delta, gama, theta)| Pandas, NumPy, fórmulas matemáticas (Black-Scholes adaptado) | DataFrame com valores atualizados dos gregos para cada opção analisada.                |  
| Análise fundamentalista                | Web scraping (Fundamentus), métricas P/L, Dívida Líquida/EBITDA | Relatório comparativo das 5 ações com indicadores fundamentais.                        |  
| Validação de dados                     | Jupyter Notebook, testes unitários (`pytest`) | Dados consistentes e sem erros críticos (ex.: valores negativos para theta).           |  
| Dashboard inicial                      | Streamlit ou Power BI            | Visualização básica dos gregos e métricas fundamentais em gráficos/tabelas.           |  

---  

### **Lições Aprendidas (Retrospectiva)**  

#### **Ajustes Necessários:**  
1. **Limitações da API Neologica Profit:**  
   - *Problema:* Limite de requisições diárias no plano gratuito inviabiliza testes em escala.  
   - *Solução:* Priorizar ações específicas (ex.: VALE3) ou negociar acesso temporário ao plano premium.  

2. **Cálculo dos Gregos:**  
   - *Problema:* Fórmulas complexas exigem validação cruzada com fontes externas (ex.: plataformas como TradingView).  
   - *Solução:* Implementar uma função de comparação com dados públicos do Yahoo Finance.  

3. **Web Scraping no Fundamentus:**  
   - *Problema:* Estrutura HTML do site mudou, quebrando o script de coleta.  
   - *Solução:* Atualizar seletores CSS/XPath e adicionar tratamento de exceções (`try-except`).  

4. **Performance do Código:**  
   - *Problema:* Processamento dos gregos está lento para múltiplas opções simultâneas.  
   - *Solução:* Otimizar operações com `vectorize` do NumPy ou paralelizar tarefas (`multiprocessing`).  

---  

### **Ferramentas Definidas**  
- **APIs:** Neologica Profit (via token), Yahoo Finance (`yfinance`).  
- **Bibliotecas Python:** Pandas (análise), NumPy (cálculos), Streamlit (dashboard), `pytest` (testes).  
- **Gestão:** Trello atualizado com novas tarefas da Sprint 3 (*ex.: backtesting*).  

---  

### ***Checklist* Final da Sprint 2**  
- [ ] Integração completa com a API da Neologica Profit funcional.  
- [ ] Cálculo automatizado dos gregos para as 5 ações-alvo.  
- [ ] Relatório fundamentalista gerado para todas as ações.    
- [ ] Dashboard mínimo criado para visualização dos dados (*exemplo abaixo*).    

#### ***Exemplo de Dashboard no Streamlit***:    
```python
import streamlit as st
import pandas as pd

st.title("Deseret Investments - Análise de Opções")
dados = pd.read_csv("dados_gregos.csv")
st.line_chart(dados[["delta", "gamma", "theta"]].head(20))
```