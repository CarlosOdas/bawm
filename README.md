# BAWM — skills da cadeia de produção

Skills do selo **BAWM — Brazilian Artificial World Music**, de Carlos Alberto Odas.

A direção do selo descreve uma cadeia de **sete funções**, cada uma produzindo um artefato que a seguinte consome:

```
1. bawm-direcao     briefing: artista, tema, geografia sonora, função no plano
2. bawm-letrista    letra + dossiê de autoria humana          ← neste repo
3. bawm-arranjador  mapa da faixa, tags, Styles, Exclude      ← neste repo
4. bawm-producao    Suno gera · Audacity monta · LANDR masteriza
5. bawm-lancamento  metadados, arte, data, ISRC, declaração   ← neste repo
6. bawm-marketing   pitch, Canvas, cortes, calendário         ← neste repo
7. bawm-artista     personas do elenco (consultada por todas)
```

**Este repo contém as quatro que faltavam:** `bawm-letrista`, `bawm-arranjador`, `bawm-lancamento` e `bawm-marketing`.

As outras três — `bawm-direcao`, `bawm-artista` e `bawm-producao` — já existem como skills sincronizadas na conta Claude e **não estão versionadas aqui**, para não haver duas fontes de verdade. A skill auxiliar `suno-pro`, usada pelo arranjo e pela produção, também vive lá.

## Instalar

```
/plugin marketplace add carlosodas/bawm
/plugin install bawm@bawm
```

Depois disso as quatro skills ficam disponíveis como `/bawm:bawm-letrista`, `/bawm:bawm-arranjador`, `/bawm:bawm-lancamento` e `/bawm:bawm-marketing` — e também carregam sozinhas quando a conversa bate com a descrição de cada uma.

Alternativa: subir cada `SKILL.md` avulso pela interface de skills da conta, como foi feito com as três primeiras. Aí os nomes ficam idênticos aos que a `bawm-direcao` já referencia, sem prefixo de plugin.

## Estrutura

```
.claude-plugin/marketplace.json
plugins/bawm/
  .claude-plugin/plugin.json
  skills/
    bawm-letrista/SKILL.md
    bawm-arranjador/SKILL.md
    bawm-lancamento/SKILL.md
    bawm-marketing/SKILL.md
```

## Convenções

Herdadas das três skills existentes, para o conjunto soar como uma coisa só:

- Texto em português; termos de interface do Suno, Audacity, LANDR e das lojas em inglês.
- ⚠️ marca armadilha operacional — o que custa crédito, retrabalho, rejeição ou takedown.
- Cada skill declara o que consome e o que entrega, e fecha com um checklist de passagem.
- Números concretos, sem maquiagem. Onde a informação da plataforma é instável, a skill manda conferir na interface em vez de fixar um valor.
- Nada de folclore apresentado como especificação.
