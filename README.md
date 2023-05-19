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
