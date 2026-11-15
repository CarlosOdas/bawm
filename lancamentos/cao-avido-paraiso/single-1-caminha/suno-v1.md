# Caminha (o grumete) — pacote Suno v1

> 15/11/2026 · `bawm-arranjador` sobre a letra **v2** ([`rascunhos/v2-2026-11-15.md`](rascunhos/v2-2026-11-15.md)).
> ⚠️ A v2 é proposta de autoria mista e **ainda não foi aprovada verso a verso** pelo autor. O Carlos pediu o prompt sobre ela. Se algum verso mudar, a caixa Lyrics muda junto e este arquivo ganha uma v2.
> ⚠️ Se a geração usar uma voz salva do Bento (Style Persona), selecioná-la **preenche a caixa Styles sozinha**. Ver a nota no fim.

## 1. Mapa da faixa

| Seção | Letra | Quem toca | O que muda | Duração aprox. |
|---|---|---|---|---|
| Intro | — | **Glória**, sete cordas sozinho | as baixarias abrem a noite | 8–12 s |
| Verso 1 | estrofe 1 | **Bento** + sete cordas | a faixa assenta só com voz e violão | ~22 s |
| Verso 2 | estrofe 2 | + **Lia** no pandeiro | o pandeiro entra com o remo | ~22 s |
| Verso 3 | estrofe 3 | pandeiro mais cheio | a travessia; sobe a densidade, não o volume | ~22 s |
| Refrão | estrofe 4 | + coro do grupo respondendo | a promessa; o coro devolve um verso | ~25 s |
| Ponte | estrofe 5 | o pandeiro sai; voz e sete cordas | o que ele viu nos dez dias; a ponte subtrai | ~22 s |
| Refrão | estrofe 4 | coro, pandeiro de volta | igual ao primeiro | ~25 s |
| Verso final | estrofe 6 | **cuíca** da Lia entra, uma vez | a testemunha; a única entrada dela na faixa | ~22 s |
| Coda | — | sete cordas sozinho | desce ao que abriu; fim seco | 8–10 s |

Duração projetada: **3:00 a 3:20**.

Três dos cinco com função clara: **Bento** (voz), **Glória** (sete cordas), **Lia** (pandeiro e cuíca). **Guilherme** só no coro do refrão. **Helena** fica de fora: os singles são acústicos e nus, e as cordas chegam no EP.

**Decisões do arranjo:**
- As estrofes 1, 2 e 3 ficam juntas, para a deixa entre elas ser ouvida.
- O refrão aparece **duas vezes**, escrito por extenso.
- A estrofe 5 é a ponte: muda o tempo do verbo (*viu*) e tira o pandeiro.
- A faixa termina em *paraíso*, e não no refrão.
- **O coro só repete palavras do autor.** Os dois ecos entre parênteses são versos da própria letra.

## 2. Styles

```
Afro-Barroco brasileiro de sotaque nativo sobre base de samba de terreiro dos anos 60, barítono grave e solene de terreiro em fraseado lento, violão de sete cordas, pandeiro, gravação de sala crua e próxima em wide stereo, samba lento de mesa com voz e violão à frente
```

6 descritores: fundação · variação do Bento (posição 2) · 2 instrumentos · produção · descritor livre. A cuíca entra por tag.

## 3. Exclude styles

```
autotune, electronic drums, 808, distorted guitar, synth lead
```

## 4. Lyrics

```
[Intro - solo sete cordas]

[Verse 1 - voice and guitar]
No silêncio da modorra
a frota já adormeceu
o grumete desce a amarra
para o mar que agora é seu
sob a noite em Vera Cruz
foge à luz e ganha o breu

[Verse 2 - pandeiro enters]
Vai no esquife que escolheu
longe do mestre, aprendiz
deixa o porão e a estopa
o biscoito que não quis
pois a fome deste moço
pede a terra por raiz

[Verse 3 - fuller pandeiro]
Corta o mar sem cicatriz
onde o fura-buxos vem
bate o remo contra a onda
sem olhar para ninguém
já não é moço de bordo
já não é refém de alguém

[Chorus - group choir answers]
Ah, escrivão, guarde a pena
que a promessa já se faz
nesta terra que dá tudo
ninguém volta para trás
(ninguém volta para trás)
amanhã a frota parte
sem levar este rapaz

[Bridge - pandeiro falls away]
Viu o fogo na ribeira
sob o Monte Pascoal
viu a dança ao som da gaita
e deixou a grande nau
com a inocência de Adão
para ser um natural

[Chorus - group choir answers]
Ah, escrivão, guarde a pena
que a promessa já se faz
nesta terra que dá tudo
ninguém volta para trás
(ninguém volta para trás)
amanhã a frota parte
sem levar este rapaz

[Final Verse - cuíca enters]
Quando a cuíca gemer
de testemunha e de aviso
lá se vai o capitão
pelo mar escuro e liso
mas quem chega no areal
entra no seu paraíso
(entra no seu paraíso)

[Outro - solo sete cordas]

[End]
```

## 5. Sliders

**Weirdness 30 · Style Influence 80 · Vocal Gender: Male**

## Notas de geração

- **Título no Suno:** o título é do autor e ainda não existe. Use *Caminha* como nome de trabalho.
- **Voz do Bento.** Se há voz salva dele, faça o teste de uma variável: 2 gerações com a Persona selecionada, deixando a caixa Styles como ela preencher, e 2 gerações sem Persona, com o Styles acima. Compare os mesmos 20 segundos nas quatro. Se não há, a primeira geração boa daqui vira a Style Persona dele.
- **Esta é também a prova de som do lançamento** para sete cordas, pandeiro e cuíca. Duas gerações antes de mudar qualquer coisa.
- **Custo de cada geração entra no dossiê**, bloco 2: o que ficou, o que foi descartado e por quê.

**Se sair errado, nesta ordem:**

| Sintoma | Primeira coisa a tentar |
|---|---|
| Vem um samba cheio, com bateria, surdo e cavaquinho | Acrescente `drum kit, cavaquinho` ao Exclude. Não mexa no Styles ainda |
| Vem MPB de câmara sem samba | Suba o Style Influence para 85; se persistir, troque o descritor livre por `samba de roda lento` |
| A cuíca não aparece, ou aparece na faixa toda | Replace Section só no verso final; não regenere a música |
| O vocal atropela algum verso | É sílaba, não tag. Os candidatos são *"o grumete desce a amarra"* e *"longe do mestre, aprendiz"* |
| A voz sai aguda ou leve demais | Confira o botão Male; depois troque `em fraseado lento` por `e escuro` na variação |
| A faixa passa muito de 3:30 | Crop no fim, ou tire o eco final entre parênteses |
