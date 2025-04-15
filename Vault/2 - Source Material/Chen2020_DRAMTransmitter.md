---
title: A Single-Ended Transmitter With Low Switching Noise Injection and Quadrature Clock Correction Schemes for DRAM Interface
authors:
  - Chen, Yu
  - et al.
year: 2020
source: IEEE Journal of Solid-State Circuits
zotero-key: chen2020dram
tags:
  - DRAM
  - transmitter
  - jitter
  - clock
  - correction
  - PLL
related:
  - DRAM_Interface
  - "[[Chen2020_DRAMTransmitter]]"
  - Transmitter_Circuits
---
## 🔍 Resumo da ideia central

Apresenta um transmissor single-ended para interface DRAM com técnicas de mitigação de ruído de comutação e correção de quadratura de clock. A proposta melhora o desempenho do sistema sem aumentar complexidade de clocking.

## 📌 Anotações importantes (copiadas do Zotero)

> - Page 3: "Quadrature clock correction reduces timing skew due to mismatch in routing."
> - Page 5: "Noise injection is reduced using a pseudo-differential driver design."

## 🧠 Minhas reflexões

- Essa abordagem pode ser útil para o projeto do driver da minha interface.
- O uso de correção de clock quadratura se relaciona com o que Razavi apresenta em [[PLL]].
- Talvez eu possa estudar mais sobre como implementar pseudo-diferencial sem aumentar consumo.

## 🔗 Conexões

- [[DRAM_Interface]]
- [[Transmitter_Circuits]]
- [[Clock_Skew]]
- [[PLL_Jitter_Reduction]]

## ✅ Próximos passos

- Estudar mais sobre pseudo-differential drivers
- Ver se há simulações públicas disponíveis no GitHub ou artigos semelhantes
- Tentar reimplementar o esquema proposto no Qucs ou LTSpice
