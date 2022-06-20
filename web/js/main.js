const inputCSV = document.getElementById("inputCSV");
const btnTrain = document.getElementById("btnTrain");
const selectHomeTeam = document.getElementById("selectHomeTeam");
const selectVisitorTeam = document.getElementById("selectVisitorTeam");
const btnPredict = document.getElementById("btnPredict");

let teams = [
    {id_team: "1", team: "ATL"},
    {id_team: "2", team: "BOS"},
    {id_team: "3", team: "CLE"},
    {id_team: "4", team: "NOP"},
    {id_team: "5", team: "CHI"},
    {id_team: "6", team: "DAL"},
    {id_team: "7", team: "DEN"},
    {id_team: "8", team: "GSW"},
    {id_team: "9", team: "HOU"},
    {id_team: "10", team: "LAC"},
    {id_team: "11", team: "LAL"},
    {id_team: "12", team: "MIA"},
    {id_team: "13", team: "MIL"},
    {id_team: "14", team: "MIN"},
    {id_team: "15", team: "BKN"},
    {id_team: "16", team: "NYK"},
    {id_team: "17", team: "ORL"},
    {id_team: "18", team: "IND"},
    {id_team: "19", team: "PHI"},
    {id_team: "20", team: "PHX"},
    {id_team: "21", team: "POR"},
    {id_team: "22", team: "SAC"},
    {id_team: "23", team: "SAS"},
    {id_team: "24", team: "OKC"},
    {id_team: "25", team: "TOR"},
    {id_team: "26", team: "UTA"},
    {id_team: "27", team: "MEM"},
    {id_team: "28", team: "WAS"},
    {id_team: "29", team: "DET"},
    {id_team: "30", team: "CHA"},
    {id_team: "31", team: "HUS"},
    {id_team: "32", team: "BOM"},
    {id_team: "33", team: "CHS"},
    {id_team: "34", team: "PRO"},
    {id_team: "35", team: "DEF"},
    {id_team: "36", team: "CLR"},
    {id_team: "37", team: "PIT"},
    {id_team: "38", team: "PHW"},
    {id_team: "39", team: "BAL"},
    {id_team: "40", team: "JET"},
    {id_team: "41", team: "FTW"},
    {id_team: "42", team: "ROC"},
    {id_team: "43", team: "MNL"},
    {id_team: "44", team: "TCB"},
    {id_team: "45", team: "INO"},
    {id_team: "46", team: "WAT"},
    {id_team: "47", team: "SYR"},
    {id_team: "48", team: "SHE"},
    {id_team: "49", team: "AND"},
    {id_team: "50", team: "DN"},
    {id_team: "51", team: "BUF"},
    {id_team: "52", team: "SEA"},
    {id_team: "53", team: "PHL"},
    {id_team: "54", team: "NYN"},
    {id_team: "55", team: "GOS"},
    {id_team: "56", team: "KCK"},
    {id_team: "57", team: "NJN"},
    {id_team: "58", team: "NOH"},
    {id_team: "59", team: "CHH"},
    {id_team: "60", team: "VAN"},
    {id_team: "61", team: "UTH"},
    {id_team: "62", team: "SAN"},
    {id_team: "63", team: "NOJ"},
    {id_team: "64", team: "SDR"},
    {id_team: "65", team: "BLT"},
    {id_team: "66", team: "SFW"},
    {id_team: "67", team: "MIH"},
    {id_team: "68", team: "SDC"},
    {id_team: "69", team: "CAP"},
    {id_team: "70", team: "CIN"},
    {id_team: "71", team: "NOK"},
    {id_team: "72", team: "STL"},
    {id_team: "73", team: "CHZ"},
    {id_team: "74", team: "CHP"},
  ],
  data;

document.addEventListener("DOMContentLoaded", function (event) {
  btnTrain.setAttribute("disabled", "disabled");
  selectHomeTeam.setAttribute("disabled", "disabled");
  selectVisitorTeam.setAttribute("disabled", "disabled");
  btnPredict.setAttribute("disabled", "disabled");
  loadSelects();
});

inputCSV.addEventListener("change", () => {
  if (inputCSV.value !== "") {
    const reader = new FileReader();

    reader.onload = async () =>
      (data = JSON.parse(csvJSON(await reader.result)));

    document.getElementsByClassName("file-upload")[0].classList.add("active");
    document.getElementById("noFile").innerText = "Archivo seleccionado";
    btnTrain.removeAttribute("disabled");

    reader.readAsBinaryString(inputCSV.files[0]);
  } else {
    document
      .getElementsByClassName("file-upload")[0]
      .classList.remove("active");
    document.getElementById("noFile").innerText = "Ningún archivo seleccionado";
    btnTrain.setAttribute("disabled", "disabled");
  }
});

btnTrain.addEventListener("click", async () => {
  let inputs = [],
    outputs = [];

  for (let i = 0; i < data.length; i++) {
    let input = [],
      output = [];

    for (let feature in data[i])
      if (feature == "id_team_h" || feature == "id_team_v")
        input.push(parseInt(data[i][feature]));
      else output.push(parseInt(data[i][feature]));

    inputs.push(input);
    outputs.push(outputs);
  }

  await createModel(inputs, outputs);

  selectHomeTeam.removeAttribute("disabled");
  selectVisitorTeam.removeAttribute("disabled");
  btnPredict.removeAttribute("disabled");
});

btnPredict.addEventListener("click", () => {
  if (selectHomeTeam.value != 0 && selectVisitorTeam.value != 0) {
  }
});

const loadSelects = () => {
  for (let i = 0; i < teams.length; i++) {
    selectHomeTeam.innerHTML =
      selectHomeTeam.innerHTML +
      '<option value="' +
      teams[i].id_team +
      '">' +
      teams[i].team +
      "</option>";

    selectVisitorTeam.innerHTML =
      selectHomeTeam.innerHTML +
      '<option value="' +
      teams[i].id_team +
      '">' +
      teams[i].team +
      "</option>";
  }
};

const csvJSON = (csv) => {
  let lines = csv.split("\n"),
    result = [],
    headers = lines[0].split(","),
    resultTemp = [],
    counter = 0;

  for (let i = 1; i < lines.length; i++) {
    let obj = {},
      currentline = lines[i].split(",");

    for (let j = 0; j < headers.length; j++) obj[headers[j]] = currentline[j];

    let randomNumber = Math.floor(Math.random() * (2 - 0)) + 0;

    if (randomNumber && counter <= 20000) {
      resultTemp.push(obj);
      counter++;
    } else result.push(obj);
  }

  console.log(JSON.stringify(result).replace(/[\\n\\r]/g, ""));
  console.log(JSON.stringify(resultTemp).replace(/[\\n\\r]/g, ""));

  return JSON.stringify(result).replace(/[\\n\\r]/g, "");
};

const createModel = async (inputs, outputs) => {
  model = await tf.load_model("../python/saved/nba-model-wins.h5");

  model.predict([[5, 10]]);
};
