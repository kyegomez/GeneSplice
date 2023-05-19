# GeneSplice 🧬 

![GeneSpliceBanner](genesplice-banner.png)

My own attempt at a long context genomics model, leveraging recent advances in long context attention modeling (<a href="https://arxiv.org/abs/2205.14135">Flash Attention</a> + other hierarchical methods).

If you would like to collaborate and not averse to having the final model completely open sourced, get in touch. My goal is to simply figure out if long context is what holds us back from a new SOTA model.

# Research Technical Analysis: Next Steps for Gene Expression Transformers

## Introduction
Gene expression models have seen significant advancements with the introduction of models like Enformer. However, there is still room for further improvements to push the state-of-the-art (SOTA) in gene expression analysis. In this technical analysis, we will explore five explicit architectural model improvements that can advance the field of gene expression transformers.

## 1. Hierarchical Attention Mechanism
Implementing a hierarchical attention mechanism within gene expression transformers can enhance their ability to capture dependencies at different levels. This mechanism would allow the model to attend to both the global structure of the gene sequence and the local dependencies within sub-sequences. By incorporating hierarchical attention, the model can better understand the complex relationships between different parts of the gene sequence and improve its performance in capturing relevant information.

## 2. Adaptive Learning Rate Scheduling
Integrating adaptive learning rate scheduling techniques, such as Cyclical Learning Rates or Learning Rate Warmup, can improve the training efficiency and convergence speed of gene expression transformers. These techniques dynamically adjust the learning rate during training, allowing the model to quickly adapt to changing patterns and make better use of the available training data. By optimizing the learning rate schedule, we can accelerate training and potentially achieve better generalization performance.

## 3. Graph Attention Networks
Introducing graph attention networks within gene expression transformers can enable the model to capture the underlying biological interactions and dependencies between genes. By representing the gene sequence as a graph, where genes are nodes and their interactions are edges, the model can apply graph attention mechanisms to attend to relevant genes and capture the complex relationships between them. This approach can provide a more comprehensive understanding of gene expression patterns and potentially improve the accuracy of predictions.

## 4. Contrastive Learning and Self-Supervised Pre-training
Applying contrastive learning and self-supervised pre-training techniques to gene expression transformers can help enhance their ability to learn meaningful representations from unlabeled gene data. By designing pretext tasks that require the model to predict relationships between different parts of the gene sequence, we can encourage the model to capture higher-level features and dependencies. This self-supervised pre-training can provide a valuable initialization for downstream tasks and potentially improve the model's performance on gene expression analysis.

## 5. Integration of Domain-Specific Knowledge
Incorporating domain-specific knowledge, such as biological pathway information or gene function annotations, into gene expression transformers can enhance their interpretability and robustness. By leveraging this knowledge during training and inference, the model can prioritize relevant genes, identify key biological processes, and provide more meaningful insights. Integration of domain-specific knowledge can help bridge the gap between gene expression analysis and biological understanding, advancing the practical applications of gene expression transformers.

## Conclusion
Advancing the field of gene expression transformers requires explicit architectural model improvements. The proposed enhancements, including hierarchical attention mechanisms, adaptive learning rate scheduling, graph attention networks, contrastive learning with self-supervised pre-training, and integration of domain-specific knowledge, aim to push the state-of-the-art in gene expression analysis. By incorporating these improvements, we can expect to achieve more accurate predictions, better capture complex dependencies, and enhance the interpretability of gene expression models, ultimately advancing our understanding of gene regulation and its implications in various biological processes.

### What is gene expression? Can enformer create genes? 

Gene expression refers to the process by which information encoded in a gene is used to create functional gene products, such as proteins or RNA molecules. It involves the transcription of DNA into messenger RNA (mRNA) and the subsequent translation of mRNA into proteins. Gene expression is tightly regulated and can vary across different cell types, developmental stages, and environmental conditions.

As for Enformer, it is important to clarify that Enformer is not capable of creating genes. Enformer is a transformer-based deep learning model architecture that has been applied to the task of gene expression prediction. It uses gene sequence data as input and learns to model the relationships and patterns within the sequences to make predictions about gene expression levels. Enformer and similar models leverage the power of deep learning to analyze and make predictions based on existing gene expression data, but they do not have the ability to generate or create entirely new genes.


Enformer, like other deep learning models, is designed to analyze and learn patterns from existing data. It learns from the patterns and relationships present in the input data to make predictions or generate outputs based on that learned knowledge. However, generating entirely new genes is a complex biological process that involves the rearrangement, mutation, and recombination of DNA sequences, which is beyond the capabilities of Enformer or any other deep learning model.

Creating new genes requires biological mechanisms such as DNA replication, transcription, and translation, which are part of the intricate machinery of living cells. These processes involve various regulatory elements, complex interactions, and evolutionary forces that are not within the scope of deep learning models. Enformer, being a computational model, operates within the realm of analyzing and predicting based on the patterns it has learned from existing data, rather than creating entirely novel genetic sequences.

The generation of new genes is a complex biological phenomenon driven by natural evolutionary processes, mutation events, and selection pressures over long periods of time. While deep learning models like Enformer can assist in analyzing and interpreting gene expression data, the creation of new genes still remains a fascinating and ongoing area of study in molecular biology and evolutionary genetics.


### Then what task does Enformer and other gene expression models solve?
Enformer and other gene expression models are designed to address the task of gene expression prediction. Gene expression prediction involves estimating the levels or activity of genes in different biological samples or conditions. The models analyze gene sequence data, typically represented as DNA or RNA sequences, and learn patterns and relationships within the sequences to predict the expression levels of genes.

The gene expression models aim to provide insights into how genes are regulated and how their activity varies across different cell types, tissues, developmental stages, or environmental conditions. By predicting gene expression levels, these models can help researchers understand the underlying mechanisms of gene regulation, identify genes involved in specific biological processes or diseases, and uncover potential biomarkers or therapeutic targets.

Enformer and similar models leverage deep learning techniques, often based on transformer architectures, to capture the dependencies and patterns within gene sequences and make accurate predictions of gene expression levels. They learn from large-scale gene expression datasets to build models that can generalize to new samples and make predictions based on the learned patterns.

In summary, gene expression models like Enformer solve the task of predicting gene expression levels, enabling researchers to gain insights into the regulation and activity of genes in different biological contexts.





### Holy Grail of BioMl
The concept of the "holy grail" of biological AI encompasses a vision of advanced artificial intelligence systems that can deeply understand and simulate the complexities of biological systems. While the holy grail remains an aspirational goal, here is an explicit picture of what it could potentially look like:

Comprehensive Biological Understanding: The holy grail of biological AI involves AI systems that possess a deep understanding of biological processes at multiple scales, ranging from molecular interactions to cellular networks, organ systems, and beyond. These systems would integrate knowledge from various disciplines, such as genomics, proteomics, systems biology, and bioinformatics, to provide a holistic understanding of the complexity of living organisms.

Prediction of Genetic and Protein Functions: The AI system would have the capability to accurately predict the functions and properties of genes and proteins. It would leverage advanced machine learning algorithms, large-scale biological datasets, and comprehensive biological knowledge to infer gene functions, protein structures, and interactions. This would facilitate the discovery of novel therapeutic targets, biomarkers, and drug candidates.

Computational Design of Genes and Proteins: The holy grail AI system would be able to design and engineer genes and proteins with specific desired properties. By simulating the structure-function relationship of biological molecules, it could generate novel genetic sequences or modify existing ones to enhance protein functionality, create new enzymes, optimize metabolic pathways, and develop customized therapeutics.

Simulating Biological Systems: AI systems would simulate the behavior and dynamics of complex biological systems, such as cells, tissues, and organs, at various levels of detail. They would integrate molecular interactions, cellular processes, and environmental factors to provide accurate predictions and simulations of biological phenomena. This could aid in understanding disease mechanisms, drug responses, and personalized medicine.

Accelerated Drug Discovery and Development: The holy grail AI system would revolutionize the drug discovery and development process. It would efficiently screen vast libraries of compounds, predict drug-target interactions, optimize drug candidates, and simulate drug metabolism and toxicity. This would significantly reduce the time, cost, and failure rates associated with traditional drug development pipelines.

It's important to note that while the holy grail AI system would revolutionize biological research and healthcare, it does not create genes or proteins in the sense of generating entirely novel biological molecules. The system's strength lies in its ability to analyze vast amounts of biological data, simulate biological processes, predict functions, and assist in the design and engineering of genes and proteins to address specific research and therapeutic needs. The creation of new genes and proteins still remains a biological process governed by the laws of genetics and biochemistry.

## Citations

```bibtex
@inproceedings{dao2022flashattention,
    title   = {Flash{A}ttention: Fast and Memory-Efficient Exact Attention with {IO}-Awareness},
    author  = {Dao, Tri and Fu, Daniel Y. and Ermon, Stefano and Rudra, Atri and R{\'e}, Christopher},
    booktitle = {Advances in Neural Information Processing Systems},
    year    = {2022}
}
```

```bibtex
@article {Dalla-Torre2023.01.11.523679,
    author  = {Hugo Dalla-Torre and Liam Gonzalez and Javier Mendoza Revilla and Nicolas Lopez Carranza and Adam Henryk Grzywaczewski and Francesco Oteri and Christian Dallago and Evan Trop and Hassan Sirelkhatim and Guillaume Richard and Marcin Skwark and Karim Beguir and Marie Lopez and Thomas Pierrot},
    title   = {The Nucleotide Transformer: Building and Evaluating Robust Foundation Models for Human Genomics},
    elocation-id = {2023.01.11.523679},
    year    = {2023},
    doi     = {10.1101/2023.01.11.523679},
    publisher = {Cold Spring Harbor Laboratory},
    URL     = {https://www.biorxiv.org/content/early/2023/01/15/2023.01.11.523679},
    eprint  = {https://www.biorxiv.org/content/early/2023/01/15/2023.01.11.523679.full.pdf},
    journal = {bioRxiv}
}
```

```bibtex
@article {Benegas2022.08.22.504706,
    author  = {Gonzalo Benegas and Sanjit Singh Batra and Yun S. Song},
    title   = {DNA language models are powerful zero-shot predictors of genome-wide variant effects},
    elocation-id = {2022.08.22.504706},
    year    = {2023},
    doi     = {10.1101/2022.08.22.504706},
    publisher = {Cold Spring Harbor Laboratory},
    URL     = {https://www.biorxiv.org/content/early/2023/04/12/2022.08.22.504706},
    eprint  = {https://www.biorxiv.org/content/early/2023/04/12/2022.08.22.504706.full.pdf},
    journal = {bioRxiv}
}
```
