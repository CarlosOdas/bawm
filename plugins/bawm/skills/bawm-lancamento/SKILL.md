---
name: bawm-lancamento
description: "Fecha e publica um release do BAWM pela LANDR: metadados, arte, data, ISRC, registro autoral e declaração de IA. Use para \"subir o release\", \"os metadados\", \"a capa\", \"que data lanço\", \"declaração de IA\", \"ISRC\", \"ECAD\", \"registrar a obra\", ou quando o master volta da masterização."
---

# Lançamento do BAWM

Etapa 5 da cadeia. Consome o **master** de `bawm-producao` e o **dossiê da faixa**; entrega o release no ar e os registros feitos. Escreva em português; campos da LANDR e das lojas ficam em inglês.

## Portão de entrada — não negocie

**Dossiê fechado ou não há lançamento.** É veto da direção, não preferência. Confira os cinco blocos antes de abrir a LANDR: autoria (letra humana, rascunhos, datas) · componente de IA (modelo, assinatura ativa **no momento da geração**, Styles e Exclude exatos, sliders, gerações descartadas, ID do download) · montagem no Audacity · masterização (Style, Loudness, LUFS e true peak **medidos**) · direitos.

Se faltar bloco, volte à etapa dona dele. Não preencha de memória.

## Calendário

**Nunca lance com menos de quatro semanas de antecedência** — veto da direção, e é o que dá espaço ao pitch editorial. Cadência do selo: um single a cada 3 ou 4 semanas.

| Marco | Quando |
|---|---|
| Master aprovado e dossiê fechado | D−35 |
| Arte pronta e conferida | D−32 |
| Envio à LANDR, com data futura marcada | D−30 |
| Distribuição chega às lojas; link do Spotify existe | D−14 a D−10 |
| **Pitch editorial no Spotify for Artists** | **D−10, no mínimo D−7** |
| Canvas, cortes e calendário prontos (`bawm-marketing`) | D−7 |
| Lançamento | D, sexta-feira |

⚠️ O prazo entre envio e loja varia. **Confirme o que a LANDR mostra na tela de envio** e conte para trás a partir dele — o pitch precisa de 7 dias de folga *depois* de a faixa aparecer no Spotify for Artists.

**Teto da LANDR: 30 faixas com IA por mês por assinante.** É teto, não meta — o filtro de spam do Spotify sinaliza **contas**, não só faixas.

## Arte

Regras da LANDR, todas eliminatórias:

- Quadrado **1:1**, de **1500×1500 a 6000×6000 px**, **JPG ou PNG**
- **Sem perfil eSRGB**
- **Sem URL, sem @, sem logo de marca**
- ⚠️ **Arte duplicada entre releases é motivo de rejeição** — nem entre singles do mesmo ciclo

**Sem rosto humano fotorrealista gerado por IA.** Não é estética, é operação: aciona o selo *AI Persona* do Spotify. Linguagens do selo: ilustração, pintura, gravura, colagem, silhueta, máscara, grafismo, tipografia, textura, abstração, fotografia real de pessoas reais.

## Metadados

| Campo | Valor |
|---|---|
| Artist | Nome exato do elenco: `Caô`, `Carlos Odas` ou `BAWM` |
| **Artist ID** | **Sempre explícito.** Sem ID, a loja cria perfil novo e o catálogo racha |
| Label / Gravadora | `BAWM - Brazilian Artificial World Music` |
| Language | Português (ou a língua real da faixa) |
| Contributors | Compositor(es) da letra, com nome completo |
| Explicit | Marque de verdade quando for |

⚠️ **O campo mais caro de errar é o Artist ID.** Antes do primeiro release de um artista, procure o nome no Spotify, Apple Music e Deezer; depois entregue sempre apontando para o mesmo ID.

**Título:** sem palavra-chave de SEO, sem sufixo de gênero, sem `(Official)`. Nome próprio no título é marca do Caô — mantenha.

## ISRC e registro — três atos distintos

Confundir os três é o erro mais comum do selo.

1. **ISRC** — a LANDR gera. Identifica o **fonograma**. Só isso.
2. **Registro na associação** (agência nacional: **Pro-Música Brasil**) — não acontece sozinho.
3. **ECAD** — ato separado do anterior. Ter ISRC não põe a obra no ECAD.

⚠️ **A ABRAMUS exige nome completo e CPF de músicos, intérprete e produtor fonográfico. Não há como preencher isso para gravação sem intérprete humano.** Consequência prática: **registre a obra** (a letra e a composição, onde a autoria humana é real e documentada); **não prometa que o fonograma de IA passa no ECAD.** Se o usuário planejar receita em cima disso, diga que não fecha.

## Declaração de IA

**Obrigatória na LANDR.** Declarar remove a entrega para **YouTube Content ID, Meta, TikTok, Deezer, Lissen, Pandora e Tencent**. Continuam **Spotify, Apple Music e Amazon**.

⚠️ **Contradição não resolvida na própria LANDR:** o artigo de ajuda aceita faixa com IA (teto de 30/mês) e as diretrizes gerais proíbem "música inteiramente gerada por IA". **Peça ao suporte um posicionamento por escrito sobre o caso do selo e guarde a resposta no dossiê.** Enquanto não houver resposta, o risco de takedown é real e o usuário precisa saber disso antes de subir, não depois.

**Spotify.** *AI Credits* — opcional, via distribuidor: **declare**. *AI Persona* — aplica-se quando o rosto público do artista é humano fotorrealista gerado por IA; exclui de editoriais e de **toda** recomendação algorítmica, e a autodeclaração é **irreversível**. Fazer a música com IA não aciona; o rosto aciona.

**Apple** está tornando as AI Transparency Tags obrigatórias em 2026. **Deezer** detecta assinatura de Suno com 99,8%, exclui do Flow e remove faixa sem stream há 6+ meses — mas a declaração de IA já tira a Deezer da entrega.

## A armadilha da assinatura

Royalties são 100% **enquanto a assinatura da LANDR está ativa**. **Se cancelar, ela retém 15% para sempre — e isso atinge também os colaboradores nos splits.**

**Nunca deixe a assinatura cair com catálogo no ar.** Se o usuário falar em cortar custo, é este o custo que não se corta.

## Nunca

Comprar streams · promoção com plays garantidos · bot · loop do próprio catálogo · palavra-chave de SEO em nome ou título · versão sped up/slowed do próprio catálogo · arte repetida · faixa entre 30 e 60 segundos · variante quase idêntica de outra faixa do catálogo.

## Antes de apertar o botão

- [ ] Dossiê fechado, cinco blocos
- [ ] Master medido: LUFS integrado e true peak registrados
- [ ] Arte 1:1, dentro das dimensões, inédita no catálogo, sem rosto fotorrealista de IA
- [ ] Artist ID correto e explícito
- [ ] Gravadora: `BAWM - Brazilian Artificial World Music`
- [ ] Declaração de IA feita; consequências de entrega compreendidas
- [ ] AI Credits declarados no Spotify
- [ ] Data a 4+ semanas, com folga de 7 dias para o pitch
- [ ] Registro da obra encaminhado (associação e ECAD são atos separados)
- [ ] Assinatura da LANDR ativa e paga
- [ ] Perfil do artista reivindicado e com bio — hoje é pendência aberta do selo

Feche entregando a `bawm-marketing`: data, link, tema da faixa e a imagem central da letra.
