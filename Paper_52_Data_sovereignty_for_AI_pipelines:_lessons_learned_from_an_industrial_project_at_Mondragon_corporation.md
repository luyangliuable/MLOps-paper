# Paper 53:

## Paper Title: Paper_52_Data_sovereignty_for_AI_pipelines:_lessons_learned_from_an_industrial_project_at_Mondragon_corporation

## Authors:
- Andrei Paleyes
- Neil D. Lawrence

## Publication Year:
2023

## Source/Conference/Journal:
EuroMLSys ’23, May 8, 2023, Rome, Italy

## Abstract/Introduction Summary:
The paper introduces the concept of using causal inference techniques in dataflow systems for fault localization. It presents a practical demonstration of this approach using various dataflow frameworks and experiments. The authors discuss the causal attribution procedure and how it can accurately pinpoint faulty components in dataflow graphs.

## Motivation:
The motivation behind this research is to explore the application of causal inference techniques in dataflow systems for fault localization. Dataflow systems are prevalent in various domains, and the ability to quickly identify and locate faults is crucial for maintaining system reliability. The paper aims to validate the feasibility of using causal inference for this purpose.

## Tools:
The paper mentions the following tools:
- Seldon Core v2 (SCv2)
- Node-RED
- SciPipe
- DoWhy-GCM package

## Benefits:
- Accurate fault localization in dataflow systems.
- Potential for integrating causal fault localization into dataflow frameworks for monitoring.
- Applicability in various dataflow engines and domains.

## Metrics:
The paper primarily focuses on the use of causal attribution scores to identify faulty components in dataflow systems. It uses mean attribution scores and statistical significance (p-values) as metrics to evaluate the effectiveness of the approach.

## Approaches:
The paper introduces the concept of causal fault localization using causal inference techniques. It employs a causal attribution procedure based on the work of Paleyes et al. [22]. The approach involves traversing the dataflow graph to compute deviation and attribution scores for each node.

## Challenges:
- Scalability of the approach for large dataflow graphs.
- Handling dataflow graphs with cycles.
- Application to cases where only approximate dataflow graphs are available.
- Extending the technique to handle datasets rather than single records.

## How to implement responsible AI methods:
The paper does not explicitly discuss responsible AI methods, as its primary focus is on causal fault localization. However, responsible AI practices can be integrated into the implementation of causal fault localization by ensuring transparency, fairness, and accountability in the fault localization process.

## Reviewer's Comments:
The paper provides a valuable contribution to the field of dataflow systems by demonstrating the applicability of causal inference techniques for fault localization. The experiments conducted across different dataflow frameworks showcase the robustness of the approach. However, further research is needed to address scalability and handle more complex dataflow scenarios with loops.

## A 400-word pitch for the paper:
The paper "Causal fault localisation in dataflow systems" offers an innovative approach to fault localization in dataflow systems using causal inference techniques. In today's software-driven world, dataflow systems are crucial for various applications, and identifying faults swiftly is paramount. This paper provides a practical demonstration of how causal inference can accurately pinpoint faulty components within dataflow graphs, paving the way for improved system reliability and easier debugging.

The authors introduce the concept of causal attribution, a technique that assigns scores to different nodes within a dataflow graph, allowing developers to identify the root causes of system faults. They showcase the effectiveness of this approach through a series of experiments conducted on various dataflow frameworks, including Seldon Core v2, Node-RED, and SciPipe. In each experiment, the causal fault localization method correctly identified the faulty node, even in complex scenarios, thus proving its robustness.

One notable feature of this research is its applicability across different dataflow engines and domains. Whether you're dealing with machine learning models, IoT applications, scientific workflows, or other data-driven systems, the causal attribution technique has the potential to streamline fault localization and improve system maintenance.

However, the paper also highlights some challenges. Scalability remains a concern, as the experiments primarily focused on relatively small dataflow graphs. Handling larger and more complex graphs is an area for future research. Additionally, addressing dataflow graphs with loops and extending the method to handle datasets, which is common in machine learning pipelines, are potential avenues for improvement.

Despite these challenges, the paper's findings hold promise for the broader adoption of causal fault localization in dataflow systems. By open-sourcing the source code for their experiments, the authors encourage further research and development in this area, making it accessible to the community.

In conclusion, "Causal fault localisation in dataflow systems" represents a significant step towards the practical implementation of causal inference techniques for fault localization in dataflow systems. Its potential impact spans various industries and applications, making it a valuable contribution to the field of data-driven software engineering.
