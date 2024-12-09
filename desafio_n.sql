WITH descontos_empregado AS (
    SELECT
        emp.matr AS matr,
        SUM(COALESCE(dsc.valor, 0)) AS vlr_desconto
    FROM empregado emp
    LEFT JOIN emp_desc ON emp_desc.matr = emp.matr
    LEFT JOIN desconto dsc ON dsc.cod_desc = emp_desc.cod_desc
    GROUP BY matr
),
vencimentos_empregado AS (
    SELECT
        emp.matr AS matr,
        SUM(COALESCE(venc.valor, 0)) AS vlr_vencimento
    FROM empregado emp
    LEFT JOIN emp_venc ON emp_venc.matr = emp.matr
    LEFT JOIN vencimento venc ON venc.cod_venc = emp_venc.cod_venc
    GROUP BY matr
)

SELECT
    dpt.nome AS "Nome departamento",
    COUNT(emp.matr) AS "Numero de Empregados"
    ROUND(AVG(venc.vlr_vencimento - dsc.vlr_desconto), 2) AS "Media Salarial",
    ROUND(MAX(venc.vlr_vencimento - dsc.vlr_desconto), 2) AS "Maior Salario",
    ROUND(MIN(venc.vlr_vencimento - dsc.vlr_desconto), 2) AS "Menor Salario"
FROM
    empregado emp
    LEFT JOIN departamento dpt ON emp.lotacao = dpt.cod_dep
    LEFT JOIN descontos_empregado dsc ON dsc.matr = emp.matr
    LEFT JOIN vencimentos_empregado venc ON venc.matr = emp.matr
GROUP BY departamento
ORDER BY media DESC;