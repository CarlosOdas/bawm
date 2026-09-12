# BAWM — skills da cadeia de produção

Skills do selo **BAWM — Brazilian Artificial World Music**, de Carlos Alberto Odas.

A cadeia tem **sete funções**, cada uma produzindo um artefato que a seguinte consome. Todas estão neste repo, mais o manual de operação do Suno que duas delas invocam.

```
1. bawm-direcao     briefing: artista, tema, geografia sonora, função no plano
2. bawm-letrista    letra + dossiê de autoria humana
3. bawm-arranjador  mapa da faixa, tags, Styles, Exclude, sliders
4. bawm-producao    Suno gera · Audacity monta · LANDR masteriza
5. bawm-lancamento  metadados, arte, data, ISRC, declaração de IA
6. bawm-marketing   pitch, Canvas, cortes, calendário

   bawm-artista     personas do elenco — consultada por todas as etapas
   suno-pro         mecânica de prompt do Suno — usada por 3 e 4
```

Trabalhe **uma faixa por vez** até o dossiê fechar. Comece pela `bawm-direcao`: ela é a porta de entrada e despacha para as outras.

## Instalar

```
/plugin marketplace add carlosodas/bawm
/plugin install bawm@bawm
```

As oito ficam disponíveis como `/bawm:bawm-direcao`, `/bawm:bawm-letrista` e assim por diante — e carregam sozinhas quando a conversa bate com a descrição de cada uma.

O plugin é **autocontido**: toda skill que outra invoca por nome está aqui dentro. Instalar o plugin numa conta limpa não deixa referência pendurada.

### ⚠️ Antes de instalar: remova as duplicatas da conta

`bawm-direcao`, `bawm-artista`, `bawm-producao` e `suno-pro` **também existem como skills sincronizadas na conta Claude** (aparecem como `anthropic-skills:…`). Instalar este plugin sem mexer nelas deixa **duas cópias com o mesmo `name`** — o disparo automático fica ambíguo e uma edição no repo não aparece na cópia da conta.

Escolha um dos dois caminhos e siga só ele:

- **Repo como fonte de verdade** (recomendado) — instale o plugin e **apague as quatro skills sincronizadas** pela interface de skills da conta. A partir daí, editar é `git commit`.
- **Conta como fonte de verdade** — não instale o plugin; trate este repo como arquivo e histórico, e suba as quatro novas avulsas pela interface, como foi feito com as primeiras.

Misturar os dois é o que dá problema.

## Procedência

Escritas para este repo, a partir do cânone estabelecido nas outras: `bawm-letrista`, `bawm-arranjador`, `bawm-lancamento` e `bawm-marketing`.

Copiadas **verbatim** das skills sincronizadas da conta, sem uma vírgula alterada e conferidas por checksum:

| Skill | sha256 (12 primeiros) |
|---|---|
| bawm-direcao | `2844ce0bfe0e` |
| bawm-artista | `d6c5357fcdb3` |
| bawm-producao | `8f9a0b552c42` |
| suno-pro | `30d1953a984e` |

`suno-pro` não é etapa da cadeia — é o manual de operação do Suno, e serve a qualquer projeto de música. Está aqui porque `bawm-arranjador` e `bawm-producao` a invocam pelo nome: sem ela, o plugin instalado numa conta limpa teria as mesmas referências quebradas que motivaram este repo.

## Estrutura

```
.claude-plugin/marketplace.json
plugins/bawm/
  .claude-plugin/plugin.json
  skills/
    bawm-direcao/SKILL.md
    bawm-artista/SKILL.md
    bawm-letrista/SKILL.md
    bawm-arranjador/SKILL.md
    bawm-producao/SKILL.md
    bawm-lancamento/SKILL.md
    bawm-marketing/SKILL.md
    suno-pro/SKILL.md
```

## Convenções

Para o conjunto soar como uma coisa só:

- Texto em português; termos de interface do Suno, Audacity, LANDR e das lojas em inglês.
- ⚠️ marca armadilha operacional — o que custa crédito, retrabalho, rejeição ou takedown.
- Cada skill declara o que consome e o que entrega, e fecha com um checklist de passagem.
- Números concretos, sem maquiagem. Onde a informação da plataforma é instável, a skill manda conferir na interface em vez de fixar um valor.
- Nada de folclore apresentado como especificação: ao afirmar que algo funciona no Suno, sinalize **oficial**, **consenso** ou **anedótico**.
