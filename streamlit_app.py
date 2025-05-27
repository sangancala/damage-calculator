import streamlit as st
import numpy as np

def calculate_values(actual_resistance, required_resistance, squad_power):
    missing_resist = required_resistance - actual_resistance
    dmg_factor = np.ceil(missing_resist  * 100 / required_resistance) / 100
    actual_dmg = max(1 - (2 * dmg_factor), 0.01)
    actual_power = squad_power * actual_dmg
    actual_dmg_reduction = 1 - actual_dmg
    
    return missing_resist, dmg_factor, actual_dmg, actual_power, actual_dmg_reduction

st.title('Season 2: Virus Resistance to Damage % Calculation')

# Input fields for user
actual_resistance = st.number_input('Actual Resistance', min_value=0, value=0)
required_resistance = st.number_input('Required Resistance', min_value=0, value=0)
squad_power = st.number_input('Squad Power', min_value=0, value=0)

if st.button('Calculate'):
    missing_resist, dmg_factor, actual_dmg, actual_power, actual_dmg_reduction = calculate_values(actual_resistance, required_resistance, squad_power)

    # Display results
    st.subheader('Results:')
    st.write(f'Actual DMG Reduction: {actual_dmg_reduction*100:.1f}%')
    st.write(f'Actual DMG: {actual_dmg*100:.1f}%')
    st.write(f'Actual Power: {actual_power:,.0f}')
