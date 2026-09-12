---
name: suno-pro
description: "Operar o Suno Pro (v5.5): escrever prompts de Styles, tags estruturais e de performance na letra, ajustar sliders e Exclude, e diagnosticar geração ruim. Use sempre que a conversa envolver criar, corrigir ou revisar música no Suno."
---

# Operação do Suno Pro (v5.5)

Escreva sempre em português. Tags estruturais e descritores de estilo ficam **em inglês** (é o vocabulário treinado); nomes de instrumentos e gêneros brasileiros ficam **em português**.

## Princípio central

A Suno **não publica lista oficial de tags**. Quase todo "meta tag" é folclore de comunidade. Ao afirmar que algo funciona, sinalize o nível: **oficial** (documentado ou visível na interface), **consenso** (reprodutível, 4+ fontes) ou **anedótico** (fonte única / provável placebo). Nunca apresente folclore como especificação.

## Divisão de trabalho entre os campos

- **Styles** = identidade global: gênero, groove, caráter vocal, produção, mood. Nunca colchetes aqui. Nunca negativas aqui.
- **Lyrics** = palavras cantadas + rótulos de seção + cues locais curtos.
- **Exclude styles** = todo prompt negativo.
- **Botões/sliders** = gênero vocal, duração, weirdness, style influence, audio influence.

## Regras que mais evitam retrabalho

1. **4 a 7 descritores** no Styles, no máximo 2 gêneros e 2–4 instrumentos. O limite de 1.000 caracteres não é meta.
2. **Posição é o único peso.** Coloque o inegociável nas primeiras 20–30 palavras. Não existe `(termo:1.3)` nem `((ênfase))`.
3. **Uma fundação de gênero + temperos**: `bossa nova foundation with trip-hop drums` supera `bossa nova, trip-hop`.
4. **Colchete não é cantado; parêntese é cantado.** `(with heavy reverb)` vira letra. Ad-lib e backing vocal usam parênteses; direção usa colchetes.
5. **Tag parametrizada rende mais que tag nua**, com no máximo 3 palavras: `[Bridge - drums fall away, close vocal]`.
6. **Negativa vai no Exclude**, 1–3 itens específicos, nomeando a coisa no positivo (`autotune, trap hi-hats`), e diga no Styles quem ocupa o lugar do que foi removido.
7. **Gênero vocal é botão** (Vocal Gender: Male/Female), não tag. Reserve o Styles para timbre e sotaque.
8. **Não regenere a música inteira** por causa de um trecho — use Replace Section, Crop, Extend ou Remaster.
9. **Instrumental = três controles juntos**: Lyrics vazio + `instrumental` no Styles + `vocals` no Exclude.
10. **Se o vocal sai apressado**, o problema é densidade silábica da letra, não BPM. Em português, mire redondilha (7) ou decassílabo (10), não a métrica traduzida do inglês.

## Sliders (0–100, padrão 50)

| Objetivo | Weirdness | Style Influence |
|---|---|---|
| Limpo e previsível | 25–40 | 60–75 |
| Adesão forte ao gênero | 25–40 | 75–90 |
| Ponte aventureira | 55–70 | 50–65 |

**Audio Influence** só aparece com áudio anexado; para Voices, mantenha alto.

## Não funciona (diga isso quando pedirem)

- Qualquer parâmetro numérico de mixagem em colchete: `[Reverb: 30%]`, `[EQ: +3dB]`.
- `(x2)`, `[Chorus x2]`, `(repeat)` — escreva a linha duas vezes.
- Progressões, modos, escalas e fórmula de compasso em colchete.
- Jargão de engenharia (`sidechain compression`) — descreva o resultado audível.
- BPM exato — é orientação probabilística.
- Nome de artista vivo — não funciona e é filtro de moderação; descreva as características sônicas.

## Diagnóstico quando a geração sai errada

Pergunte, nesta ordem: (1) há sinais em excesso ou contraditórios? (2) o Styles e a letra estão pedindo coisas diferentes? (3) a seção está fraca na escrita, e a tag está sendo chamada para salvá-la? (4) o cue local se perdeu num prompt inchado? Só depois sugira acrescentar tag.

## Teste controlado

A Suno é não-determinística — uma geração não prova nada. Protocolo: 2 gerações de baseline → mude **uma** variável → 2 gerações → compare os mesmos 15–30 s nas quatro. Desligue a varinha do My Taste durante o teste e fixe o modelo.

## Ao entregar um prompt

Entregue sempre em três blocos separados e copiáveis: **Styles**, **Exclude styles** e **Lyrics** (com as tags já no lugar), mais uma linha com a sugestão de sliders. Não misture tudo num parágrafo.