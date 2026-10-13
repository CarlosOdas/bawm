# Sozinho em Procissão — pacote Suno v1

> ⚠️ **Substituído pelo [v2](suno-v2.md) em 02/10/2026** (quatro partes, 9+ min). Mantido como histórico.

> 01/10/2026 · `bawm-arranjador` sobre a letra v1 ([`letra.md`](letra.md)).
> Faixa longa (~7 min) com instrumentais longos: ver **Como gerar** antes de gastar crédito.
> ⚠️ Com Custom Model ou Style Persona do Caô, **não cole o Styles**.

## 1. Mapa da faixa

| Seção | Quem toca | Duração aprox. |
|---|---|---|
| Prelúdio | mellotron (a lua) + violino solo da **Helena**: o tema da procissão | 0:00–0:50 |
| Estação I | **Bento** canta, cello e nylon | 0:50–1:30 |
| Interlúdio: o mar | tambores de cortejo ao longe, coro sem palavras | 1:30–2:10 |
| Estação II | **Bento**, cordas graves | 2:10–2:50 |
| O fado | percussão de mão da **Lia** acelerando, ostinato de cello, violino em desatino, flauta como vento, murmúrio grave sem palavras; tudo cresce até o auge | 2:50–4:50 |
| Silêncio | nada | 2–3 s |
| Interlúdio: a estrela | flauta solo aguda | 4:55–5:25 |
| Estação final | **Bento** + o grupo inteiro em coro, cordas cheias | 5:25–6:20 |
| Coda | sino ao longe, o tema do violino, o mellotron sumindo | 6:20–7:10 |

Os cinco têm função: Helena conduz, Bento canta, Lia faz o fado e a estrela, Glória e Guilherme no coro, nylon da Glória nas estações.

## 2. Styles

```
Afro-Barroco brasileiro de sotaque nativo sobre base de MPB de câmara, violino chorado e cordas em primeiro plano, violão de nylon, cello, percussão de mão, gravação ritual acústica e próxima em wide stereo, suíte cinematográfica com longos interlúdios instrumentais
```

Fundação · variação da Helena (posição 2) · 3 instrumentos (+ violino da variação = 4) · produção · descritor livre.

## 3. Exclude styles

```
autotune, electronic drums, 808, distorted guitar, synth lead
```

## 4. Lyrics

```
[Intro - mellotron drone, solo violin]

[Instrumental - violin theme, slow]

[Verse - baritone, cello, nylon]
Primeira curva da serra
Primeira conta do terço
Lá embaixo, luzes no mar
Contas soltas sobre a água

[Interlude - distant procession drums]

[Interlude - wordless choir, far]

[Verse - baritone, low strings]
Na segunda, pesa a chave
Que não abriu casa alguma
Na terceira, a lua cresce
E o homem esquece o nome

[Instrumental - hand drums accelerating]

[Instrumental - cello ostinato, violin frenzy]

[Instrumental - distant low hum, flute wind]

[Instrumental - full crescendo]

[Break - silence]

[Interlude - solo flute, first light]

[Final Chorus - full choir, strings]
Clara estrela
Estrela linda
Última conta do terço
A manhã me devolveu
(Sozinho em procissão)
(Sozinho em procissão)
(Sozinho em procissão)

[Outro - distant church bell, violin theme]

[Outro - mellotron fading]

[End]
```

## 5. Controles

**Vocal Gender:** Male · **Weirdness:** 40 · **Style Influence:** 70

## Como gerar

Instrumental longo é o ponto fraco do Suno: numa geração única ele tende a encurtar os instrumentais, enfiar voz onde não tem letra ou terminar antes (**consenso**). Dois caminhos, nesta ordem:

**Caminho A: geração única.** Cole o pacote inteiro e gere 2 vezes. Se uma delas passar de ~6 min com o fado instrumental de verdade, é ela. Confira a duração máxima por geração na interface do Suno antes, porque ela muda com a versão.

**Caminho B: em três partes, com Extend** (o mais provável de funcionar):
1. **Parte 1:** gere só do `[Intro]` até o fim da Estação II, mais `[Instrumental - hand drums accelerating]`.
2. **Parte 2:** **Extend** a partir do fim da Estação II, com a caixa Lyrics contendo **só as tags** do fado (`[Instrumental - …]` × 4, `[Break - silence]`, `[Interlude - solo flute, first light]`). Sem nenhuma palavra cantada.
3. **Parte 3:** **Extend** a partir do fim da flauta, com a Estação final e a coda.

O Extend mantém tom, timbre e andamento da parte anterior. Gerar o fado como faixa instrumental separada daria tom e timbre diferentes; use isso só em último caso.

**No Audacity:** abra o silêncio de 2–3 s antes da flauta se o Suno não o deixar; corte qualquer voz que tenha entrado no fado; faça os fades da coda à mão. Registre cada emenda no bloco 3 do dossiê: esta é a faixa com mais montagem do EP.

## Notas para a geração

- **O murmúrio grave** no fado é o outro Loupi, o mesmo que Graça ouviu às três horas. Opcional e **anedótico**. Nunca uivo: se vier uivo, tire a tag e faça Replace Section.
- **`violin frenzy`** pode sair agressivo demais. O desatino é de corrida noturna, não de filme de terror: se passar do ponto, troque por `violin running`.
- **O coro final** canta *(Sozinho em procissão)* entre parênteses, como resposta. Se o Suno não cantar, tire os parênteses só dessas três linhas.
- **O sino da coda** é o sino das seis da faixa 4. Se sair sino de terror, tire a tag e deixe só o violino.
- **Duração.** Faixa de ~7 min no streaming: ótimo para o EP e para a escuta do disco inteiro, ruim como single. Ela não vai como single.
