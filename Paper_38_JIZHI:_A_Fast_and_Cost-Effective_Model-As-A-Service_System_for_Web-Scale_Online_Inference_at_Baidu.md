# Paper 38:

## Paper Title:
JiZhi: A Fast and Cost-effective Web-scale Online Inference System at Baidu

## Authors:

## Publication Year:

## Source/Conference/Journal:

## Abstract/Introduction Summary:
JiZhi is an online inference system developed at Baidu, aimed at providing fast and cost-effective web-scale recommendations. The system integrates an asynchronous pipeline named SEDP, a hierarchical storage system, and an intelligent resource management module to efficiently handle web-scale recommendations.

## Motivation:
- Need for a fast and efficient online inference system at a web-scale.
- Requirement to handle large-scale recommendation tasks without compromising on the latency.
- Desire to save computational costs while maintaining high-quality recommendations.

## Tools:
- JiZhi
- SEDP (Stage Executor Directed Pipeline)
- BRPC (a scalable Remote Procedure Call framework used in Baidu)

## Benefits:
- Efficient management of web-scale recommendations.
- Significant reduction in computational costs.
- Capable of handling hundreds of millions of online inference requests per second.
- Flexibility in workflow customization and auto-tuning.

## Metrics:
- Latency (measured in milliseconds)
- Throughput (number of tasks processed per second)
- Computational resource utilization (number of required instances)

## Approaches:
- Directed acyclic graph style asynchronous pipeline (SEDP) for modularized online inference serving.
- Heterogeneous and hierarchical storage system for efficient sparse DNN model management.
- Intelligent resource management for offline and online optimization.

## Challenges:
- Managing vast and diverse web-scale recommendation scenarios.
- Reducing computational overheads while accelerating online inferences.
- Balancing between computational cost and inference latency.

## How to implement responsible AI methods:
[Not mentioned in the provided excerpts]

## Reviewer's Comments:
[Not applicable unless you want to add personal comments about the paper]

## A 400 word pitch for the paper:
In today's fast-paced digital age, efficient online inference systems are a necessity, especially for tech giants like Baidu. The presented paper introduces JiZhi, Baidu's answer to this demand. This cutting-edge system is not only fast but is also cost-effective, proving essential in handling web-scale recommendations. What sets JiZhi apart is its unique Stage Executor Directed Pipeline (SEDP). This asynchronous pipeline allows for a modular approach, decoupling the intricate inference process. As a result, the system dramatically reduces pipeline stalls and offers flexibility in workflow customization. This adaptability is particularly crucial in catering to a myriad of recommendation scenarios. The paper also delves into the heterogeneous and hierarchical storage system, crafted meticulously for the effective management of sparse DNN models. This storage innovation results in accelerated online inferences and a marked reduction in computational overheads. However, JiZhi's genius doesn't end here. The system boasts an intelligent resource management module that optimizes computational resource utilization. This optimization, performed both offline and online, always keeps in mind the latency constraints of inferences, ensuring that speed is never compromised. JiZhi's deployment at Baidu has translated into significant computational savings for the company. While handling hundreds of millions of online inference requests every second, Baidu has managed to save over ten million US dollars annually in computational resources. The insights from this paper serve as a beacon for both the academic and industry communities, highlighting the design and practical experiences associated with building a web-scale online inference system. In a world where efficiency and cost-saving are paramount, JiZhi stands out as a paragon, setting the gold standard for online inference systems.
