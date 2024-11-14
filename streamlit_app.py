import streamlit as st

st.title("CV Shield Calculator")

# Shield Generator Type Selection
st.subheader("Shield Generator Type")
shield_types = ["Compact", "Regular", "Advanced"]
sel_shield_type = st.radio("Select Shield Type", shield_types)

# Set initial values based on shield type
gen_capacity, gen_regen, gen_cooldown, gen_per_crystal = 0, 0, 0, 0
if sel_shield_type == "Advanced":
    gen_capacity, gen_regen, gen_cooldown, gen_per_crystal = 24000, 600, 15, 1000
elif sel_shield_type == "Regular":
    gen_capacity, gen_regen, gen_cooldown, gen_per_crystal = 12000, 300, 20, 750
elif sel_shield_type == "Compact":
    gen_capacity, gen_regen, gen_cooldown, gen_per_crystal = 6000, 300, 25, 500

# Shield Upgrade Boosters with Total Display and Alerts
st.subheader("Shield Upgrades")

col1,col2,col3 = st.columns(3)

# Basic Upgrades
max_basic = 8
col1.markdown("**Basic**")
basic_cap = col1.slider("Basic Capacitors", 0, max_basic, key="basic_cap")
basic_chg = col1.slider("Basic Chargers", 0, max_basic, key="basic_chg")
total_basic = basic_cap + basic_chg
if total_basic > max_basic:
    col1.markdown(f"**Basic Upgrades:** <span style='color:red'>{total_basic}/{max_basic} (Over Limit!)</span>", unsafe_allow_html=True)
else:
    col1.markdown(f"**Basic Upgrades:** {total_basic}/{max_basic}")

# Improved Upgrades
max_improved = 6
col2.markdown("**Improved**")
improved_cap = col2.slider("Improved Capacitors", 0, max_improved, key="improved_cap")
improved_chg = col2.slider("Improved Chargers", 0, max_improved, key="improved_chg")
total_improved = improved_cap + improved_chg
if total_improved > max_improved:
    col2.markdown(f"**Improved Upgrades:** <span style='color:red'>{total_improved}/{max_improved} (Over Limit!)</span>", unsafe_allow_html=True)
else:
    col2.markdown(f"**Improved Upgrades:** {total_improved}/{max_improved}")

# Advanced Upgrades
max_advanced = 4
col3.markdown("**Advanced**")
advanced_cap = col3.slider("Advanced Capacitors", 0, max_advanced, key="advanced_cap")
advanced_chg = col3.slider("Advanced Chargers", 0, max_advanced, key="advanced_chg")
total_advanced = advanced_cap + advanced_chg
if total_advanced > max_advanced:
    col3.markdown(f"**Advanced Upgrades:** <span style='color:red'>{total_advanced}/{max_advanced} (Over Limit!)</span>", unsafe_allow_html=True)
else:
    col3.markdown(f"**Advanced Upgrades:** {total_advanced}/{max_advanced}")

# Calculate booster totals
boosters_total_capacity = (
    (basic_cap * 8000) + (basic_chg * -4000) +
    (improved_cap * 16000) + (improved_chg * -8000) +
    (advanced_cap * 32000) + (advanced_chg * -16000)
)
boosters_total_charge = (
    (basic_chg * 300) + (basic_cap * -150) +
    (improved_chg * 600) + (improved_cap * -300) +
    (advanced_chg * 1200) + (advanced_cap * -600)
)


# Fusion Reactors
st.subheader("Fusion Reactors")
fcol1, fcol2 = st.columns(2)
sm_fusion = fcol1.slider("Small Fusion Reactors (Max 4)", 0, 4, key="sm_fusion")
lg_fusion = fcol2.slider("Large Fusion Reactors (Max 2)", 0, 2, key="lg_fusion")
reactor_charge = (sm_fusion * 250) + (lg_fusion * 1000)

# Final Totals
total_capacity = boosters_total_capacity + gen_capacity
total_charge = boosters_total_charge + gen_regen + reactor_charge

# Display Totals
st.subheader("Total Shield Stats")
st.write(f"**Shield Capacity:** {total_capacity}")
st.write(f"**Shield Charge Rate:** {total_charge}/s")
st.write(f"**Time to Fully Charge:** {total_capacity / max(total_charge, 1):.1f} s")
st.write(f"**Charge Delay:** {gen_cooldown} s")

