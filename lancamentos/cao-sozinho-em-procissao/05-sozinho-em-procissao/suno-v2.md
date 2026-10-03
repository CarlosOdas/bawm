# Sozinho em Procissão — pacote Suno v2 (quatro partes, Extend)

> 02/10/2026 · substitui o v1. Pedido do Carlos: **no mínimo 9 minutos**, em **quatro partes** com Extend, a primeira só a introdução; **hipnótico e cheio, música que enche a nave de uma capela**, sem perder a estética do EP. Letra mantida (v1).
> ⚠️ Com Custom Model ou Style Persona do Caô, **não cole o Styles**.

## Plano

| Parte | Conteúdo | Duração-alvo | Acumulado |
|---|---|---|---|
| 1 | Introdução instrumental: a lua, o órgão, o tema do violino, o pulso | 2:30 | 2:30 |
| 2 | Estação I · interlúdio do mar · Estação II | 2:30 | 5:00 |
| 3 | O fado: longo instrumental, silêncio, a flauta da primeira luz | 2:30–3:00 | 7:30–8:00 |
| 4 | Estação final em coro, repetição hipnótica, coda longa | 2:00–2:30 | **9:30–10:30** |

**O que faz ser hipnótico:** um **ostinato** (cello e percussão de mão) que nasce na parte 1 e não para até o silêncio da parte 3; o **tema do violino** que volta em toda parte; e o *(Sozinho em procissão)* repetido no fim como ladainha.
**O que faz encher a nave:** **órgão** (já previsto na paleta do Caô como "às vezes") sustentando o chão, coro do grupo inteiro e o espaço de capela no descritor livre.
**O que mantém o EP:** os 6 descritores fixos do Caô em todas as partes, o mellotron como lua, o violino da Helena liderando, o Bento cantando, nada de bateria, nada de horror.

**Styles:** os seis primeiros descritores são iguais nas quatro partes; **só o sétimo muda**, porque é ele que diz ao Extend o que vem agora.
**Controles nas quatro partes:** Vocal Gender **Male** · Weirdness **40** · Style Influence **75**.

---

## Parte 1 — Introdução (geração nova)

**Styles**
```
Afro-Barroco brasileiro de sotaque nativo sobre base de MPB de câmara, violino chorado e cordas em primeiro plano, violão de nylon, cello, percussão de mão, gravação ritual acústica e próxima em wide stereo, abertura instrumental hipnótica sob a nave de uma capela
```

**Exclude styles**
```
vocals, autotune, electronic drums, 808, synth lead
```
*(Só nesta parte: `vocals` entra para garantir a introdução sem voz; `distorted guitar` sai para não passar de cinco itens. Volte ao Exclude padrão na parte 2.)*

**Lyrics**
```
[Intro - mellotron drone, organ pedal]

[Instrumental - solo violin theme]

[Instrumental - hand drums heartbeat]

[Instrumental - cello ostinato, hypnotic]

[Instrumental - violin theme, strings]
```

Sem `[End]`: a parte precisa terminar **aberta**, ainda soando, para o Extend continuar.

---

## Parte 2 — Primeiras estações (Extend da parte 1)

**Styles**
```
Afro-Barroco brasileiro de sotaque nativo sobre base de MPB de câmara, violino chorado e cordas em primeiro plano, violão de nylon, cello, percussão de mão, gravação ritual acústica e próxima em wide stereo, procissão hipnótica que enche a nave de uma capela
```

**Exclude styles**
```
autotune, electronic drums, 808, distorted guitar, synth lead
```

**Lyrics**
```
[Verse - baritone, cello, nylon]
Primeira curva da serra
Primeira conta do terço
Lá embaixo, luzes no mar
Contas soltas sobre a água

[Interlude - distant procession drums]

[Interlude - wordless choir, chapel]

[Verse - baritone, low strings]
Na segunda, pesa a chave
Que não abriu casa alguma
Na terceira, a lua cresce
E o homem esquece o nome

[Instrumental - hand drums accelerating]
```

---

## Parte 3 — O fado (Extend da parte 2)

**Styles**
```
Afro-Barroco brasileiro de sotaque nativo sobre base de MPB de câmara, violino chorado e cordas em primeiro plano, violão de nylon, cello, percussão de mão, gravação ritual acústica e próxima em wide stereo, longo instrumental hipnótico em crescendo de cortejo
```

**Exclude styles**
```
autotune, electronic drums, 808, distorted guitar, synth lead
```

**Lyrics**
```
[Instrumental - cello ostinato, violin running]

[Instrumental - distant low hum]

[Instrumental - organ, full crescendo]

[Instrumental - drums at peak]

[Break - silence]

[Interlude - solo flute, first light]
```

Nenhuma palavra na caixa: só tags. Não ponha `vocals` no Exclude aqui, ou o murmúrio grave some (ele é o "outro" Loupi; opcional).

---

## Parte 4 — Final em coro e coda (Extend da parte 3)

**Styles**
```
Afro-Barroco brasileiro de sotaque nativo sobre base de MPB de câmara, violino chorado e cordas em primeiro plano, violão de nylon, cello, percussão de mão, gravação ritual acústica e próxima em wide stereo, final coral hipnótico que enche a nave de uma capela barroca
```

**Exclude styles**
```
autotune, electronic drums, 808, distorted guitar, synth lead
```

**Lyrics**
```
[Final Chorus - full choir, organ]
Clara estrela
Estrela linda
Última conta do terço
A manhã me devolveu
(Sozinho em procissão)
(Sozinho em procissão)

[Chorus - choir, hypnotic repetition]
(Sozinho em procissão)
(Sozinho em procissão)
(Sozinho em procissão)
(Sozinho em procissão)

[Outro - distant church bell, violin theme]

[Outro - organ and mellotron fading]

[End]
```

A letra é a mesma da v1; só o *(Sozinho em procissão)* se repete mais, como ladainha.

---

## Como estender sem quebrar

- **Extend a partir de 2–3 s antes do fim** da parte anterior, não do último segundo. Se a parte terminar diminuindo, comece o Extend antes da queda, onde a música ainda está cheia; senão o Suno "entende" que é fim e recomeça do zero (**consenso**).
- **Gere 2 versões de cada parte** e escolha antes de estender a seguinte. Estender a versão errada contamina todas as partes depois dela.
- **Confira a duração de cada parte.** Se a parte 1 sair curta (menos de 2 min), estenda-a uma vez a mais só com `[Instrumental - violin theme, strings]` antes da parte 2. O mínimo de 9 min depende das partes 1 e 3.
- **Junte as partes** pela ferramenta de música inteira do Suno, se aparecer na sua interface, e baixe o WAV completo. Se as emendas soarem, monte no Audacity a partir das partes baixadas.
- **No Audacity:** abra os 2–3 s de silêncio antes da flauta se o Suno não deixar; corte voz que tenha entrado no fado; faça os fades da coda à mão. Registre cada emenda e o ID de cada parte no dossiê (blocos 2 e 3).

## Se der errado

| Sintoma | O que fazer |
|---|---|
| Órgão vira órgão de igreja pop, ou toma a faixa | Tire `organ` das tags da parte em que isso aconteceu; o chão fica com o mellotron e o cello |
| A parte 1 ganha voz mesmo com `vocals` no Exclude | Gere de novo; se insistir, corte a voz no Audacity |
| O ostinato some na parte 3 | Repita `cello ostinato` na primeira tag da parte 3, como já está, e estenda de um ponto onde ele ainda está tocando |
| Uivo no murmúrio grave | Replace Section no trecho, sem `distant low hum`. Nunca uivo |
| `violin running` agressivo demais | Troque por `violin theme, faster` |
| O coro final soa como hino genérico | Tire `organ` da parte 4 e deixe `full choir, strings` |
