# Weekly ToC Digest (week of 2026-02-16)

> Two papers on tensor-network-accelerated Vlasov-Poisson and structure-preserving discrete-gradient methods scored highest, targeting computational efficiency in kinetic plasma simulation. Five additional papers address MHD instabilities, moment models, and warm dense matter—all relevant to plasma physics fundamentals, but none directly target applied-field MPD thrusters, non-ideal MHD effects, or agentic R&D workflows. Remaining batch skews toward quantum chemistry, molecular kinetics, and materials processing with minimal direct relevance. One paper on aerospace optimal control and one on lattice Boltzmann multiphase flow methods show modest relevance to computational methods. Multiple papers on LLM agents and agentic workflows (reasoning adaptation, trajectory optimization, skill benchmarking) align with the R&D acceleration pillar, though none explicitly address scientific discovery in plasma or MHD contexts. One paper stands out: "Perceptual Self-Reflection in Agentic Physics Simulation Code Generation" (0.88) directly targets agentic automation for physics code—core to R&D acceleration. Secondary themes include CUDA optimization (0.72) for HPC infrastructure and modular agent architectures (0.70) for scientific workflow design. Most remaining papers focus on RL, LLM evaluation, or business applications disconnected from MHD, plasma, or aerospace research. Two papers demonstrate strong PINN-based computational approaches and RL-driven design automation in physical systems

**Included:** 40 (score ≥ 0.35)  
**Scored:** 198 total items

---

## [Perceptual Self-Reflection in Agentic Physics Simulation Code Generation](https://arxiv.org/abs/2602.12311)
*[ArXiv] Artificial Intelligence*  
Score: **0.88**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Physics-Simulation, Code-Generation, Automated-Workflows

Directly addresses agentic R&D pipelines for physics simulation code generation with automated self-correction and multi-agent frameworks. Bridges LLM-driven automation with computational physics workflows.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12311v1 Announce Type: cross Abstract: We present a multi-agent framework for generating physics simulation code from natural language descriptions, featuring a novel perceptual self-reflection mechanism for validation. The system employs four specialized agents: a natural language interpreter that converts user requests into physics-based descriptions; a technical requirements generator that produces scaled simulation parameters; a physics code generator with automated self-correctio…

</div>
</details>

---

## [A Machine Learning Approach to the Nirenberg Problem](https://arxiv.org/abs/2602.12368)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.78**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, PINNs, Computational Physics, Neural Networks

PINN-based approach to a classical differential geometry problem demonstrates mesh-free physics-informed neural networks applicable to complex multi-scale phenomena. Relevant to SciML stack for computational physics problems.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12368v1 Announce Type: new Abstract: This work introduces the Nirenberg Neural Network: a numerical approach to the Nirenberg problem of prescribing Gaussian curvature on $S^2$ for metrics that are pointwise conformal to the round metric. Our mesh-free physics-informed neural network (PINN) approach directly parametrises the conformal factor globally and is trained with a geometry-aware loss enforcing the curvature equation. Additional consistency checks were performed via the Gauss-B…

</div>
</details>

---

## [Variability of MHD Instabilities in Benign Termination of High-Current Runaway Electron Beams in the JET and DIII-D Tokamaks](https://arxiv.org/abs/2601.02262)
*[ArXiv] Plasma Physics*  
Score: **0.75**  
Published: 2026-02-16T05:00:00+00:00
Tags: MHD, Plasma, Tokamak, Instabilities

Directly addresses MHD instabilities and plasma confinement dynamics in fusion tokamaks. Relevant to understanding nonlinear MHD effects and disruption mitigation, though not focused on propulsion applications.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2601.02262v2 Announce Type: replace Abstract: Benign termination, in which magnetohydrodynamic (MHD) instabilities deconfine runaway electrons (REs) following hydrogenic injections, is a promising strategy for mitigating dangerous RE loads after disruptions. Recent experiments on the Joint European Torus (JET) have explored this scenario at higher pre-disruptive plasma currents than are achievable on other devices, revealing challenges in obtaining benign terminations at $I_p \geq 2.5$ MA.…

</div>
</details>

---

## [Tensor Network Compression for Fully Spectral Vlasov-Poisson Simulation](https://arxiv.org/abs/2602.13092)
*[ArXiv] Plasma Physics*  
Score: **0.73**  
Published: 2026-02-16T05:00:00+00:00
Tags: Plasma, Computational Methods, Vlasov-Poisson, Numerical Solvers

Presents advanced computational methods for kinetic plasma simulation using tensor networks. Relevant to efficient numerical solvers for plasma dynamics, complementing the researcher's interest in computational plasma physics methods.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13092v1 Announce Type: cross Abstract: We propose a numerical method for kinetic plasma simulation in which the phase-space distribution function is represented by a low-rank tensor network with an adaptive level of compression. The Vlasov-Poisson system is advanced using Strang splitting, and each substep is treated spectrally in the corresponding variable. By expressing both the distribution function and the Fourier transform as tensor network objects (state and operator representat…

</div>
</details>

---

## [Tensor Network Compression for Fully Spectral Vlasov-Poisson Simulation](https://arxiv.org/abs/2602.13092)
*[ArXiv] Computational Physics*  
Score: **0.73**  
Published: 2026-02-16T05:00:00+00:00
Tags: Plasma, Computational Methods, Vlasov-Poisson, Numerical Solvers

Presents advanced computational methods for kinetic plasma simulation using tensor networks. Relevant to efficient numerical solvers for plasma dynamics, complementing the researcher's interest in computational plasma physics methods.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13092v1 Announce Type: new Abstract: We propose a numerical method for kinetic plasma simulation in which the phase-space distribution function is represented by a low-rank tensor network with an adaptive level of compression. The Vlasov-Poisson system is advanced using Strang splitting, and each substep is treated spectrally in the corresponding variable. By expressing both the distribution function and the Fourier transform as tensor network objects (state and operator representatio…

</div>
</details>

---

## [Structure preservation using discrete gradients in the Vlasov-Poisson-Landau system](https://arxiv.org/abs/2602.13068)
*[ArXiv] Plasma Physics*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: Plasma, Numerical Methods, Conservation Laws, Kinetic Theory

Addresses structure-preserving numerical schemes for kinetic plasma equations with conservation properties. Relevant to developing robust solvers for collisional plasma transport and kinetic effects in complex plasma systems.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13068v1 Announce Type: new Abstract: We present a novel structure-preserving framework for solving the Vlasov-Poisson-Landau system of equations using a particle in cell (PIC) discretization combined with discrete gradient time integrators. The Vlasov-Poisson-Landau system is an accurate model for studying hot plasma dynamics at a kinetic scale where small-angle Coulomb collisions dominate. Our scheme guarantees conservation of mass, momentum and energy as well as preservation of the …

</div>
</details>

---

## [Optimal Take-off under Fuzzy Clearances](https://arxiv.org/abs/2602.13166)
*[ArXiv] Artificial Intelligence*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: Aerospace, Optimal Control, Fuzzy Logic, Autonomous Systems

Addresses optimal control for unmanned aircraft with adaptive constraint handling and fuzzy logic—relevant to aerospace vehicle autonomy and control systems applicable to plasma propulsion vehicle dynamics.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13166v1 Announce Type: new Abstract: This paper presents a hybrid obstacle avoidance architecture that integrates Optimal Control under clearance with a Fuzzy Rule Based System (FRBS) to enable adaptive constraint handling for unmanned aircraft. Motivated by the limitations of classical optimal control under uncertainty and the need for interpretable decision making in safety critical aviation systems, we design a three stage Takagi Sugeno Kang fuzzy layer that modulates constraint ra…

</div>
</details>

---

## [OptiML: An End-to-End Framework for Program Synthesis and CUDA Kernel Optimization](https://arxiv.org/abs/2602.12305)
*[ArXiv] Artificial Intelligence*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: CUDA, Program-Synthesis, Optimization, High-Performance-Computing

Relevant to computational physics acceleration via high-performance CUDA kernel synthesis and optimization. Maps to scientific computing infrastructure needed for large-scale MHD simulations.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12305v1 Announce Type: cross Abstract: Generating high-performance CUDA kernels remains challenging due to the need to navigate a combinatorial space of low-level transformations under noisy and expensive hardware feedback. Although large language models can synthesize functionally correct CUDA code, achieving competitive performance requires systematic exploration and verification of optimization choices. We present OptiML, an end-to-end framework that maps either natural-language in…

</div>
</details>

---

## [AstRL: Analog and Mixed-Signal Circuit Synthesis with Deep Reinforcement Learning](https://arxiv.org/abs/2602.12402)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, RL, Hardware Design, Automated Optimization

Demonstrates RL-driven optimization of physical systems with non-differentiable constraints and diverse design spaces. Relevant to agentic R&D workflows and automated design exploration for physical systems.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12402v1 Announce Type: new Abstract: Analog and mixed-signal (AMS) integrated circuits (ICs) lie at the core of modern computing and communications systems. However, despite the continued rise in design complexity, advances in AMS automation remain limited. This reflects the central challenge in developing a generalized optimization method applicable across diverse circuit design spaces, many of which are distinct, constrained, and non-differentiable. To address this, our work casts c…

</div>
</details>

---

## [OptiML: An End-to-End Framework for Program Synthesis and CUDA Kernel Optimization](https://arxiv.org/abs/2602.12305)
*[ArXiv] Multi-Agent Systems (cs.MA)*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Code-Generation, Optimization, Computational-Science

Agentic framework combining LLMs with systematic exploration for high-performance kernel optimization. Relevant to R&D acceleration through automated synthesis and verification of computational choices.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12305v1 Announce Type: cross Abstract: Generating high-performance CUDA kernels remains challenging due to the need to navigate a combinatorial space of low-level transformations under noisy and expensive hardware feedback. Although large language models can synthesize functionally correct CUDA code, achieving competitive performance requires systematic exploration and verification of optimization choices. We present OptiML, an end-to-end framework that maps either natural-language in…

</div>
</details>

---

## [Physics-Informed Transformer operator for the prediction of three-dimensional turbulence](https://arxiv.org/abs/2601.19351)
*[ArXiv] Fluid Dynamics*  
Score: **0.72**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, Physics-Informed, Turbulence, Neural Operators

Physics-informed neural operators for 3D turbulence prediction align with SciML methods applicable to MHD plasma simulation. Transformer architecture for operator learning demonstrates modern ML approaches for complex PDE systems.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2601.19351v4 Announce Type: replace Abstract: Data-driven turbulence prediction methods often face challenges related to data dependency and lack of physical interpretability. In this paper, we propose a physics-informed Transformer operator (PITO) and its implicit variant (PIITO) for predicting three-dimensional (3D) turbulence, which are developed based on the vision Transformer (ViT) architecture with an appropriate patch size. Given the current flow field, the Transformer operator comp…

</div>
</details>

---

## [Safe Reinforcement Learning via Recovery-based Shielding with Gaussian Process Dynamics Models](https://arxiv.org/abs/2602.12444)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.71**  
Published: 2026-02-16T05:00:00+00:00
Tags: RL, Control, Gaussian Processes, Safety

Integrates learned dynamics models with control policies for safety-critical systems. Relevant to spacecraft control and real-world deployment of RL-based agents in physical environments.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12444v1 Announce Type: new Abstract: Reinforcement learning (RL) is a powerful framework for optimal decision-making and control but often lacks provable guarantees for safety-critical applications. In this paper, we introduce a novel recovery-based shielding framework that enables safe RL with a provable safety lower bound for unknown and non-linear continuous dynamical systems. The proposed approach integrates a backup policy (shield) with the RL agent, leveraging Gaussian process (…

</div>
</details>

---

## [Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward](https://arxiv.org/abs/2602.12430)
*[ArXiv] Artificial Intelligence*  
Score: **0.70**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, LLM-Architecture, Modular-Systems, Autonomous-Research

Explores modular, skill-equipped agent architectures that enable dynamic capability extension. Relevant to designing composable agentic systems for scientific research automation.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12430v1 Announce Type: cross Abstract: The transition from monolithic language models to modular, skill-equipped agents marks a defining shift in how large language models (LLMs) are deployed in practice. Rather than encoding all procedural knowledge within model weights, agent skills -- composable packages of instructions, code, and resources that agents load on demand -- enable dynamic capability extension without retraining. It is formalized in a paradigm of progressive disclosure,…

</div>
</details>

---

## [Roadmap for warm dense matter physics](https://arxiv.org/abs/2505.02494)
*[ArXiv] Plasma Physics*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: Plasma, High Energy Density, Computational Physics

Comprehensive review of warm dense matter bridging high-energy-density physics and strongly coupled plasmas. Relevant to understanding high-temperature, high-pressure plasma regimes applicable to advanced propulsion concepts.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2505.02494v2 Announce Type: replace Abstract: This roadmap presents the state-of-the-art, current challenges and near future developments anticipated in the thriving field of warm dense matter physics. Originating from strongly coupled plasma physics, high pressure physics and high energy density science, the warm dense matter physics community has recently taken a giant leap forward. This is due to spectacular developments in laser technology, diagnostic capabilities, and computer simulat…

</div>
</details>

---

## [A Corrected Open Boundary Framework for Lattice Boltzmann Immiscible Pseudopotential Models](https://arxiv.org/abs/2512.12934)
*[ArXiv] Computational Physics*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: Computational Physics, Lattice Boltzmann, Multiphase Flow, Numerical Methods

Advances computational methods for multiphase flow simulation via lattice Boltzmann methods—relevant to plasma-fluid interaction modeling and computational mesh techniques for complex boundary conditions.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2512.12934v2 Announce Type: replace-cross Abstract: The pseudopotential lattice Boltzmann method (LBM) is a prominent approach for simulating multiphase flows, valued for its physical intuitiveness and computational tractability. However, existing immiscible pseudopotential methods for modeling dynamic multi-component immiscible fluid systems involving open boundaries face persistent challenges, notably the influence of spurious currents on interface formation and breakup, as well as the e…

</div>
</details>

---

## [AstRL: Analog and Mixed-Signal Circuit Synthesis with Deep Reinforcement Learning](https://arxiv.org/abs/2602.12402)
*[ArXiv] Artificial Intelligence*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: Reinforcement-Learning, Design-Automation, Optimization, Circuit-Synthesis

Demonstrates RL for automated synthesis in complex design spaces (analog circuits). Conceptually transferable to parameter optimization in non-ideal MHD simulators.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12402v1 Announce Type: cross Abstract: Analog and mixed-signal (AMS) integrated circuits (ICs) lie at the core of modern computing and communications systems. However, despite the continued rise in design complexity, advances in AMS automation remain limited. This reflects the central challenge in developing a generalized optimization method applicable across diverse circuit design spaces, many of which are distinct, constrained, and non-differentiable. To address this, our work casts…

</div>
</details>

---

## [MASPRM: Multi-Agent System Process Reward Model](https://arxiv.org/abs/2510.24803)
*[ArXiv] Multi-Agent Systems (cs.MA)*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, MARL, Inference-Optimization

Demonstrates agentic inference-time control and search guidance for multi-agent coordination. Applicable to R&D pipelines requiring selective computation and quality improvement.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2510.24803v2 Announce Type: replace Abstract: Practical deployment of multi-agent systems (MAS) demands strong performance at test time, motivating methods that guide search during inference and selectively spend compute to improve quality. We present the Multi-Agent System Process Reward Model (MASPRM). It assigns values to partial inter-agent transcripts for each action and each agent, and acts as a controller during inference. MASPRM is trained from multi-agent Monte Carlo Tree Search (…

</div>
</details>

---

## [Latent-space variational data assimilation in two-dimensional turbulence](https://arxiv.org/abs/2512.15470)
*[ArXiv] Fluid Dynamics*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: Data Assimilation, Turbulence, Computational Fluid Dynamics

Data assimilation in turbulent systems relates to computational methods for inferring flow states from limited observations; relevant to plasma state estimation in MHD simulations.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2512.15470v2 Announce Type: replace Abstract: Starting from limited measurements of a turbulent flow, data assimilation (DA) attempts to estimate all the spatio-temporal scales of motion. Success is dependent on whether the system is observable from the measurements, or how much of the initial turbulent field is encoded in the available measurements. Adjoint-variational DA minimises the discrepancy between the true and estimated measurements by optimising the initial velocity or vorticity …

</div>
</details>

---

## [Agentic AI for Robot Control: Flexible but still Fragile](https://arxiv.org/abs/2602.13081)
*[ArXiv] Robotics*  
Score: **0.68**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Robot-Control, Planning, Hierarchical-Systems

Demonstrates agentic control systems with language models planning and executing robot tasks. Relevant to agentic R&D pipelines for autonomous decision-making, though not directly applied to MHD or plasma domains.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13081v1 Announce Type: new Abstract: Recent work leverages the capabilities and commonsense priors of generative models for robot control. In this paper, we present an agentic control system in which a reasoning-capable language model plans and executes tasks by selecting and invoking robot skills within an iterative planner and executor loop. We deploy the system on two physical robot platforms in two settings: (i) tabletop grasping, placement, and box insertion in indoor mobile mani…

</div>
</details>

---

## [Long-Pulse Fast Ignition in MagLIF](https://arxiv.org/abs/2602.12673)
*[ArXiv] Plasma Physics*  
Score: **0.67**  
Published: 2026-02-16T05:00:00+00:00
Tags: MHD, Plasma, Fusion, High Magnetic Fields

Investigates magnetized liner inertial fusion with strong magnetic confinement effects. Relevant to understanding high-field MHD dynamics and plasma heating under extreme conditions.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12673v1 Announce Type: new Abstract: The fast ignition paradigm for inertial confinement fusion (ICF) allows for extremely high gains but requires fuel to be heated very quickly to outpace hotspot disassembly and energy losses. This demands lasers with high power and intensity, posing engineering challenges that have called into question the fundamental practicality of fast ignition. Magnetized liner inertial fusion (MagLIF) circumvents these problems through its large-aspect-ratio cy…

</div>
</details>

---

## [Exact moment models for conservation laws in phase space](https://arxiv.org/abs/2602.13180)
*[ArXiv] Plasma Physics*  
Score: **0.66**  
Published: 2026-02-16T05:00:00+00:00
Tags: Plasma, Kinetic Theory, Moment Methods, Conservation Laws

Develops moment-based reduced models for kinetic plasma transport with exact conservation. Applicable to bridging kinetic and fluid descriptions in plasma simulation frameworks.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13180v1 Announce Type: new Abstract: Moment equations offer a compelling alternative to the kinetic description of plasmas, gases, and liquids. Their simulation requires fewer degrees of freedom than phase space models, yet it can still incorporate kinetic effects to a certain extent. To derive moment equations, we use a parameterization of the distribution function using centered moments, as proposed by Burby. This yields moment equations for which the parameterized distribution func…

</div>
</details>

---

## [UniManip: General-Purpose Zero-Shot Robotic Manipulation with Agentic Operational Graph](https://arxiv.org/abs/2602.13086)
*[ArXiv] Robotics*  
Score: **0.66**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, VLA-Models, Hierarchical-Control, Zero-Shot

Bridges high-level semantic intent with low-level physical interaction using agentic graphs and VLA models. Relevant methodology for hierarchical autonomous systems and agent coordination, transferable to propulsion/thruster control.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13086v1 Announce Type: new Abstract: Achieving general-purpose robotic manipulation requires robots to seamlessly bridge high-level semantic intent with low-level physical interaction in unstructured environments. However, existing approaches falter in zero-shot generalization: end-to-end Vision-Language-Action (VLA) models often lack the precision required for long-horizon tasks, while traditional hierarchical planners suffer from semantic rigidity when facing open-world variations. …

</div>
</details>

---

## [Quantitative 3D non-linear simulations of shattered pellet injection in ASDEX Upgrade using JOREK](https://arxiv.org/abs/2602.12813)
*[ArXiv] Plasma Physics*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: MHD, Plasma, Tokamak, Simulation

Demonstrates 3D nonlinear MHD simulations of disruption mitigation in tokamaks using JOREK code. Relevant to advanced MHD simulation techniques for complex plasma dynamics.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12813v1 Announce Type: new Abstract: Shattered pellet injection (SPI) as primary mitigation method for major disruptions in ITER has a large parameter space available for optimization including the total amount of injected material, the size of the individual pellet fragments, the material composition, and the timing of multiple injections. This flexibility needs to be exploited to simultaneously minimize thermal heat loads, electromagnetic vessel forces, and formation of relativistic…

</div>
</details>

---

## [Odd Radio Circles Modeled by Shock-Bubble Interactions](https://arxiv.org/abs/2602.12479)
*[ArXiv] Computational Physics*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: MHD, Shock Physics, Computational Physics

Uses 3D MHD simulations to model astrophysical shock interactions. Relevant to advanced MHD simulation methodology and shock physics, though application domain differs from propulsion.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12479v1 Announce Type: cross Abstract: The physical nature and origins of the newly discovered class of Odd Radio Circles (ORCs) remain unclear. We investigate a model whereby ORCs are synchrotron-emitting vortex rings formed by the Richtmyer-Meshkov instability (RMI) when a shock interacts with a low-density fossil radio lobe in the intergalactic medium using 3D magnetohydrodynamic simulations. These rings initially exhibit oscillatory behavior that damps over time. We implement a ne…

</div>
</details>

---

## [Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents](https://arxiv.org/abs/2602.12662)
*[ArXiv] Artificial Intelligence*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, LLM, Reasoning, Autonomous Decision-Making

Proposes adaptive reasoning depth for LLM agents in multi-turn decision-making—directly applicable to agentic R&D pipelines that require variable cognitive effort for hypothesis generation and experimental design.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12662v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly deployed as autonomous agents for multi-turn decision-making tasks. However, current agents typically rely on fixed cognitive patterns: non-thinking models generate immediate responses, while thinking models engage in deep reasoning uniformly. This rigidity is inefficient for long-horizon tasks, where cognitive demands vary significantly from step to step, with some requiring strategic planning and othe…

</div>
</details>

---

## [Safe Reinforcement Learning via Recovery-based Shielding with Gaussian Process Dynamics Models](https://arxiv.org/abs/2602.12444)
*[ArXiv] Artificial Intelligence*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: Reinforcement-Learning, Gaussian-Processes, Dynamics-Modeling, Safe-Control

Combines RL with Gaussian process surrogate models for safe control in non-linear dynamical systems. Relevant to plasma propulsion control under uncertainty.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12444v1 Announce Type: cross Abstract: Reinforcement learning (RL) is a powerful framework for optimal decision-making and control but often lacks provable guarantees for safety-critical applications. In this paper, we introduce a novel recovery-based shielding framework that enables safe RL with a provable safety lower bound for unknown and non-linear continuous dynamical systems. The proposed approach integrates a backup policy (shield) with the RL agent, leveraging Gaussian process…

</div>
</details>

---

## [Intrinsic Credit Assignment for Long Horizon Interaction](https://arxiv.org/abs/2602.12342)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, RL, Credit Assignment, LLM

Addresses long-horizon credit assignment in RL using language model beliefs for intermediate goal specification. Applicable to agentic workflows requiring multi-step reasoning in scientific discovery pipelines.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12342v1 Announce Type: new Abstract: How can we train agents to navigate uncertainty over long horizons? In this work, we propose {\Delta}Belief-RL, which leverages a language model's own intrinsic beliefs to reward intermediate progress. Our method utilizes the change in the probability an agent assigns to the target solution for credit assignment. By training on synthetic interaction data, {\Delta}Belief-RL teaches information-seeking capabilities that consistently outperform purely…

</div>
</details>

---

## [WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2602.04634)
*[ArXiv] Multi-Agent Systems (cs.MA)*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, MARL, Information-Seeking

Addresses organizational capability via multi-agent width scaling for complex problem-solving. Relevant to agentic R&D workflows that distribute broad search across teams.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.04634v2 Announce Type: replace-cross Abstract: Recent advancements in Large Language Models (LLMs) have largely focused on depth scaling, where a single agent solves long-horizon problems with multi-turn reasoning and tool use. However, as tasks grow broader, the key bottleneck shifts from individual competence to organizational capability. In this work, we explore a complementary dimension of width scaling with multi-agent systems to address broad information seeking. Existing multi-…

</div>
</details>

---

## [An Oscillation-Free Real Fluid Quasi-Conservative Finite Volume Method for Transcritical and Phase-Change Flows](https://arxiv.org/abs/2602.00658)
*[ArXiv] Fluid Dynamics*  
Score: **0.65**  
Published: 2026-02-16T05:00:00+00:00
Tags: Finite Volume, Numerical Methods, Compressible Flows

Quasi-conservative finite volume schemes for complex fluid flows with equations of state relate to numerical methods for high-density plasma and thruster plume modeling.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.00658v2 Announce Type: replace-cross Abstract: A new Real Fluid Quasi-Conservative (RFQC) finite volume method is developed to address the numerical simulation of real fluids involving shock waves in transcritical and phase-change flows. To eliminate the spurious pressure oscillations inherent in fully conservative schemes, we extend the classic quasi-conservative method, originally designed for two-phase flows, to real fluids governed by arbitrary equations of state (EoS). The RFQC m…

</div>
</details>

---

## [OptiML: An End-to-End Framework for Program Synthesis and CUDA Kernel Optimization](https://arxiv.org/abs/2602.12305)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.64**  
Published: 2026-02-16T05:00:00+00:00
Tags: Program Synthesis, Optimization, Computational Efficiency, LLM

Addresses automated exploration of complex non-differentiable optimization spaces using language models and systematic verification. Applicable to R&D acceleration through automated code generation and performance tuning.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12305v1 Announce Type: new Abstract: Generating high-performance CUDA kernels remains challenging due to the need to navigate a combinatorial space of low-level transformations under noisy and expensive hardware feedback. Although large language models can synthesize functionally correct CUDA code, achieving competitive performance requires systematic exploration and verification of optimization choices. We present OptiML, an end-to-end framework that maps either natural-language inte…

</div>
</details>

---

## [RLinf-Co: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models](https://arxiv.org/abs/2602.12628)
*[ArXiv] Robotics*  
Score: **0.64**  
Published: 2026-02-16T05:00:00+00:00
Tags: RL, Sim-to-Real, VLA-Models, Control

Addresses closed-loop reinforcement learning and sim-to-real transfer for vision-language-action models. Relevant to bridging simulation validation and real-world deployment—critical for plasma thruster prototype iterations.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12628v1 Announce Type: new Abstract: Simulation offers a scalable and low-cost way to enrich vision-language-action (VLA) training, reducing reliance on expensive real-robot demonstrations. However, most sim-real co-training methods rely on supervised fine-tuning (SFT), which treats simulation as a static source of demonstrations and does not exploit large-scale closed-loop interaction. Consequently, real-world gains and generalization are often limited. In this paper, we propose an \…

</div>
</details>

---

## [WebClipper: Efficient Evolution of Web Agents with Graph-based Trajectory Pruning](https://arxiv.org/abs/2602.12852)
*[ArXiv] Artificial Intelligence*  
Score: **0.63**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Graph Methods, Agent Optimization, Information Retrieval

Optimizes web agent efficiency through trajectory pruning and graph-based reasoning—applicable to agentic R&D workflows that require efficient exploration of scientific literature and experimental parameter spaces.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12852v1 Announce Type: new Abstract: Deep Research systems based on web agents have shown strong potential in solving complex information-seeking tasks, yet their search efficiency remains underexplored. We observe that many state-of-the-art open-source web agents rely on long tool-call trajectories with cyclic reasoning loops and exploration of unproductive branches. To address this, we propose WebClipper, a framework that compresses web agent trajectories via graph-based pruning. Co…

</div>
</details>

---

## [Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control](https://arxiv.org/abs/2602.13193)
*[ArXiv] Robotics*  
Score: **0.63**  
Published: 2026-02-16T05:00:00+00:00
Tags: VLM, Hierarchical-Control, Embodied-AI, Reasoning

Combines VLMs with hierarchical control and semantic reasoning for robot tasks. Hierarchical abstraction approach aligns with potential layering of high-level thruster control commands and low-level plasma physics.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.13193v1 Announce Type: new Abstract: Pretrained vision-language models (VLMs) can make semantic and visual inferences across diverse settings, providing valuable common-sense priors for robotic control. However, effectively grounding this knowledge in robot behaviors remains an open challenge. Prior methods often employ a hierarchical approach where VLMs reason over high-level commands to be executed by separate low-level policies, e.g., vision-language-action models (VLAs). The inter…

</div>
</details>

---

## [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/abs/2602.12670)
*[ArXiv] Artificial Intelligence*  
Score: **0.62**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Benchmarking, Skill Transfer, Task Generalization

Establishes evaluation framework for agent skill transfer across domains—relevant to scaling agentic R&D systems that must generalize computational and experimental capabilities across diverse scientific tasks.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12670v1 Announce Type: new Abstract: Agent Skills are structured packages of procedural knowledge that augment LLM agents at inference time. Despite rapid adoption, there is no standard way to measure whether they actually help. We present SkillsBench, a benchmark of 86 tasks across 11 domains paired with curated Skills and deterministic verifiers. Each task is evaluated under three conditions: no Skills, curated Skills, and self-generated Skills. We test 7 agent-model configurations …

</div>
</details>

---

## [Computationally sufficient statistics for Ising models](https://arxiv.org/abs/2602.12449)
*[ArXiv] Machine Learning (cs.LG)*  
Score: **0.62**  
Published: 2026-02-16T05:00:00+00:00
Tags: Statistical Physics, Computational Methods, Physics Simulation

Computational approach to learning Gibbs distributions with partial observations relevant to statistical physics. Tangentially applicable to plasma state estimation in MHD contexts.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12449v1 Announce Type: new Abstract: Learning Gibbs distributions using only sufficient statistics has long been recognized as a computationally hard problem. On the other hand, computationally efficient algorithms for learning Gibbs distributions rely on access to full sample configurations generated from the model. For many systems of interest that arise in physical contexts, expecting a full sample to be observed is not practical, and hence it is important to look for computational…

</div>
</details>

---

## [A Corrected Open Boundary Framework for Lattice Boltzmann Immiscible Pseudopotential Models](https://arxiv.org/abs/2512.12934)
*[ArXiv] Fluid Dynamics*  
Score: **0.62**  
Published: 2026-02-16T05:00:00+00:00
Tags: Lattice Boltzmann, Multiphase Flows, Numerical Simulation

Lattice Boltzmann methods for multiphase flows provide alternative computational paradigms applicable to plasma-fluid interaction simulation in certain regimes.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2512.12934v2 Announce Type: replace Abstract: The pseudopotential lattice Boltzmann method (LBM) is a prominent approach for simulating multiphase flows, valued for its physical intuitiveness and computational tractability. However, existing immiscible pseudopotential methods for modeling dynamic multi-component immiscible fluid systems involving open boundaries face persistent challenges, notably the influence of spurious currents on interface formation and breakup, as well as the effects…

</div>
</details>

---

## [Gradient-Enhanced Partitioned Gaussian Processes for Real-Time Quadrotor Dynamics Modeling](https://arxiv.org/abs/2602.12487)
*[ArXiv] Robotics*  
Score: **0.62**  
Published: 2026-02-16T05:00:00+00:00
Tags: SciML, Surrogate Models, Aerospace, Control

Gaussian process surrogate modeling with state-space partitioning for real-time dynamics inference parallels SciML approaches for spacecraft control and trajectory optimization.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12487v1 Announce Type: new Abstract: We present a quadrotor dynamics Gaussian Process (GP) with gradient information that achieves real-time inference via state-space partitioning and approximation, and that includes aerodynamic effects using data from mid-fidelity potential flow simulations. While traditional GP-based approaches provide reliable Bayesian predictions with uncertainty quantification, they are computationally expensive and thus unsuitable for real-time simulations. To a…

</div>
</details>

---

## [SafeFlowMPC: Predictive and Safe Trajectory Planning for Robot Manipulators with Learning-based Policies](https://arxiv.org/abs/2602.12794)
*[ArXiv] Robotics*  
Score: **0.62**  
Published: 2026-02-16T05:00:00+00:00
Tags: MPC, Learning-Based-Control, Safety, Optimization

Integrates learning-based policies with optimization-based predictive control for safety and interpretability. Relevant to constrained control synthesis for thruster systems requiring rigorous safety guarantees.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12794v1 Announce Type: new Abstract: The emerging integration of robots into everyday life brings several major challenges. Compared to classical industrial applications, more flexibility is needed in combination with real-time reactivity. Learning-based methods can train powerful policies based on demonstrated trajectories, such that the robot generalizes a task to similar situations. However, these black-box models lack interpretability and rigorous safety guarantees. Optimization-b…

</div>
</details>

---

## [Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation](https://arxiv.org/abs/2602.12544)
*[ArXiv] Artificial Intelligence*  
Score: **0.61**  
Published: 2026-02-16T05:00:00+00:00
Tags: AI-Agents, Data Generation, Training Pipelines, Evaluation Methods

Presents scalable training pipeline for agents with constraint-based progress evaluation—methodologically relevant to automating scientific discovery workflows in computational research.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2602.12544v1 Announce Type: new Abstract: We present a scalable pipeline for automatically generating high-quality training data for web agents. In particular, a major challenge in identifying high-quality training instances is trajectory evaluation - quantifying how much progress was made towards task completion. We introduce a novel constraint-based evaluation framework that provides fine-grained assessment of progress towards task completion. This enables us to leverage partially succes…

</div>
</details>

---

## [Quantum-inspired space-time PDE solver and dynamic mode decomposition](https://arxiv.org/abs/2510.21767)
*[ArXiv] Computational Physics*  
Score: **0.60**  
Published: 2026-02-16T05:00:00+00:00
Tags: Computational Methods, PDE Solvers, Machine Learning

Proposes efficient PDE solvers using quantum-inspired tensor methods to overcome dimensionality challenges. Potentially applicable to accelerating plasma/MHD simulations, though not directly demonstrated.

<details>
<summary>RSS summary</summary>
<div class="rss-content">

arXiv:2510.21767v2 Announce Type: replace Abstract: The curse of dimensionality is ubiquitous in both numerical and data-driven methods. This is particularly severe for space-time methods, which treat the combined space-time domain simultaneously. We investigate the effectiveness of a quantum-inspired approach in alleviating this curse, both for solving PDEs and making data-driven predictions. We achieve this goal by treating both spatial and temporal dimensions within a single matrix product st…

</div>
</details>

---
