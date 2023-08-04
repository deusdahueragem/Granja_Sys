document.getElementById("qt_gastos").addEventListener("input", function() {
    var inputValue = this.value.replace(/\D/g, ''); // Remove caracteres não numéricos

    if (inputValue.length > 2) {
        inputValue = inputValue.replace(/^0+/, ''); // Remove zeros à esquerda após os dois primeiros dígitos
    }

    // Adiciona zeros à esquerda para garantir pelo menos dois dígitos para os centavos
    while (inputValue.length < 3) {
        inputValue = '0' + inputValue;
    }

    // Formata o valor para o formato desejado: R$ 000.000,00
    var formattedValue = "R$ " + inputValue.substring(0, inputValue.length - 2) + "." + inputValue.substring(inputValue.length - 2);

    this.value = formattedValue;
});

function formatCurrency(inputString) {
    var inputValue = inputString.replace(/[^\d.-]/g, ''); // Remover tudo exceto dígitos, ponto e hífen

    var parts = inputValue.split('.');
    var dollars = parts[0] || "0";
    var cents = parts[1];

    // Adicionar separador de milhar nos dólares
    var formattedDollars = "";
    for (var i = dollars.length - 1, count = 0; i >= 0; i--) {
        formattedDollars = dollars[i] + formattedDollars;
        count++;
        if (count === 3 && i !== 0) {
            formattedDollars = "." + formattedDollars;
            count = 0;
        }
    }

    if (!cents) {
        cents = "00";
    } else if (cents.length === 1) {
        cents = cents + "0";
    } else if (cents.length > 2) {
        cents = cents.substring(0, 2); // Limitar a 2 casas decimais
    }

    var formattedValue = "R$ " + formattedDollars + "," + cents;

    return formattedValue;
};







// Função para carregar os gastos registrados na tabela
function carregargastosRegistrados() {
    // Realizar a requisição GET para a API (usando Fetch API)
    fetch('http://192.168.3.7/tb_gastos')
    .then(response => response.json())
    .then(data => {
        // Limpar a tabela para inserir os ngastos dados
        const tabelagastos = document.getElementById('tabelagastos');
        tabelagastos.innerHTML = `
            <tr>
                <th>ID</th>
                <th>Data e Hora</th>
                <th>Valor</th>
                <th>Tipo de Gasto</th>
                <th>Deletar</th>
            </tr>
        `;

        // Inserir os gastos registrados na tabela
        data.forEach(gasto => {
            const newRow = tabelagastos.insertRow();
            var valor_gasto = gasto.qt_gastos;
            valor_gasto = valor_gasto.toString();
            var valor_formatado = formatCurrency(valor_gasto);
            //console.log("Valor recebido: " + valor_gasto + " Valor formatado: " + valor_formatado);
            newRow.innerHTML = `
                <td>${gasto.id_gastos}</td>
                <td>${gasto.dt_gastos}</td>
                <td>${valor_formatado}</td>
                <td>${gasto.tp_gastos}</td>
                <td><button onclick="deletarGasto(${gasto.id_gastos})">Deletar</button></td>
            `;
        });
    })
    .catch(error => console.error('Erro:', error));
}

// Carregar os gastos registrados na tabela ao carregar a página
carregargastosRegistrados();

// Função para deletar um registro de gasto
function deletarGasto(id) {
    // Realizar a requisição DELETE para a API (usando Fetch API)
    fetch(`http://192.168.3.7/tb_gastos/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        // Carregar novamente os gastos registrados na tabela após deletar
        carregargastosRegistrados();
    })
    .catch(error => console.error('Erro:', error));
}

// Evento de clique no botão "Registrar"
document.getElementById('btnRegistrar').addEventListener('click', function() {
    var quantidade = document.getElementById('qt_gastos').value;
    quantidade = quantidade.replace("R$ ", "");
    quantidade = parseFloat(quantidade);
    const dataHora = document.getElementById('dt_gastos').value;
    const tipogasto = document.getElementById('tp_gastos').value;

    // Verifica se os campos estão vazios
    if (!quantidade || !dataHora || !tipogasto) {
        // Pintar as bordas de vermelho
        if (!quantidade) {
            document.getElementById('qt_gastos').style.border = '2px solid red';
        }
        if (!dataHora) {
            document.getElementById('dt_gastos').style.border = '2px solid red';
        }
        if (!tipogasto) {
            document.getElementById('tp_gastos').style.border = '2px solid red';
        }

        // Mostrar mensagem de aviso
        alert('Preencha todos os campos para registrar as informações.');
        return; // Sai da função sem continuar o código
    }

    // Restaurar as bordas para o estado normal
    document.getElementById('qt_gastos').style.border = '1px solid #ccc';
    document.getElementById('dt_gastos').style.border = '1px solid #ccc';
    document.getElementById('tp_gastos').style.border = '1px solid #ccc';

    // Criação do objeto de dados para enviar ao servidor
    const dados = {
        "qt_gastos": quantidade,
        "dt_gastos": dataHora,
        "tp_gastos": tipogasto
    };

    // Restante do código para enviar os dados ao servidor
    fetch('http://192.168.3.7/tb_gastos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('qt_gastos').value = "";
        document.getElementById('dt_gastos').value = "";
        document.getElementById('tp_gastos').value = "0";
        alert('O Registro foi realizado com sucesso !');
        // Inserir o novo registro na tabela de gastos registrados
        const tabelagastos = document.getElementById('tabelagastos');
        const newRow = tabelagastos.insertRow();
        newRow.innerHTML = `
            <td>${data.id_gastos}</td>
            <td>${data.dt_gastos}</td>
            <td>${data.qt_gastos}</td>
            <td><button onclick="deletarGasto(${data.id_gastos})">Deletar</button></td>
        `;
    })
    .catch(error => console.error('Erro:', error));
});