---
name: bawm-artista
description: "Cria e mantém as personas artísticas do selo BAWM. Use para \"criar um artista\", \"a banda\", \"a persona\", \"quem canta isso\", \"bio do artista\", \"identidade visual\", \"a voz do Bento\", ou quando outra etapa precisa saber como um artista do elenco soa."
---

# Artistas e personas do BAWM

Uma persona do BAWM não é uma bio bonita: é um **conjunto de restrições que faz o arranjador e o produtor tomarem decisões diferentes**. Se a bíblia do artista não muda o prompt, ela não serve.

## Regra do elenco

Cada artista é **uma geografia sonora**, não um gênero. Antes de aprovar um artista novo, pergunte: *que região, diáspora ou cruzamento este artista traz que o elenco ainda não tem?* Máximo de 2 a 3 personas ativas — mais que isso vira fazenda de personas, o padrão que os filtros de spam procuram.

## Identidade visual — decisão estruturante

**Nenhuma persona do BAWM usa rosto humano fotorrealista gerado por IA** em foto de perfil, header ou capa.

Motivo operacional: desde ago/2026 o Spotify marca como *AI Persona* o artista cuja identidade pública é um humano fotorrealista gerado por IA, e **exclui esses artistas de playlists editoriais e de toda recomendação algorítmica**. Fazer a música com IA não aciona o selo. O rosto aciona. Personagem de ficção ilustrado não aciona.

Linguagens permitidas: ilustração, pintura, gravura, colagem, silhueta, máscara, grafismo, tipografia, textura, abstração, fotografia real de pessoas reais. Cada persona tem **uma** e a mantém.

Arte de release (regras da LANDR): quadrado 1:1, de 1500×1500 a 6000×6000 px, JPG ou PNG, sem perfil eSRGB, sem URL, sem @, sem logo de marca. **Arte duplicada entre releases é motivo de rejeição.**

Antes de fechar um nome, procure-o no Spotify, Apple Music e Deezer. Escolha um com **zero** correspondências e depois entregue sempre com o ID de artista explícito.

## Bíblia do Caô

**Caô — coletivo digital brasileiro.** Primeira persona-banda do selo.

**Geografia sonora:** a travessia entre Minas e o Rio, atravessada por barroco mineiro, herança africana e câmara europeia. Música de ritual e de rio. O Caô chama isso de **Afro-Barroco**.

| Integrante | Idade | Função | Instrumento / voz | No arranjo |
|---|---|---|---|---|
| **Bento** | 30 | O Alicerce | Voz **barítono** | Abre o portal. Peso de Minas e balanço do Rio. Voz principal, guardião do ritual. Quando ele entra, a faixa assenta |
| **Guilherme** | 28 | O Harmonizador | Voz e harmonia | Frescor e técnica. Segunda voz, contracanto, resolução harmônica |
| **Glória** | 25 | A Alma Bossa | Voz feminina, **violão de nylon** | Sofisticação e leveza à maneira de Nara Leão. Sopro, não peso |
| **Helena** | 22 | A Ancestralidade e a Corda | **Cello e violino** | O "choro" e a glória do Afro-Barroco. Coração resiliente do grupo |
| **Lia** | 24 | A Brisa Indie | **Flauta e percussão** | Ar, movimento, textura. É por onde entra o mundo contemporâneo |

**Regra de arranjo:** toda faixa do Caô se explica por quem está tocando. Se não há função clara para ao menos três dos cinco, ou é do artista errado, ou o arranjo não está pronto.

**Paleta.** Sempre: violão de nylon, cello ou violino, percussão de mão, voz barítono. Frequente: flauta, contrabaixo acústico, piano, coro do grupo, viola. Às vezes: órgão, metais discretos, cordas em naipe. **Nunca:** bateria eletrônica moderna, 808, autotune audível, guitarra distorcida, sintetizador em primeiro plano.

**Vocabulário próprio.** *Afro-Barroco* · *o ritual* · *o portal* · *o colar* e *as contas* (cada faixa é uma conta) · *travessia* · *rio* · *o outro lado*.

**Temas.** Pertencimento, travessia, ancestralidade, fé popular, figuras humanas nomeadas — o Caô canta **pessoas**, e o nome próprio no título é marca do projeto (Walter, Ana Flor, Quasimodo, Ìaro). Tabus: ironia fácil, gíria de internet, tema de consumo, qualquer coisa que soe a jingle.

**Catálogo.** Contas Para Um Colar — Primeiro Ato (EP, jan/2026) e Segundo Ato (EP, fev/2026); Efeito Borboleta (single, jun/2026); Meu Rio Corre a Ti (single, jun/2026). **Doze faixas — suficiente para treinar um Custom Model no Suno v5.5 (mínimo 6). É a maior alavanca técnica disponível para o artista hoje.**

**Linguagem visual.** Ilustrada/pictórica, decisão de set/2026 saindo dos retratos fotorrealistas. Direção coerente com o Afro-Barroco: talha e ex-voto mineiros, xilogravura, ouro sobre madeira escura, santos populares, água. Os cinco podem continuar existindo como figuras — **desenhadas**.

### Bloco Styles base do Caô

```
Afro-Barroco, MPB de câmara, violão de nylon, cello, violino,
percussão de mão, voz masculina barítono brasileira, sotaque nativo,
mid-tempo, gravação acústica próxima, wide stereo,
ritual, melancólico, reverente
```

**Exclude styles:** `autotune, electronic drums, 808, distorted guitar, synth lead`

**Sliders:** Weirdness 35 · Style Influence 75. Câmara mais nua: 30 / 80. Experimental: 55 / 60.

**Vocal Gender:** Male para Bento e Guilherme; Female para Glória. Use o botão, nunca tag.

**Variações por integrante**, acrescentadas ao bloco base:
- Bento: `deep baritone lead, low register, grave e assentado`
- Guilherme: `second voice, close harmony, contracanto, técnica limpa`
- Glória: `voz feminina suave, bossa, violão de nylon em primeiro plano, leveza`
- Helena: `solo cello, violino chorado, cordas em primeiro plano`
- Lia: `flauta, percussão de mão, textura arejada, indie folk global`

## Consistência de voz no Suno

Três caminhos, em ordem de robustez:

1. **Custom Model** (Pro/Premier, v5.5): mínimo 6 faixas, até 3 modelos, 100 créditos, pronto em 2–5 minutos, privado.
2. **Style Persona** salva de uma faixa boa, dentro do menu **Voice**. ⚠️ Selecionar a Persona **preenche automaticamente a caixa Styles** — não escreva estilo à mão por cima.
3. **Bloco Styles fixo** repetido. Menos estável, mas auditável.

**Voices** (a voz real do usuário) é outra coisa: exige v5.5, maioridade, 15 s a 4 min de áudio, verificação por leitura de frase e Audio Influence alto.

## Criar um artista novo

Conduza como briefing, não como formulário. Pergunte primeiro a **geografia sonora** e o **conflito interno**; o resto decorre. A bíblia precisa ter: nome e o que significa · geografia sonora · formação (cada integrante uma função de arranjo) · ficha de voz (tessitura, textura, sotaque, entrega, o que a voz nunca faz) · paleta instrumental (sempre / frequente / nunca) · vocabulário próprio · temas e tabus · linguagem visual · **bloco Styles base + Exclude** · sliders de partida · verificação de colisão de nome nas três lojas.

Os dois penúltimos itens são o que torna a bíblia útil. Sem eles é literatura.