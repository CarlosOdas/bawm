# Caô — *Sozinho em Procissão* · plano de lançamento do EP

> 04/10/2026 · decisão do Carlos: **sem singles**, o EP sai inteiro. As cinco faixas finais foram entregues hoje (MP3 analisado aqui; WAV com o Carlos).
> Substitui o plano em cascata do README (seção 5).

## Tracklist

| # | Faixa | Suno ID | Duração | Download Suno (medido) | Tom |
|---|---|---|---|---|---|
| 1 | Loupi Menino | `f1e01e54…f9ea` | 4:50 | −15,9 LUFS · −2,3 dBTP | Mi maior |
| 2 | O Outro Lado da Serra | `d14b2001…9a5d` | 3:34 | −15,6 LUFS · −2,2 dBTP | Mi maior |
| 3 | Passado Não Tem Endereço | `cdbe6033…b72b` | 4:59 | −15,0 LUFS · −2,1 dBTP | Mi menor |
| 4 | Outras Vozes no Salão | `0f349829…9daf` | 3:39 | −16,1 LUFS · −2,9 dBTP | Mi menor |
| 5 | Sozinho em Procissão | `bf344892…183bab` | 6:58 | −15,1 LUFS · −3,1 dBTP | Mi menor → maior |
| | **Total** | | **24:00** | | |

**É EP nas lojas:** 5 faixas, 24 min (regra comum das lojas: até 6 faixas e menos de 30 min).
**O disco inteiro gira em Mi.** O plano previa tons diferentes; o Suno levou todas para Mi maior/menor. Não é defeito: o EP soa como uma peça só, e a passagem de Mi menor (faixas 3–4) para o Mi maior do fim de *Sozinho em Procissão* continua sendo o arco. Loudness parecido nas cinco (−15 a −16 LUFS): bom ponto de partida para um master coeso.

## O que precisa de atenção antes do master

| Faixa | Ponto | O que fazer |
|---|---|---|
| **3. Passado Não Tem Endereço** | **Título no Suno: "(Remastered)".** É o nome da ferramenta do Suno, não um remaster de algo lançado | Nas lojas, só **Passado Não Tem Endereço**. "Remastered" num título inédito engana o ouvinte |
| **3. Passado Não Tem Endereço** | A letra desta geração ainda abre com **"Loupi Garoupi desce a serra"**, com a grafia que o Suno lê *lôu-pi* | **Ouça a primeira frase.** Se sair *lôu-pi*, Replace Section só nesse trecho com *"Lupi Garupi desce a serra"*. Eu não consigo julgar pronúncia pelo arquivo |
| **5. Sozinho em Procissão** | **Buraco digital de ~1 s em 6:47** (silêncio absoluto, −92 dB) no meio do aplauso final: é a emenda de um Extend | No Audacity, feche o buraco com um crossfade curto entre os dois lados do aplauso |
| **5. Sozinho em Procissão** | A versão do EP é a **com plateia** (murmúrio, aplausos, público cantando), com 6:58 | Escolha artística sua; vale. Duas consequências abaixo, em *Metadados* |
| **5. Sozinho em Procissão** | O coro *"Caô, Caô"* e o *"Obrigado!"* do Bento **não estão na letra desta geração** (a caixa terminou em `[crowd shoting - no choir…]`) | Se quiser o fim com o coro e a fala, é um Extend a partir do aplauso; senão, fica como está |
| **1. Loupi Menino** | Queda de volume em 3:56 (~1 s) | Provavelmente uma pausa do arranjo. Ouça; se for corte, crossfade |
| **4. Outras Vozes no Salão** | Silêncios em 2:31, 2:38 e ~3:18 | São as pausas pedidas (o silêncio antes das *Três horas*). Ouça e confirme |

## Cadeia de produção, faixa a faixa

Do `bawm-producao`. Vale para as cinco:

1. **Audacity 3.7.9**, a partir do **WAV** (nunca do MP3). Project Rate na taxa do arquivo antes de tudo.
2. Só reparo: cortes, crossfades, silêncios, high-pass se precisar. **Nada de compressor, limiter, loudness normalization ou dither** antes da LANDR.
3. Normalize o pico em **−6 dB**. Exporte **WAV 24-bit**, taxa original.
4. **LANDR, as cinco na mesma sessão, com o mesmo Style e Loudness** (padrão do selo: **Warm / Medium**). Para soar como disco, use o modo **Album Master** se a sua interface oferecer, sabendo que ele **não aceita revisão**: só depois de as cinco estarem prontas no Audacity.
5. **Meça cada master devolvido** (LUFS integrado e true peak) e registre no bloco 4 do dossiê. True peak acima de −1 dBTP: baixe o Loudness e meça de novo.
6. **Ordem e intervalos:** confira na LANDR o silêncio entre faixas. A 3 termina em *"E sobe de volta a serra"* e a 4 começa às onze da noite, do lado de dentro do portão: um respiro de 2 s funciona.

## Metadados

| Campo | Valor |
|---|---|
| Release | **Sozinho em Procissão** · tipo **EP** |
| Artist | **Caô**, com o **Artist ID** de *Contas Para Um Colar* (sem ID, a loja cria outro perfil) |
| Label | `BAWM - Brazilian Artificial World Music` |
| Gênero | MPB (primário) · World (secundário), conforme a lista da LANDR |
| Idioma | Português |
| Explicit | Não, nas cinco |
| Letra (lyricist) | **Carlos Alberto Odas**. Faixas em coautoria assistida por IA: ver dossiês (bloco 1) |
| Capa | [`arte/capa-ep.jpg`](arte/capa-ep.jpg) (sem texto) ou [`arte/capa-ep-titulo.jpg`](arte/capa-ep-titulo.jpg). 3000 × 3000, JPG, sRGB, sem rosto |
| ISRC | 5 novos, gerados pela LANDR |
| Declaração de IA | **Sim**, nas cinco. Consequência: sai de YouTube Content ID, Meta, TikTok, Deezer, Lissen, Pandora e Tencent; fica em Spotify, Apple Music e Amazon |
| AI Credits (Spotify) | Declarar |

**Títulos exatos:** Loupi Menino · O Outro Lado da Serra · Passado Não Tem Endereço · Outras Vozes no Salão · Sozinho em Procissão.

**Sobre a plateia em *Sozinho em Procissão*.** O título fica sem "Ao Vivo", e nenhum texto do lançamento (descrição, pitch, post) pode dizer que a faixa foi gravada num show ou numa capela. A plateia é parte da cena, como o sino e o mar. Se alguém perguntar, a resposta é essa.

## Calendário

Regra do selo: master, dossiê e arte prontos **antes** de marcar a data; envio à LANDR em **D−28**; lançamento numa sexta.

| Marco | Data | |
|---|---|---|
| Audacity das cinco + correções acima | até **11/10** (dom) | |
| Masters LANDR medidos, dossiês fechados | até **15/10** (qui) | |
| **Envio à LANDR** com data marcada | **16/10** (sex) | D−28 |
| EP aparece no Spotify for Artists | ~30/10 a 03/11 | D−14 a D−10 |
| **Pitch editorial** (escolher a faixa foco: *Sozinho em Procissão* ou *Passado Não Tem Endereço*) | até **03/11** | D−10 |
| Canvas, cortes e calendário (`bawm-marketing`) | até **06/11** | D−7 |
| **Lançamento** | **sexta, 13/11/2026** | D |

Por que 13/11: é a primeira sexta possível respeitando D−28 com duas semanas de produção na frente; o Caô está sem lançar desde 27/06 e o selo desde 21/08 (*Stranger Samba*). Se a produção atrasar, a data anda junto: **nunca envie com menos de 28 dias**.

## Pendências que travam o envio

- [ ] **Dossiês, bloco 1 (autoria):** *Passado Não Tem Endereço* ainda sem autor/data/rascunhos da letra registrados.
- [ ] **Dossiês, bloco 2 (IA):** **Styles e Exclude exatos** e **data da assinatura ativa** de cada geração final. Copie da página de cada música no Suno. Os IDs e as datas de geração já estão anotados.
- [ ] **Blocos 3 e 4:** montagem no Audacity e masters medidos, à medida que acontecem.
- [ ] **Bloco 5 (direitos):** ISRC, declaração de IA, posicionamento por escrito da LANDR sobre IA (pedir ao suporte se ainda não houver), assinatura LANDR ativa.
- [ ] **Bio do Caô** no Spotify for Artists (pendência antiga).
- [ ] **Registro da obra** (as letras): associação e ECAD são atos separados; o fonograma de IA não entra no ECAD.

Sem esses itens, a direção não libera o envio.
