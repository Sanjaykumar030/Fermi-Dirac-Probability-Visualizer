
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# Constants
k = 8.617e-5  # Boltzmann constant in eV/K

# Semiconductor parameters
Eg_intrinsic = 1.12   # Silicon bandgap at 0K (eV)
Eg_temp_coeff = -4.73e-4  # Eg temperature coefficient

def bandgap(T):
    return Eg_intrinsic + Eg_temp_coeff * T

def get_fermi_level(sem_type, Eg):
    if sem_type == "Intrinsic":
        return Eg / 2
    elif sem_type == "n-type":
        return Eg * 0.7
    elif sem_type == "p-type":
        return Eg * 0.3
    else:
        return Eg / 2

def get_E(E_relation, Ef, Eg):
    if E_relation == "E < Ef":
        return Ef - 0.05
    elif E_relation == "E = Ef":
        return Ef
    elif E_relation == "E > Ef":
        return Ef + 0.05
    else:
        return Ef

def fermi_dirac(E, Ef, T):
    if T == 0:
        if E < Ef:
            return 1.0
        elif E > Ef:
            return 0.0
        else:
            return 0.5
    return 1 / (1 + np.exp((E - Ef) / (k * T)))

def get_description(T, sem_type, E_relation, prob):
    temp_desc = f"Temperature = {T} K. "
    if T == 0:
        temp_desc += "At absolute zero, electron states are either fully occupied or empty.\n"
    else:
        temp_desc += "At finite temperature, occupation probabilities follow Fermi-Dirac distribution.\n"

    if sem_type == "Intrinsic":
        sem_desc = "Intrinsic semiconductor: Fermi level near middle of bandgap.\n"
    elif sem_type == "n-type":
        sem_desc = "n-type semiconductor: Fermi level shifted closer to conduction band.\n"
    else:
        sem_desc = "p-type semiconductor: Fermi level shifted closer to valence band.\n"

    if E_relation == "E < Ef":
        energy_desc = "Energy state is below Fermi level; state likely occupied.\n"
    elif E_relation == "E = Ef":
        energy_desc = "Energy state equals Fermi level; occupation probability is about 0.5.\n"
    else:
        energy_desc = "Energy state is above Fermi level; state likely unoccupied.\n"

    prob_desc = f"Occupation probability f(E) = {prob:.3f}"

    return temp_desc + sem_desc + energy_desc + prob_desc

# Initial parameters
init_T = 300
init_sem_type = "Intrinsic"
init_E_relation = "E = Ef"

fig, ax = plt.subplots(figsize=(8,6))
plt.subplots_adjust(left=0.38, bottom=0.35)  # Increased left margin from 0.3 to 0.38

vb_line, = ax.plot([0,1],[0,0], color='blue', lw=10, label="Valence Band (VB)")
cb_y = bandgap(init_T)
cb_line, = ax.plot([0,1],[cb_y,cb_y], color='red', lw=10, label="Conduction Band (CB)")

Ef = get_fermi_level(init_sem_type, cb_y)
fermi_line = ax.axhline(Ef, color='green', lw=2, label="Fermi Level (Ef)", linestyle='--')

E_val = get_E(init_E_relation, Ef, cb_y)
E_marker, = ax.plot(0.5, E_val, marker='o', color='black', markersize=12)
prob_text = ax.text(0.6, E_val + 0.02, "", fontsize=12)

# Description text box
ax_desc = fig.add_axes([0.1, 0.08, 0.6, 0.05])  # Below the slider
ax_desc.axis('off')  # Hide axis
desc_text = ax_desc.text(0, 0.5, "Description of current conditions here...", 
                         fontsize=10, va='center', ha='left',
                         bbox=dict(facecolor='lightgrey', alpha=0.5, boxstyle='round,pad=0.5'))


ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.2, cb_y + 0.3)
ax.set_xticks([])
ax.set_ylabel("Energy (eV)")
ax.set_title("Energy Band Diagram with Fermi Level and Occupation")
ax.legend(loc='upper right')

ax_temp = plt.axes([0.3, 0.2, 0.6, 0.03])
slider_temp = Slider(ax_temp, "Temperature (K)", 0, 1000, valinit=init_T, valstep=1)

ax_sem = plt.axes([0.05, 0.6, 0.2, 0.2], facecolor='lightyellow')
radio_sem = RadioButtons(ax_sem, ("Intrinsic", "n-type", "p-type"))

ax_Erel = plt.axes([0.05, 0.4, 0.2, 0.15], facecolor='lightcyan')
radio_Erel = RadioButtons(ax_Erel, ("E < Ef", "E = Ef", "E > Ef"))

def update(val):
    T = slider_temp.val
    sem_type = radio_sem.value_selected
    E_relation = radio_Erel.value_selected

    Eg = bandgap(T)
    cb_line.set_ydata([Eg, Eg])

    Ef_new = get_fermi_level(sem_type, Eg)
    fermi_line.set_ydata([Ef_new, Ef_new])

    E_new = get_E(E_relation, Ef_new, Eg)
    E_marker.set_ydata([E_new])

    prob = fermi_dirac(E_new, Ef_new, T)
    color = plt.cm.viridis(prob)
    E_marker.set_color(color)

    prob_text.set_position((0.6, E_new + 0.02))
    prob_text.set_text(f"f(E) = {prob:.3f}")

    # Update description text
    description = get_description(T, sem_type, E_relation, prob)
    desc_text.set_text(description)

    ax.set_ylim(-0.2, Eg + 0.3)

    fig.canvas.draw_idle()

slider_temp.on_changed(update)
radio_sem.on_clicked(update)
radio_Erel.on_clicked(update)

update(None)
plt.show()

