# AI 비서(Personal AI Assistant) 오픈소스 저장소 조사 · 학습 노트

> Meta **Muse**, **Pickle(피클)** 같은 '개인 AI 비서' 제품을 공부하기 위해 GitHub 오픈소스 생태계를 조사한 기록입니다.
> 두 제품은 **비공개 상용 앱이라 공식 저장소가 없습니다.**

## 1. 요약

- Meta Muse: 2026-09 출시한 개인 AI 에이전트(자기 클라우드 컴퓨터에서 웹 브라우징·앱 연동·다단계 작업 수행). **공식 GitHub 저장소 없음.**
- Pickle(피클): 초대제 상용 AI 비서 앱. **공식 GitHub 저장소 없음.**
- 대신 같은 개념(상시 실행 + 자기 컴퓨터/VM + 앱 제어 + 기억)의 오픈소스가 다수 존재합니다.
- GitHub 토픽 규모: `personal-agent` **605개**, `ai-assistant` **10,055개** (조사 시점 기준).

## 2. 공부용 추천 5선

레이어가 서로 다르고, 코드가 읽히고, 로컬에서 돌아가는 것을 골랐습니다.

### 1. [browser-use/browser-use](https://github.com/browser-use/browser-use) — 121,979★ · 입문 · LLM이 웹을 조작하는 최소 구조

- **왜**: LLM이 DOM/accessibility tree를 '읽고' → 액션 스키마로 '결정' → Playwright로 '실행'하는 3단계를 가장 작은 코드로 보여줍니다.
- **학습 포인트**: 액션 공간(action schema) 설계, 실패 복구·재시도 루프, CDP/Playwright 연동
- **언어/라이선스**: Python / MIT
- **실행 조건**: 모델 API 키 1개 (30분 내 첫 실행)

### 2. [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) — 48,065★ · 개인비서 전체 아키텍처 (Python)

- **왜**: 스킬/툴 레지스트리, 메모리+지식, 멀티에이전트, 채널 어댑터가 한 저장소에 모여 있어 '비서 제품'의 뼈대를 통째로 볼 수 있습니다.
- **학습 포인트**: 툴 호출 루프, 스킬 등록·실행 방식, 세션 상태 관리
- **언어/라이선스**: Python / MIT
- **실행 조건**: Python 실행 환경 / 문서 일부 중국어

### 3. [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) — 31,158★ · 상시 실행 · 격리 아키텍처

- **왜**: 에이전트마다 Docker 컨테이너 1개, 하네스(Claude Code/Codex/opencode) 교체 가능. Muse·Pickle이 왜 '자기 VM'을 쓰는지 이해하게 됩니다.
- **학습 포인트**: 컨테이너 격리·권한, 세션 수명 관리, 메신저 브리지(WhatsApp·Telegram·Slack)
- **언어/라이선스**: TypeScript / MIT
- **실행 조건**: Docker

### 4. [leon-ai/leon](https://github.com/leon-ai/leon) — 17,718★ · 플러그인형 스킬 설계의 교과서

- **왜**: 2017년부터 이어진 클래식 구조: NLU → 스킬 라우팅 → 액션, 음성 STT/TTS, 오프라인 동작. 최신 에이전트와 비교 학습에 좋습니다.
- **학습 포인트**: 의도 분류 → 스킬 라우팅, 플러그인 구조, 음성 파이프라인
- **언어/라이선스**: TypeScript / MIT
- **실행 조건**: Node.js + Python

### 5. [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) — 13,043★ · 연구 수준 컴퓨터 유즈 (SOTA)

- **왜**: grounding(화면 요소 찾기) · planning · memory · in-context RL. GUI 에이전트 벤치마크와 평가 방법까지 다룹니다.
- **학습 포인트**: GUI grounding, 계획-실행 분리, 벤치마크·평가 설계
- **언어/라이선스**: Python / Apache-2.0
- **실행 조건**: Python + 별도 모델, 논문 병행 권장

**추천 순서:** 1 → 2 → 3 → 4 → 5 (입문 → 구조 → 운영 → 설계 → 연구). 시간이 없으면 2·3만 봐도 '개인 비서'의 뼈대는 잡힙니다.

**보너스:** [n8n-io/nod](https://github.com/n8n-io/nod) — '행동 전 승인(human-in-the-loop)' 게이트 설계 사례. 3번과 함께 보면 좋습니다.

## 3. 후보 전체 목록 (카테고리별)

### 개인 상시 비서형 (Muse·Pickle에 가장 근접)

| 저장소 | ★ | 언어 | 최근 푸시 | 설명 |
|---|---:|---|---|---|
| [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) | 48,065 | Python | 2026-11-25 | Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memor |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | 42,845 | Rust | 2026-11-24 | The fastest, cheapest, most efficient open-source agent harness. Run more than 500 agents on a $10 VPS. |
| [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | 38,189 | Python | 2026-11-25 | Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple cha |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 31,158 | TypeScript | 2026-11-25 | Your own always-on AI assistant: self-hosted, open source, lightweight. Each agent runs in its own container o |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 27,652 | TypeScript | 2026-11-25 | Open-source Grok Bot alternative with a virtual machine that bots can use |
| [titanwings/distilly](https://github.com/titanwings/distilly) | 26,851 | Python | 2026-10-13 | Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skil |
| [leon-ai/leon](https://github.com/leon-ai/leon) | 17,718 | TypeScript | 2026-11-24 | 🧠 Leon is your open-source personal assistant. |
| [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | 12,479 | Python | 2026-11-25 | A smarter, self-hosted AI assistant — multi-user, multi-agent. |
| [makecindy/cindy](https://github.com/makecindy/cindy) | 10,600 | TypeScript | 2026-11-25 | Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。 |
| [elie222/rakazo](https://github.com/elie222/rakazo) | 9,735 | TypeScript | 2026-11-25 | Open-source Grok Bot alternative. Choose your own model and sandbox. |
| [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin) | 9,724 | TypeScript | 2026-11-24 | Coolest app to use agents, local, multi provider and open source grok bot alternative. Build custom worlds for |
| [Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas) | 9,591 | JavaScript | 2026-11-25 | Orkas is an open-source (MIT), local-first AI team for your desktop: a Commander turns your goal into to-dos a |
| [kuafuai/andee](https://github.com/kuafuai/andee) | 6,196 | Kotlin | 2026-11-24 | Andee lives on your phone or Mac and uses any app like you do—no integrations, no root, any model; memory and  |
| [memovai/mimiclaw](https://github.com/memovai/mimiclaw) | 5,842 | C | 2026-10-04 | MimiClaw: Personal Agent on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS. Hardwar |
| [simplexai-labs/linger](https://github.com/simplexai-labs/linger) | 4,515 | TypeScript | 2026-11-25 | Linger is An Open-Source Personal Agent That Runs Fully on Your PC.  We aim to break Big Tech’s grip on AI by  |
| [nano-muse/nanoMuse](https://github.com/nano-muse/nanoMuse) | 3,695 | Swift | 2026-11-25 | nanoMuse: an open-source personal agent for every device you own. One agent with a name and a look of its own  |
| [n8n-io/nod](https://github.com/n8n-io/nod) | 3,411 | TypeScript | 2026-11-24 | Open source personal agent with its own computer. It chases invoices, preps your calls and cancels trials on r |

### 컴퓨터 유즈 엔진 (자기 컴퓨터 레이어)

| 저장소 | ★ | 언어 | 최근 푸시 | 설명 |
|---|---:|---|---|---|
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 121,979 | Python | 2026-11-24 | Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent  |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | 39,590 | TypeScript | 2026-10-09 | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra |
| [trycua/cua](https://github.com/trycua/cua) | 32,884 | Rust | 2026-11-25 | Scale computer-use 2.0 with open-source drivers, cross-OS sandboxes, and benchmarks for training, evaluation,  |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 26,559 | Rust | 2026-11-24 | Computer use CLI for AI agents |
| [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | 15,551 | TypeScript | 2026-11-24 | 本地优先的跨平台 Claude Code / AI Agent 桌面工作台：多 Agent 协作、Git Worktree、代码 Diff、技能市场、多模型、Computer Use、桌面宠物；支持微信、飞书、钉钉及 H |
| [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | 13,043 | Python | 2026-11-25 | Agent S: the state-of-the-art open source computer use agents |
| [bytebot-ai/bytebot](https://github.com/bytebot-ai/bytebot) | 11,072 | TypeScript | 2025-09-12 | Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, ope |

### 로컬 LLM 워크스페이스/인프라

| 저장소 | ★ | 언어 | 최근 푸시 | 설명 |
|---|---:|---|---|---|
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 68,618 | JavaScript | 2026-11-24 | Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent  |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | 53,856 | TypeScript | 2026-11-25 | Your AI workspace for models, agents, and productivity. |
| [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | 38,960 | TypeScript | 2026-11-24 | The Frontend Stack for Agents & Generative UI. React, Angular, Mobile, Slack, and more.  Makers of the AG-UI P |

### 이름이 직접 겹치는 저장소

| 저장소 | ★ | 설명 |
|---|---:|---|

### Meta(facebookresearch) 공식 계정 — Muse 저장소는 없음

연구용 에이전트 스택만 존재합니다: `meta-agents-research-environments`, `HyperAgents`, `Pearl`, `Cicero`(diplomacy_cicero), `MLGym`, `ReAgent`.

## 4. 조사 방법 (재현 가능)

GitHub Search API를 `sort=stars`로 조회했습니다. 사용한 쿼리:

```
"personal AI assistant" in:description
topic:personal-agent
topic:ai-assistant stars:>1500
"computer use" agent in:description stars:>500
topic:computer-use
"self-hosted" "AI assistant" in:description stars:>300
muse ai assistant in:name,description stars:>50
pickle ai assistant in:name,description
org:facebookresearch agent
```

갱신용 스크립트: [`scripts/collect_repos.py`](scripts/collect_repos.py) — 토큰 없이 실행 가능(시간당 60회 제한).

## 5. 주의

- 별 수·푸시 날짜는 **조사 시점의 GitHub API 응답**입니다. 이후 변동될 수 있습니다.
- 저장소 설명은 각 프로젝트의 자기 소개를 그대로 인용했습니다. 실제 성숙도·유지보수 상태는 직접 확인하세요.
- 이 저장소는 조사·학습 기록이며, 어떤 프로젝트와도 제휴 관계가 없습니다.
