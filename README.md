# Argumentation Theory

This repository is a TEI-XML an initiave corpus for early modern Arabic argumentation theory, especially the Ottoman reception of *ādāb al-baḥth wa-al-munāẓara*. It converts locally edited eScriptorium HTR outputs manuscript transcriptions into interoperable TEI records with manuscript description, multilingual metadata, light semantic markup, explicit editorial statements, and small analytical companion files. 

## Scope

The corpus currently has five witnesses, however important to note that, it will keep adding annotated manuscripts:

- `Hasiyetül_Kevâkibî_alâ_risâletil_bahs_Tasköprizâde`: gloss on Taşköprüzade.
- `Risālat fī al-Ādāb al-Baḥth Al-Samarqandi`: foundational base text by al-Samarqandī.
- `Risâle fî 'ilm-i âdâbi’l-bahŝ ve’l-münâzara Tasköprizâde`: concise Ottoman didactic epitome.
- `Serh_‘alâ_âdâbil_bahs_ve’l_münâzarâ_li’l_Birgivî`: compact pedagogical witness associated with Birgivī.
- `Telhîsü’l-Hüseyniyye fi’lâdâb Akkirmani`: later summary or *talḫīṣ*.

## Folder Pattern

Each manuscript folder is intended to contain the same core deliverables:

- source transcription as `*.txt`
- line-by-line annotated companion as `*.annotated.txt`
- manuscript TEI record as `tei.xml`
- particular argumentation terms, fields, researchers, and manuscript-level analytics data, such as `term_frequency_all.csc` and `visualization_all.csv`.
- local PDF witness

### Note 

The CSV files are light analytical aids, not authoritative scholarly ontologies. In folders where the raw transcription preserves duplicate or appended non-target material, the CSVs follow the main encoded witness rather than blindly counting every line in the raw file.

## Corpus Logic

The repository is not a random cluster of similar texts. It documents a layered teaching and commentary tradition around a shared technical vocabulary of disputation and/or dabate tradition. 

- Al-Samarqandī's *Risālah fī Ādāb al-Baḥth* serves as the conceptual base text. It gives concise definitions of `المناظرة`, `الدليل`, `المناقضة`, `النقض`, and `المعارضة`.
- Taşköprüzade and the Birgivī-associated witness compress the tradition into short pedagogical forms. Their wording is procedural and role-based, with emphasis on `السائل`, `المعلل`, and the order of objection.
- Al-Aqkirmanī expands the system into a summary that classifies argumentative states, response-types, and study methods.
- Al-Kawākibī's ḥāshiya is the most discursive witness in the set. It comments on authorities, elaborates definitions, and reflects the layered style of Ottoman gloss culture.

In practical terms, the corpus contains one base treatise, two concise teaching recensions, one summary, and one gloss. That genealogical relation matters for future topic modeling, terminology extraction, intellectual network analysis, and manuscript pedagogy research.

## Editorial Policy

Each `tei.xml` file carries its own `<editorialDecl>`, but the shared repository policy is:

- use the local edited transcription files as the certain source witness (Small mistakes or misspellings of words, etc., could be present )
- preserve Arabic orthography and sparse punctuation as transmitted in those edited files
- regularize only BOM artifacts, obvious XML-breaking characters, and excess whitespace introduced by transcription workflows
- encode folio-level or local witness-level divisions only where the source material supports them
- document exclusions when a raw transcription file contains another text, a duplicate witness, or an uncertain appendix
- avoid inventing marginalia, damage reports, or codicological detail not identified in the supplied witness
- keep generalize AI English translation blocks close to the supplied edited witness rather than reconstructing an idealized diplomatic text

## Witness-Specific Manuscript Annotation Notes

- `Hasiyetül_Kevâkibî_alâ_risâletil_bahs_Tasköprizâde`: the richest TEI profile in the repository; the gloss is encoded as an 8-folio edition with translation and commentary-aware markup.
- `Risālat fī al-Ādāb al-Baḥth Al-Samarqandi`: the foundational text; encoded as a concise base witness with a translation block and line-based companion annotation.
- `Risâle fî 'ilm-i âdâbi’l-bahŝ ve’l-münâzara Tasköprizâde`: the raw transcription continues with an unrelated logic text beginning with an Abharī/Isagoge-style incipit. That appended logic material is retained in the raw `.txt` and annotated companion but excluded from the main TEI witness and analytical CSV counts.
- `Serh_‘alâ_âdâbil_bahs_ve’l_münâzarâ_li’l_Birgivî`: the raw transcription preserves two parallel witnesses. The TEI encodes the cleaner primary witness; the duplicate noisier witness remains documented in the raw `.txt` and annotated companion.
- `Telhîsü’l-Hüseyniyye fi’lâdâb Akkirmani`: the raw transcription ends with an uncertain appended philosophical fragment after the dated colophon. The TEI preserves that fragment as an uncertain appendix, while the main analytical summaries track the summary text itself.

## FAIR and Licensing

The repository is structured for FAIR reuse.

- `Findable`: each TEI document has a stable `xml:id`, local identifier, and shelfmark.
- `Accessible`: files are plain UTF-8 XML, TXT, and CSV and can be processed with standard tools.
- `Interoperable`: metadata uses TEI elements for manuscript description, people, titles, dates, language, and keywords.
- `Reusable`: each file states its editorial basis and is released under `CC BY 4.0`.

## Bibliographic References

The repository-level TEI records and manuscript descriptions currently draw especially on:

- Diyanet manuscript catalog records linked in each witness-level `tei.xml`
- `tarajm.com` authority matching where applicable for Arabic biographical identification
- local project metadata from `arg_theory.js`
- local edited transcription witnesses and annotated companion files in each manuscript folder

### Note 

These references are documented at the witness level rather than centralized into a single bibliography file, because authority evidence varies from manuscript to manuscript.

## Source Basis

Primary local sources used for this repository build:

- `../Transcription of the Manuscripts/...`
- `../arg_theory.js`

Project framing and DH rationale were aligned with proposal materials on Arabic HTR, TEI, Ottoman intellectual history, and the transmission of *ādāb al-baḥth*.

## Citation

Suggested GitHub-style repository citation:

- Acar, Serhat. *Argumentation Theory: TEI-XML Pilot Corpus for Arabic and Ottoman Debate Theory Manuscripts*. GitHub repository, 2026.

## Copyright

@ Copyright Serhat Acar 2026.
