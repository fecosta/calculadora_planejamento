import streamlit as st

def calcular_planejamento():
    st.title("Calculadora de Planejamento de Aulas")

    # Entradas do usuário
    tempo_planejamento_por_aula = st.number_input("Tempo para planejar uma aula de 1h (em horas)", min_value=0.0, value=1.0, step=0.5)
    aulas_por_semana = st.number_input("Quantas aulas você dá por semana?", min_value=0, value=10, step=1)
    preco_hora_aula = st.number_input("Preço da sua hora/aula (R$)", min_value=0.0, value=100.0, step=10.0)

    if st.button("Calcular"):
        # Cálculos
        planejamento_por_semana = tempo_planejamento_por_aula * aulas_por_semana
        planejamento_por_mes = planejamento_por_semana * 4
        custo_planejamento_por_hora = preco_hora_aula / 2
        custo_total_planejamento_mensal = custo_planejamento_por_hora * planejamento_por_mes

        # Exibição dos resultados
        st.subheader("Resultados")
        st.write(f"Horas de planejamento por semana: **{planejamento_por_semana}h**")
        st.write(f"Horas de planejamento por mês: **{planejamento_por_mes}h**")
        st.write(f"Custo do planejamento por hora: **R${custo_planejamento_por_hora:.2f}**")
        st.write(f"Custo total do planejamento mensal: **R${custo_total_planejamento_mensal:.2f}**")

if __name__ == "__main__":
    calcular_planejamento()