# Tanta Manhã — pacote Suno v1

> 05/11/2026 · `bawm-arranjador` sobre a letra v1 ([`letra.md`](letra.md)). **Só vale se a v1 for aprovada**; se o Carlos mexer na letra, o pacote é refeito.
> Troca fonética na caixa Lyrics: *estrela-d'alva* vira *estrela dalva* (o apóstrofo e o hífen confundem a leitura).
> ⚠️ Com Custom Model ou Style Persona do Caô, **não cole o Styles**: a Persona preenche a caixa sozinha.
> ⚠️ **Nada de *Sapato Velho* entra no Suno**: nem áudio, nem nome, nem trecho de letra. Ver o briefing, seção 7.

## 1. Mapa da faixa

| Seção | Quem toca | O que muda | Duração aprox. |
|---|---|---|---|
| Intro | **Glória**, nylon sozinho, arpejo | a cozinha no escuro | 8–12 s |
| Verso 1 | **Bento**, voz próxima, quase confidência · nylon | o rito: água no fogo, a espera | ~25 s |
| Verso 2 | + **Helena**, cello em notas longas | a memória: o morro, o poço | ~25 s |
| Mas (1) | o cello desce | o mundo cresceu | ~12 s |
| Refrão 1 | Bento + **Guilherme** em duas vozes · percussão de mão entra | o coador | ~25 s |
| Verso 3 | Bento · + **Lia**, chocalho leve | a xícara acorda a casa | ~25 s |
| Mas (2) | só nylon e voz | o que ainda sabe | ~12 s |
| Ponte | **Glória**, sozinha · nylon · cello em nota presa | Dalva responde | ~25 s |
| Último refrão | **o grupo inteiro** em harmonia fechada · cello · flauta da Lia | quem canta agora são todos | ~30 s |
| Coda | Bento sozinho, nylon | *Toma, enquanto tá quente*. Fim seco, a corda soando | ~10 s |

A faixa cresce pelo **número de vozes**, não pelo volume: uma, duas, a dela sozinha, o grupo inteiro. Os cinco têm função, e nenhuma seção tem mais de três tocando, fora o último refrão.

## 2. Styles

```
Afro-Barroco brasileiro de sotaque nativo sobre base de MPB de câmara, barítono grave e assentado, violão de nylon, cello, percussão de mão, gravação ritual acústica e próxima em wide stereo, balada lenta e terna com coro em harmonia fechada
```

Fundação · variação do Bento (posição 2) · 3 instrumentos · produção · descritor livre (a balada e a harmonia vocal). **7 descritores.**

## 3. Exclude styles

```
autotune, electronic drums, 808, distorted guitar, synth lead
```

O do Caô, sem mudança. Ele já barra o timbre que deixaria a faixa com cara de época (`synth lead`).

## 4. Lyrics

```
[Intro - solo nylon, sparse]

[Verse 1 - close baritone, nylon]
Me levanto antes do galo
Sem fazer barulho, Dalva
Ponho a chaleira no fogo
E espero a estrela dalva

[Verse 2 - cello enters]
Aos vinte, eu descia o morro
Saco de café nas costas
Pescava no balde do poço
A estrela que você gosta

[Pre-Chorus - cello descends]
Mas o morro ficou mais alto
E o poço ficou mais fundo

[Chorus - two-voice harmony, hand percussion]
Fiquei que nem coador
Encardido de tanta manhã
Café bom passa devagar
E passa de novo amanhã

[Verse 3 - soft shaker]
A xícara canta no pires
Da minha mão que treme tanto
E você ri, ainda deitada,
Feito quem tem vinte anos

[Pre-Chorus - nylon only]
Mas inda sei o ponto da água
Um tiquinho antes de ferver

[Bridge - female vocal, nylon only]
Nunca quis estrela, meu velho
Eu queria era esse cheiro
Que vem da cozinha no escuro
E me diz que você tá lá

[Final Chorus - full group harmony, flute]
Fiquei que nem coador
Encardido de tanta manhã
Café bom passa devagar
E passa de novo amanhã
(Se Deus quiser, amanhã)

[Outro - baritone alone, nylon]
Deixa a estrela lá no céu
Toma, enquanto tá quente

[End]
```

## 5. Controles

**Vocal Gender:** Male · **Weirdness:** 30 · **Style Influence:** 80 (câmara mais nua)

## Notas para a geração

- **A ponte na voz dela é o ponto frágil.** Com Vocal Gender em Male, só a tag `female vocal` pede a voz da Glória na ponte. Às vezes funciona, às vezes não (**anedótico**). Se a ponte sair na voz do Bento: **Replace Section só na ponte**, mantendo a tag, com duas tentativas. Se ainda falhar, gere uma tomada à parte com Vocal Gender **Female** e a variação da Glória na posição 2 do Styles, e emende a ponte no Audacity, desde que tom e andamento batam. **A ponte não pode ficar na voz dele.** É ela respondendo, e sem isso a faixa perde a razão de existir.
- **Harmonia que cresce.** `two-voice harmony` no primeiro refrão e `full group harmony` no último. Se o primeiro já vier com coro cheio, o último perde o efeito. Nesse caso, Replace Section no refrão 1 com `[Chorus - two voices only]`.
- **Sem bateria.** O Exclude barra bateria eletrônica, mas não a acústica. Se uma bateria de balada aparecer no último refrão, a faixa vira a década errada: Replace Section com `[Final Chorus - group harmony, no drums]`.
- **O eco** *(Se Deus quiser, amanhã)* deve vir do coro, mais baixo que a voz principal. Se o Bento cantar sozinho, serve; se sumir, não serve, porque é o eco mais importante da homenagem.
- **Andamento.** Se a geração passar de ~90 BPM, a balada vira canção de rádio apressada. Gere de novo antes de mexer em qualquer outra coisa.
- **O fim seco.** Se a geração arrastar depois de *quente*, corte no Audacity logo depois da palavra, deixando a corda do nylon soar.
- **Teste controlado** (`suno-pro`): duas gerações de baseline, mude uma variável, mais duas, e compare os mesmos 15–30 s. O trecho de comparação recomendado é **ponte + último refrão**: é onde a faixa ganha ou perde.
