---
name: bawm-arranjador
description: "Transforma a letra pronta de uma faixa BAWM no pacote de arranjo: mapa da faixa, tags estruturais, bloco Styles, Exclude e sliders. Use para \"montar o arranjo\", \"onde entra o cello\", \"quem toca nessa parte\", \"as tags da letra\", \"o bloco de Styles\", \"a ponte não funciona\", ou quando a letra fecha e a faixa precisa ir para o Suno."
---

# Arranjo do BAWM

Etapa 3 da cadeia. Consome a **letra limpa** de `bawm-letrista` e entrega o **pacote de arranjo** que `bawm-producao` cola no Suno. Para a mecânica de prompt — o que é tag, o que não funciona, como diagnosticar geração ruim — use `suno-pro`. Esta skill decide **o que a faixa é**, não como o Suno se escreve.

## A pergunta que abre o arranjo

**Quem está tocando, e por quê?**

Regra do Caô: toda faixa se explica por quem toca. Se não há função clara para **ao menos três dos cinco**, ou é do artista errado, ou o arranjo não está pronto. Não conserte isso empilhando instrumento no Styles — volte à letra.

| Integrante | O que traz | Entra quando |
|---|---|---|
| **Bento** — barítono | Peso de Minas, balanço do Rio. Guardião do ritual | Abre o portal. Quando ele entra, a faixa assenta |
| **Guilherme** — 2ª voz | Contracanto, resolução harmônica, técnica limpa | Refrão, e onde a harmonia precisa fechar |
| **Glória** — voz e nylon | Leveza à maneira de Nara Leão. Sopro, não peso | Estrofe que precisa respirar; ponte de contraste |
| **Helena** — cello e violino | O choro e a glória do Afro-Barroco | Introdução, ponte, luto, virada emocional |
| **Lia** — flauta e percussão | Ar, movimento, textura contemporânea | Sustenta groove; abre e areja seção fechada |

## Mapa da faixa

Escreva o mapa **antes** de tocar nas tags. Uma linha por seção: quem toca, o que muda, quanto dura.

Arco padrão do Afro-Barroco — ponto de partida, não fôrma:

```
INTRO      Helena sozinha ou nylon da Glória. Estabelece o rito. 8-15 s
VERSO 1    Bento entra. Percussão de mão baixa. A faixa assenta
VERSO 2    Lia acrescenta ar. Sobe densidade, não volume
REFRÃO     Coro do grupo. Guilherme fecha a harmonia. Cordas em naipe
PONTE      A travessia. Tira o chão: cordas nuas, ou só voz e nylon
REFRÃO     Volta cheio. É aqui que o colar fecha
CODA       Desce ao que abriu. Fade curto ou fim seco
```

**Dinâmica é subir densidade, não volume.** Volume é assunto da LANDR, e compressão feita cedo estraga a masterização — ver `bawm-producao`.

**Duração:** nunca deixe a faixa cair entre 30 e 60 segundos (veto da direção). Alvo usual de single do selo: 2:30 a 3:40.

## Tags na letra

Regras que valem sempre (detalhe em `suno-pro`):

- **Colchete não é cantado; parêntese é cantado.** `(with heavy reverb)` vira letra na boca do Bento.
- **Tag parametrizada rende mais que tag nua**, no máximo 3 palavras: `[Bridge - strings only, no drums]` supera `[Bridge]`.
- **Cue local perto do que ele afeta.** Cue no topo de um prompt inchado se perde.
- **Ad-lib e backing vocal em parêntese**, na linha em que devem soar.
- `(x2)`, `[Chorus x2]` e `(repeat)` não funcionam — a letra volta escrita por extenso.

Tags que servem bem ao arco acima:

```
[Intro - solo cello, sparse]
[Verse - baritone lead, hand percussion]
[Chorus - group choir, close harmony, strings]
[Bridge - drums fall away, nylon and voice]
[Outro - cello returns, slow fade]
```

⚠️ **Gênero vocal é botão, não tag.** Vocal Gender: Male para Bento e Guilherme, Female para Glória. Escrever `male vocals` no Styles gasta descritor à toa.

## Bloco Styles

O Styles é **montado em cinco posições**, não colado inteiro. Teto de **sete descritores** — regra 1 da `suno-pro`, sem exceção para o Caô. O bloco base fixo tem cinco, a variação de quem lidera ocupa uma, e sobra **uma** para o que esta faixa pedir.

```
Afro-Barroco brasileiro de sotaque nativo sobre base de MPB de câmara,   ← fixo  (1)
<variação de quem lidera>,                                              ← muda    (2)
violão de nylon, cello, percussão de mão,                               ← fixo  (3-5)
gravação ritual acústica e próxima em wide stereo,                      ← fixo    (6)
<um descritor livre da faixa>                                           ← opcional(7)
```

⚠️ **A variação entra na posição 2.** Colada no fim, ela cai fora das primeiras 20–30 palavras — o dado mais específico da faixa na posição mais fraca do prompt. Posição é o único peso que existe.

| Lidera | Variação (posição 2) | Vocal Gender |
|---|---|---|
| Bento | `barítono grave e assentado` | Male |
| Guilherme | `segunda voz em harmonia próxima e contracanto limpo` | Male |
| Glória | `voz leve e sofisticada à maneira da bossa, nylon à frente` | Female |
| Helena | `violino chorado e cordas em primeiro plano` | — |
| Lia | `flauta e textura arejada de indie folk global` | — |

**Uma variação só.** Duas estouram o teto e diluem quem lidera.

⚠️ **Nenhuma delas nomeia gênero vocal** — `voz masculina`, `male vocals` e afins são botão, não Styles. Barítono é tessitura; o Styles guarda **timbre e sotaque**.

**Exclude styles:** `autotune, electronic drums, 808, distorted guitar, synth lead`

**Sliders:** Weirdness 35 · Style Influence 75. Câmara mais nua: 30 / 80. Experimental: 55 / 60.

⚠️ Se a faixa for gerada por **Style Persona**, selecionar a Persona **preenche a caixa Styles sozinha** — não escreva estilo à mão por cima. Nesse caso o pacote entrega só Lyrics, Exclude e sliders.

## Erros de arranjo, não de prompt

Antes de mexer em tag, cheque se o problema está aqui:

| Sintoma | Causa provável no arranjo |
|---|---|
| Faixa não decola | Bento entra tarde demais, ou nunca há mudança de densidade |
| Refrão não fecha | Refrão longo demais, ou Guilherme sem função harmônica |
| Ponte soa igual à estrofe | A ponte não tirou nada. Ponte é subtração |
| Tudo soa cheio o tempo todo | Cinco integrantes tocando em toda seção. Escolha três |
| Vocal apressado | Densidade silábica da letra — volte a `bawm-letrista`, não acrescente tag |

## Pacote de arranjo — o artefato desta etapa

Entregue sempre em **blocos separados e copiáveis**, nunca num parágrafo:

1. **Mapa da faixa** (a tabela de seções)
2. **Styles**
3. **Exclude styles**
4. **Lyrics** com as tags já no lugar
5. **Uma linha de sliders** + Vocal Gender

Registre no **bloco 2 do dossiê** (`modelos/dossie-de-faixa.md`): o mapa, o Styles e o Exclude **exatos**, e os sliders. `bawm-producao` vai registrar o que aconteceu com eles.

## Antes de passar à produção

- [ ] Ao menos três dos cinco integrantes com função clara
- [ ] Mapa escrito, com uma mudança de densidade audível por seção
- [ ] Ponte subtrai alguma coisa
- [ ] Nenhuma tag com mais de 3 palavras; nenhum parêntese que não deva ser cantado
- [ ] Styles com **6 ou 7 descritores**: os 5 fixos + a variação de quem lidera + no máximo 1 livre
- [ ] A variação está na **posição 2**, dentro das primeiras 20-30 palavras
- [ ] Nenhum termo de gênero vocal no Styles — está no botão
- [ ] Duração projetada fora da faixa morta de 30 a 60 s
- [ ] Os cinco blocos copiáveis, prontos para colar
