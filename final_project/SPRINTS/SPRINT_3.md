### Capa
- Nome da instituição: IbmecRJ
- Nome do aluno: Diogo Costa Ferraz
- Nome do projeto: Deseret Investments
- Nome do orientador: Ítalo de Souza Lucena
- Divinópolis, 06/05/2025 

## 4.3 Sprint 3: Planejamento

### Objetivo da Sprint
Implementar estratégias de operações com opções baseadas no livro "Fique Rico Operando Opções", realizar backtesting com dados históricos e validar o modelo com profissionais do mercado financeiro.

### Evidências (Entregáveis)

| Atividade                          | Ferramentas/Recursos                     | Resultado Esperado                                                                 |
|------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------|
| Implementação das estratégias      | Livro referência, Python (Pandas/NumPy)  | Código funcional que aplica 3 estratégias principais do livro (ex: spread vertical) |
| Backtesting com dados históricos   | Dados Yahoo Finance (2015-2025),         | Relatório com taxa de acerto ≥70% em operações simuladas                          |
|                                    | Backtrader ou PyAlgoTrade                 |                                                                                   |
| Validação com profissionais        | Entrevistas com traders/analistas        | Documento com feedbacks e ajustes sugeridos para o modelo                         |
| Otimização do dashboard            | Streamlit/Power BI, Plotly               | Visualizações interativas de performance histórica por estratégia                 |

### Lições Aprendidas (Retrospectiva)

#### Ajustes Necessários:
1. **Dados Históricos Incompletos**
   - *Problema:* Falta de dados de gregos históricos nas APIs gratuitas
   - *Solução:* Usar aproximações matemáticas baseadas em preços spot e IV

2. **Latência no Backtesting**
   - *Problema:* Processamento lento ao testar múltiplas estratégias
   - *Solução:* Implementar cache com `joblib` e reduzir timeframe analisado

3. **Validação Profissional**
   - *Problema:* Dificuldade em alinhar horários com especialistas
   - *Solução:* Criar formulário padronizado no Google Forms para coleta assíncrona

4. **Divergência Teórica-Prática**
   - *Problema:* Estratégias do livro não consideram taxas de corretagem
   - *Solução:* Incluir custos fixos por operação no cálculo de rentabilidade

### Ferramentas Definidas
- **Backtesting:** Biblioteca Backtrader (Python)
- **Visualização:** Plotly + Streamlit para gráficos interativos
- **Documentação:** Google Docs compartilhado para registro dos feedbacks

### Checklist Final da Sprint 3
- [ ] 3 estratégias principais implementadas no código
- [ ] Relatório de backtesting com métricas de performance
- [ ] Feedback de pelo menos 2 profissionais incorporado
- [ ] Dashboard atualizado com abas por tipo de estratégia