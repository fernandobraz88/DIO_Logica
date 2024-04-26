function calcularNivel(vitorias, derrotas) {
    
    let saldoVitorias = vitorias - derrotas
    let nivel

    if (vitorias < 10) {
        nivel = "Ferro"
    } else if (vitorias < 21) {
        nivel = "Bronze"
    } else if (vitorias < 51) {
        nivel = "Prata"
    } else if (vitorias < 81) {
        nivel = "Ouro"
    } else if (vitorias < 91) {
        nivel = "Diamante"
    } else if (vitorias < 101) {
        nivel = "Lendário"
    } else {
        nivel = "Imortal"
    }

    return `O Herói tem um saldo de ${saldoVitorias} e está no nível de ${nivel}`
}

console.log(calcularNivel(30,12))