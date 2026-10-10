# Contributing to Awesome Secondary Aluminum Recycling & Pyrometallurgy

Thank you for your interest in contributing to **Awesome Secondary Aluminum Recycling & Pyrometallurgy**! This curated directory provides an exhaustive, high-fidelity resource for engineers, researchers, and data scientists working across high-temperature recycling, rotary and reverberatory melting, refractory computer vision, laser spectroscopy, and industrial telemetry.

---

## Contents

- [Code of Conduct](#code-of-conduct)
- [Inclusion Criteria](#inclusion-criteria)
- [How to Submit](#how-to-submit)
- [Entry Format](#entry-format)
- [Review Process](#review-process)

---

## Code of Conduct

We are committed to providing a welcoming, respectful, and professional environment. Please review and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Inclusion Criteria

To maintain high technical quality, proposed additions must satisfy these guidelines:

1. **Domain Relevance:** The project, dataset, paper, or tool must have a direct connection to secondary aluminum recycling, pyrometallurgy, furnace combustion, infrared thermography, refractory health inspection, casthouse CFD, scrap characterization (LIBS, XRF, hyperspectral), charge optimization (MILP blending), or industrial IoT (OPC-UA/SCADA).
2. **Quality and Maintenance:**
   - Open-source projects should have clear documentation, a recognized license, and active development or proven engineering utility.
   - Datasets must include accessible download links, clear annotations, and metadata describing industrial capture conditions.
   - Academic papers should be peer-reviewed benchmarks or seminal literature published in reputable journals or conference proceedings with valid DOI links.
3. **No Marketing Spam:** Open-source software, reproducible tools, and public datasets are prioritized. Proprietary vendor brochures, marketing teasers, or commercial advertisements are not accepted.
4. **Style Consistency:** Maintain clean Markdown formatting without emoji clutter. Headings and entries must adhere to professional engineering terminology.

---

## How to Submit

1. **Fork** the repository to your GitHub account.
2. **Create a branch** for your addition (`git checkout -b add/my-tool-name`).
3. **Edit `README.md`** and insert your item into the appropriate section.
4. Verify your formatting matches surrounding entries.
5. **Run test suite**: `python -m pytest tests/test_readme.py` to ensure zero broken anchors, clean syntax, and zero emoji clutter.
6. **Commit** your changes with a clear commit message (`git commit -m "feat: add PyCalphad salt flux modeling library"`).
7. **Push** your branch (`git push origin add/my-tool-name`) and open a **Pull Request**.

---

## Entry Format

For open-source repositories, libraries, and frameworks, use the canonical Awesome format:

```markdown
- [**Tool Name**](https://github.com/owner/repo) - Concise, technically grounded description detailing capabilities, algorithms, and practical utility in secondary aluminum pyrometallurgy or industrial computer vision.
```

For scientific papers and literature citations:

```markdown
- [**Paper Title**](https://doi.org/xxx) - **Authors (Year)**, *Journal/Publisher*. Summary of contribution, methodology, and domain relevance.
```

For benchmark datasets:

```markdown
- [**Dataset Name**](https://url) - Modality, defect taxonomy, sample counts, and metallurgical inspection relevance.
```

For industry standards and specifications:

```markdown
- [**Standard Code**](https://url) - Issuing body, scrap grade definitions, chemical limits, or inspection protocols.
```

---

## Review Process

Pull requests are reviewed regularly. We verify link validity, license status, domain relevance, and formatting standards before merging.

Thank you for contributing to the open metallurgical engineering and industrial computer vision ecosystem!
