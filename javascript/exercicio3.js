const { gets, print } = require("./funcoes-auxiliares-ex3");

const valorSalarioBruto = gets();
const valorBeneficio = gets();


function calcularPorcentagem(valor, percentual) {
  return valor * (percentual / 100);
}

function pegarPercentualImpostoComBaseNoSalario(salario){
    if (salario <= 1100){
        return 5;
    } else if (salario > 1100 && salario <= 2500){
        return 10;
    } else {
        return 15;
    }
}

const valorSalarioLiquido = valorSalarioBruto - (calcularPorcentagem(valorSalarioBruto, pegarPercentualImpostoComBaseNoSalario(valorSalarioBruto))) + valorBeneficio

print(valorSalarioLiquido)
