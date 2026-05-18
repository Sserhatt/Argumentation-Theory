# Argumentation Theory

This repository is a TEI-XML an initiave corpus for early modern Arabic argumentation theory, especially the Ottoman reception of *ādāb al-baḥth wa-al-munāẓara*. It converts locally edited eScriptorium HTR manuscript transcriptions outputs into interoperable TEI records with manuscript description, multilingual metadata, light semantic markup, explicit editorial statements, and small analytical companion files. 

## Scope

The corpus currently has five witnesses, but important to note that, I will continue updating annotated manuscripts and listing :

- `Hasiyetül_Kevâkibî_alâ_risâletil_bahs_Tasköprizâde`: gloss on Taşköprüzade.
- `Risālat fī al-Ādāb al-Baḥth Al-Samarqandi`: foundational base text by al-Samarqandī.
- `Risâle fî 'ilm-i âdâbi’l-bahŝ ve’l-münâzara Tasköprizâde`: concise Ottoman didactic epitome.
- `Serh_‘alâ_âdâbil_bahs_ve’l_münâzarâ_li’l_Birgivî`: compact pedagogical witness associated with Birgivī.
- `Telhîsü’l-Hüseyniyye fi’lâdâb Akkirmani`: later summary or *talḫīṣ*.

## Folder Pattern

Each manuscript folder is intended to contain the same core deliverables:

- source transcription as `*.txt`
- line-by-line annotated companion as `*.annotated.tsv`
- manuscript TEI record as `tei.xml`
- manuscript-level analytical companion files derived from the encoded witness and visualization process in the future, such as `term_frequency.csv` and `visualization_entities.csv`, with repository-wide aggregate files at the root as `term_frequency_all.csv` and `visualization_all.csv`
- local PDF witness

### Note 

CSV files are light analytical aids, not authoritative scholarly ontologies. In folders where the raw transcription preserves duplicate or appended non-target material, the files follow the main encoded witness rather than blindly counting every line in the raw file.

The `.annotated.tsv` companions and the aggregate CSV files are saved as UTF-8 with BOM so that Arabic text opens more reliably without errors in Windows spreadsheet and text-viewing software.

## Corpus Logic

Argumentation manuscripts repository is not a random cluster of similar texts. It documents a layered teaching and commentary tradition around a shared technical vocabulary of disputation and/or dabate tradition. For instance ; 

- Al-Samarqandī's *Risālah fī Ādāb al-Baḥth* serves as the conceptual base text. It gives concise definitions of  `المناظرة` (disputation), `الدليل` (proof), `المناقضة` (ambivalence) , `النقض` (disproofs), and `المعارضة` (opposition).
- Taşköprüzade and the Birgivī-associated witness compress the tradition into short pedagogical forms. Their wording is procedural and role-based, with emphasis on `السائل` (inquirer), `المعلل` (justified), and ` الاعتراض` order of objection.
- Al-Aqkirmanī expands the system into a summary that classifies argumentative states, response-types, and study methods.
- Al-Kawākibī's ḥāshiya is the most discursive witness in the set. It comments on authorities, elaborates definitions, and reflects the layered style of Ottoman gloss culture.

In practical terms, the corpus contains one base treatise, two concise teaching recensions, one summary, and one gloss. That genealogical relation matters for future topic modeling, terminology extraction, intellectual network analysis, and manuscript pedagogy research.

## Editorial Policy

Each `tei.xml` file carries its own `<editorialDecl>`, but shared repository OA policy is:

- use local edited transcription files as the certain source witness (minor errors, typos, etc., may be present)
- preserve Arabic orthography and sparse punctuation as transmitted in those edited files
- regularize only BOM artifacts, obvious XML-breaking characters, and excess whitespace introduced by transcription workflows
- document exclusions when a raw transcription file contains another text, a duplicate witness, or an uncertain appendix
- avoid inventing marginalia, damage reports, or codicological detail not identified in the supplied witness
- keep generalize AI English translation blocks close to the supplied edited witness rather than reconstructing an idealized diplomatic text

## Witness-Specific Manuscript Annotation Notes

- `Hasiyetül_Kevâkibî_alâ_risâletil_bahs_Tasköprizâde`: a richest TEI profile in the repository; the gloss is encoded as an 8-folio edition with translation and commentary-aware markup.
- `Risālat fī al-Ādāb al-Baḥth Al-Samarqandi`: a foundational text; encoded as a concise base witness with a translation block and line-based companion annotation.
- `Risâle fî 'ilm-i âdâbi’l-bahŝ ve’l-münâzara Tasköprizâde`: the raw transcription continues with an unrelated logic text beginning with an Abharī/Isagoge-style incipit. That appended logic material is retained in annotated `.tsv` companion but excluded from the main TEI witness and analytical CSV counts.
- `Serh_‘alâ_âdâbil_bahs_ve’l_münâzarâ_li’l_Birgivî`: the raw transcription preserves two parallel witnesses. The TEI encodes the cleaner primary witness; the duplicate noisier witness remains documented in the raw `.txt` and annotated `.tsv` companion.
- `Telhîsü’l-Hüseyniyye fi’lâdâb Akkirmani`: the raw transcription ends with an uncertain appended philosophical fragment after the dated colophon. The TEI preserves that fragment as an uncertain appendix, while the main analytical summaries track the summary text itself.

## FAIR and Licensing

The repository is structured according to FAIR Principles: 

- `Findable`: each TEI document has a stable `xml:id`, local identifier, and shelfmark.
- `Accessible`: files are plain UTF-8 XML, TXT, TSV, and CSV and can be processed with standard tools.
- `Interoperable`: metadata uses TEI elements for manuscript description, people, titles, dates, language, and keywords.
- `Reusable`: each file states its editorial basis and is released under `CC BY 4.0`.

## Local Docker Check

The repository can be checked and downloaded locally from the root `Dockerfile`:

```bash
docker build --no-cache -t argumentation-theory .
docker run --rm -p 8000:8000 --name argumentation-theory-test argumentation-theory
```

The container validates all `tei.xml` files with `xmllint --noout` before starting a UTF-8-aware static file server. This keeps the local browser view aligned with the repository's Unicode text files.

## Corpus Dashboard

The repository already includes a local HTML visualization file:

- `adab_al_bahth_corpus_dashboard.html`

If you want to visualize it in a browser, you can either open the file directly or serve the repository root locally. For example:

```bash
 python3 -m http.server 8010 "
```

Then open:

- `http://localhost:8010/adab_al_bahth_corpus_dashboard.html`  

The dashboard is currently feasible and useful as a lightweight corpus-facing interface. It presents four linked views:

- aggregate term frequency across the five witnesses
- entity-type distribution by manuscript
- a scholar/person layer with historical figures cited in the corpus
- a simple term co-occurrence network across manuscripts


## Bibliographic References

The repository-level TEI records and manuscript descriptions currently draw especially on:

- Diyanet manuscript catalog records linked in each witness-level `tei.xml`
- `tarajm.com` authority matching where applicable for Arabic biographical identification if there is no authority records found in `VIAF`, `wikidata`, `ISNI`
- local project metadata from `arg_theory.js` 
- local edited transcription witnesses and annotated companion files in each manuscript folder

### Note 

These references are documented at the witness level rather than centralized into a single bibliography file, because authority evidence varies from manuscript to manuscript.

## Source Basis

Primary local sources used ––will use –– for this repository build:

- `../Transcription of the Manuscripts/...`
- `../arg_theory.js`

Project framing and DH rationale were aligned with proposal materials on Arabic HTR, TEI, Ottoman intellectual history, and the transmission of *ādāb al-baḥth*.

## Citation

Suggested GitHub-style repository citation:

- Acar, Serhat. *Argumentation Theory: TEI-XML Pilot Corpus for Arabic and Ottoman Debate Theory Manuscripts*. GitHub repository, 2026.

## Copyright

@ Copyright Serhat Acar 2026.
