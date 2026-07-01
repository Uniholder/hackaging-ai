# 🧬 1. Gene / Protein Overview
- **Gene Symbol / Name:** GHSR (Growth Hormone Secretagogue Receptor)
- **Protein Name:** Growth hormone secretagogue receptor
- **Identifiers:**
  - UniProt ID: [Q92847](https://www.uniprot.org/uniprot/Q92847)
  - KEGG ID: [hsa:2693](https://www.kegg.jp/entry/hsa:2693)
  - HGNC ID: [HGNC:4267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4267)
  - Ensembl ID: [ENSG00000121853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121853)
- **Organism:** *Homo sapiens*
- **Sequence Links:**  
  - [Protein (UniProt)](https://www.uniprot.org/uniprot/Q92847.fasta)  
  - [DNA / mRNA (Ensembl)](https://www.ensembl.org/Homo_sapiens/Transcript/Sequence_cDNA?db=core;g=ENSG00000121853;r=3:128000000-128100000)

---

## 🔬 2. Structure and Functional Domains
- **Protein Length:** 366 amino acids (canonical isoform 1A)
- **Key Domains / Motifs:**
  - 7 transmembrane helices (positions 41–66, 73–96, 118–139, 163–183, 212–235, 264–285, 303–326)
  - G-protein coupled receptor (GPCR) family signature
  - Disulfide bond between positions 116–198
- **Functional Roles:**
  - Mediates ghrelin-induced growth hormone secretion
  - Regulates energy homeostasis and appetite via Gαq signaling [GO:0004930, GO:0030252]
- **Post-Translational Modifications (PTMs):**
  - N-linked glycosylation at positions 13 and 27
- **Orthologs / Paralogs:**
  - No significant paralogs reported in KEGG/UniProt
  - Evolutionary conservation discussed in Section 7

---

## ⚙️ 3. Sequence-to-Function Relationships
| Interval | Type of Modification | Experimental Effect | Functional Outcome | Source |
|-----------|---------------------|---------------------|--------------------|--------|
| 204 (A→E) | Point mutation (rs121917883) | Impaired constitutive activity | Reduced cell-surface expression; GHDP pathogenesis | UniProt |
| 237 (R→W) | Point mutation (rs199588904) | Partial loss of constitutive activity | Normal cell-surface expression; GHDP pathogenesis | UniProt |
| 5 (T→I) | Point mutation (rs2232165) | Unknown functional impact | Population variant with unknown clinical significance | UniProt |

---

## 🧠 4. Pathways and Functional Networks
- **KEGG Pathways:**
  - [cAMP signaling pathway (hsa04024)](https://www.kegg.jp/pathway/hsa04024): Activates adenylate cyclase upon ghrelin binding → ↑ cAMP → hormone secretion
  - [Growth hormone synthesis/secretion (hsa04935)](https://www.kegg.jp/pathway/hsa04935): Central regulator of pituitary GH release
- **Interaction Partners:**
  - Ghrelin (ligand)
  - Gαq proteins (signaling)
  - KEAP1/NRF2 pathway (indirect via oxidative stress regulation)
- **Subcellular Localization:**
  - Plasma membrane (multi-pass), membrane rafts, glutamatergic synapses [GO:0005886]

---

## 🧓 5. Longevity and Aging Associations
- **Human Genetic Associations:**
  - rs572169 SNP associated with longevity in Danish populations [DOI:10.1016/j.exger.2012.02.010]
  - Haplotypes including rs572169 linked to longevity via INS/IGF-1 pathway dysregulation [DOI:10.1111/acel.12755]
- **Model Organism Data:**
  - *No experimental lifespan data available in OpenGenes*
- **Interventions:**
  - Pharmacological: Relamorelin (GHSR agonist) improves cachexia but longevity effects unstudied

| Model | Intervention | Result | Reference |
|--------|--------------|--------|------------|
| Human | rs572169 variant | Longevity association | [DOI:10.1016/j.exger.2012.02.010](https://doi.org/10.1016/j.exger.2012.02.010) |
| Human | rs572169 haplotypes | Longevity association | [DOI:10.1111/acel.12755](https://doi.org/10.1111/acel.12755) |

---

## 💊 6. Small Molecule and Drug Interactions
- **Relamorelin (D10660):**
  - Synthetic ghrelin receptor agonist
  - Mechanism: Mimics ghrelin → activates GHSR → ↑ GH secretion
  - Applications: Gastrointestinal motility disorders, cachexia
  - [Structure](https://www.kegg.jp/ligand/D10660)
- **Endogenous Ligand:**
  - Ghrelin: Binds extracellular domain → conformational change → G-protein activation

---

## 🌍 7. Evolutionary Conservation
- **Domain Conservation:**
  - Transmembrane topology conserved across vertebrates
  - GPCR signature motif preserved from fish to mammals
- **Functional Conservation:**
  - Orthologous pathways regulate growth/metabolism in *Mus musculus* (Ghsr), *Danio rerio* (ghsra/b)
  - No direct longevity ortholog data in invertebrates (e.g., *C. elegans* lacks direct GHSR homolog)
- **Longevity Link:**
  - INS/IGF-1 pathway conservation connects GHSR to aging mechanisms across species

---

## 📚 8. References
1. UniProt: [Q92847](https://www.uniprot.org/uniprot/Q92847)
2. KEGG: [hsa:2693](https://www.kegg.jp/entry/hsa:2693)
3. Ensembl: [ENSG00000121853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121853)
4. Reactome: [R-HSA-375276](https://reactome.org/content/detail/R-HSA-375276), [R-HSA-416476](https://reactome.org/content/detail/R-HSA-416476)
5. PDB: [6KO5](https://www.rcsb.org/structure/6KO5), [7F9Y](https://www.rcsb.org/structure/7F9Y)
6. DOI: [10.1016/j.exger.2012.02.010](https://doi.org/10.1016/j.exger.2012.02.010)
7. DOI: [10.1111/acel.12755](https://doi.org/10.1111/acel.12755)
8. KEGG Drug: [D10660](https://www.kegg.jp/entry/D10660)