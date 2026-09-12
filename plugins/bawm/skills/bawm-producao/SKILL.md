---
name: bawm-producao
description: "Produção de faixa do selo BAWM na cadeia Suno → Audacity → LANDR. Use para \"gerar a música\", \"produzir a faixa\", \"montar no Audacity\", \"masterizar\", \"que Style uso\", \"ficou baixo demais\", \"o master ficou estranho\", \"extrair stems\"."
---

# Produção do BAWM

Três ferramentas, uma cadeia: **Suno gera → Audacity monta e repara → LANDR masteriza**. Para a mecânica de prompt do Suno, use a skill `suno-pro`.

## Etapa 1 — Geração

Cole os blocos do pacote de arranjo. **Gere duas vezes** — nunca aceite a primeira coisa. Ouça os mesmos 15 a 30 segundos das quatro faixas resultantes e escolha comparando o mesmo trecho. Se sair errado, diagnostique antes de acrescentar tag: sinais em excesso? Styles e letra pedindo coisas diferentes? Seção fraca na escrita? Cue local perdido num prompt inchado?

**Nunca regenere a faixa inteira por causa de um trecho.** Use Replace Section, Crop, Extend ou Remaster — mais rápido, gasta menos crédito e é intervenção humana documentável.

| Ferramenta | Para quê |
|---|---|
| Replace Section | Trocar trecho no meio, inclusive a letra |
| Crop | Cortar excesso no começo ou no fim |
| Extend | Continuar de um ponto; depois `Get Whole Song` |
| Remaster | Variação sutil; no v5+ escolha Variation Strength Subtle/Normal/High |
| Song Editor | Mover seções, fades, Quick Replace, inserir seção |
| Sounds | Efeito ou sample isolado |

**Saída:** baixe **WAV**, melhor qualidade do plano, **sem nenhum processamento**.

**Stems são do Suno**, não da LANDR: Auto Split (até 12 stems, 50 créditos), Split from Mix (10 por extração) e Advanced Split (~100 instrumentos, só Premier). ⚠️ Pedir instrumento que não está na faixa consome crédito e devolve lixo.

## Etapa 2 — Audacity

**A regra: aqui é reparo e montagem, não volume.** Cada dB de compressão, limitação ou normalização de loudness aplicado aqui corrompe a análise que a LANDR faz depois. Uma faixa já limitada chega como "isto já está masterizado" — e o motor ou não faz nada de útil, ou processa por cima: bombeamento e transiente achatado.

**Nunca antes da LANDR: Compressor · Limiter · Loudness Normalization · Dither.**

⚠️ **Versão:** o Audacity 4.0 saiu em 03/09/2026 sem o Macro Manager e com o manual oficial desatualizado; a conversão `.aup3` → `.aup4` é de mão única. **Trabalhe no 3.7.9.**

⚠️ **O Audacity não mede true peak** — só pico de amostra. Um arquivo que marca 0,0 dBFS lá pode reconstruir acima disso na conversão. Daí a margem de −6 dBFS.

⚠️ **A exportação usa a taxa do PROJETO, não a do arquivo.** Ajustar a Project Rate é o passo 1, ou você reamostra o master em silêncio.

```
 1. Project Rate = taxa do arquivo do Suno
 2. Importar; conferir faixa em 32-bit float
 3. Analyze > Find Clipping
 4. Montagem: Z antes de cada corte (zero crossings);
    Crossfade Constant Power 1 nas emendas; renomear clipes por geração
 5. Corte de início e fim; Studio Fade Out no final
 6. Reparo pontual: Repair (máx. 128 amostras), Notch, high-pass 25–30 Hz
    — Mix and Render ANTES de qualquer filtro: EQ apaga envelope
 7. EQ só corretivo, cortes suaves
 8. Normalize → pico -6,0 dB
    Remove DC offset LIGADO · canais independentes DESLIGADO
 9. Conferir o pico pelo truque do Amplify (o valor pré-preenchido é o
    negativo do pico atual) e CANCELAR
10. Export > WAV, Signed 24-bit PCM, taxa original
```

**Normalize ≠ Loudness Normalization.** O primeiro mede pico, protege o teto, vem em −1 dB. O segundo mede LUFS, **não protege pico nenhum** e vem em −23 LUFS (norma de broadcast, ~25% da escala). Não use o segundo.

**Noise Reduction** é o efeito mais destrutivo do conjunto e material do Suno raramente é ruidoso — normalmente pule. Se usar, confira sempre no modo **Residue** antes de aplicar.

Registre no dossiê: quantas gerações entraram, de onde veio cada trecho, onde foram os cortes e por quê. Guarde o projeto do Audacity e uma exportação sem processamento de cada geração usada.

## Etapa 3 — LANDR

Padrão histórico do selo: **Warm / Medium**. Bom para o Afro-Barroco; não é padrão para tudo.

| Style | O que faz | Quando |
|---|---|---|
| **Warm** | Calor vintage, compressão mais macia. Agudo íntimo, grave e médio-grave cheios | Caô, MPB de câmara, bossa, seresta — acústico e próximo |
| **Balanced** | Controlado, foco em equilíbrio, clareza e profundidade | Faixa com muitos elementos; quando não souber |
| **Open** | Moderno e aberto, punch e presença, escavada no médio | Samba, axé, funk, piseiro, eletrônico — andamento rápido |

| Loudness | Uso |
|---|---|
| **Low** | A própria LANDR recomenda **para streaming**, e para acústico e orquestral |
| **Medium** | Padrão do selo; serve à maioria |
| **High** | Só faixa de pista |

⚠️ **A LANDR não publica valor de LUFS para Low/Medium/High.** Qualquer número que circule por aí é chute. **Meça o master devolvido.**

**Formato de entrega:** WAV 44,1 kHz / 16 bits é o padrão da indústria e o que a LANDR indica. HD WAV (24 bits) só para sync e arquivo, e exige fonte 24 bits.

**Revisions** — cinco controles (Loudness, EQ Intensity, ajuste de EQ incluindo a faixa do vocal, Sibilance Protection, Stereo Width), **ilimitados e sem custo de crédito**. ⚠️ **Album Master e Reference Master não podem ser revisados** — escolha o modo antes.

**Reference Mastering:** escolha a referência por equilíbrio de frequência, imagem estéreo e nível de dinâmica — nunca porque gosta da música. Uso natural: coerência dentro de um EP.

### Verificação obrigatória

1. **Volume Match ligado** para comparar original e master no mesmo volume.
2. Medir **LUFS integrado** e **true peak**.
3. ⚠️ O master da LANDR costuma sair com **true peak perto de −0,2 dBFS**, acima da margem de −1 dBFS — risco de clipping intersample após conversão para AAC. Se passar de −1 e a faixa tiver muito agudo, **baixe o Loudness em Revisions** e meça de novo.
4. Ouvir em fone, celular e caixa.
5. Registrar Style, Loudness, formato, revisões, LUFS e true peak no dossiê.

Alvos das plataformas, para calibrar: Spotify −14 LUFS (−11 no mobile), Apple −16, YouTube/Amazon/TIDAL/Deezer −14. Não persiga o número — persiga um master equilibrado e meça o que saiu.

**Teste de Style, uma vez por artista:** masterize uma faixa representativa nos três Styles com a mesma Loudness e compare os mesmos 20 segundos com Volume Match ligado. O resultado vira o padrão daquele artista.

## Nota sobre planos

O Suno Studio e as ferramentas mais profundas da LANDR ficam em planos superiores. No Pro, o caminho até um DAW é: **stems no Suno → download → montagem fora**. Diga isso quando o usuário pedir controle que o plano não dá, em vez de improvisar.