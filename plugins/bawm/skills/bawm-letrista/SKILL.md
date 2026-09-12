---
name: bawm-letrista
description: "Escreve, lapida e documenta a letra de uma faixa do BAWM. Use para \"escrever a letra\", \"revisar a letra\", \"o refrão não fecha\", \"a métrica\", \"rima forçada\", \"o vocal sai apressado\", \"falta uma estrofe\", \"dossiê de autoria\", ou quando a direção fecha um briefing e a faixa precisa de texto."
---

# Letra e autoria do BAWM

Etapa 2 da cadeia. Consome o **briefing** da direção (artista, tema, geografia sonora, função no plano) e entrega duas coisas que andam sempre juntas: a **letra limpa** e o **dossiê de autoria humana**. Sem o segundo, a primeira não serve ao selo. Escreva em português; termos de interface do Suno ficam em inglês.

## Por que esta é a etapa mais importante juridicamente

Obra gerada por IA não tem autor e não é registrável — Lei 9.610/98 art. 11 e posição do INPI no Brasil, USCO e *Thaler* nos EUA. O fonograma que sai do Suno não é seu de forma robusta: a cessão é só "o direito que a Suno detenha", sem garantia de não-infração, com teto de responsabilidade de 100 dólares.

**A letra é a única parte da faixa que pode ser inequivocamente humana, autoral e registrável.** É ela que sustenta o registro na associação, o pleito no ECAD e qualquer conversa de sync. Por isso a direção veta lançamento cuja letra não seja humana e documentada.

Consequência direta: **quem escreve a letra é o humano.** Esta skill é oficina, não ghostwriter.

## Três modos de ajuda — escolha antes de começar

O usuário decide o modo; o dossiê registra qual foi usado. O objetivo do dossiê é ser **verdadeiro**, não ser bonito.

| Modo | O que a skill faz | Autoria resultante |
|---|---|---|
| **Oficina** (padrão) | Escande métrica, aponta clichê, rima forçada, imagem que não fecha, seção fraca. Não escreve verso | 100% humana, registrável |
| **Provocação** | Devolve perguntas, imagens, campo semântico, vocabulário de época ou de lugar. Não escreve verso | 100% humana, registrável |
| **Coautoria assistida** | Propõe versos e alternativas de linha | **Mista.** Não registre como obra puramente humana. Declare no dossiê linha a linha |

Se o usuário pedir "escreve a letra pra mim", diga o custo em uma frase e ofereça o modo Oficina. Se ele confirmar mesmo assim, é decisão dele: entregue e **marque cada linha proposta no dossiê**. Não deixe passar sem registro — é isso que quebra a defesa depois.

## Método de oficina

Quatro movimentos, nesta ordem. Não pule para o verso.

1. **Achar a pessoa.** O Caô canta gente — figura nomeada, de preferência no título (Walter, Ana Flor, Quasimodo, Ìaro). Quem é? O que quer? O que a impede? Sem isso, sai hino genérico.
2. **Achar a travessia.** Toda faixa do Caô move alguém de um lado a outro: margem, portal, rio, morte, fé, cidade. Qual é a passagem desta?
3. **Achar a imagem única.** Uma imagem concreta que a faixa possa repetir e virar. O colar e as contas são do projeto; esta faixa precisa da sua.
4. **Só então escrever**, e escrever em voz alta.

## Métrica em português — o que evita retrabalho no Suno

Quando o vocal sai apressado no Suno, **o problema é densidade silábica da letra, não BPM**. Não se corrige com tag; corrige-se cortando sílaba.

**Conte à maneira portuguesa: até a última sílaba tônica do verso.** O que vem depois dela não conta.

```
Me / u  ri / o  cor / re  a  ti          → "ti" é tônica e é a 7ª: redondilha maior
```

- **Redondilha maior (7)** — a medida natural da canção popular brasileira. Padrão do Caô.
- **Decassílabo (10)** — para verso de peso, entrada do Bento, seção de ritual.
- **Redondilha menor (5)** — refrão curto, coro, resposta.
- **Elisão:** vogal final que encontra vogal inicial funde numa sílaba só (`corre_a`). Conte cantando, não lendo.

⚠️ **Nunca traduza métrica do inglês.** Uma linha que cabe em inglês estoura em português — a mesma ideia pede mais sílabas. Letra vertida sem remetrificar é a causa número um de vocal atropelado.

**Teste prático:** cante a estrofe em andamento médio batendo o pé. Se faltou ar, sobra sílaba.

## Rima

- **Consoante** (som inteiro: *colar / altar*) fecha e assenta. Use no refrão e no fim de seção.
- **Toante** (só as vogais: *rio / abrigo*) respira e soa moderno. Use nas estrofes.
- Rima pobre entre palavras da mesma classe (*-ção* com *-ção*, verbo no infinitivo com verbo no infinitivo) é o que mais envelhece o texto.
- **Rima forçada é sempre pior que verso branco.** Se a rima está mandando na frase, corte a rima.

## O que o Caô canta — e o que não canta

**Vocabulário do artista:** *o ritual* · *o portal* · *o colar* e *as contas* · *travessia* · *rio* · *o outro lado* · *Afro-Barroco*. Use com parcimônia: se aparecer em toda faixa, vira maneirismo.

**Temas:** pertencimento, travessia, ancestralidade, fé popular, figuras humanas nomeadas.

**Tabus:** ironia fácil, gíria de internet, tema de consumo, qualquer coisa que soe a jingle. Some a isso o que envelhece qualquer letra: abstração empilhada sem uma imagem concreta, e a palavra "alma" usada como muleta.

Para outro artista do elenco, peça a bíblia dele a `bawm-artista` antes de escrever.

## Estrutura que o Suno aguenta

Escreva pensando em seções, mas **entregue a letra limpa, sem tag nenhuma** — colchete, cue e bloco Styles são trabalho de `bawm-arranjador`. Dois autores mexendo nas tags é como o prompt incha.

- 2 a 3 estrofes, refrão que volta 2 ou 3 vezes, uma ponte que muda de lugar.
- Refrão de 2 ou 4 linhas. Refrão longo dilui.
- Ponte é onde a travessia acontece — mude a pessoa do verbo, o tempo, ou quem fala.
- Faixa nunca entre 30 e 60 segundos (regra da direção). Letra curta demais empurra a faixa para essa faixa morta.
- Repetição é para ser escrita por extenso. `(x2)` e `[Chorus x2]` não funcionam no Suno.

## Dossiê de autoria — o artefato desta etapa

Modelo: **`modelos/dossie-de-faixa.md`**. O briefing que abre esta etapa vem em **`modelos/briefing-de-faixa.md`**.

Abra no briefing, feche antes do lançamento. Esta etapa preenche o **bloco 1, Autoria**:

- **Quem escreveu, quando e onde.** Nome completo, datas, local.
- **Rascunhos.** Onde estão os arquivos, com data de modificação preservada. Guarde as versões intermediárias — a cadeia de rascunhos é a prova mais forte que existe.
- **Decisões.** O que mudou entre a v1 e a final e por quê. Duas ou três linhas bastam.
- **Modo de assistência usado** (Oficina / Provocação / Coautoria) e, se houve coautoria, **quais linhas**.
- **Fontes e referências** — se algum verso cita, adapta ou responde a domínio público, registre.

⚠️ **Nunca reconstrua o dossiê depois.** Dossiê escrito no dia do lançamento não tem valor probatório e todo mundo percebe.

## Antes de passar ao arranjo

- [ ] A letra tem uma pessoa, uma travessia e uma imagem própria
- [ ] Métrica escandida e cantada em voz alta; nenhuma estrofe sem ar
- [ ] Nenhuma rima mandando na frase
- [ ] Nenhum tabu do artista
- [ ] Letra **sem tags**, pronta para `bawm-arranjador`
- [ ] Bloco de autoria do dossiê preenchido, com rascunhos guardados
