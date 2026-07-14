<!--
  G-Deepak-05 / G-Deepak-05
  ─────────────────────────────────────────────────────
  Hacker/terminal aesthetic. No badge walls.
  Snake · WIP · Wakatime · Featured repos · Full system diagram.
-->

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=52&duration=1&pause=99999&color=FFFFFF&center=true&vCenter=true&repeat=false&width=700&height=80&lines=G+DEEPAK" alt="G Deepak"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=400&size=15&duration=1&pause=99999&color=70A5FD&center=true&vCenter=true&repeat=false&width=700&height=30&lines=Backend+Engineer+%E2%80%94+Java+17+%C2%B7+Spring+WebFlux+%C2%B7+Kafka+%C2%B7+Kubernetes+%C2%B7+AWS" alt="role"/>

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-gdeepak--ase-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/gdeepak-ase)
[![Email](https://img.shields.io/badge/Email-gdepakise2025@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:gdepakise2025@gmail.com)
[![Profile Views](https://komarev.com/ghpvc/?username=G-Deepak-05&color=70a5fd&style=flat-square&label=profile+views)](https://github.com/G-Deepak-05)

<br/>

<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight&border=false" alt="dev quote"/>

</div>

<br/>

---

<table width="100%"><tr>
<td width="58%" valign="top">

### `$ whoami`

Backend engineer obsessed with **latency, observability, and systems that don't break at 3AM.**

1.5 years shipping production microservices at scale — reactive APIs, distributed tracing, event-driven architecture.

- ⚡ Cut p99 response times **~30%** via non-blocking reactive pipelines
- 🗄️ Reduced DB load **~40%** with Redis (Redisson) JWT caching
- 🔍 Drove production 403 errors to **~zero** with OpenTelemetry + OpenSearch
- 🌍 Currently deepening into **Go · gRPC · Raft · CQRS**

📍 Bengaluru, India

</td>
<td width="42%" valign="top">

```java
class Deepak implements BackendEngineer {

  String[] stack = {
    "Java 17",      "Spring WebFlux",
    "Kafka",        "Redis (Redisson)",
    "Docker",       "Kubernetes (EKS)",
    "Terraform",    "OpenTelemetry"
  };

  String location  = "Bengaluru 🇮🇳";
  String learning  = "Go + gRPC";
  String motto     = "Trace everything.";
}
```

</td>
</tr></table>

---

## ◈ Tech Radar — `skillicons --render`

<div align="center">

<img src="https://skillicons.dev/icons?i=java,go,python,spring,kafka,redis,docker,kubernetes,aws,postgres,terraform,prometheus,grafana,git&theme=dark" alt="tech radar"/>

</div>

---

## ◈ Currently Building — `tail -f /var/log/deepak/wip.log`

```
[2025-09-xx] [INFO]  spawning goroutines... learning Go internals
[2025-09-xx] [INFO]  protobuf schemas defined · gRPC server skeleton up
[2025-09-xx] [INFO]  reading: Raft consensus paper (Ongaro & Ousterhout)
[2025-09-xx] [INFO]  exploring: Event Sourcing + CQRS patterns
[2025-09-xx] [INFO]  target: distributed KV store in Go  ← WIP
[2025-09-xx] [WARN]  sleep() not called in 48h — feature, not a bug
```

> **Next milestone:** gRPC service with bidirectional streaming, deployed on EKS — eta unknown, ETA always lies.

---

## ◈ Architecture — `deepak.service`

> *I think in systems. Here's mine.*

```mermaid
flowchart TB
    subgraph SYS[" G-DEEPAK-05 · v1.5.0 — runtime: AWS EKS · region: ap-south-1 "]
        direction LR

        subgraph INPUT[" 📥 INPUT ADAPTERS "]
            direction TB
            AUTH["🔐 Auth Gateway<br/>JWT · Redisson"]
            KAFKAIN["📨 Kafka Topics<br/>Event-driven"]
            DB["🗄️ R2DBC / PostgreSQL<br/>Non-blocking"]
        end

        subgraph CORE[" ⚙️ CORE ENGINE "]
            direction TB
            REACTOR["⚛️ Project Reactor<br/>Mono / Flux"]
            JAVA["🧠 Java 17 + Streams API"]
            REDIS["🔴 Redis Cache<br/>Redisson · TTL"]
        end

        subgraph OUTPUT[" 📤 OUTPUT ADAPTERS "]
            direction TB
            REST["🌐 REST API<br/>15+ Endpoints"]
            KAFKAOUT["📮 Kafka Producer"]
            LOGS["📝 OpenSearch Logs"]
        end

        AUTH <--> REACTOR
        KAFKAIN <--> JAVA
        DB <--> REDIS
        REACTOR --> REST
        JAVA --> KAFKAOUT
        REDIS --> LOGS
    end

    subgraph OBS[" 📊 OBSERVABILITY "]
        direction LR
        OTEL[OpenTelemetry]
        MICRO[Micrometer]
        PROM[Prometheus]
    end

    OUTPUT -.-> OBS

    subgraph INFRA[" 🔧 INFRA PIPELINE "]
        direction LR
        TF["Terraform · Ansible"] --> JENKINS["Jenkins CI/CD"] --> DOCKER["Docker"] --> EKSN["EKS"]
    end

    SYS ==> INFRA

    subgraph METRICS[" 📈 PRODUCTION METRICS "]
        direction LR
        M1["Latency<br/>▼ ~30%"]
        M2["DB Load<br/>▼ ~40%"]
        M3["403 Errors<br/>~zero"]
    end

    INFRA ==> METRICS

    classDef inputStyle fill:#1a1b26,stroke:#70a5fd,stroke-width:2px,color:#c9d1d9
    classDef coreStyle fill:#1a1b26,stroke:#bf91f3,stroke-width:2px,color:#c9d1d9
    classDef outputStyle fill:#1a1b26,stroke:#38bdae,stroke-width:2px,color:#c9d1d9
    classDef obsStyle fill:#1a1b26,stroke:#f7768e,stroke-width:2px,color:#c9d1d9
    classDef infraStyle fill:#1a1b26,stroke:#e0af68,stroke-width:2px,color:#c9d1d9
    classDef metricStyle fill:#1a1b26,stroke:#9ece6a,stroke-width:2px,color:#c9d1d9

    class AUTH,KAFKAIN,DB inputStyle
    class REACTOR,JAVA,REDIS coreStyle
    class REST,KAFKAOUT,LOGS outputStyle
    class OTEL,MICRO,PROM obsStyle
    class TF,JENKINS,DOCKER,EKSN infraStyle
    class M1,M2,M3 metricStyle
```

---

## ◈ Career — `git log --oneline`

```
HEAD  wip:  learning Go · gRPC · Raft · Event Sourcing · CQRS

●  Backend Engineer — Tejmonvi → Sportstech GmbH            [Sep 2025 – present]
   ├─ Built 15+ Spring WebFlux APIs; ~30% latency improvement
   ├─ Redis (Redisson) JWT caching → ~40% DB load reduction
   ├─ Zero prod 403s via OpenTelemetry distributed tracing + OpenSearch
   └─ Docker + EKS + Jenkins across dev / staging / prod

●  4× Oracle Cloud Certifications                           [Jun – Sep 2025]
   └─ Data Science Pro · Architect Associate · AI Foundations · Foundations

●  AWS Cloud Engineer — Cravita Technologies                [Mar 2025]
   ├─ CI/CD: CodePipeline + CodeDeploy + Jenkins
   ├─ IaC: Terraform + Ansible across 3 environments
   └─ 3-tier AWS stack: ALB · EC2 AutoScaling · RDS · VPC

●  Cloud Intern — Rooman Technologies                       [Sep 2024]
   ├─ 510h AWS + IBM Cloud training · NSDC Level 5 Certified
   └─ Delivered Figma-prototyped app across 4 user journeys

●  init: B.E. Information Science & Engineering             [2025]
          The Oxford College of Engineering · CGPA 7.69
```

---

## ◈ Featured Repos — `find . -name "*.prod" -type f`

<div align="center">

[![StakeLite](https://github-readme-stats.vercel.app/api/pin/?username=G-Deepak-05&repo=StakeLite&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=70a5fd&icon_color=bf91f3&text_color=c9d1d9&border_radius=6)](https://github.com/G-Deepak-05/StakeLite)
[![Java_Internals_Visualizer](https://github-readme-stats.vercel.app/api/pin/?username=G-Deepak-05&repo=Java_Internals_Visualizer&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=70a5fd&icon_color=bf91f3&text_color=c9d1d9&border_radius=6)](https://github.com/G-Deepak-05/Java_Internals_Visualizer)

[![HirePilotAI](https://github-readme-stats.vercel.app/api/pin/?username=G-Deepak-05&repo=HirePilotAI&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=70a5fd&icon_color=bf91f3&text_color=c9d1d9&border_radius=6)](https://github.com/G-Deepak-05/HirePilotAI)
[![DS-Visualizer](https://github-readme-stats.vercel.app/api/pin/?username=G-Deepak-05&repo=DS-Visualizer&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=70a5fd&icon_color=bf91f3&text_color=c9d1d9&border_radius=6)](https://github.com/G-Deepak-05/DS-Visualizer)

</div>

---

## ◈ Projects — `ls ./projects`

<table width="100%">
<tr>
<td width="33%" valign="top">

**⚡ StakeLite**
`Virtual Betting Platform`

SHA-256 provably fair REST APIs for auth, wallet, and game logic. Real-time animated frontend.

`Next.js 14` · `Spring Boot 3` · `Java 21` · `PostgreSQL` · `JWT`

🚀 Zero-cost deploy — Vercel + Render + Supabase

</td>
<td width="33%" valign="top">

**🧠 Seizure Detector**
`ML · Signal Processing`

Feature-engineered ECG signals from 3 patient datasets. Integrated with wearable alert prototype.

`Python` · `scikit-learn` · `Signal Processing`

📈 +15% accuracy over baseline

</td>
<td width="33%" valign="top">

**✋ Sign Language AI**
`Real-time Computer Vision`

Live video pipeline → frame capture → classifier. Recognises 10 ASL signs in real time.

`Python` · `OpenCV` · `scikit-learn`

🎯 95%+ accuracy in real-time

</td>
</tr>
</table>

---

## ◈ Stack — `cat ./tech-stack.json`

```json
{
  "languages":    ["Java 17", "Go", "Python", "SQL", "Shell"],
  "frameworks":   ["Spring Boot", "Spring WebFlux", "Project Reactor",
                   "Hibernate", "Django", "Next.js 14"],
  "messaging":    ["Apache Kafka", "Redis (Redisson)", "Spring Integration"],
  "databases":    ["PostgreSQL (R2DBC + JDBC)", "MySQL"],
  "cloud_devops": ["AWS (EKS · RDS · S3 · CodePipeline)", "Docker",
                   "Kubernetes", "Jenkins", "Terraform", "Ansible"],
  "observability":["OpenTelemetry", "Micrometer", "Prometheus",
                   "Logstash", "OpenSearch"],
  "architecture": ["Microservices", "Event-driven", "Reactive",
                   "Distributed Systems", "RESTful APIs"]
}
```

---

## ◈ Certifications

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

## ◈ Trophy Case — `unlock --achievements`

<div align="center">

<img src="https://github-profile-trophy-liard-delta.vercel.app/?username=G-Deepak-05&theme=tokyonight&no-frame=true&no-bg=true&margin-w=8&row=1&column=6" alt="trophies"/>

</div>

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

## ◈ Coding Activity — `uptime`

<!--START_SECTION:waka-->
```text
Java          ██████████████░░░░░░░░░░░   56.4 %
Shell         ████░░░░░░░░░░░░░░░░░░░░░   15.2 %
Python        ███░░░░░░░░░░░░░░░░░░░░░░   11.8 %
Go            ██░░░░░░░░░░░░░░░░░░░░░░░    8.1 %
SQL           █░░░░░░░░░░░░░░░░░░░░░░░░    5.3 %
Other         ░░░░░░░░░░░░░░░░░░░░░░░░░    3.2 %
```
<!--END_SECTION:waka-->

---

## ◈ Contribution Snake — `./snake --eat-commits`

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/G-Deepak-05/G-Deepak-05/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/G-Deepak-05/G-Deepak-05/output/github-contribution-grid-snake.svg"/>
  <img alt="contribution snake" src="https://raw.githubusercontent.com/G-Deepak-05/G-Deepak-05/output/github-contribution-grid-snake-dark.svg"/>
</picture>

</div>

---

## ◈ Beyond the terminal

```
cricket        →  Team Captain  ·  led 15-member squad
community      →  Programming Club Coordinator  ·  100+ members
reading        →  Designing Data-Intensive Applications — Kleppmann
learning_queue →  Go · gRPC · Raft · Event Sourcing · CQRS
philosophy     →  "Build things you'd be proud to be paged about at 3AM."
```

---

<div align="center">
<sub>
<code>G-Deepak-05</code> &nbsp;·&nbsp; Bengaluru, India &nbsp;·&nbsp;
<a href="mailto:gdepakise2025@gmail.com">gdepakise2025@gmail.com</a> &nbsp;·&nbsp;
<a href="https://linkedin.com/in/gdeepak-ase">linkedin.com/in/gdeepak-ase</a>
</sub>
</div>
