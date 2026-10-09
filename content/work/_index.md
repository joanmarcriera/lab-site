---
title: "Work: what I have built and run"
description: "A catalogue of Marc Riera's hands-on technical work from 2003 to now: HPC clusters, petabyte storage, Linux automation, identity, self-hosted AI infrastructure and shipped software."
---

I have been building and running infrastructure since 2007, and writing about it since 2009.
My job titles drifted towards management. The work underneath did not: clusters racked and
accepted node by node, storage migrated while in use, fleets rebuilt from bare metal, and
these days GPUs, fabrics and software I ship myself. This page is the catalogue. Every line
is something I did with my own hands or designed and saw through to handover.

Employer names for the most recent decade are on my [CV](https://riera.co.uk/); the
[field notes](/field-notes/) on this site are deliberately not about a named organisation.

## Now (2026)

- **GPU and AI infrastructure lab.** One 8 GB RTX 4060 shared between Ollama, WhisperX and
  ComfyUI containers on TrueNAS, with Prometheus and Grafana GPU telemetry.
  Code: [whisperx-gpu-queue](https://github.com/joanmarcriera/whisperx-gpu-queue) (one
  advisory lock so jobs take turns on the card).
- **InfiniBand without hardware.** A fabric simulator lab (ibsim, OpenSM, infiniband-diags in
  Docker) with 14 exercises on LIDs, GIDs, subnet management, forwarding tables and link
  failure: [infiniband-lab](https://github.com/joanmarcriera/infiniband-lab).
- **A three-host ZFS fleet.** TrueNAS SCALE with an 8×16 TB raidz2 pool, an NVMe app pool, a
  replication target and a test box; nightly replication, audited. Runbooks an AI assistant
  executes against it: [homelab-ai-skills](https://github.com/joanmarcriera/homelab-ai-skills).
  Rebuild guide: [self-hosted-stack](https://github.com/joanmarcriera/self-hosted-stack).
- **A production VPS.** Docker Compose behind Traefik with Let's Encrypt, single sign-on,
  n8n, CRM, monitoring, nightly backups and a CI pipeline that deploys through an
  unprivileged user.
- **Grid capacity for data centres.** The Spanish transmission operator's monthly
  node-level capacity file parsed, geolocated and mapped: 936 nodes.
  [spain-grid-capacity-map](https://github.com/joanmarcriera/spain-grid-capacity-map).
  Write-up: [why my site-screening tool refuses to give you a score](/lab/why-my-site-screening-tool-refuses-to-give-you-a-score/).
- **Study with labs behind it.** Google Professional Cloud Architect (Sep 2026). NVIDIA
  Academy courses on AI factory reference architectures, InfiniBand administration, Cumulus
  Linux, SONiC and NetQ (Sep–Oct 2026).

## Software I have shipped

| What | Stack | Where |
|---|---|---|
| **Distavo**: macOS menu-bar app turning recordings into Markdown notes through your own WhisperX and Ollama servers. On the Mac App Store. | Swift | [repo](https://github.com/joanmarcriera/distavo) · [how the release is automated](/lab/shipping-a-mac-app-store-release-through-an-api-not-a-human/) |
| **Gemina**: a VPN that sends every packet over two uplinks and keeps the first copy, so calls and SSH survive a dropped link. | Go | [repo](https://github.com/joanmarcriera/Gemina) |
| **LabPeek**: home-lab inventory and network discovery, server-rendered, SQLite. | Go | [repo](https://github.com/joanmarcriera/LabPeek-Go) |
| **TalkBalance**: on-device Android talk-time tracker, no network permission. | Kotlin | [repo](https://github.com/joanmarcriera/talkbalance) |
| **Tankmate**: local-first aquarium care app. | PWA | [repo](https://github.com/joanmarcriera/tankmate) |
| **knowledge-mcp**: self-hosted hybrid search with citations over private sources, exposed over MCP. | Python | [repo](https://github.com/joanmarcriera/knowledge-mcp) |
| **vikunja-mcp**, **research-queue**: a task tracker used as the control plane for AI agents and a deep-research daemon. | Python | [vikunja-mcp](https://github.com/joanmarcriera/vikunja-mcp) · [research-queue](https://github.com/joanmarcriera/research-queue) |
| **llmx**: a curl-only bash client for a self-hosted LLM gateway. | Bash | [repo](https://github.com/joanmarcriera/llm-offload) |
| Small tools: [truenas-ncdu](https://github.com/joanmarcriera/truenas-ncdu), [searxng-merge-proxy](https://github.com/joanmarcriera/searxng-merge-proxy), [pdf-layout-translate](https://github.com/joanmarcriera/pdf-layout-translate), [linkwarden-to-karakeep](https://github.com/joanmarcriera/linkwarden-to-karakeep). | Bash, Python | GitHub |

## 2016–2026: archive, transfer and identity at a research institute

Compute engineer, then lead for archive, transfer and identity services, then deputy head
of operations. More than 4,500 Linux servers and VMs.

- **First job there: a broken 25-node LSF cluster** running the transfer services as
  scheduled containers, on single 1 GbE links. I rebuilt it and wrote the self-healing and
  monitoring scripts that adjusted the queue configuration.
- **A petabyte archive, re-plumbed while in use.** Five teams each had their own staging
  area, database and pull daemon. They were replaced by one HTTP upload API with
  S3-compatible reads, as Java services on Kubernetes. Old and new ran side by side; reads
  moved first, then writes. The archive went from about 15 PB to more than 150 PB active.
  Story: [the first 15 petabytes took ten years](/field-notes/fifteen-to-125-petabytes/).
- **An S3-to-tape tier.** I wrote the tender and ran the staged acceptance tests. The result
  writes S3 objects to tape through a RAM cache with no disk buffer, and cut recovery time
  from months to days.
- **Transfer services consolidated.** 40 mount points to 3, 80 Globus installations to 3,
  sustained throughput from 10–16 Gbps to 60–75 Gbps. FTP and HTTP moved *off* Kubernetes
  onto three bare-metal hosts, because the workload chose the platform.
- **3.9 PB ingested for one project in 2020**, at close to a petabyte a month.
- **Identity rebuilt.** OpenLDAP with bespoke schemas to Red Hat Identity Management with an
  Active Directory trust, driven by HR records. Privileged directory administrators went
  from about 50 to 3 behind a bastion. Story: [rotating every password](/field-notes/rotating-every-password/).
- **A data-centre move with no downtime**, on stretched VLANs, with no address changes.
  Story: [migrating data centres by lorry](/field-notes/migrating-data-centres-by-lorry/).
- Puppet, Ansible and SaltStack with source control, peer review and tests; Rundeck for
  delegated actions; external link upgrades from 2×10 to 100 Gbps.

## 2011–2016: HPC clusters and automation (Bull, then Atos)

L3 HPC engineer and trainer, then technical lead for managed services, then solutions architect.

- **MinoTauro, a GPU cluster at the Barcelona Supercomputing Center**, was my first full
  installation: racks and water-cooled rear doors in, blades racked and flashed, Ethernet
  bonding, InfiniBand and GPU cabling, CUDA drivers, firmware and BIOS problems resolved,
  Slurm with a highly available controller, then acceptance node by node and across the
  fabric. I trained the customer's administrators and maintained it afterwards.
- **More installations** at research sites across Spain: CPU clusters, storage and tape.
  Acceptance with Linpack and IOzone, results gathered with awk to find the bad cable or
  the bond without LACP.
- **InfiniBand fabrics** designed with Voltaire and Mellanox subnet management. Storage from
  Lustre on DDN to Ceph and enterprise NAS at petabyte scale.
- **A 1 PB Lustre file system moved to a new 2 PB one.** Direct copying between storage
  targets was too slow, so I bonded interfaces on the InfiniBand cards and ran the copy as
  Slurm jobs.
- **A 700-node cluster cut down and rebuilt.** 500 nodes shut down, their RAM and disks moved
  into the remaining 250, then rebuilt from bare metal with Katello, PXE and SaltStack in
  about 16 minutes a pass, with OpenStack and Hadoop on top. Three complete rebuilds in two weeks.
- **SaltStack orchestration for about 4,500 Unix and Windows servers.** FreeIPA to federate
  about 400 Active Directory operators. Automated OpenStack deployment for a distributed
  research cloud.
- Posts from these years: [InfiniBand and bonding configured at once](/archive/2014/configure-infiniband-and-bonding-at-once/),
  [a Data Guard-alike in bash and cron](/archive/2014/dataguard-alike-using-bash-and-cron/),
  [scripts that become functions](/archive/2014/the-scripts-that-become-functions-and-the-functions-that-belong-to-a-library/).

## 2007–2011: infrastructure for a research centre (Barcelona Media)

- Linux, identity, mail, monitoring, backup and a compute grid for an organisation that
  grew from about 50 to 250 people. Puppet and SVN for provisioning, Ganglia and Zabbix for
  monitoring.
- **An eight-GPU system on an unsupported stack.** The vendor supported Red Hat and its own
  suite. I installed it on Debian with Sun Grid Engine, designed the queues and had it
  running within a week of delivery. The vendor then hired me.
  Post from the time: [Sun Grid Engine](/archive/2010/sun-grid-engine/).
- This is when the blog started. The [archive](/archive/) has what I wrote then, in
  English, Spanish and Catalan.

## 2003–2007: before infrastructure

Taught assembler and microcomputing for three years, wrote remote software-licence control
as a freelancer, then Java on a secure-communications project for a bank and an airline.
BSc in Computer Science and Engineering (La Salle, Barcelona); final-year project at the
University of Strathclyde.

## Writing and community

- **This site**: [lab](/lab/) for current build logs, [archive](/archive/) for 2009–2014.
- **Stack Exchange**, mostly Server Fault, since 2009: 81 questions and answers on Debian,
  iptables, storage, backup and directory services.
  [Profile](https://stackexchange.com/users/126028).
- **Certifications, including the lapsed ones**: Google Professional Cloud Architect (2026),
  Oracle Database 11g OCP (2015), Red Hat RHCSA and RHCE (2011, lapsed), LPIC-1 (2010, lapsed),
  Chartered IT Professional (2026).
- **Mentoring** a computer-engineering undergraduate in Ghana since February 2026.
