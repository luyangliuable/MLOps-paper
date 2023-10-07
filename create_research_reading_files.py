import os

# Titles for files
titles = ["MLOps Pipeline Development: The OSSARA Use Case",
"MLOps: a guide to its adoption in the context of responsible AI",
"From Ad-Hoc Data Analytics to DataOps",
"MLOps Automation – Developing a RESTful API for Text Based Emotion Detection",
"Model Provenance Management in MLOps Pipeline",
"A Preliminary Investigation of MLOps Practices in GitHub",
"Auto-Validate by-History: Auto-Program Data Quality Constraints to Validate Recurring Data Pipelines",
"Scarecrow - Intelligent Annotation platform for Engine Health Management",
"DQSOps: Data Quality Scoring Operations Framework for Data-Driven Applications",
"Machine Learning on Insurance Premium Prediction",
"Operationalizing machine learning models: a systematic literature review",
"Testing of machine learning models with limited samples: an industrial vacuum pumping application",
"A Software Ecosystem for Deploying Deep Learning in Gravitational Wave Physics",
"Looper: An End-to-End ML Platform for Product Decisions",
"Amazon SageMaker Model Monitor: A System for Real-Time Insights into Deployed Machine Learning Models",
"AI governance in the system development life cycle: insights on responsible machine learning engineering",
"Towards a roadmap on software engineering for responsible AI",
"Profiling Deep Learning Workloads at Scale using Amazon SageMaker",
"Enhancing Performance of Operationalized Machine Learning Models by Analyzing User Feedback",
"JIZHI: A Fast and Cost-Effective Model-As-A-Service System for Web-Scale Online Inference at Baidu",
"Studying the Practices of Deploying Machine Learning Projects on Docker",
"TinyMLOps for real-time ultra-low power MCUs applied to frame-based event classification",
"dcbench: a benchmark for data-centric AI systems",
"AlerTiger: Deep Learning for AI Model Health Monitoring at LinkedIn",
"Telling Stories from Computational Notebooks: AI-Assisted Presentation Slides Creation for Presenting Data Science Work",
"Multi Datasource LTV User Representation (MDLUR)",
"Quality assurance of generative dialog models in an evolving conversational agent used for Swedish language practice",
"Skadi: Building a Distributed Runtime for Data Systems in Disaggregated Data Centers",
"Dynamic data management for continuous retraining",
"Primeval",
"MDE for machine learning-enabled software systems: a case study and comparison of MontiAnna &amp; ML-Quadrat",
"BlindFL: Vertical Federated Machine Learning without Peeking into Your Data",
"DComp: Efficient Offload of LSM-tree Compaction with Data Processing Units",
"Making Data Clouds Smarter at Keebo: Automated Warehouse Optimization using Data Learning",
"Survey of automation practices in model-driven development and operations",
"Pythia: A Customizable Hardware Prefetching Framework Using Online Reinforcement Learning",
"OPS: Optimized Shuffle Management System for Apache Spark",
"SplitFS: reducing software overhead in file systems for persistent memory",
"PipeDevice: a hardware-software co-design approach to intra-host container communication",
"On-the-fly deterministic binary filters for memory efficient keyword spotting applications on embedded devices",
"Taming metadata storms in parallel filesystems with metaFS",
"Hyperscale Hardware Optimized Neural Architecture Search",
"Evolving Operating System Kernels Towards Secure Kernel-Driver Interfaces",
"Transformation rules from UML4MBT meta-model to SMT meta-model for model animation",
"On Understanding Data Worker Interaction Behaviors",
"How Data Analysts Use a Visualization Grammar in Practice",
"FunUL: a method to incorporate functions into uplift mapping languages",
"Open question answering over curated and extracted knowledge bases",
"FPGA-based biophysically-meaningful modeling of olivocerebellar neurons",
"HexRIC: Building a Better near-Real Time Network Controller for the Open RAN Ecosystem",
"Architectural Support for Dynamic Linking",
"Triggered instructions: a control paradigm for spatially-programmed architectures",
"Beyond human-level accuracy: computational challenges in deep learning",
"FinRL-podracer: high performance and scalable deep reinforcement learning for quantitative finance",
"Accelerating container-based deep learning hyperparameter optimization workloads",
"The Mozart reuse exposed dataflow processor for AI and beyond: industrial product",
"ReCFA: Resilient Control-Flow Attestation",
"Automated derivation of parametric data movement lower bounds for affine programs",
"Asynchronous intrusion recovery for interconnected web services",
"Conflict exceptions: simplifying concurrent language semantics with precise hardware exceptions for data-races",
"How to measure useful, sustained performance",
"Impact Factors and Best Practices to Improve Effort Estimation Strategies and Practices in DevOps",
"Towards understanding end-to-end learning in the context of data: machine learning dancing over semirings &amp; Codd's table",
"What is an AI engineer? an empirical analysis of job ads in The Netherlands",
"A classification and review of tools for developing and interacting with machine learning systems",
"Reactive Software Architectures in IoT: A Literature Review",
"CNDAS-WF: Cloud Native Data Analysis System Based On Workflow Engine",
"Collaboration challenges in building ML-enabled systems: communication, documentation, engineering, and process",
"An urban sensing architecture as essential infrastructure for future cities",
"Scalable Execution of Big Data Workflows using Software Containers",
"CPscan: Detecting Bugs Caused by Code Pruning in IoT Kernels",
"Concerto: A High Concurrency Key-Value Store with Integrity",
"Data Management and Visualization for Benchmarking Deep Learning Training Systems",
"A Drift Handling Approach for Self-Adaptive ML Software in Scalable Industrial Processes",
"How I stopped worrying about training data bugs and started complaining",
"Characterizing Practices, Limitations, and Opportunities Related to Text Information Extraction Workflows: A Human-in-the-loop Perspective",
"Where Is My Training Bottleneck? Hidden Trade-Offs in Deep Learning Preprocessing Pipelines",
"Emergency communications leveraging decentralized swarm computing",
"Data sovereignty for AI pipelines: lessons learned from an industrial project at Mondragon corporation",
"Causal fault localisation in dataflow systems",
"Angler: Helping Machine Translation Practitioners Prioritize Model Improvements",
"A knowledge and reasoning toolkit for cognitive applications",
"On-Premise AI Platform: From DC to Edge",
"Investigating Software Engineering Artifacts in DevOps Through the Lens of Boundary Objects",
"The PMS and ISP descriptive systems for computer structures",
"On the cost-effectiveness of composite metamorphic relations for testing deep learning systems",
"Towards A Platform and Benchmark Suite for Model Training on Dynamic Datasets",
"Bilateral anti-entropy for eventual consistency",
"FDLS: A Deep Learning Approach to Production Quality, Controllable, and Retargetable Facial Performances.",
"Towards Building Autonomous Data Services on Azure",
"Health Assurance: AI Model Monitoring Platform",
"gridds: a data science toolkit for energy grid machine learning",
"Beyond CO2 Emissions: The Overlooked Impact of Water Consumption of Information Retrieval Models",
"Identifying Roles, Requirements and Responsibilities in Trustworthy AI Systems",
"How Provenance helps Quality Assurance Activities in AIML Systems",
"Exploring ML testing in practice: lessons learned from an interactive rapid review with axis communications",
"Hyacinth macaw: a project-based learning program to develop talents in Software Engineering for Artificial Intelligence",
"Security Patterns for Machine Learning: The Data-Oriented Stages",
"Project smells: experiences in analysing the software quality of ML projects with mllint",
"Sensible AI: Re-imagining Interpretability and Explainability using Sensemaking Theory",
"Dancing, not Wrestling: Moving from Compliance to Concordance for Secure Software Development",
"iRec: An Interactive Recommendation Framework",
"Developers’ Perception of GitHub Actions: A Survey Analysis",
"Aspirations and Practice of ML Model Documentation: Moving the Needle with Nudging and Traceability",
"Reckoning with the Disagreement Problem: Explanation Consensus as a Training Objective",
"Serving deep neural networks at the cloud edge for vision applications on mobile platforms",
"Use Microsoft office components and Database to quickly build a lightweight website",
"Assuage: Assembly Synthesis Using A Guided Exploration"]

template = """
# Paper X:

## Paper Title: {title}

## Authors: [Names of the Authors]

## Publication Year: [Year of Publication]

## Source/Conference/Journal: [Source of the Paper]
 
## Abstract/Introduction Summary:

## Motivation:

## Benefits:

## Metrics:

## Approaches:

## Challenges:

## Reviewer's Comments:
"""

directory = "/Users/blackfish/MLOps-paper/"

if not os.path.exists(directory):
    os.makedirs(directory)

for title in titles:
    file_name = title.replace(' ', '_') + ".md"
    file_path = os.path.join(directory, file_name)
    
    with open(file_path, 'w') as f:
        f.write(template.format(title=title))

print(f"Files created in {directory}")
