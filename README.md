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

Comandos e ordem em **Fonte de verdade**, logo abaixo. Depois de instalado, as oito ficam disponíveis como `/bawm:bawm-direcao`, `/bawm:bawm-letrista` e assim por diante — e carregam sozinhas quando a conversa bate com a descrição de cada uma.

O plugin é **autocontido**: toda skill que outra invoca por nome está aqui dentro. Instalar o plugin numa conta limpa não deixa referência pendurada.

## Fonte de verdade: este repo

Quatro skills existem em dois lugares — `bawm-direcao`, `bawm-artista`, `bawm-producao` e `suno-pro` também estão sincronizadas na conta Claude, como `anthropic-skills:…`. **Duas cópias com o mesmo `name` deixam o disparo automático ambíguo, e uma edição num lado não aparece no outro.** Só pode haver uma fonte. A decisão é: **o repo.**

**Por quê:**

1. **A conta falha em silêncio.** Editar pela interface envelhece a cópia do repo sem avisar ninguém; seis meses depois não dá para saber qual vale. Esquecer de atualizar o plugin falha alto — a skill simplesmente não muda, e a versão aparece no `/plugin`.
2. **O histórico aqui é conteúdo, não metadado.** Estas skills carregam regra de compliance que muda com política de plataforma. Quando o Spotify mexer de novo no AI Persona, ou a Apple tornar as tags obrigatórias, o valor está no diff: o que o selo afirmava antes, quando mudou e por quê. Num takedown ou numa disputa, histórico datado é ativo.
3. **O problema que originou este repo foi de referência quebrada** — a direção mandava invocar quatro skills inexistentes e ninguém percebeu. Fonte única e versionada é o que pega isso; a checagem de referências roda a cada commit.

**O que custa, honestamente:** o plugin não se sincroniza sozinho como a conta. Em outra máquina ou sessão é preciso `/plugin marketplace update bawm` para puxar mudança.

### Migração — faça de uma vez só

```
/plugin marketplace add carlosodas/bawm
/plugin install bawm@bawm
```

Depois, **na mesma sentada**, apague pela interface de skills da conta as quatro duplicatas: `bawm-direcao`, `bawm-artista`, `bawm-producao` e `suno-pro`. Fazer em dois momentos deixa uma janela com as duas cópias ativas, que é justamente o que se quer evitar.

As quatro escritas para este repo — `bawm-letrista`, `bawm-arranjador`, `bawm-lancamento` e `bawm-marketing` — nunca estiveram na conta e não precisam de nada.

## Os dois artefatos da cadeia

Duas coisas atravessam a cadeia inteira e por isso vivem fora das skills, em `plugins/bawm/modelos/`:

| Modelo | Aberto por | Fechado por |
|---|---|---|
| `briefing-de-faixa.md` | `bawm-direcao` | antes de a letra começar |
| `dossie-de-faixa.md` | `bawm-letrista`, no briefing | `bawm-lancamento`, antes do release |

O **dossiê** é a espinha de compliance do selo: cinco blocos, cada um preenchido pela etapa dona dele, e `bawm-lancamento` veta o release com qualquer bloco em aberto. Copie o modelo para a pasta da faixa e preencha **no dia em que cada coisa acontece** — dossiê reconstruído na véspera do lançamento não tem valor probatório.

`bawm-direcao` e `bawm-producao` também mandam registrar no dossiê, mas não apontam para o modelo: são cópias verbatim e apontá-las quebraria o checksum. O dossiê é encontrado pelas duas pontas — `bawm-letrista` o abre e `bawm-lancamento` o fecha.

## Procedência

Escritas para este repo, a partir do cânone estabelecido nas outras: `bawm-letrista`, `bawm-arranjador`, `bawm-lancamento` e `bawm-marketing`.

Copiadas **verbatim** das skills sincronizadas da conta, sem uma vírgula alterada e conferidas por checksum:

| Skill | sha256 (12 primeiros) |
|---|---|
| bawm-direcao | `2844ce0bfe0e` |
| bawm-artista | `d6c5357fcdb3` |
| bawm-producao | `8f9a0b552c42` |

`suno-pro` veio da mesma origem (`30d1953a984e`) com **uma única alteração**: removida a linha que apontava para o artifact do manual completo, para não expor o identificador num repo que pode vir a ser público. Nada mais foi tocado — o arquivo aqui é `065973bbfc31`. O manual completo continua existindo fora do repo.

`suno-pro` também não é etapa da cadeia — é o manual de operação do Suno, e serve a qualquer projeto de música. Está aqui porque `bawm-arranjador` e `bawm-producao` a invocam pelo nome: sem ela, o plugin instalado numa conta limpa teria as mesmas referências quebradas que motivaram este repo.

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
  modelos/
    briefing-de-faixa.md
    dossie-de-faixa.md
```

## Convenções

Para o conjunto soar como uma coisa só:

- Texto em português; termos de interface do Suno, Audacity, LANDR e das lojas em inglês.
- ⚠️ marca armadilha operacional — o que custa crédito, retrabalho, rejeição ou takedown.
- Cada skill declara o que consome e o que entrega, e fecha com um checklist de passagem.
- Números concretos, sem maquiagem. Onde a informação da plataforma é instável, a skill manda conferir na interface em vez de fixar um valor.
- Nada de folclore apresentado como especificação: ao afirmar que algo funciona no Suno, sinalize **oficial**, **consenso** ou **anedótico**.
