### **CAPA**
Nome da instituição: IbmecRJ
Nome do aluno: Diogo Costa Ferraz
Nome do projeto: Deseret Investments
Nome do orientador: Ítalo de Souza Lucena
Divinópolis, 14/04/2025  

### **3.1 Objetivo SMART**  

**Objetivo:**  
Desenvolver um agente de investimentos autônomo que auxilie investidores na tomada de decisões para compra e venda de opções (call e put) no mercado acionário brasileiro (Ibovespa), utilizando análise fundamentalista e indicadores gregos (delta, gama e theta), baseado nas estratégias do livro *Fique Rico Operando Opções*.  

**Específico:**  
- Criar um algoritmo capaz de analisar 5 ações específicas (VALE3, CMIG4, BBDC4, ABEV3, PETR4) e recomendar operações estruturadas.  
- Integrar APIs (Neologica Profit, Fundamentos, Yahoo Finance) para coleta de dados em tempo real.  
- Implementar análise de gregos (delta, gama, theta) para decisões estratégicas.  

**Mensurável:**  
- Acurácia das recomendações (taxa de acerto ≥ 70% em backtesting).  
- Redução de tempo na análise (de horas para minutos por operação).  
- Número de operações recomendadas com lucro consistente após 3 meses de testes.  

**Atingível:**  
- Utilizar Python e bibliotecas como Pandas, NumPy e Scikit-learn para modelagem.  
- Acesso às APIs disponíveis (Neologica Profit, Yahoo Finance e Fundamentus).  
- Base teórica consolidada (*Fique Rico Operando Opções*).  

**Relevante:**  
- Alinhado à demanda por automação e análise quantitativa no mercado financeiro.  
- Potencial para reduzir riscos e aumentar assertividade em operações com opções.  

**Temporal:**  
- Conclusão do MVP em 4 meses (16 semanas), divididos em sprints quinzenais.  

### **3.2 Proposta de Solução**  

**Solução Proposta:**  
Um agente automatizado que:  
1. **Coleta dados** via APIs (preços de strike, preço de exercício, valores de prêmio, gregos, IFR, balanços).  
2. **Processa indicadores** análise fundamentalista para decidir sobre a compra ou venda das açoes, e analise do cenário correte + gregos.  
3. **Gera recomendações** com base em estratégias do livro referência.  
4. **Apresenta resultados** em dashboard ou relatório simplificado. 

**Requisitos Técnicos:**  
- Linguagem: Python (bibliotecas: Pandas, Requests, Matplotlib).  
- Dados: APIs (Neologica Profit, Yahoo Finance), web scraping (Fundamentus).  
- Infraestrutura: Ambiente cloud (AWS/GCP) ou local (Jupyter Notebook).  

**Restrições e Riscos:**  
- Dependência de APIs externas (limitações de requisições, custos).  
- Volatilidade do mercado pode exigir ajustes frequentes no modelo.  
- Backtesting limitado a dados históricos disponíveis.  


### **3.3 Plano de Ação**  

**Backlog (4 Sprints de 2 semanas cada):**  

| **Sprint** | **Atividades** |  
|------------|---------------|  
| **Sprint 1** | - Levantamento de requisitos das APIs. <br> - Configuração do ambiente Python. <br> - Protótipo de coleta de dados (Yahoo Finance/ Fundamentus). |  
| **Sprint 2** | - Integração com API da Neologica Profit. <br> - Cálculo dos gregos (delta, gama, theta). <br> - Análise fundamentalista (P/L, Dívida líquida/EBITDA). |  
| **Sprint 3** | - Implementação das estratégias do livro. <br> - Backtesting com dados históricos. <br> - Validação com equipe de profissionais. |  
| **Sprint 4** | - Desenvolvimento do dashboard (Streamlit ou Power BI). <br> - Documentação final. <br> - Apresentação dos resultados. |  

**Ferramenta de Gestão:**  
- **Trello** ou **Jira** para acompanhamento das tarefas (exemplo de quadro):  
  - *To Do*: Tarefas pendentes.  
  - *Doing*: Em desenvolvimento.  
  - *Testing*: Validação.  
  - *Done*: Concluídas.  

