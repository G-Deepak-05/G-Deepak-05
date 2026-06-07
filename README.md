<!--
  G-Deepak-05 / G-Deepak-05
  ─────────────────────────────────────────────────────
  Design: Dark editorial — no capsule banners, no typing SVGs,
  no badge walls. SVG sections baked inline. Unique layout.
-->

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=52&duration=1&pause=99999&color=FFFFFF&center=true&vCenter=true&repeat=false&width=700&height=80&lines=G+DEEPAK" alt="G Deepak"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=400&size=15&duration=1&pause=99999&color=70A5FD&center=true&vCenter=true&repeat=false&width=700&height=30&lines=Backend+Engineer+%E2%80%94+Java+17+%C2%B7+Spring+WebFlux+%C2%B7+Kafka+%C2%B7+Kubernetes+%C2%B7+AWS" alt="role"/>

</div>

<br/>

---

<table width="100%"><tr>
<td width="60%" valign="top">

### `$ whoami`

Backend engineer who obsesses over **latency, observability, and systems that don't break at 3AM.**

1.5 years shipping production microservices at scale — reactive APIs, distributed tracing, event-driven architecture. I've cut response times by ~30%, dropped DB load by ~40%, and traced cross-service failures to zero using OpenTelemetry.

Currently learning **Go** and **gRPC**. Always building something.

📍 Bengaluru, India &nbsp;·&nbsp; ✉️ gdepakise2025@gmail.com

[![LinkedIn](https://img.shields.io/badge/—%20linkedin-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/gdeepak-ase)
[![Profile Views](https://komarev.com/ghpvc/?username=G-Deepak-05&color=70a5fd&style=flat-square&label=profile+views)](https://github.com/G-Deepak-05)

</td>
<td width="40%" valign="top" align="right">

```java
class Deepak implements BackendEngineer {

  Stack stack = new Stack(
    "Java 17", "Spring WebFlux",
    "Kafka",   "Redis",
    "Docker",  "Kubernetes",
    "AWS EKS", "Terraform"
  );

  String location  = "Bengaluru 🇮🇳";
  String currently = "Learning Go + gRPC";
  String motto     = "Trace everything.";
}
```

</td>
</tr></table>

---

## ◈ System Design — `deepak.service`

> *I am a microservice. Here's my architecture.*

```
                         ┌─────────────────────────────────────────────────────┐
                         │               G-DEEPAK-05 / v1.5.0                 │
                         │           runtime: AWS EKS  ·  region: ap-south-1  │
                         └──────────────────────┬──────────────────────────────┘
                                                │
              ┌─────────────────────────────────┼──────────────────────────────┐
              │                                 │                              │
    ┌─────────▼──────────┐          ┌───────────▼────────────┐      ┌─────────▼────────┐
    │   INPUT ADAPTERS   │          │     CORE ENGINE        │      │  OUTPUT ADAPTERS │
    │ ─────────────────  │          │  ──────────────────    │      │ ──────────────── │
    │  🔐 Auth Gateway   │          │  ⚛  Project Reactor   │      │  🌐 REST (15+ EP)│
    │  JWT · Redisson    │◄────────►│  Mono / Flux Streams   │─────►│  Kafka Producer  │
    │                    │          │                         │      │  OpenSearch Logs │
    │  📨 Kafka Consumer │          │  🧠 Business Logic      │      └──────────────────┘
    │  Event-driven I/O  │◄────────►│  Java 17 · Streams     │
    │                    │          │                         │      ┌──────────────────┐
    │  🗄  R2DBC / PG    │          │  🔴 Redis Cache         │      │  OBSERVABILITY   │
    │  Non-blocking I/O  │◄────────►│  Redisson · TTL         │─────►│  OpenTelemetry   │
    └────────────────────┘          └─────────────────────────┘      │  Micrometer      │
                                                                      │  Prometheus      │
                                                                      └──────────────────┘
    INFRA
    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │  Terraform · Ansible  ──►  Jenkins CI/CD  ──►  Docker  ──►  Kubernetes (EKS)    │
    └──────────────────────────────────────────────────────────────────────────────────┘

    PROD METRICS
    ┌──────────────────┬───────────────────┬──────────────────┬──────────────────────┐
    │  latency  ▼ ~30% │  DB load   ▼ ~40% │  uptime   99.9%+ │  403 errors   ~zero  │
    └──────────────────┴───────────────────┴──────────────────┴──────────────────────┘
```

---

## ◈ Career — `git log --oneline`

```
a3f91c2  (HEAD)  WIP: learning Go · gRPC · distributed systems patterns
d7e2b41  feat: Backend Engineer @ Tejmonvi → Sportstech GmbH (Sep 2025)
                 · 15+ Spring WebFlux APIs · ~30% latency reduction
                 · Redis (Redisson) JWT caching → ~40% DB load cut
                 · Zero prod 403s via OpenTelemetry + OpenSearch
                 · Docker + EKS + Jenkins across 3 environments
c1a09f8  feat: 4× Oracle Cloud Certifications in 3 months (Jun–Sep 2025)
b5d3177  feat: AWS Cloud Engineer @ Cravita (Mar 2025)
                 · CI/CD: CodePipeline + CodeDeploy + Jenkins
                 · IaC: Terraform + Ansible across dev/staging/prod
                 · 3-tier AWS: ALB · EC2 AutoScaling · RDS · VPC
8f4e220  feat: Cloud Intern @ Rooman Technologies (Sep 2024)
                 · 510h AWS + IBM Cloud · NSDC Level 5 Certified
                 · Shipped Figma-prototyped app across 4 user journeys
0d1c994  init: B.E. Information Science & Engineering, CGPA 7.69
                 The Oxford College of Engineering, Bengaluru — 2025
```

---

## ◈ Shipped — `ls ./projects`

<table width="100%">
<tr>
<td width="33%" valign="top">

**⚡ StakeLite**
`Virtual Betting Platform`

SHA-256 provably fair REST APIs for auth, wallet & game logic. Real-time animated frontend.

`Next.js 14` `Spring Boot 3` `Java 21` `PostgreSQL` `JWT`

🚀 Zero-cost deploy — Vercel + Render + Supabase

</td>
<td width="33%" valign="top">

**🧠 Seizure Detector**
`ML · Signal Processing`

Feature-engineered ECG signals from 3 patient datasets. Integrated with wearable alert prototype.

`Python` `scikit-learn` `Signal Processing`

📈 +15% accuracy over baseline

</td>
<td width="33%" valign="top">

**✋ Sign Language AI**
`Real-time CV`

Real-time video pipeline → frame capture → classifier. 10 ASL signs recognised live.

`Python` `OpenCV` `scikit-learn`

🎯 95%+ accuracy in real-time

</td>
</tr>
</table>

---

## ◈ Stack — `cat ./tech-stack.json`

```json
{
  "languages":   ["Java 17", "Go", "Python", "SQL", "Shell"],
  "frameworks":  ["Spring Boot", "Spring WebFlux", "Project Reactor",
                  "Hibernate", "Django", "Next.js 14"],
  "messaging":   ["Apache Kafka", "Redis (Redisson)", "Spring Integration"],
  "databases":   ["PostgreSQL (R2DBC + JDBC)", "MySQL"],
  "cloud_devops":["AWS (EKS · RDS · S3)", "Docker", "Kubernetes",
                  "Jenkins", "Terraform", "Ansible"],
  "observability":["OpenTelemetry", "Micrometer", "Prometheus",
                   "Logstash", "OpenSearch"],
  "architecture":["Microservices", "Event-driven", "Reactive",
                  "Distributed Systems", "RESTful APIs"]
}
```

---

## ◈ Stats

<div align="center">

<a href="https://github.com/G-Deepak-05">
<img height="160" src="https://github-readme-stats.vercel.app/api?username=G-Deepak-05&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&bg_color=0d1117&title_color=70a5fd&icon_color=bf91f3&text_color=c9d1d9&border_radius=6&hide_title=true"/>
</a>&nbsp;
<a href="https://github.com/G-Deepak-05">
<img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=G-Deepak-05&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=70a5fd&text_color=c9d1d9&langs_count=6&border_radius=6"/>
</a>

<br/><br/>

<img src="https://streak-stats.demolab.com?user=G-Deepak-05&theme=tokyonight-duo&hide_border=true&background=0D1117&ring=70A5FD&fire=BF91F3&currStreakLabel=70A5FD&sideLabels=38BDAE&dates=8B949E&currStreakNum=C9D1D9&sideNums=C9D1D9&stroke=0D1117&border_radius=6"/>

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=G-Deepak-05&theme=tokyo-night&bg_color=0d1117&color=70a5fd&line=bf91f3&point=38bdae&area=true&hide_border=true&radius=6"/>

</div>

---

## ◈ Certified

<div align="center">

| Certification | Issuer | Date |
|---|---|---|
| Cloud Infrastructure — Data Science Professional | Oracle | Sep 2025 |
| Cloud Infrastructure — Architect Associate | Oracle | Sep 2025 |
| Cloud Infrastructure — AI Foundations Associate | Oracle | Aug 2025 |
| Cloud Infrastructure — Foundations Associate | Oracle | Aug 2025 |
| CDN with IBM Cloud Akamai Integration | IBM | Apr 2025 |
| NSDC Level 5 Certification | NSDC | 2025 |

</div>

---

## ◈ Beyond the terminal

```
role_outside_work  →  Cricket Team Captain  ·  led 15-member squad
community          →  Programming Club Coordinator  ·  100+ members
currently_reading  →  Designing Data-Intensive Applications — Kleppmann
learning_queue     →  Go · gRPC · Raft · Event Sourcing · CQRS
philosophy         →  "Build things you'd be proud to be paged about at 3AM."
```

---

<div align="center">
<sub>
<code>G-Deepak-05</code> &nbsp;·&nbsp; Bengaluru, India &nbsp;·&nbsp;
<a href="mailto:gdepakise2025@gmail.com">gdepakise2025@gmail.com</a> &nbsp;·&nbsp;
<a href="https://linkedin.com/in/gdeepak-ase">linkedin</a>
</sub>
</div>
