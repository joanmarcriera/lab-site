---
title: "A DGX SuperPOD that draws itself"
date: 2026-10-16
draft: false
tags: [ai-infrastructure, datacenter, nvidia, infrastructure-as-code, netbox]
summary: "A 504-GPU DGX SuperPOD designed from NVIDIA's public reference architecture, written as YAML and generated into NetBox, drawings, rack elevations, a bill of materials, a cable map and 3D renders. Tests hold it to the reference."
---

*The design side of the same question as the [two H100 nodes on a real fabric](/lab/two-h100-nodes-eight-rails-what-the-fabric-actually-does/):
that post measures a GPU fabric from inside a tenant VM, and this one designs a whole pod around one.*

![The mixed pod: an H200 row with rear-door heat exchangers and a GB300 NVL72 row on direct liquid](/img/lab/superpod-hero.jpg)

## Problem

NVIDIA publishes a reference architecture for the DGX SuperPOD (RA-11336-001 for H200). It
tells you how many nodes go in a scalable unit (SU), how many leaf and spine switches the
compute fabric needs, how the racks are powered and which storage is certified. To go from
that document to something a data-centre team can build, you have to get several
interlocking things right at once:

- **Four networks.** A rail-optimised InfiniBand compute fabric (eight rails per node, one
  adapter per GPU), a storage fabric, an in-band Ethernet network and an out-of-band network.
- **Power.** Three power paths per rack, every DGX power supply on the right outlet, every
  rack inside its budget.
- **Cooling.** Hot-aisle containment for air-cooled H200, rear-door heat exchangers, direct
  liquid for GB300 NVL72.
- **Racks and hall.** Rack-unit positions, aisle widths, cable lengths.

Change one number, the SU count or the storage tier, and all four move. A spreadsheet drifts
from the drawings, and the drawings go stale. I wanted one source that everything else is
generated from, and tests that fail when the design stops matching the reference.

## Approach

The design is YAML. A generator turns it into a desired-state model, and everything else
is an output of that model:

```
spec/*.yaml  ->  topology generator  ->  NetBox (optional source of truth)
                                     ->  draw.io pages and rack elevations
                                     ->  bill of materials, cable map, IP plan
                                     ->  scene.json  ->  Blender renders
```

- **Every sizing number cites the reference.** Switch counts, cable counts and rack budgets
  point at a section or table of the RA in `docs/ra-notes.md`.
- **Every judgement call is labelled.** Where the RA is silent or leaves it to the buyer, the
  option chosen, the alternatives and the reason go into `docs/design-choices.md`.
- **Every unsourced value is registered.** A value I could not find in a public document is
  written down as NOT FOUND with the estimate used and the cheapest way to close it. There
  are 39 of them, mostly cooling-vendor details behind sales contacts.
- **NetBox is optional.** A reconciler applies the model to NetBox idempotently and only
  prunes what it owns, but every drawing, table and render is produced without it.

The same pipeline produces three designs:

| Design | Compute | Racks |
|---|---|---|
| 2-SU DGX H200, as the reference architecture | 63 DGX H200, 504 GPUs | 38 |
| 1-SU DGX GB300 NVL72 | 8 NVL72 racks, 576 GPUs | 12 |
| Mixed liquid pod: one H200 SU with rear-door heat exchangers and one GB300 SU on direct liquid, sharing one cooling plant | 824 GPUs | 33 |

![A compute leaf switch in the render, its cable ties coloured by rail](/img/lab/superpod-fabric.jpg)

## What the model enforces

The tests run offline, against the generated model, so a change to the YAML that breaks
the design fails before anyone opens a drawing:

- node, GPU, switch and rack counts equal the RA's scale tables, from one to four SUs;
- every DGX has eight compute cables to eight different leaf switches, one per rail, and each
  leaf serves one rail only;
- no leaf has more downlinks than uplinks, so the fat tree stays non-blocking;
- every cable has two ends, and no port is cabled twice;
- every DGX power supply lands on a free outlet of the right type, two per rPDU, across three
  power paths;
- peak draw per rack stays inside its budget, and in the mixed pod each cooling loop's load
  stays inside its units' capacity with one unit failed;
- the output is deterministic: generate twice, get the same drawing.

Rail-optimised means one thing above all: GPU *n* in every node talks to GPU *n* in every
other node through its own leaf. The eight-cables-to-eight-leaves test is that sentence
written as code, and it is the same property I watched from the other side on the [rented
H100 nodes](/lab/two-h100-nodes-eight-rails-what-the-fabric-actually-does/), where taking seven
rails away left a job running at a fifth of its speed without an error.

## Fabric Atlas

The repo also builds a single-file configurator, the Fabric Atlas. Pick a GPU generation from
H100 to GB300, the cooling, the SU count and the workload, and it shows live counts of GPUs,
switches, cables, racks and power, the topology, rack elevations and a bill of materials in
which each line is tagged RA, DERIVED, CHOICE or NON-RA. It runs in the browser and has no
backend: [try it here](https://joanmarcriera.github.io/dgx-superpod-as-code/).

![Fabric Atlas: configurator for DGX SuperPODs from H100 to GB300](/img/lab/superpod-atlas.png)

## What was hard and what that taught me

**The reference architecture is precise until it isn't.** It names a rack PDU by part
number, but that exact model is not published anywhere I could find. Its nearest sibling is
a horizontal 3U unit, while the stand-in I had used was a 0U vertical strip. I switched the
DGX racks to three 3U horizontal units at the top of the rack, which fits the rack layout in
NVIDIA's data-centre guide better than a 0U strip did.
A design review is mostly an argument about choices like this, and it is shorter when each
one is written down with its reason.

**Two correct tools can give different numbers.** For the same 2-SU H200 pod the generator
counts 2,445 cables and 38 racks, and the Atlas counts 1,812 and 35. Neither is wrong: the
generator counts power cords and models storage and management cabling in full, and the Atlas
counts data cables only. The fix was not to make them agree but to state each one's scope next
to the number. A bill of materials without its scope is a number someone will quote wrongly.

**No reference covers a mixed pod.** NVIDIA's documents describe H200 pods and GB300 pods,
not a hall that holds both. I built each pod with its own unchanged rules and its own
fabrics, and shared only what a building shares: the hall, the power distribution, the
cooling plant and one data-centre core. Everything on top of that is labelled CHOICE. I found
no rear-door heat exchanger for an NVL72 rack, so the ~10% of its heat that still goes to air
is handled by room units instead.

**NetBox has no pipes.** To keep the cooling loops inside the same source of truth as the
cables, every hose and header is modelled as a cable with a coolant custom field. It is a
workaround, but it means one graph can be walked from a rack's coolant manifold back to the plant.

![The coolant distribution units of the mixed pod, with the coolant headers overhead](/img/lab/superpod-cdu.jpg)

## What this is not

- Not a validated deployment. It is a design exercise that follows the public reference
  architecture closely, and says so wherever it had to choose.
- Not NVIDIA's work, and not endorsed by NVIDIA.
- Not a pricing tool. The bill of materials counts parts; it does not price them.
- Not complete on cooling hydraulics: pressure drops, pipe sizing beyond the headers and
  several vendor ratings are in the NOT FOUND register, not invented.

I built it with Claude Code as a pair programmer; the design choices and the review are mine.

## Further reading

- [dgx-superpod-as-code](https://github.com/joanmarcriera/dgx-superpod-as-code): the specs,
  generator, tests, draw.io files, cable maps, renders and the design-choices log.
- [Fabric Atlas](https://joanmarcriera.github.io/dgx-superpod-as-code/): the configurator.
- The hands-on side: [an InfiniBand fabric with no InfiniBand hardware](/lab/an-infiniband-fabric-with-no-infiniband-hardware/)
  and [two H100 nodes, eight rails](/lab/two-h100-nodes-eight-rails-what-the-fabric-actually-does/).
