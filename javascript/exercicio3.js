const { gets, print } = require("./funcoes-auxiliares-ex3");

const valorSalario = parseFloat(gets());
const valorBeneficios = parseFloat(gets());


function calcularPorcentagem(valor, percentual) {
  return valor * (percentual / 100);
}

function pegarAliquota(salario){
    if (salario <= 1100){
        return 5;
    } else if (salario > 1100 && salario <= 2500){
        return 10;
    } else {
        return 15;
    }
}

const aliquotaImposto = pegarAliquota(valorSalario)

const valorImposto = calcularPorcentagem(valorSalario, aliquotaImposto)

const valorSalarioLiquido = valorSalario - valorImposto + valorBeneficios

print(parseFloat(valorSalarioLiquido))
