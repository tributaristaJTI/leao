# Lacunas: nomear, nunca preencher

Regra herdada da `atas-leao`: a skill jamais cria dono, prazo, dado ou decisão que a entrada não trouxe. Toda inferência é redirecionada de "preencher" para "apontar". Plano que inventa estrutura é pior que plano incompleto, porque esconde onde a decisão ainda não foi tomada.

## Formato

```
[LACUNA — tipo — o que falta — quem resolve — bloqueia: Fn / Tn.m / nada]
```

## Tipos

| Tipo | Exemplo | Quem costuma resolver |
|---|---|---|
| `dado` | área, faturamento, regime tributário, número de matrícula | cliente, contador-rural |
| `documento` | contrato social vigente, DIAT dos dois anos, matrícula atualizada | cliente, cartorio-registro |
| `decisao-cliente` | doar com ou sem usufruto; PF ou PJ; vender ou arrendar | decisor |
| `decisao-socio` | régua de risco, tese principal, aceitar caso no modo neutro | socio-responsavel |
| `entidade-dona` | não dá para saber se o projeto é AeM, Agricompany ou conjunto | socio-responsavel |
| `terceiro` | banco credor não identificado, contador do cliente desconhecido | cliente |
| `ambiguidade` | dois nomes ou dois valores contraditórios na entrada | quem redigiu a ata |

## Marcação de inferência

Quando a skill precisar assumir premissa para seguir (fase que depende de dado ausente), a premissa entra no plano com a marca `(inferido)` e gera a lacuna correspondente. O relatório de fechamento conta lacunas por tipo; plano com lacuna do tipo `decisao-socio` ou `entidade-dona` aberta não avança para o v1.
