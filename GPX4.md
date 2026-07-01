# 🧬 1. Gene / Protein Overview
- **Gene Symbol / Name:** GPX4 (Glutathione Peroxidase 4)
- **Protein Name:** Phospholipid hydroperoxide glutathione peroxidase GPX4
- **Identifiers:**
  - UniProt ID: [P36969](https://www.uniprot.org/uniprotkb/P36969/entry)
  - KEGG ID: [hsa:2879](https://www.kegg.jp/entry/hsa:2879)
  - HGNC: [HGNC:4556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4556)
  - Ensembl ID: [ENSG00000167468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167468)
- **Organism:** *Homo sapiens*
- **Sequence Links:**  
  - [Protein (UniProt)](https://www.uniprot.org/uniprotkb/P36969/entry)  
  - [DNA / mRNA (Ensembl)](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167468)

---

## 🔬 2. Structure and Functional Domains
- **Protein Length:** 197 amino acids (mitochondrial isoform), 170 amino acids (cytoplasmic isoform)
- **Key Domains / Motifs:**
  - Catalytic selenocysteine residue at position 73 (Sec, U)
  - Beta strands (45–48, 53–55, 62–69, 71–73, 95–101, 127–130, 135–137, 158–160, 167–170, 176–180)
  - Alpha helices (41–43, 56–59, 76–90, 91–93, 113–121, 142–149, 151–153, 186–192, 195–197)
- **Functional Roles:** Reduces phospholipid hydroperoxides using glutathione, critical for preventing ferroptosis and maintaining redox homeostasis [GO:0004602, GO:0047066, GO:0110076].
- **Post-Translational Modifications (PTMs):** Phosphorylation at Ser40.
- **Orthologs / Paralogs:** Structural data available for multiple species via PDB (e.g., 2GS3, 5H5Q), but specific ortholog % identity not provided in source data.

---

## ⚙️ 3. Sequence-to-Function Relationships
| Interval | Type of Modification | Experimental Effect | Functional Outcome | Source |
|-----------|---------------------|---------------------|--------------------|--------|
| 73        | Selenocysteine → Alanine | Loss of enzyme activity | Abolished phospholipid hydroperoxide reduction | UniProt |
| 73        | Selenocysteine → Cysteine | Near-complete activity loss | Severely impaired antioxidant function | UniProt |
| 90–197    | Deletion | Loss of functional domain | Spondylometaphyseal dysplasia, Sedaghatian type | UniProt |
| 120       | Threonine variant (rs76201145) | Altered protein function | Associated with cryptorchidism | UniProt |

---

## 🧠 4. Pathways and Functional Networks
- **KEGG Pathways:**
  - [Glutathione metabolism (hsa00480)](https://www.kegg.jp/pathway/hsa00480): GPX4 utilizes glutathione to reduce lipid hydroperoxides, maintaining cellular redox balance.
  - [Ferroptosis (hsa04216)](https://www.kegg.jp/pathway/hsa04216): GPX4 is the central negative regulator of ferroptosis; its inhibition causes iron-dependent lipid peroxidation and cell death.
- **Interaction Partners:** Binds FUNDC1 to regulate mitochondrial recruitment and mitophagy [UniProt].
- **Biological Roles:** Protects against oxidative damage in membranes, critical for neuronal survival, cardiac function, and embryonic development.

---

## 🧓 5. Longevity and Aging Associations
| Model | Intervention | Result | Reference |
|--------|--------------|--------|------------|
| Mouse (C57BL/6, male) | GPX4 knockout | ↑ Lifespan (5.4% mean, 6.9% median) under standard chow | OpenGenes |
| Mouse (unspecified) | GPX4 knockout | ↑ Oxidation/antioxidant function, ↓ stress response survival | OpenGenes |

- **Key Findings:**
  - Loss of GPX4 extends lifespan but reduces stress resilience.
  - Associated with dual roles in aging: protection against age-related impairment (e.g., carcinogenesis) and enhancement of deterioration (e.g., stress sensitivity).
  - Linked to the aging hallmark of reactive oxygen species accumulation.

---

## 💊 6. Small Molecule and Drug Interactions
- **Ferroptosis Inducers:** GPX4 inhibition (e.g., by RSL3 or ML162) triggers ferroptosis, though specific compounds are not listed in provided KEGG/UniProt data.
- **Mechanism:** Direct binding to GPX4’s active site (Sec73) disrupts phospholipid hydroperoxide reduction, leading to lethal lipid peroxidation.
- **Therapeutic Relevance:** Targeted in cancer therapy to induce ferroptosis in tumor cells.

---

## 🌍 7. Evolutionary Conservation
- **Domain Conservation:** Catalytic selenocysteine motif and structural folds are conserved from mammals to invertebrates.
- **Orthologs:** Functional analogs include *C. elegans* PHGPX-1 and *Drosophila* CG31148, though specific % identity not provided.
- **Longevity Link:** Conservation of ferroptosis regulation suggests ancient role in stress response and aging across metazoans.

---

## 📚 8. References
1. UniProt: [P36969](https://www.uniprot.org/uniprotkb/P36969/entry)
2. KEGG: [hsa:2879](https://www.kegg.jp/entry/hsa:2879)
3. KEGG Pathway hsa00480: [Glutathione metabolism](https://www.kegg.jp/pathway/hsa00480)
4. KEGG Pathway hsa04216: [Ferroptosis](https://www.kegg.jp/pathway/hsa04216)
5. KEGG Disease H01825: [Spondylometaphyseal dysplasia](https://www.kegg.jp/entry/H01825)
6. Ensembl: [ENSG00000167468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167468)
7. OpenGenes: GPX4 longevity analysis (source data provided in task)