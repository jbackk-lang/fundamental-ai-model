# Examples — Practical Usage of the Fundamental AI Model  
*Fundamental AI Model*

## 1. Overview
This document provides **practical examples** of how to use the  
Fundamental AI Model through:

- API calls  
- Python code  
- carrier simulations  
- chain evolution  
- FFT analysis  
- horizon visualization  

These examples are intended for developers, researchers and engineers.

---

# 2. Orientation Examples

## 2.1 Flip Orientation (API)

## 2.2 Flip Orientation (Python)
```python
from model import flip, Orientation

print(flip(Orientation.D))  # → Orientation.I
POST /collapse
BODY: { "structure_id": "mobius_01" }
→ { "orientation": "I", "residue": 0.382 }
event = collapse(mobius)
print(event.residue.value)
GET /chain/length
→ { "length": 42 }
link = Link(mobius, collapse_event, horizon.total_residue)
chain.add_link(link)
POST /carrier/create
BODY: { "type": "Photon" }
→ { "carrier_id": "photon_17" }photon = Photon(orientation=Orientation.D)
event = photon.step()
print(photon.orientation, event.residue.value)
POST /simulation/step
→ { "link": {...}, "residue": 0.12, "horizon": 4.98 }
for _ in range(100):
    mobius = cycle(mobius)
    event = collapse(mobius)
    horizon.add(event.residue)
    chain.add_link(Link(mobius, event, horizon.total_residue))
POST /fft/compute
BODY: { "sequence": [0.1, 0.2, 0.15, 0.3] }
→ { "spectrum": [0.75, 0.12, 0.05, 0.12] }
residues = [link.collapse.residue.value for link in chain.links]
spectrum = np.abs(np.fft.fft(residues))
plt.plot(spectrum)
GET /horizon
→ { "total_residue": 12.44, "boundary_size": 12.44 }
plot_horizon([link.horizon for link in chain.links])
POST /eye/event
→ { "collapse": true, "residue": 0.41 }
print(eye.transition_density)
chain = Chain()
horizon = Horizon()
mobius = Mobius(orientation=Orientation.D)

for step in range(50):
    mobius = cycle(mobius)
    event = collapse(mobius)
    horizon.add(event.residue)
    chain.add_link(Link(mobius, event, horizon.total_residue))

print("Chain length:", len(chain.links))
print("Total residue:", horizon.total_residue)
POST /carrier/create
BODY: { "type": "Photon" }
→ { "carrier_id": "photon_01" }
POST /carrier/step
BODY: { "carrier_id": "photon_01" }
GET /carrier/photon_01
→ { "orientation": "I", "local_residue": 1.92 }
POST /fft/compute
BODY: { "sequence": [ ... ] }

