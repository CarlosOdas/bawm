# Outras Vozes no Salão — pacote Suno v1

> 30/09/2026 · `bawm-arranjador` sobre a letra v2 ([`letra.md`](letra.md)). Vale se a v2 for aprovada.
> A letra não cita o nome de Loupi: sem troca fonética.
> ⚠️ Com Custom Model ou Style Persona do Caô, **não cole o Styles**.

## 1. Mapa da faixa

| Seção | Quem toca | O que muda | Duração aprox. |
|---|---|---|---|
| Intro | piano de armário desafinado, sozinho | a valsa da casa, meio torta | 8–10 s |
| Onze horas | **Glória**, voz muito próxima, quase sussurro; piano | o susto na fechadura | ~20 s |
| Meia-noite | + nylon | ela olha pela fresta | ~25 s |
| Uma hora | **mellotron** + harmônicos de cello (**Helena**) | a lua cheia; ele sobe | ~20 s |
| Pausa | silêncio | 1 a 2 s de nada | ~2 s |
| Três horas | quase nada: voz e um murmúrio grave e distante | a coisa que canta na serra | ~20 s |
| Seis horas | sino, a valsa inteira volta, flauta da **Lia** | o dia; o portão fechado; o reconhecimento | ~35 s |
| Fim | piano sozinho, corte seco | *Foi alguém.* | ~5 s |

As vozes da família, entre parênteses, vêm de longe, como de outro cômodo.

## 2. Styles

```
Afro-Barroco brasileiro de sotaque nativo sobre base de MPB de câmara, voz leve e sofisticada à maneira da bossa, nylon à frente, violão de nylon, cello, percussão de mão, gravação ritual acústica e próxima em wide stereo, valsa noturna com piano de armário desafinado
```

Fundação · variação da Glória (posição 2) · 3 instrumentos · produção · descritor livre (a valsa e o piano).

## 3. Exclude styles

```
autotune, electronic drums, 808, distorted guitar, synth lead
```

## 4. Lyrics

```
[Intro - detuned upright piano, waltz]

[Verse - whispered close vocal, piano]
Onze horas.
Alguém gira a fechadura
Da casa que é minha agora
Quem tem chave lá de fora?
(Graça, quem é?)
Foi só o portão.

[Verse - nylon joins, waltz]
Meia-noite.
Apago a luz do salão
Calo as vozes da família
Pela fresta da janela
Um velho, chapéu na mão
Olha a casa e não entra
(Graça, quem é?)
Foi só o vento.

[Verse - mellotron, cello harmonics]
Uma hora.
A lua está tão cheia
Que clareia a rua inteira
E o velho, de costas, sobe
Sozinho em procissão
(Graça, quem é?)
Foi só a lua.

[Break - silence]

[Verse - almost silent, distant low hum]
Três horas.
Os cães da rua se calam
Lá na serra, alguma coisa
Canta sem ter voz de gente
(Graça, quem é?)
Não é ninguém.

[Verse - church bell, full waltz, flute]
Seis horas.
Bate o sino da missão
De manhã, portão fechado
Quem fechou não disse adeus
No batente, um giz antigo
Mais velho que os dias meus
Minha casa tem um dono
Que eu nunca vou conhecer
(Graça, quem era?)
Foi alguém.

[Outro - piano alone, abrupt end]

[End]
```

## 5. Controles

**Vocal Gender:** Female · **Weirdness:** 45 · **Style Influence:** 70

## Notas para a geração

- **Valsa.** Compasso não se pede em tag (não funciona); `valsa` no Styles e `waltz` na intro é o que puxa o 3/4 (**consenso** para gênero, **anedótico** para garantir o compasso). Se sair em 4, gere de novo antes de mexer em mais nada.
- **O piano desafinado** é o tempero da estranheza (**anedótico**). Se vier desafinado demais, com cara de filme de terror, tire `detuned` da intro e deixe só `upright piano`. Nada de horror.
- **O silêncio** (`[Break - silence]`) tende a virar pausa curta ou a sumir. Se sumir, abra o buraco no Audacity: 1 a 2 s de nada antes de *Três horas*.
- **O murmúrio distante** às três horas é opcional e **anedótico**: o Suno pode ignorar ou cantar alto demais. Se entrar em primeiro plano, tire `distant low hum` e deixe a seção só com a voz dela. Nunca uivo.
- **Horas e respostas** são versos curtos e cantados, não falados. A voz falada grave continua reservada ao "outro" Loupi.
- **O fim seco.** Se a geração arrastar depois de *Foi alguém*, corte no Audacity logo depois da palavra, com o piano soando.
- **Weirdness 45** é o ponto de estranheza: se as duas primeiras gerações saírem convencionais demais, suba para 55 (uma variável por vez).
