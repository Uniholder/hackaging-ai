# 🧬 1. Gene / Protein Overview
- **Gene Symbol / Name:** TERT (Telomerase Reverse Transcriptase)
- **Protein Name:** Telomerase reverse transcriptase
- **Identifiers:**
  - UniProt ID: [O14746](https://www.uniprot.org/uniprotkb/O14746/entry)
  - KEGG ID: [hsa:7015](https://www.kegg.jp/entry/hsa:7015)
  - HGNC: [HGNC:11730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11730)
  - Ensembl ID: [ENSG00000164362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164362)
- **Organism:** *Homo sapiens*
- **Sequence Links:**  
  - [Protein (UniProt)](https://www.uniprot.org/uniprotkb/O14746/entry)  
  - [DNA / mRNA (Ensembl)](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164362)

---

## 🔬 2. Structure and Functional Domains
- **Protein Length:** 1,132 amino acids (canonical isoform)
- **Key Domains / Motifs:**
  - Reverse transcriptase domain (605–935): Catalytic core with RNA-dependent DNA polymerase activity
  - RNA-interacting domains RD1 (1–230) and RD2 (325–550)
  - G-quadruplex binding motif (GQ, 58–197)
  - TFLY motif (328–333) and QFP motif (376–521) for RNA binding
  - Primer grip sequence (930–934) and Mg²⁺ binding sites (D712, D868, D869)
- **Functional Roles:** Telomere maintenance via telomeric repeat addition, regulation of oxidative stress response, and Wnt/β-catenin signaling modulation [Reactome: R-HSA-171319, R-HSA-201722].
- **Post-Translational Modifications (PTMs):**
  - S227 phosphorylation by AKT promotes nuclear localization
  - S457 phosphorylation by DYRK2 triggers ubiquitination and degradation
  - Y707 phosphorylation by SRC kinases under oxidative stress induces cytoplasmic translocation
- **Orthologs / Paralogs:**
  - *C. elegans*: SKN-1 (conserved role in stress resistance and longevity)
  - *Drosophila*: CncC (regulates oxidative stress response)
  - High conservation of reverse transcriptase domain across vertebrates

---

## ⚙️ 3. Sequence-to-Function Relationships
| Interval       | Type of Modification | Experimental Effect                     | Functional Outcome                          | Source   |
|----------------|----------------------|-----------------------------------------|---------------------------------------------|----------|
| 55 (L55Q)      | Point mutation       | Impaired telomerase activity            | Premature bone marrow failure (PFBMFT1)     | UniProt  |
| 570 (K570N)    | Point mutation       | Abolished catalytic activity            | Aplastic anemia                             | UniProt  |
| 605–935        | RT domain deletion   | Loss of polymerase activity             | Telomere shortening and cellular senescence | UniProt  |
| 712 (D712A)    | Mg²⁺ site mutation   | Complete loss of activity               | Disrupted telomere elongation               | UniProt  |
| 867 (V867M)    | Point mutation       | Severe processivity defect              | PFBMFT1 with shortened telomeres            | UniProt  |
| 930–934        | Primer grip mutation | Complete loss of catalytic activity     | Failed telomeric primer binding             | UniProt  |

---

## 🧠 4. Pathways and Functional Networks
- **KEGG Pathways:**
  - [Gastric cancer (hsa05226)](https://www.kegg.jp/pathway/hsa05226): TERT contributes to tumorigenesis via telomere maintenance and cellular immortalization.
  - [HPV infection (hsa05165)](https://www.kegg.jp/pathway/hsa05165): HPV upregulates TERT expression, promoting oncogenesis through telomerase activation.
- **Reactome Pathways:**
  - [Telomere extension by telomerase (R-HSA-171319)](https://reactome.org/content/detail/R-HSA-171319)
  - [Wnt/β-catenin signaling regulation (R-HSA-201722)](https://reactome.org/content/detail/R-HSA-201722)
- **Interaction Partners:** TERC (telomerase RNA component), dyskerin, and shelterin complex proteins (e.g., TRF1, TRF2).

---

## 🧓 5. Longevity and Aging Associations
- **Longevity Associations:** TERT overexpression extends lifespan in mice (16.7–41.5% median increase) and is linked to human longevity via SNPs like rs2853676 [PMID: 10.1093/gerona/glx247].
- **Model Organism Data:**

| Model                          | Intervention               | Result                                      | Reference                     |
|--------------------------------|----------------------------|---------------------------------------------|-------------------------------|
| Mouse (C57BL/6)                | AAV9-mTERT at 420 days     | ↑ 18.1% median lifespan                     | OpenGenes                     |
| Mouse (C57BL/6J)               | MCMV-TERT at 18 months     | ↑ 41.5% median lifespan (females)           | OpenGenes                     |
| Human (Japanese American men)  | rs2853676 variant          | Associated with longevity (p = 0.0159)      | [DOI: 10.1093/gerona/glx247] |

- **Human Disease Links:** Variants (e.g., A202T, H412Y) cause dyskeratosis congenita, aplastic anemia, and pulmonary fibrosis via telomere shortening.

---

## 💊 6. Small Molecule and Drug Interactions
- **Ateganosine (D13071):** Antiviral compound indirectly modulating TERT via HPV inhibition [KEGG: D13071].
- **Phosphorylation Regulators:**
  - AKT-mediated S227 phosphorylation enhances nuclear localization and activity.
  - DYRK2-mediated S457 phosphorylation promotes proteasomal degradation.
- **Oxidative Stress Response:** SRC kinase phosphorylation at Y707 reduces antiapoptotic activity under stress.

---

## 🌍 7. Evolutionary Conservation
- **Domain Conservation:** Reverse transcriptase domain (605–935) is >80% identical across mammals.
- **Ortholog Functions:**
  - *C. elegans* SKN-1: Regulates oxidative stress resistance and lifespan.
  - *Drosophila* CncC: Mediates antioxidant responses via Keap1-Nrf2 pathway.
- **Longevity Mechanism:** Conservation of telomere maintenance and stress response roles underscores TERT’s fundamental role in aging across species.

---

## 📚 8. References
1. UniProt: [O14746](https://www.uniprot.org/uniprotkb/O14746/entry)
2. KEGG: [hsa:7015](https://www.kegg.jp/entry/hsa:7015), [Gastric cancer pathway](https://www.kegg.jp/pathway/hsa05226), [HPV infection pathway](https://www.kegg.jp/pathway/hsa05165)
3. Reactome: [R-HSA-171319](https://reactome.org/content/detail/R-HSA-171319), [R-HSA-201722](https://reactome.org/content/detail/R-HSA-201722)
4. OpenGenes: [rs2853676 longevity association](https://doi.org/10.1093/gerona/glx247)
5. Disease associations: [Medulloblastoma (H01667)](https://www.kegg.jp/entry/H01667)
6. Structural data: PDB [7QXA](https://www.rcsb.org/structure/7QXA), [7TRD](https://www.rcsb.org/structure/7TRD)