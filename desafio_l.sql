WITH descontos_empregado AS (
    SELECT
        emp.matr AS matr,
        SUM(COALESCE(dsc.valor, 0)) AS vlr_desconto
    FROM empregado emp
    LEFT JOIN emp_desc ON emp_desc.matr = emp.matr
    LEFT JOIN desconto dsc ON dsc.cod_desc = emp_desc.cod_desc
    GROUP BY emp.matr
),
vencimentos_empregado AS (
    SELECT
        emp.matr AS matr,
        SUM(COALESCE(venc.valor, 0)) AS vlr_vencimento
    FROM empregado emp
    LEFT JOIN emp_venc ON emp_venc.matr = emp.matr
    LEFT JOIN vencimento venc ON venc.cod_venc = emp_venc.cod_venc
    GROUP BY emp.matr
)

SELECT
    dpt.nome AS departamento,
    dvs.nome AS divisao,
    ROUND(AVG(venc.vlr_vencimento - dsc.vlr_desconto), 2) AS media,
    ROUND(MAX(venc.vlr_vencimento - dsc.vlr_desconto), 2) AS maior
FROM
    empregado emp
    LEFT JOIN divisao dvs ON emp.lotacao_div = dvs.cod_div AND emp.lotacao = dvs.cod_dep
    LEFT JOIN departamento dpt ON dvs.cod_dep = dpt.cod_dep
    LEFT JOIN descontos_empregado dsc ON dsc.matr = emp.matr
    LEFT JOIN vencimentos_empregado venc ON venc.matr = emp.matr
GROUP BY departamento, divisao
ORDER BY media DESC;