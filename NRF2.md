# 🧬 1. Gene / Protein Overview
- **Gene Symbol / Name:** NFE2L2 (Nuclear factor erythroid 2-like 2)
- **Protein Name:** NFE2-like bZIP transcription factor 2 (NRF2)
- **Identifiers:**
  - UniProt: [Q16236](https://www.uniprot.org/uniprotkb/Q16236/entry)
  - KEGG: [hsa:4780](https://www.kegg.jp/entry/hsa:4780)
  - HGNC: [7782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7782)
  - Ensembl: [ENSG00000116044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116044)
- **Organism:** *Homo sapiens*
- **Sequence Links:**  
  - [Protein (UniProt)](https://www.uniprot.org/uniprotkb/Q16236/entry)  
  - [DNA / mRNA (Ensembl)](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116044)

---

## 🔬 2. Structure and Functional Domains
- **Protein Length:** 605 amino acids (canonical isoform Q16236-1)
- **Key Domains / Motifs:**
  - bZIP domain (497–560): DNA-binding and dimerization
  - ETGE motif (79–82) and DLG motif (29–31): KEAP1-binding sites
  - Neh1 domain (497–560): DNA binding
  - Disordered regions (334–449, 571–605): Regulatory regions
- **Functional Roles:** Master regulator of antioxidant response, binds to Antioxidant Response Elements (AREs) to activate cytoprotective genes (UniProt, KEGG).
- **Post-Translational Modifications (PTMs):**
  - Phosphorylation at S40 (PKC-mediated) promotes nuclear translocation
  - Acetylation at K596/K599 (CREBBP) enhances nuclear localization; deacetylation by SIRT1 retains in cytoplasm
  - Glycation at K462/K472/K487/R499/R569/K574 impairs function; deglycation by FN3K restores activity
- **Orthologs / Paralogs:**
  - *C. elegans*: SKN-1 (conserved oxidative stress response)
  - *Drosophila*: CncC (regulates detoxification genes)
  - % identity not specified in provided data

---

## ⚙️ 3. Sequence-to-Function Relationships
| Interval | Type of Modification | Experimental Effect | Functional Outcome | Source |
|-----------|---------------------|---------------------|--------------------|--------|
| 29–31 (DLG) | R31G mutation | Disrupted KEAP1 binding | Immunodeficiency, developmental delay (IMDDHH) | UniProt |
| 79–82 (ETGE) | E79K/T80K/G81S mutations | Abolished KEAP1 interaction | Constitutive NRF2 activation, ↑ stress resistance | UniProt |
| 497–560 (bZIP) | R499A mutation | Impaired DNA binding | Loss of transcriptional activity | UniProt |
| 591–596 | CHD6 interaction region deletion | Loss of transcriptional activation | Reduced antioxidant response | UniProt |

---

## 🧠 4. Pathways and Functional Networks
- **KEGG Pathways:**
  - [hsa05418: Fluid shear stress and atherosclerosis](https://www.kegg.jp/pathway/hsa05418): Regulates endothelial antioxidant defenses against oxidative stress in vascular disease.
  - [hsa04141: Protein processing in endoplasmic reticulum](https://www.kegg.jp/pathway/hsa04141): Mediates unfolded protein response (UPR) during ER stress, linking proteostasis to aging.
- **Interaction Partners:**
  - KEAP1 (primary regulator, targets NRF2 for degradation)
  - Small Maf proteins (heterodimerization via leucine-zipper domain)
  - CHD6 (transcriptional co-activator)
- **Biological Roles:** Central to oxidative stress response, inflammation regulation, and metabolic homeostasis (KEGG, Reactome).

---

## 🧓 5. Longevity and Aging Associations
- **Longevity Relevance:**
  - Constitutive activation (e.g., T80K) enhances stress resistance and suppresses inflammation/ferroptosis, mechanisms linked to aging.
  - Declining NRF2 activity with age contributes to accumulation of oxidative damage and age-related diseases (OpenGenes).
- **Model Organism Data:**
  - *C. elegans* SKN-1 ortholog: Overexpression extends lifespan and stress resistance (literature, not in provided dataset).
  - NRF2 activation in mice reduces age-related inflammation and neurodegeneration (OpenGenes).

| Model | Intervention | Result | Reference |
|--------|--------------|--------|------------|
| Human cells | T80K mutation | Constitutive activation, ↑ antioxidant response | UniProt |
| Mouse models | NRF2 knockout | ↓ Lifespan, ↑ inflammation and tissue damage | KEGG (H00048) |

---

## 💊 6. Small Molecule and Drug Interactions
- **Omaveloxolone (D10964):**
  - Mechanism: Direct NRF2 activator, enhances antioxidant response.
  - Relevance: Treats conditions involving oxidative stress (e.g., Friedreich's ataxia).
  - [KEGG Drug Entry](https://www.kegg.jp/entry/D10964)
- **Sulforaphane (indirect):**
  - Mechanism: Disrupts KEAP1-NRF2 binding via electrophilic modification of KEAP1 cysteines.
  - Source: Broccoli sprouts; not in provided dataset but widely documented in literature.

---

## 🌍 7. Evolutionary Conservation
- **Conserved Motifs:** ETGE/DLG KEAP1-binding motifs and bZIP domain preserved from *C. elegans* (SKN-1) to mammals.
- **Functional Conservation:** Orthologs regulate oxidative stress response across species:
  - *C. elegans* SKN-1: Required for longevity under dietary restriction.
  - *Drosophila* CncC: Mediates detoxification and stress resistance.
- **Longevity Link:** Conservation of NRF2/SKN-1 pathway underscores its fundamental role in aging across metazoans (OpenGenes).

---

## 📚 8. References
1. UniProt: [Q16236](https://www.uniprot.org/uniprotkb/Q16236/entry)
2. KEGG: [hsa:4780](https://www.kegg.jp/entry/hsa:4780), [hsa05418](https://www.kegg.jp/pathway/hsa05418), [hsa04141](https://www.kegg.jp/pathway/hsa04141), [D10964](https://www.kegg.jp/entry/D10964)
3. HGNC: [7782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7782)
4. Ensembl: [ENSG00000116044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116044)
5. OpenGenes: [NFE2L2 analysis](provided input data)
6. Reactome: [KEAP1-NFE2L2 regulation (R-HSA-9755511)](https://reactome.org/content/detail/R-HSA-9755511)