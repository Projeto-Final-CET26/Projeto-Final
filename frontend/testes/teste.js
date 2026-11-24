let url = '192.168.1.76:8000'
const DESPORTOS = {
  futebol:     { periodos: 2, duracao: 2700, nomes: ['1ª parte', '2ª parte'] },
  andebol:     { periodos: 2, duracao: 1800, nomes: ['1ª parte', '2ª parte'] },
  basquetebol: { periodos: 4, duracao: 600,  nomes: ['1º quarto', '2º quarto', '3º quarto', '4º quarto'] },
  voleibol:    { periodos: 5, duracao: null, nomes: ['1º set', '2º set', '3º set', '4º set', '5º set'] } // sem relógio
};

let inicioTimestamp = null;
let tempoAcumuladoMs = 0;
let cronometroId = null;

function formatarMmSs(totalSegundos) {
  const segInteiros = Math.floor(totalSegundos);
  const minutos = Math.floor(segInteiros / 60);
  const segundos = segInteiros % 60;

  const mm = String(minutos).padStart(2, '0');
  const ss = String(segundos).padStart(2, '0');

  return `${mm}:${ss}`;
}

function obterSegundosDecorridos() {
  const atualMs = cronometroId ? (Date.now() - inicioTimestamp) : 0;
  return (tempoAcumuladoMs + atualMs) / 1000;
}

function atualizarCronometro() {
  const totalSegundos = obterSegundosDecorridos();
  $('#tempo').text(formatarMmSs(totalSegundos));
}

function iniciarCronometro() {
  if (cronometroId !== null) return; // já está a correr

  inicioTimestamp = Date.now();
  atualizarCronometro();
  cronometroId = setInterval(atualizarCronometro, 100); // verifica a cada 100ms, mas mostra só mm:ss inteiro
}

function pausarCronometro() {
  if (cronometroId === null) return;

  tempoAcumuladoMs += Date.now() - inicioTimestamp;
  clearInterval(cronometroId);
  cronometroId = null;
  atualizarCronometro();
}

let periodo = 0;
let desporto = 'basquetebol';

function getDesporto() {
  return desporto;
}

function reiniciarCronometro() {
  pausarCronometro();
  tempoAcumuladoMs = 0;
  inicioTimestamp = null;
  $('#tempo').text('00:00');
}

function getPeriodo() {
  const infoDesporto = DESPORTOS[getDesporto()];
  const nomePeriodo = infoDesporto.nomes[periodo - 1] || periodo;
  $('#periodo').text(nomePeriodo);
}

function atualizarPeriodo() {
  const infoDesporto = DESPORTOS[getDesporto()];

  // Se ainda não estamos no último período, avança para o próximo
  if (periodo < infoDesporto.periodos) {
    periodo++;

    getPeriodo();

    // Reinicia o relógio quando muda de período (a partir do 2º)
    if (periodo > 1) {
      reiniciarCronometro();
    }

    // Se acabámos de entrar no último período, muda logo o botão para "Terminar Análise"
    if (periodo === infoDesporto.periodos) {
      $('#btnPeriodo').text('Terminar Análise');
    }
  } else {
    // O utilizador clicou em "Terminar Análise" no último período
    pausarCronometro();
    console.log('Análise terminada!');
  }
}

function getTitulares(){
    $.ajax({
        url: url + '/jogo_jogadores',
        method: 'GET',

        success: function(dados){
            let txt = ''

            for(let dado of dados){
                txt += `<tr>
                        <td>${dado.id}</td>
                        <td>
                            <button type="button" class="btn btn-success btn-sm" onclick="editarCampo()">Editar</button>
                            <button type="button" class="btn btn-danger btn-sm" onclick="removerCampo()">Remover</button>
                        </td>
                        </tr>`
            }

            $("#tabelaCorpo").html(txt)
        },

        error: function (erro){
            alert('Dados não foram possíveis de carregar')
        }
    })
}

function voltarPeriodo(){
    if(periodo > 1){
        periodo -= 1
        getPeriodo()
    }
}

$(function () {
  atualizarPeriodo();
});