import streamlit as st
import yaml


# Load data from YAML file
with open('re2data.yaml','r') as file:
    data = yaml.safe_load(file)


st.title("CV Shield Calculator")
st.logo('shieldgeneratorcv.png')
shield_class = 'CV'  # TODO: Add support for other ship types

# Shield Generator Type
shield_types = list(data[shield_class]['Shield_Generator'].keys())

shieldgen_c = st.container()
#shieldgen_c.subheader("Shield Generator Type")
sg_col1, sg_col2 = shieldgen_c.columns([.3,1])

sg_col1.image('shieldgeneratorcv.png', use_container_width='auto')
sg_col2.subheader("Shield Generator Type")
sel_shield_type = sg_col2.selectbox("Select Shield Type", shield_types)

# Set initial values based on shield type
gen_capacity = data[shield_class]['Shield_Generator'][sel_shield_type]['Capacity']
gen_regen = data[shield_class]['Shield_Generator'][sel_shield_type]['Regen']
gen_cooldown = data[shield_class]['Shield_Generator'][sel_shield_type]['Cooldown']
gen_per_crystal = data[shield_class]['Shield_Generator'][sel_shield_type]['Per_Crystal']

st.divider()

# Shield Upgrade Boosters with Total Display and Alerts
su_col1, su_col2 = st.columns([.3,1])
su_col1.image('shieldcapacitorlarget2.png', use_container_width='auto')
su_col2.subheader("Shield Upgrades")

col1, col2, col3 = st.columns(3)

# Basic Upgrades
max_basic = data[shield_class]['Shield_Boosters']['Capacitor']['Basic']['Max']
col1.markdown("**Basic**")
basic_cap = col1.slider("Basic Capacitors", 0, max_basic, key="basic_cap")
basic_chg = col1.slider("Basic Chargers", 0, max_basic, key="basic_chg")
total_basic = basic_cap + basic_chg
if total_basic > max_basic:
    col1.markdown(f"**Basic Upgrades:** <span style='color:red'>{total_basic}/{max_basic} (Over Limit!)</span>", unsafe_allow_html=True)
else:
    col1.markdown(f"**Basic Upgrades:** {total_basic}/{max_basic}")

# Improved Upgrades
max_improved = data[shield_class]['Shield_Boosters']['Capacitor']['Improved']['Max']
col2.markdown("**Improved**")
improved_cap = col2.slider("Improved Capacitors", 0, max_improved, key="improved_cap")
improved_chg = col2.slider("Improved Chargers", 0, max_improved, key="improved_chg")
total_improved = improved_cap + improved_chg
if total_improved > max_improved:
    col2.markdown(f"**Improved Upgrades:** <span style='color:red'>{total_improved}/{max_improved} (Over Limit!)</span>", unsafe_allow_html=True)
else:
    col2.markdown(f"**Improved Upgrades:** {total_improved}/{max_improved}")

# Advanced Upgrades
max_advanced = data[shield_class]['Shield_Boosters']['Capacitor']['Advanced']['Max']
col3.markdown("**Advanced**")
advanced_cap = col3.slider("Advanced Capacitors", 0, max_advanced, key="advanced_cap")
advanced_chg = col3.slider("Advanced Chargers", 0, max_advanced, key="advanced_chg")
total_advanced = advanced_cap + advanced_chg
if total_advanced > max_advanced:
    col3.markdown(f"**Advanced Upgrades:** <span style='color:red'>{total_advanced}/{max_advanced} (Over Limit!)</span>", unsafe_allow_html=True)
else:
    col3.markdown(f"**Advanced Upgrades:** {total_advanced}/{max_advanced}")

# Calculate booster totals

sbdata = data[shield_class]['Shield_Boosters']

boosters_total_capacity = (
    (basic_cap * sbdata['Capacitor']['Basic']['Capacity']) + (basic_chg * sbdata['Capacitor']['Basic']['Regen']) +
    (improved_cap * sbdata['Capacitor']['Improved']['Capacity']) + (improved_chg * sbdata['Capacitor']['Improved']['Regen']) +
    (advanced_cap * sbdata['Capacitor']['Advanced']['Capacity']) + (advanced_chg * sbdata['Capacitor']['Advanced']['Regen'])
)

boosters_total_charge = (
    (basic_chg * sbdata['Recharger']['Basic']['Regen']) + (basic_cap * sbdata['Recharger']['Basic']['Capacity']) +
    (improved_chg * sbdata['Recharger']['Improved']['Regen']) + (improved_cap * sbdata['Recharger']['Improved']['Capacity']) +
    (advanced_chg * sbdata['Recharger']['Advanced']['Regen']) + (advanced_cap * sbdata['Recharger']['Advanced']['Capacity'])
)


st.divider()

# Fusion Reactors
fr_col1, fr_col2 = st.columns([.3,1])
fr_col1.image('fusionreactorlarge.png', use_container_width='auto')
fr_col2.subheader("Fusion Reactors")
fcol1, fcol2 = st.columns(2)
f_sm_max = data[shield_class]['Fusion_Reactor']['Small']['Max']
f_lg_max = data[shield_class]['Fusion_Reactor']['Large']['Max']
sm_fusion = fcol1.slider(f'Small Fusion Reactors (Max {f_sm_max})', 0, f_sm_max, key="sm_fusion")
lg_fusion = fcol2.slider(f'Large Fusion Reactors (Max {f_lg_max})', 0, f_lg_max, key="lg_fusion")
reactor_charge = (sm_fusion * data[shield_class]['Fusion_Reactor']['Small']['Regen']) + \
                 (lg_fusion * data[shield_class]['Fusion_Reactor']['Large']['Regen'])

st.divider()
# block charge
bl_col1, bl_col2 = st.columns([.3,1])
bl_col1.image('alienlargeblocks.png', use_container_width='auto')
bl_col2.subheader("Blocks")
steel_blocks = st.slider("Steel Blocks", 0, 10000, 0)
hsteel_blocks = st.slider("Hardened Steel Blocks", 0, 10000, 0)
csteel_blocks = st.slider("Combat Steel Blocks", 0, 10000, 0)
xeno_blocks = st.slider("Xeno Blocks", 0, 10000, 0)

steel = data[shield_class]['Blocks']['Steel']
hsteel = data[shield_class]['Blocks']['Hardened_Steel']
csteel = data[shield_class]['Blocks']['Combat_Steel']
xeno = data[shield_class]['Blocks']['Xeno_Steel']

block_capacity = (steel_blocks * steel) + (hsteel_blocks * hsteel) + (csteel_blocks * csteel) + (xeno_blocks * xeno)

st.write(f"**Block Capacity Bonus:** {block_capacity}")

# Final Totals
total_capacity = boosters_total_capacity + gen_capacity + block_capacity
total_charge = boosters_total_charge + gen_regen + reactor_charge

# Display Totals
#st.sidebar.subheader("Total Shield Stats")
#st.sidebar.markdown(f":blue[Shield Capacity]:  ")
#st.sidebar.markdown(f":green[**{total_capacity:,}**]")
#st.sidebar.write(f"**Capacity:** {total_capacity:,}")
#st.sidebar.write(f"**Shield Charge Rate:** {total_charge:,}/s")
#st.sidebar.write(f"**Time to Fully Charge:** {total_capacity / max(total_charge, 1):.1f} s")
#st.sidebar.write(f"**Charge Delay:** {gen_cooldown} s")

stats = f'''
## **Capacity:**  :blue[{total_capacity:,}]    
## **Recharge:**  :green[{total_charge:,}/s]  
## **Full Charge:**  :orange[{total_capacity / max(total_charge, 1):.1f} s]  
## **Charge Delay:** :red[{gen_cooldown} s]  
'''
st.sidebar.markdown(stats)
