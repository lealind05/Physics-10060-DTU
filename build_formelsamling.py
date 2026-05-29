"""Bygger Formelsamling.ipynb fra Mandags-slides og Fysik_noter.

Kør:  python3 build_formelsamling.py
Output: Formelsamling.ipynb i samme mappe.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "Formelsamling.ipynb"


def md(src: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": src.splitlines(keepends=True),
    }


def code(src: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": src.splitlines(keepends=True),
    }


cells: list[dict] = []

# =====================================================================
# Forside / indholdsfortegnelse
# =====================================================================
cells.append(md(r"""# Formelsamling – Fysik PG 10060 (DTU)

Søgbar oversigt over alle formler fra **mandags-forelæsningerne**
(Lecture 1–13). Bygget fra slides "Relevante formler" og krydstjekket
mod `Fysik_noter (1).pdf`.

**Sådan bruger du den:**
- Brug `Ctrl/Cmd + F` i Jupyter for at søge efter et begreb (fx
  "centripetal", "impuls", "Stokes", "drag").
- Hvert afsnit svarer til én uge / ét lecture.
- Symboler følger DTU-notation (vektorer med pil, skalarer uden).

## Indholdsfortegnelse
1. [Kinematik 1D](#1)
2. [Kinematik 2D](#2)
3. [Usikkerhed](#3)
4. [Eksperimenter & dimensionsanalyse](#4)
5. [Kræfter 1 – Newtons love](#5)
6. [Kræfter 2 – Modstand, drag & cirkelbevægelse](#6)
7. [Bevægelsesligninger (numerisk)](#7)
8. [Arbejde og energi](#8)
9. [Potentiel energi og energibevarelse](#9)
10. [Stød og impulsbevarelse](#10)
11. [Rotation 1 – Inertimomenter](#11)
12. [Rotation 2 – Kraftmoment & impulsmoment](#12)
13. [Energitema – Flywheels](#13)

**Konstanter**

| Symbol | Værdi | Betydning |
|---|---|---|
| $g$ | $9{,}82~\text{m/s}^2$ | Tyngdeacceleration ved jordoverfladen |
| $G$ | $6{,}674\cdot 10^{-11}~\text{N m}^2/\text{kg}^2$ | Gravitationskonstanten |
"""))

# =====================================================================
# Uge 1 – Kinematik 1D
# =====================================================================
cells.append(md(r"""<a id="1"></a>
## Uge 1 – Kinematik 1D

**Kapitel 3 – fra slide "Relevante formler".**

### Gennemsnit (definitioner)

$$\bar v = \frac{\Delta x}{\Delta t}, \qquad \bar a = \frac{\Delta v}{\Delta t}$$

### Konstant acceleration (4 ligninger)

| Ligning | Mangler |
|---|---|
| $v = v_0 + a t$ | $x$ |
| $x = x_0 + \tfrac{1}{2}(v_0 + v)\,t$ | $a$ |
| $x = x_0 + v_0 t + \tfrac{1}{2}\,a t^{2}$ | $v$ |
| $v^{2} = v_0^{2} + 2a(x - x_0)$ | $t$ |

### Generel acceleration (integration)

$$\frac{dv}{dt}=a \;\Rightarrow\; v(t)=\int_0^{t} a(t')\,dt' + v_0$$

$$\frac{dx}{dt}=v \;\Rightarrow\; x(t)=\int_0^{t} v(t')\,dt' + x_0$$

### Frit fald (positiv y opad)

$$v = v_0 - g t, \qquad y = y_0 + v_0 t - \tfrac{1}{2}\,g t^{2}$$
"""))

# =====================================================================
# Uge 2 – Kinematik 2D
# =====================================================================
cells.append(md(r"""<a id="2"></a>
## Uge 2 – Kinematik 2D

**Kapitel 4.**

### Projektilbevægelse (skrå kast)

Generelt (med $v_{0x}=v_0\cos\theta$, $v_{0y}=v_0\sin\theta$):

$$x(t) = v_{0x}\,t \qquad y(t) = v_{0y}\,t - \tfrac{1}{2}g t^{2}$$

$$v_x(t) = v_{0x} \qquad v_y(t) = v_{0y} - g t$$

$$v_y^{2} = v_{0y}^{2} - 2g(y-y_0)$$

Baneligning:

$$y(x) = y_0 + \tan\theta \cdot x - \frac{g}{2 v_0^{2}\cos^{2}\theta}\,x^{2}$$

### Affyring og landing i samme højde

$$T_{\text{tof}} = \frac{2 v_0 \sin\theta}{g} \quad\text{(time of flight)}$$

$$y_{\max} = \frac{(v_0\sin\theta)^{2}}{2g} \quad\text{(højeste punkt)}$$

$$R = \frac{v_0^{2}\sin(2\theta)}{g} \quad\text{(rækkevidde)}$$

### Cirkelbevægelse

$$v = \frac{2\pi r}{T}, \qquad a_c = \frac{v^{2}}{r}, \qquad a_t = \frac{d|\vec v|}{dt}$$

### Relativ bevægelse (Galilei)

$$\vec v_{PS} = \vec v_{PS'} + \vec v_{S'S}, \qquad \vec a_{PS} = \vec a_{PS'} + \vec a_{S'S}$$

### Nyttige trigonometriske formler

$$\sin(2\theta) = 2\sin\theta\cos\theta, \qquad \tan\theta = \frac{\sin\theta}{\cos\theta}$$
"""))

# =====================================================================
# Uge 3 – Usikkerhed
# =====================================================================
cells.append(md(r"""<a id="3"></a>
## Uge 3 – Usikkerhed

### Notation

- $x$  = bedste bud på størrelse
- $\delta x$  = usikkerhed (altid positiv)
- $x \pm \delta x$  = absolut usikkerhed
- $\dfrac{\delta x}{|x|}$  = relativ usikkerhed

### Måleserie (stikprøve, N datapunkter)

Standardafvigelsen:

$$\delta x \;=\; \sqrt{\frac{\sum_i (\bar x - x_i)^{2}}{N-1}}$$

Standardafvigelsen på gennemsnittet (SDOM):

$$\delta \bar x \;=\; \frac{\delta x}{\sqrt{N}}$$

### Normalfordeling

$$f(x) = \frac{1}{\sqrt{2\pi}\,\sigma}\, e^{-\tfrac{1}{2}\left(\tfrac{x-\mu}{\sigma}\right)^{2}}$$

| Interval | Sandsynlighed |
|---|---|
| $\mu \pm \delta x$ | 0,68 |
| $\mu \pm 2\delta x$ | 0,95 |
| $\mu \pm 3\delta x$ | 0,99 |

### Fejlophobningsloven (generelt)

For $z = f(x, y)$ med $x \pm \delta x,\; y \pm \delta y$:

$$\text{Uafhængige:}\quad \delta z = \sqrt{\left(\tfrac{\partial f}{\partial x}\,\delta x\right)^{2} + \left(\tfrac{\partial f}{\partial y}\,\delta y\right)^{2}}$$

$$\text{Afhængige:}\quad \delta z = \left|\tfrac{\partial f}{\partial x}\right|\delta x + \left|\tfrac{\partial f}{\partial y}\right|\delta y$$

### Specialtilfælde: $z = x \pm y$

$$\text{Uafhængige:}\quad z \pm \delta z = x \pm y \pm \sqrt{\delta x^{2} + \delta y^{2}}$$

$$\text{Afhængige:}\quad z \pm \delta z = x \pm y \pm (\delta x + \delta y)$$

### Specialtilfælde: $z = x \cdot y$ (eller $x/y$)

$$\text{Uafhængige (relativ):}\quad \frac{\delta z}{|z|} = \sqrt{\left(\frac{\delta x}{|x|}\right)^{2} + \left(\frac{\delta y}{|y|}\right)^{2}}$$

$$\text{Afhængige (relativ):}\quad \frac{\delta z}{|z|} = \frac{\delta x}{|x|} + \frac{\delta y}{|y|}$$

### Tilfældige vs. systematiske usikkerheder

$$\delta x = \sqrt{\delta x_{\text{tilfældige}}^{2} + \delta x_{\text{systematiske}}^{2}}$$
"""))

# =====================================================================
# Uge 4 – Eksperimenter / dimensionsanalyse
# =====================================================================
cells.append(md(r"""<a id="4"></a>
## Uge 4 – Eksperimenter & dimensionsanalyse

### Vurdering af målinger med stdscore

$$\text{stdscore} = \frac{x - \bar x}{\delta \bar x} \quad(\text{for et tal})$$

$$\text{stdscore} = \frac{x - \bar x}{\delta x} \quad(\text{for en fordeling})$$

| stdscore | Vurdering |
|---|---|
| $< 2$ | Good |
| $2 \le \cdot < 3$ | Grey zone |
| $\ge 3$ | Reject |

### Sammenligning af to målinger

$$z = x - y, \qquad \delta z = \sqrt{\delta x^{2} + \delta y^{2}}, \qquad \text{stdscore} = \frac{|z|}{\delta z}$$

### Naturlige skalaer (dimensionsløse størrelser)

| Symbol | Skala | Dimension |
|---|---|---|
| $\mu = m$ | masseskala | $M$ |
| $\lambda = l$ | længdeskala | $L$ |
| $\tau = \sqrt{l/g}$ | tidsskala | $T$ |
| $\alpha = \lambda/\tau^{2}$ | accelerationsskala | $L/T^{2}$ |

### Dimensionsløs formulering

Eksempel: model $v_2 = f(v_1, a, x)$ giver

$$\frac{v_2}{v_1} = F\!\left(\frac{a x}{v_1^{2}}\right) \;\Leftrightarrow\; \pi_1 = F(\pi_2)$$

### Dimensionsmatricen (Buckingham $\pi$)

For $X = m^{A} \cdot g^{B} \cdot h^{C} \cdot k^{D}$
$= m^{A} \cdot (L/T^{2})^{B} \cdot L^{C} \cdot (M\cdot T^{-1})^{D}$
$= M^{A+D} \cdot L^{B+C} \cdot T^{-2B-D}$

|  | $m$ | $g$ | $h$ | $k$ |
|---|---|---|---|---|
| $M$ | $1$ | $0$ | $0$ | $1$ |
| $L$ | $0$ | $1$ | $1$ | $0$ |
| $T$ | $0$ | $-2$ | $0$ | $-1$ |
"""))

# =====================================================================
# Uge 5 – Kræfter 1
# =====================================================================
cells.append(md(r"""<a id="5"></a>
## Uge 5 – Kræfter 1 (Newtons love)

**Kapitel 5.** Enhed: $[N] = \text{kg}\cdot\text{m}/\text{s}^{2}$.

### Newtons tre love

**N1** (træghedsloven):

$$\sum \vec F = 0 \;\Rightarrow\; \vec v = \text{konstant}$$

**N2** (bevægelsesligningen):

$$\sum \vec F = m \vec a$$

**N3** (action/reaction):

$$\vec F_{AB} = - \vec F_{BA}$$

### Fem vigtige kræfter i mekanik

| Kraft | Formel / egenskab |
|---|---|
| **Tyngdekraft** | $\vec w = \vec F_g = m \vec g$ |
| **Normalkraft** | Vinkelret på underlaget; proportional med friktionen |
| **Snorkraft (tension)** | Ens i hele snoren hvis samme snor |
| **Kinematisk gnidning** | $f_k = \mu_k \cdot n$ |
| **Statisk gnidning** | $f_s \le \mu_s \cdot n$ |
| **Fjederkraft (Hookes lov)** | $\vec F = -k(x - x_0)$ |
"""))

# =====================================================================
# Uge 6 – Kræfter 2
# =====================================================================
cells.append(md(r"""<a id="6"></a>
## Uge 6 – Kræfter 2 (modstand, drag, cirkelbevægelse)

**Kapitel 6.**

### Hookes lov for fjederkraft

$$F_{\text{fjeder}} = -k\,(x - x_0)$$

### Luft- og vandmodstand

| Type | Udtryk |
|---|---|
| Generelt | $F_d = b\,v^{n}$ |
| Drag (turbulent) | $f = D\,v^{2}$, med $D = \tfrac{1}{2}\rho_{\text{luft}} C_D A$ |
| Stokes' lov (lille, rundt objekt, lav fart) | $F_s = 6\pi r \eta v$ |

### Cirkelbevægelse (polære koordinater)

Position: $\vec r = (x, y) = (r\cos\theta,\, r\sin\theta)$

$$r = \sqrt{x^{2} + y^{2}}, \qquad \theta = \tan^{-1}\!\left(\frac{y}{x}\right)$$

Vinkelhastighed og -acceleration:

$$\omega = \frac{d\theta}{dt}, \qquad \alpha = \frac{d\omega}{dt} = \frac{d^{2}\theta}{dt^{2}}$$

Sammenhæng mellem vinkel- og lineær-størrelser:

$$v = r\omega, \qquad a_t = \frac{dv}{dt} = r\alpha$$

Centripetalacceleration:

$$a_c = v\omega = r\omega^{2} = \frac{v^{2}}{r}$$

Bemærk: $a_t = 0$ ved cirkelbevægelse med konstant fart.

Periode:

$$v = \frac{\text{omkreds}}{\text{periode}} = \frac{2\pi R}{T}$$
"""))

# =====================================================================
# Uge 7 – Bevægelsesligninger
# =====================================================================
cells.append(md(r"""<a id="7"></a>
## Uge 7 – Bevægelsesligninger (numerisk integration)

**Kapitel 15 + Python notes.**

### Eulers metode

$$x(t + \Delta t) \approx x(t) + v(t)\,\Delta t$$

$$v(t + \Delta t) \approx v(t) + a(t)\,\Delta t$$

### Euler–Cromer (semi-implicit)

$$v(t + \Delta t) \approx v(t) + a(t)\,\Delta t$$

$$x(t + \Delta t) \approx x(t) + v(t + \Delta t)\,\Delta t$$

Bemærk: Brug den **nye** $v$ til at opdatere $x$. Euler–Cromer
bevarer energien bedre end ren Euler for oscillatorer.

### SciPy – numerisk løsning

Se kodeeksempel nedenfor.
"""))

cells.append(code('''"""Eksempel: Frit fald med luftmodstand – Euler, Euler-Cromer og solve_ivp.

Modellen: m a = -m g - b v   (positiv y opad).
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g, m, b = 9.82, 1.0, 0.1
v0, y0 = 0.0, 100.0
t_end, dt = 6.0, 0.01
N = int(t_end / dt)

# --- Euler ---
t = np.zeros(N); y = np.zeros(N); v = np.zeros(N)
y[0], v[0] = y0, v0
for i in range(N - 1):
    a = -g - (b / m) * v[i]
    y[i+1] = y[i] + v[i] * dt
    v[i+1] = v[i] + a * dt
    t[i+1] = t[i] + dt

# --- Euler-Cromer ---
yc = np.zeros(N); vc = np.zeros(N)
yc[0], vc[0] = y0, v0
for i in range(N - 1):
    a = -g - (b / m) * vc[i]
    vc[i+1] = vc[i] + a * dt
    yc[i+1] = yc[i] + vc[i+1] * dt   # bruger nye v

# --- solve_ivp (RK45) ---
def rhs(t, s):
    y, v = s
    return [v, -g - (b / m) * v]

# Event: stop når y rammer 0
def hit_ground(t, s): return s[0]
hit_ground.terminal = True
hit_ground.direction = -1

sol = solve_ivp(rhs, [0, t_end], [y0, v0], events=hit_ground, max_step=0.01)

plt.plot(t, y, label="Euler")
plt.plot(t, yc, label="Euler-Cromer")
plt.plot(sol.t, sol.y[0], "--", label="solve_ivp")
plt.xlabel("t [s]"); plt.ylabel("y [m]"); plt.legend(); plt.grid(True)
plt.title("Frit fald med luftmodstand")
plt.show()
print(f"solve_ivp ramte jorden ved t = {sol.t_events[0][0]:.3f} s")
'''))

# =====================================================================
# Uge 8 – Arbejde og energi
# =====================================================================
cells.append(md(r"""<a id="8"></a>
## Uge 8 – Arbejde og energi

**Kapitel 7.**

### Konstant kraft, ret linje

$$W = \vec F \cdot \vec s = F s \cos\phi$$

hvor $\phi$ er vinklen mellem $\vec F$ og $\vec s$.

### Positionsafhængig kraft, ret linje

$$W = \int_{x_1}^{x_2} F(x)\, dx$$

| Eksempel | Arbejde |
|---|---|
| Fjederkraft | $W_{\text{fjeder}} = \tfrac{1}{2} k x_1^{2} - \tfrac{1}{2} k x_2^{2}$ |
| Tyngdekraft | $W_{\text{tyngde}} = m g (x_1 - x_2)$ |

### Kraft langs kurvet bevægelse

$$W = \int_{P_1}^{P_2} \vec F \cdot d\vec l$$

### Arbejdssætningen (kinetisk energi)

$$W_{\text{tot}} = \Delta K = K_2 - K_1, \qquad K = \tfrac{1}{2} m v^{2}$$

### Effekt (konstant kraft, ret linje)

$$P = \frac{\Delta W}{\Delta t} = F v$$

Enhed: $1~\text{W} = 1~\text{J/s}$.
"""))

# =====================================================================
# Uge 9 – Potentiel energi & energibevarelse
# =====================================================================
cells.append(md(r"""<a id="9"></a>
## Uge 9 – Potentiel energi og energibevarelse

**Kapitel 8.**

### Bevarelse af mekanisk energi (tyngde + fjeder)

$$\tfrac{1}{2} m v_1^{2} + m g y_1 + \tfrac{1}{2} k x_1^{2}
= \tfrac{1}{2} m v_2^{2} + m g y_2 + \tfrac{1}{2} k x_2^{2}$$

### Den udvidede energisætning

$$K_1 + U_1 + W_{\text{andre}} = K_2 + U_2$$

$W_{\text{andre}}$ er arbejdet af ikke-konservative kræfter (fx friktion).

### Konservativ kraft – definition

$W_{\text{tot}}$ langs en hvilken som helst lukket vej (start = slut) er nul:

$$\oint \vec F \cdot d\vec l = 0$$

### Almindelige energiformer

| Form | Udtryk |
|---|---|
| Kinetisk energi | $E = \tfrac{1}{2} m v^{2}$ |
| Potentiel energi (tyngde) | $U = m g h$ |
| Potentiel energi (fjeder) | $U = \tfrac{1}{2} k x^{2}$ |
| Elektrisk energi | $E = U I \Delta t = \tfrac{U^{2}}{R}\Delta t$ |
| Indre energi (ideal gas) | $E = c_v N T$ |
| Kerneenergi | $E = m c^{2}$ |
| Strålingsenergi (foton) | $E = \hbar \omega$ |
"""))

# =====================================================================
# Uge 10 – Impuls
# =====================================================================
cells.append(md(r"""<a id="10"></a>
## Uge 10 – Stød og impulsbevarelse

**Kapitel 9.** Sproglig afklaring:

| Dansk | Engelsk | Størrelse |
|---|---|---|
| Impuls / bevægelsesmængde | momentum | $\vec p = m\vec v$ |
| Kraftens impuls (impulsændring) | impulse | $\vec J = \Delta \vec p = \int_{t_1}^{t_2} \vec F(t)\, dt$ |

### Kinetisk energi på impulsform

$$K = \frac{p^{2}}{2m}$$

### Newtons 2. lov på impulsform

$$\sum \vec F = \frac{d\vec p}{dt}$$

### Impulsbevarelse (isoleret system, 2 partikler)

$$m_A v_{A1} + m_B v_{B1} = m_A v_{A2} + m_B v_{B2}$$

### Energibevarelse ved elastisk stød (1D)

$$v_{B2} - v_{A2} = -(v_{B1} - v_{A1})$$

(Relativ hastighed vender om i tegn.)

### Tre typer af kollisioner

| Type | Impuls | Kinetisk energi | Note |
|---|---|---|---|
| Elastisk | Bevaret | Bevaret | |
| Uelastisk | Bevaret | Ikke bevaret | |
| Fuldstændig uelastisk | Bevaret | Ikke bevaret | Fælleshastighed før eller efter |
"""))

# =====================================================================
# Uge 11 – Rotation 1
# =====================================================================
cells.append(md(r"""<a id="11"></a>
## Uge 11 – Rotation 1 (inertimomenter)

**Kapitel 10.**

### Rotationsenergi

$$K_{\text{rot}} = \tfrac{1}{2} I \omega^{2}$$

### Kinetisk energi af legeme der både roterer og translaterer

$$K = K_{\text{rot}} + K_{\text{trans}} = \tfrac{1}{2} I_{cm} \omega^{2} + \tfrac{1}{2} M v_{cm}^{2}$$

hvor $cm$ = center of mass (massemidtpunkt).

### Energibevarelse for legeme i rotation + translation

$$K_{1,\text{trans}} + K_{1,\text{rot}} + U_1 + W_{\text{other}}
= K_{2,\text{trans}} + K_{2,\text{rot}} + U_2$$

### Parallelaksesætningen

$$I_{\parallel} = I_{cm} + M d^{2}$$

hvor $d$ = afstand fra cm-aksen til den parallelle akse.

### Inertimomenter – almindelige objekter

Aksen går gennem massemidtpunktet med mindre andet angives.

| Legeme | Akse | $I$ |
|---|---|---|
| Tynd stang, længde $L$ | gennem midten, vinkelret | $\tfrac{1}{12} M L^{2}$ |
| Tynd stang, længde $L$ | gennem enden, vinkelret | $\tfrac{1}{3} M L^{2}$ |
| Massiv cylinder/skive, radius $R$ | symmetriaksen | $\tfrac{1}{2} M R^{2}$ |
| Tynd cylinderskal (hoop), radius $R$ | symmetriaksen | $M R^{2}$ |
| Tyk cylinderskal (radier $R_1, R_2$) | symmetriaksen | $\tfrac{1}{2} M (R_1^{2}+R_2^{2})$ |
| Massiv kugle, radius $R$ | gennem centrum | $\tfrac{2}{5} M R^{2}$ |
| Tynd kugleskal, radius $R$ | gennem centrum | $\tfrac{2}{3} M R^{2}$ |
| Tynd plade ($a\times b$) | gennem centrum, vinkelret | $\tfrac{1}{12} M (a^{2}+b^{2})$ |
"""))

# =====================================================================
# Uge 12 – Rotation 2
# =====================================================================
cells.append(md(r"""<a id="12"></a>
## Uge 12 – Rotation 2 (kraftmoment & impulsmoment)

**Kapitel 11.**

### Kraftmoment (torque)

$$\vec \tau = \vec R \times \vec F$$

### Newtons 2. lov for rotation (impulsmomentsætningen, IMS)

$$I_{cm}\,\alpha = \sum \tau_{cm}, \qquad M \vec a_{cm} = \sum \vec F_{\text{ydre}}$$

Den centrale idé: bevægelsen opdeles i (1) bevægelsen af MM og
(2) rotationen omkring MM.

### Geometrisk bånd ved ren rulning

$$x_{cm} = R\theta, \qquad v_{cm} = R\omega, \qquad a_{cm} = R\alpha$$

### Impulsmoment (vinkelmoment)

$$\vec L = \vec R \times \vec p = R_{\perp}\, p$$

$$L = I \omega$$

### Bevarelse af impulsmoment

Hvis $\sum \tau = 0$:

$$\frac{dL}{dt} = 0 \;\Rightarrow\; L = \text{konstant} \;\Rightarrow\; I_1 \omega_1 = I_2 \omega_2$$

### Translation $\leftrightarrow$ rotation (analogi)

| Translation | Rotation |
|---|---|
| $x(t)$ | $\theta(t)$ |
| $v = dx/dt$ | $\omega = d\theta/dt$ |
| $a = dv/dt$ | $\alpha = d\omega/dt$ |
| $m$ | $I$ |
| $K = \tfrac{1}{2} m v^{2}$ | $K = \tfrac{1}{2} I \omega^{2}$ |
| $F = m a$ | $\tau = I \alpha$ |
| $p = m v$ | $L = I \omega$ |
"""))

# =====================================================================
# Uge 13 – Energitema / Flywheels
# =====================================================================
cells.append(md(r"""<a id="13"></a>
## Uge 13 – Energitema (flywheels)

**Strategi for max energi i et flywheel:**
1. Simplificér geometrien (tyndt cylinderbånd).
2. Antag konstant cirkelbevægelse.
3. Find materialets stress $\sigma$.
4. Relatér stress til kinetisk energi.
5. Find den begrænsende energi-tæthed for givne materialer.

### Stress (materialespænding)

$$\sigma = \frac{F}{A}, \qquad [\sigma] = \text{Pa} = \text{N/m}^{2}$$

Strain (relativ deformation):

$$\epsilon = \frac{\Delta L}{L_0}$$

### Geometri – tyndt cylinderbånd

Indre radius $R$, tykkelse $\Delta R \ll R$, længde $L$.

$$A = \Delta R \cdot L$$

$$V \approx 2\pi R A \;\Rightarrow\; m = \rho V = \rho\, 2\pi R A$$

### Kraft i båndet pga. centripetalkravet

$$T = \frac{m R \omega^{2}}{2\pi}$$

### Stress i flywheelet

$$\sigma = \rho R^{2} \omega^{2}$$

Stress skalerer med (1) materialets densitet, (2) radius i anden, (3) vinkelhastighed i anden.

### Begrænsende energi-tæthed (det elegante resultat)

$$\boxed{\;\frac{E_{\text{kin}}}{V} = \frac{\sigma}{2}\;}$$

Energi pr. volumen afhænger **kun** af materialets max stress – ikke
af radius, densitet eller omdrejningstal.

**Eksempler (fra slide):**

| Materiale | $\sigma_{\max}$ | $E/V \le$ |
|---|---|---|
| Konstruktionsstål | $250~\text{MPa}$ | $125~\text{MJ/m}^{3}$ |
| Kulfiber | $1600~\text{MPa}$ | $800~\text{MJ/m}^{3}$ |

### Energiformer brugt til lagring (oversigt)

| Tidsskala | Teknologi | Mekanisme |
|---|---|---|
| Sommer–vinter | Hydropower | $E = m g h$ |
| Uger | Batterier / CAES | Elektrokemisk / $E = p V$ |
| Dag–nat | Batterier | Elektrokemisk |
| Minut | Flywheel | $E = \tfrac{1}{2} m v^{2}$ |
| Sub-sekund | Flywheel / ultracap | Mekanisk / elektrokemisk + elektrostatisk |
"""))

# =====================================================================
# Appendix
# =====================================================================
cells.append(md(r"""## Appendix – nyttige Python-funktioner

Genbrugelige Python-snippets til de mest almindelige beregninger.
"""))

cells.append(code('''"""Konstant-acceleration: løs for den manglende størrelse."""
import numpy as np

def konstant_a(v0=None, v=None, a=None, t=None, dx=None):
    """Returner alle 5 størrelser når 3 er givet (v0, v, a, t, dx=x-x0)."""
    g = {"v0": v0, "v": v, "a": a, "t": t, "dx": dx}
    known = {k: val for k, val in g.items() if val is not None}
    if len(known) < 3:
        raise ValueError("Giv mindst 3 af: v0, v, a, t, dx")
    # Brute-force: prøv hver kombination af 3 inputs
    if v0 is not None and a is not None and t is not None:
        v = v0 + a*t
        dx = v0*t + 0.5*a*t**2
    elif v0 is not None and v is not None and t is not None:
        a = (v - v0) / t
        dx = 0.5*(v0 + v)*t
    elif v0 is not None and v is not None and a is not None:
        t = (v - v0) / a
        dx = (v**2 - v0**2) / (2*a)
    elif v0 is not None and v is not None and dx is not None:
        a = (v**2 - v0**2) / (2*dx)
        t = (v - v0) / a if a != 0 else dx / v0
    return dict(v0=v0, v=v, a=a, t=t, dx=dx)

print(konstant_a(v0=0, a=9.82, t=2.0))   # frit fald i 2 sek
'''))

cells.append(code('''"""Skråt kast: tid, højde og rækkevidde fra (v0, theta_grader)."""
import numpy as np

def skraat_kast(v0, theta_deg, g=9.82):
    th = np.deg2rad(theta_deg)
    T_tof = 2*v0*np.sin(th) / g
    y_max = (v0*np.sin(th))**2 / (2*g)
    R = v0**2 * np.sin(2*th) / g
    return dict(T_tof=T_tof, y_max=y_max, R=R)

print(skraat_kast(20, 45))
'''))

cells.append(code('''"""Fejlophobning: uafhængige usikkerheder via numerisk gradient."""
import numpy as np

def uafh_usikkerhed(f, vals, errs, h=1e-6):
    """f: callable, vals: list af x-værdier, errs: liste af delta_x.
    Returnerer (z, delta_z)."""
    vals = np.asarray(vals, dtype=float)
    errs = np.asarray(errs, dtype=float)
    z = f(*vals)
    grads = []
    for i in range(len(vals)):
        v = vals.copy()
        v[i] += h
        f_plus = f(*v)
        v[i] -= 2*h
        f_minus = f(*v)
        grads.append((f_plus - f_minus) / (2*h))
    grads = np.asarray(grads)
    dz = np.sqrt(np.sum((grads * errs)**2))
    return z, dz

# Eksempel: z = x*y med x=10±0.1, y=5±0.2
z, dz = uafh_usikkerhed(lambda x, y: x*y, [10, 5], [0.1, 0.2])
print(f"z = {z:.3f} ± {dz:.3f}")
'''))

cells.append(code('''"""Måleserie: gennemsnit, std og SDOM."""
import numpy as np

def maaleserie(data):
    data = np.asarray(data, dtype=float)
    N = len(data)
    xbar = data.mean()
    dx = np.sqrt(((data - xbar)**2).sum() / (N - 1))
    dxbar = dx / np.sqrt(N)
    return dict(N=N, xbar=xbar, dx=dx, dxbar=dxbar)

print(maaleserie([9.81, 9.79, 9.83, 9.82, 9.80, 9.84]))
'''))

cells.append(code('''"""stdscore for sammenligning af to målinger."""
import numpy as np

def stdscore_sammenlign(x, dx, y, dy):
    z = x - y
    dz = np.sqrt(dx**2 + dy**2)
    s = abs(z) / dz
    if s < 2:    verdict = "Good"
    elif s < 3:  verdict = "Grey zone"
    else:        verdict = "Reject"
    return dict(z=z, dz=dz, stdscore=s, verdict=verdict)

print(stdscore_sammenlign(9.82, 0.03, 9.79, 0.02))
'''))

# =====================================================================
# Build the notebook
# =====================================================================
nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "name": "python",
            "version": "3.11",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

OUT.write_text(json.dumps(nb, indent=1, ensure_ascii=False))
print(f"Wrote {OUT} with {len(cells)} cells.")
