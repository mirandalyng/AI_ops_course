# LLMOps – att hantera livscykeln för LLM-utveckling

## Fallstudie: en kundsupport-bot

- **Setup:** en bot baserad på GPT-5 med en RAG-pipeline. Den hanterar fakturering, kontohantering, teknisk felsökning och funktionsförklaringar.
- **Månad 1:** lyckad lansering med nöjda team och kunder.
- **Månad 2:** 30 nya funktioner och en ny prisplan släpps, men kunskapsbasen uppdateras inte. Boten svarar med gammal kunskap.
- **Månad 3:** en promptändring för mer koncisa svar gör att boten börjar korta ner felsökningsstegen. Det upptäcks först efter 4 dagar, via en ökning av supportärenden.
- **Månad 4:** kostnaderna skenar. Det finns ingen rate limiting och ingen spårning av tokenanvändning, och vissa användare ställer väldigt mycket frågor.
- **Månad 5:** teamet vill förbättra boten men kan inte. Det saknas promptversionering, feedbacksignal, strukturerad loggning och tokenspårning.

## Kärnbudskapet

- Traditionell mjukvara **fallerar högljutt**.
- LLM:er **fallerar tyst** och försämras över tid.
- **LLMOps** överbryggar gapet mellan "systemet är uppe" och "systemet gör det vi tror att det gör".

## Centrala utmaningar

- **Icke-deterministiskt:** samma input kan ge olika output.
- **Svårt att utvärdera.**
- **Prompten är kod:** den behöver versionering och testning.
- **Tokenkostnader, latens och optimering**, bland annat av reasoning.

## Nyckelkoncept

| Område                    | Innehåll                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Prompt engineering**    | versionering, promptmallar                                                                                         |
| **Utvärdering**           | LLM-as-judge, human-in-the-loop, offline- och online-evals                                                         |
| **Observability**         | tracing, drift, hallucinationer och toxicitet, latensövervakning                                                   |
| **RAG-pipelines**         | chunking-strategier, vektordatabashantering, versionering av embedding-modeller, övervakning av retrieval-kvalitet |
| **Deployment**            | modell-routing, fallback-kedjor, semantisk cachning, guardrails                                                    |
| **Säkerhet och styrning** | PII-detektering, audit-loggning, rate limiting                                                                     |
