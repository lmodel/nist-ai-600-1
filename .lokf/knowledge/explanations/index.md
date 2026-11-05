# Explanations

* [Where each part comes from](where-each-part-comes-from.md) - NIST publishes no machine-readable form of the Profile, so a script reads the tables of section 3 from the PDF, and tests hold section 2's definitions and Appendix A's lists to its words. The AI RMF's own terms come from lmodel/nist-ai-100-1.
* [Faults in the publication](faults-in-the-publication.md) - What the catalogue corrects in the tables, each listed in the builder and held by a test: the identifier GV4.3--001, the tag Civil Rights violations on GV-1.4-002, and one row with a missing semicolon. Two further faults stay as they are.
* [Modelling choices](modelling-choices.md) - Why AI actor tasks belong to a table and not an action, why a risk's groupings are a list, why Pre-Deployment Testing holds structured feedback, and why each primary consideration is a class of its own.
* [Scope](scope.md) - What the schema leaves out: the discussion of each risk, the running prose of Appendix A, definitions quoted from third parties and the references of Appendix B. The AI RMF itself is lmodel/nist-ai-100-1.
* [Mappings](mappings.md) - What the schema crosses to: lmodel/nist-ai-100-1, lmodel/oscal, lmodel/stix and lmodel/spdx, each read at its source. The two SSSOM sets and their mappings to OWASP lists are gone, because a matching tool wrote their rows and no source confirmed them.
