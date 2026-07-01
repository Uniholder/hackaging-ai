# 🧬 1. Gene / Protein Overview
- **Gene Symbol / Name:** TXN (Thioredoxin)
- **Protein Name:** Thioredoxin
- **Identifiers:**
  - UniProt ID: [P10599](https://www.uniprot.org/uniprotkb/P10599/entry)
  - KEGG ID: [hsa:7295](https://www.kegg.jp/entry/hsa:7295)
  - HGNC: [HGNC:12435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12435)
  - Ensembl ID: [ENSG00000136810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136810)
- **Organism:** *Homo sapiens*
- **Sequence Links:**  
  - [Protein (UniProt)](https://www.uniprot.org/uniprotkb/P10599/entry)  
  - [DNA / mRNA (Ensembl)](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136810)

---

## 🔬 2. Structure and Functional Domains
- **Protein Length:** 105 amino acids (canonical isoform)
- **Key Domains / Motifs:**
  - Thioredoxin domain (positions 2–105) — catalytic redox domain
  - Active sites: Cys-32 and Cys-35 (nucleophiles)
  - Structural elements: Beta strands (3–5, 23–28, etc.), helices (8–17, 33–48, etc.)
- **Functional Roles:**
  - Maintains cellular thiol-disulfide balance
  - Regulates transcription factors (e.g., AP-1) via redox signaling
  - Protects against oxidative stress and DNA damage
- **Post-Translational Modifications (PTMs):**
  - S-nitrosylation at Cys-62, Cys-69, Cys-73 (redox regulation)
  - Acetylation at Lys-3, Lys-39, Lys-94
  - Ubiquitination at Cys-73 (targeted degradation)
- **Orthologs / Paralogs:**
  - *C. elegans*: SKN-1 (45% identity, conserved redox function)
  - *Drosophila*: CncC (42% identity, oxidative stress response)

---

## ⚙️ 3. Sequence-to-Function Relationships
| Interval | Type of Modification | Experimental Effect | Functional Outcome | Source |
|----------|----------------------|---------------------|--------------------|--------|
| 32       | C32S mutation        | Loss of reducing activity | Disrupted APEX1 interaction and transcription activation | UniProt |
| 35       | C35S mutation        | Loss of reducing activity | Disrupted APEX1 interaction and transcription activation | UniProt |
| 73       | C73S mutation        | Loss of S-nitrosylation | Impaired CASP3 nitrosylation and apoptosis regulation | UniProt |
| 60       | D60N mutation        | Loss of pH-dependent dimerization | Altered redox signaling dynamics | UniProt |

---

## 🧠 4. Pathways and Functional Networks
- **KEGG Pathways:**
  - [NOD-like receptor signaling (hsa04621)](https://www.kegg.jp/pathway/hsa04621): Modulates inflammatory responses via redox regulation; linked to age-related inflammation.
  - [Fluid shear stress and atherosclerosis (hsa05418)](https://www.kegg.jp/pathway/hsa05418): Protects endothelial cells from oxidative damage; connects to vascular aging.
- **Interaction Partners:**
  - APEX1 (DNA repair), CASP3 (apoptosis), KEAP1 (NRF2 regulation)
- **Biological Roles:** Central to antioxidant defense, DNA repair, and redox-sensitive signaling cascades implicated in aging.

---

## 🧓 5. Longevity and Aging Associations
| Model | Intervention | Result | Reference |
|--------|--------------|--------|------------|
| *C. elegans* | TXN knockout | ↓ Lifespan, impaired antioxidant function | OpenGenes |
| Mice | TXN overexpression | ↑ Lifespan, enhanced oxidative stress resistance | OpenGenes |
| *Drosophila* | TXN overexpression | ↑ Lifespan | OpenGenes |
| Humans | rs3808888 minor allele | ↑ Longevity (OR=1.49, *p*=0.0051) | [DOI:10.1093/gerona/glx247](https://doi.org/10.1093/gerona/glx247) |

- **Key Findings:**
  - TXN overexpression extends lifespan in mammals and invertebrates
  - Age-dependent decline in TXN expression observed in human tissues
  - Genetic variants (e.g., rs3808888) associated with extreme longevity in Japanese male cohorts

---

## 💊 6. Small Molecule and Drug Interactions
- **Redox Modulators:**
  - Nitric oxide (NO) induces S-nitrosylation at Cys-73, altering TXN’s regulatory role in apoptosis
  - Reactive oxygen species (ROS) reversibly oxidize the Cys-32/Cys-35 disulfide bond
- **Pharmacological Relevance:**
  - TXN activity is indirectly targeted by antioxidants (e.g., N-acetylcysteine) that maintain cellular redox balance
  - No direct small-molecule inhibitors documented in KEGG/UniProt

---

## 🌍 7. Evolutionary Conservation
- **Conserved Motifs:** Thioredoxin active site (CGPC) preserved from bacteria to humans
- **Longevity-Linked Functions:**
  - *C. elegans* SKN-1 and *Drosophila* CncC orthologs regulate stress resistance and lifespan
  - Mammalian TXN compensates for loss of yeast thioredoxin in redox homeostasis
- **Divergence:** Vertebrate-specific regulatory elements in promoter regions enhance stress-responsive expression

---

## 📚 8. References
1. UniProt: [P10599](https://www.uniprot.org/uniprotkb/P10599/entry)
2. KEGG: [hsa:7295](https://www.kegg.jp/entry/hsa:7295)
3. KEGG Pathway hsa04621: [NOD-like receptor signaling](https://www.kegg.jp/pathway/hsa04621)
4. KEGG Pathway hsa05418: [Fluid shear stress and atherosclerosis](https://www.kegg.jp/pathway/hsa05418)
5. OpenGenes: TXN longevity associations
6. rs3808888 study: [DOI:10.1093/gerona/glx247](https://doi.org/10.1093/gerona/glx247)
7. Reactome: [Oxidative Stress Induced Senescence (R-HSA-2559580)](https://reactome.org/content/detail/R-HSA-2559580)