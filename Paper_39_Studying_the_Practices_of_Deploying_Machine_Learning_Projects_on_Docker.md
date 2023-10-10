# Paper 39:

## Paper Title:
Studying the Practices of Deploying Machine Learning Projects on Docker

## Authors:
- Moses Openja
- Forough Majidi
- Foutse Khomh
- Bhagya Chembakottu
- Heng Li

## Publication Year:
2022

## Source/Conference/Journal:
The International Conference on Evaluation and Assessment in Software Engineering 2022 (EASE 2022), Gothenburg, Sweden.

## Abstract/Introduction Summary:
Docker is a containerization service that facilitates the deployment of various applications, including machine learning (ML) models. While studies have explored Docker's use for general software deployment, there's a lack of focus on ML-based project deployment via Docker. This paper investigates the practices of deploying ML projects on Docker, including the categories of ML projects that utilize Docker, their purposes of using Docker, and the characteristics of Docker images they produce.

## Motivation:
- Understand how Docker is being used to deploy machine learning (ML) based projects.
- Shed light on the emerging practices of deploying ML projects using containers.
- Highlight areas for improvement in ML deployment practices.

## Tools:
- Docker
- Docker Hub
- GitHub

## Benefits:
- Provides insights into how ML projects are being deployed using Docker.
- Identifies emerging practices in ML software project deployment.
- Highlights potential areas for improvement in deploying ML projects with Docker.

## Metrics:
- Docker image characteristics
- Purposes of using Docker
- Types of ML projects deploying with Docker

## Approaches:
- Analyzed 406 open-source ML-based software projects from GitHub with corresponding Docker images on Docker Hub.
- Investigated the types, purposes, and characteristics of Docker usage in these projects.

## Challenges:
- Limited research focusing on how Docker is used specifically for deploying ML-based projects.

## How to implement responsible AI methods:
[Not mentioned in the provided excerpts]

## Reviewer's Comments:
[Not applicable unless you want to add personal comments about the paper]

## A 400 word pitch for the paper:
Docker's prominence in automating modern software system deployments is undeniable, given its myriad of advantages such as isolation, efficiency, and packaging convenience. While extensive research exists on Docker's application in general software systems, a conspicuous gap remains - the deployment of machine learning (ML) projects using Docker. This paper, "Studying the Practices of Deploying Machine Learning Projects on Docker," embarks on a pioneering journey to bridge this gap.

Drawing data from 406 open-source ML-based projects on GitHub that have corresponding Docker images on Docker Hub, the study offers invaluable insights into Docker's application in the ML domain. The research reveals that Docker's adoption spans across six distinct ML-based project categories, namely ML Applications, MLOps/ AIOps, Toolkits, DL Frameworks, Models, and Documentation. Digging deeper, the study unveils a taxonomy of 21 major categories elucidating Docker's purposes. Intriguingly, Docker's use isn't limited to general deployment; it extends to model-specific tasks such as testing and training, underscoring its versatility.

Platform portability emerges as a significant reason ML engineers flock to Docker. The ability to seamlessly transfer software across operating systems, varied runtimes, and language constraints positions Docker as an indispensable tool in the ML deployment toolkit. However, the study also sounds a note of caution: Docker images for ML-based projects may demand more resources, attributed to a large number of files and deeply nested directories in image layers.

In conclusion, this research stands as a beacon, guiding the software engineering community into the nuances of deploying ML applications using containers. By shedding light on current practices and spotlighting areas ripe for improvement, it lays the groundwork for future endeavors aimed at refining ML deployment practices using Docker. As machine learning continues its upward trajectory in the tech world, insights from this study will prove instrumental in shaping efficient and effective deployment strategies using Docker.
